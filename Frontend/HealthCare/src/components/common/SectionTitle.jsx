const SectionTitle = ({ title, subtitle }) => {
  return (
    <div className="section-title">
      {subtitle && <p className="section-subtitle">{subtitle}</p>}

      <h2>{title}</h2>
    </div>
  );
};

export default SectionTitle;