import React from 'react';
import TopHeaderBar from '../components/layout/TopHeaderBar';
import OpdBookingWidget from '../components/home/OpdBookingWidget';
import DoctorRosterTicker from '../components/home/DoctorRosterTicker';
import StatsCounter from '../components/home/StatsCounter';

export default function Home() {
  return (
    <div style={{ minHeight: '100vh' }}>
      <TopHeaderBar />

      <section className="hero-enterprise-banner">
        <div style={{ maxWidth: '1100px', margin: '0 auto' }}>
          <span style={{ background: 'rgba(255, 255, 255, 0.15)', padding: '6px 18px', borderRadius: '30px', fontWeight: 700, fontSize: '0.85rem', letterSpacing: '0.05em' }}>
            PURE HEALTH CLINIC & HOSPITAL SYSTEMS
          </span>
          <h1 style={{ fontSize: '3rem', margin: '16px 0', lineHeight: 1.15 }}>
            Personalized Patient Care & Enterprise Clinical Excellence
          </h1>
          <p style={{ fontSize: '1.2rem', color: '#e2e8f0', maxWidth: '750px', margin: '0 auto 24px' }}>
            Led by <strong>Dr. Divit Shah</strong> (Medical Director), providing compassionate, high-quality, tailored medical OPD services, tele-consultation video rooms, and 24x7 emergency triage.
          </p>

          <div style={{ display: 'flex', justifyContent: 'center', gap: '16px', flexWrap: 'wrap' }}>
            <a href="#booking" style={{ background: '#02c39a', color: '#0a2540', padding: '14px 32px', borderRadius: '12px', fontWeight: 800, textDecoration: 'none', fontSize: '1.05rem' }}>
              🎟️ Book OPD Token Now
            </a>
            <a href="https://project-working-snojkumar968-9939s-projects.vercel.app/api/docs/" target="_blank" rel="noopener noreferrer" style={{ background: 'rgba(255, 255, 255, 0.15)', color: '#fff', padding: '14px 32px', borderRadius: '12px', fontWeight: 700, textDecoration: 'none', fontSize: '1.05rem', border: '1px solid rgba(255, 255, 255, 0.3)' }}>
              📄 Swagger API Docs
            </a>
          </div>
        </div>
      </section>

      <div style={{ maxWidth: '1140px', margin: '0 auto', padding: '0 20px' }} id="booking">
        <OpdBookingWidget />
        <DoctorRosterTicker />
        <StatsCounter />

        {/* Clinical Departments Grid */}
        <section style={{ margin: '60px 0' }}>
          <div style={{ textAlign: 'center', marginBottom: '32px' }}>
            <span style={{ fontSize: '0.85rem', fontWeight: 700, color: '#00a896', textTransform: 'uppercase' }}>SPECIALTY CLINICAL PORTALS</span>
            <h2 style={{ fontSize: '2rem', color: '#0a2540' }}>Centers of Medical Excellence</h2>
          </div>

          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(280px, 1fr))', gap: '24px' }}>
            <div className="glass-panel" style={{ padding: '28px' }}>
              <div style={{ fontSize: '2.5rem', marginBottom: '12px' }}>🩸</div>
              <h3 style={{ fontSize: '1.3rem', color: '#0a2540' }}>Cardiology & Cardiovascular Care</h3>
              <p style={{ color: '#64748b', fontSize: '0.9rem', margin: '8px 0 16px' }}>Comprehensive heart health assessments, ECG, 24-hr Holter monitoring, and preventative cardiology under Dr. Rahul Mehta.</p>
              <div style={{ fontWeight: 700, color: '#0066cc' }}>Consultation Fee: ₹1000</div>
            </div>

            <div className="glass-panel" style={{ padding: '28px' }}>
              <div style={{ fontSize: '2.5rem', marginBottom: '12px' }}>🩺</div>
              <h3 style={{ fontSize: '1.3rem', color: '#0a2540' }}>General Consultation & Preventive Health</h3>
              <p style={{ color: '#64748b', fontSize: '0.9rem', margin: '8px 0 16px' }}>Personalized primary care, routine health screenings, and preventative consultation led by Medical Director Dr. Divit Shah.</p>
              <div style={{ fontWeight: 700, color: '#0066cc' }}>Consultation Fee: ₹600</div>
            </div>

            <div className="glass-panel" style={{ padding: '28px' }}>
              <div style={{ fontSize: '2.5rem', marginBottom: '12px' }}>💊</div>
              <h3 style={{ fontSize: '1.3rem', color: '#0a2540' }}>Chronic Care (Diabetes & Hypertension)</h3>
              <p style={{ color: '#64748b', fontSize: '0.9rem', margin: '8px 0 16px' }}>Long-term metabolic disorder management, continuous glucose tracking, and personalized lifestyle counseling by Dr. Anjali Sharma.</p>
              <div style={{ fontWeight: 700, color: '#0066cc' }}>Consultation Fee: ₹750</div>
            </div>

            <div className="glass-panel" style={{ padding: '28px' }}>
              <div style={{ fontSize: '2.5rem', marginBottom: '12px' }}>📹</div>
              <h3 style={{ fontSize: '1.3rem', color: '#0a2540' }}>Tele-Consultation Video Portal</h3>
              <p style={{ color: '#64748b', fontSize: '0.9rem', margin: '8px 0 16px' }}>Secure, high-definition video consultations with instant digital prescription delivery for remote patients.</p>
              <div style={{ fontWeight: 700, color: '#02c39a' }}>Instant Jitsi Video Link</div>
            </div>
          </div>
        </section>
      </div>

      <footer style={{ background: '#0a2540', color: '#94a3b8', padding: '40px 20px', textAlign: 'center', borderTop: '4px solid #00a896' }}>
        <p style={{ color: '#fff', fontWeight: 700, fontSize: '1.1rem' }}>🏥 Pure Health Clinic & Hospital Systems</p>
        <p style={{ marginTop: '6px', fontSize: '0.9rem' }}>PY Digital Services Pvt. Ltd. | Reference Inspiration: Divit Pure Health Clinic</p>
        <p style={{ marginTop: '12px', fontSize: '0.85rem' }}>© 2026 Pure Health Clinic. Built by Udbhav (Module 4 - Administration & System Integration).</p>
      </footer>
    </div>
  );
}