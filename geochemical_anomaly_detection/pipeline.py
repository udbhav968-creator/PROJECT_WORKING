# ==============================================================================
# NGCM Geochemical Anomaly Detection – Full Advanced Pipeline
# Variable names prefixed with udbhav_
# ==============================================================================
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import glob
import warnings
warnings.filterwarnings('ignore')

from sklearn.preprocessing import StandardScaler
from sklearn.impute import KNNImputer
from sklearn.neighbors import LocalOutlierFactor, NearestNeighbors
from sklearn.ensemble import IsolationForest
from sklearn.covariance import EllipticEnvelope
from sklearn.svm import OneClassSVM
from sklearn.decomposition import PCA
from sklearn.cluster import DBSCAN

try:
    plt.style.use('seaborn-v0_8-whitegrid')
except:
    plt.style.use('ggplot')

def udbhav_load_data():
    udbhav_files = glob.glob("NGCM*.xlsx")
    if not udbhav_files:
        udbhav_files = glob.glob("../NGCM*.xlsx")
        
    if not udbhav_files:
        raise FileNotFoundError("NGCM Excel file not found. Place a file starting with 'NGCM' and ending with '.xlsx' in this directory.")
    
    print(f"Loading dataset: {udbhav_files[0]}")
    udbhav_df = pd.read_excel(udbhav_files[0], sheet_name=0, engine='openpyxl')
    print("Dataset loaded successfully. Shape:", udbhav_df.shape)
    return udbhav_df

def udbhav_preprocess(udbhav_df):
    udbhav_num_cols = [c for c in udbhav_df.columns if pd.api.types.is_numeric_dtype(udbhav_df[c])]
    udbhav_excl = ['ID', 'SAMPLE', 'LAT', 'LONG', 'X', 'Y', 'COORD']
    udbhav_chem_cols = [c for c in udbhav_num_cols if not any(p in str(c).upper() for p in [i.upper() for i in udbhav_excl])]
    
    udbhav_df_chem = udbhav_df[udbhav_chem_cols].copy()
    
    print("Performing KNN Imputation (k=5)...")
    udbhav_imputer = KNNImputer(n_neighbors=5)
    udbhav_df_imp = pd.DataFrame(
        udbhav_imputer.fit_transform(udbhav_df_chem),
        columns=udbhav_df_chem.columns,
        index=udbhav_df_chem.index
    )
    
    print("Applying Centered Log-Ratio (CLR) Transformation...")
    def clr(data):
        data = data.clip(lower=1e-10)
        log = np.log(data)
        gm = np.exp(log.mean(axis=1))
        return pd.DataFrame(np.log(data.div(gm, axis=0)), columns=data.columns, index=data.index)
    
    udbhav_df_clr = clr(udbhav_df_imp)
    
    print("Applying StandardScaler...")
    udbhav_scaler = StandardScaler()
    udbhav_df_scaled = pd.DataFrame(
        udbhav_scaler.fit_transform(udbhav_df_clr),
        columns=udbhav_df_clr.columns,
        index=udbhav_df_clr.index
    )
    
    return udbhav_df_scaled, udbhav_chem_cols

def udbhav_detect_anomalies(udbhav_df_scaled):
    print("Running anomaly detection models...")
    udbhav_lof = LocalOutlierFactor(n_neighbors=20, contamination=0.05)
    udbhav_lof_labels = udbhav_lof.fit_predict(udbhav_df_scaled)
    udbhav_lof_scores = -udbhav_lof.negative_outlier_factor_
    
    udbhav_iforest = IsolationForest(n_estimators=100, contamination=0.05, random_state=42)
    udbhav_if_labels = udbhav_iforest.fit_predict(udbhav_df_scaled)
    udbhav_if_scores = udbhav_iforest.score_samples(udbhav_df_scaled)
    
    return {
        'lof_labels': udbhav_lof_labels, 'lof_scores': udbhav_lof_scores,
        'if_labels': udbhav_if_labels, 'if_scores': udbhav_if_scores
    }

def main():
    print("NGCM GEOCHEMICAL ANOMALY DETECTION PIPELINE")
    try:
        udbhav_df = udbhav_load_data()
        udbhav_df_scaled, udbhav_chem_cols = udbhav_preprocess(udbhav_df)
        udbhav_anoms = udbhav_detect_anomalies(udbhav_df_scaled)
        print("Anomaly detection complete.")
    except Exception as e:
        print(f"Pipeline info: {e}")

if __name__ == '__main__':
    main()
