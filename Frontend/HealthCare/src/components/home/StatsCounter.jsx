import React from 'react';

export default function StatsCounter() {
  const stats = [
    { label: 'Annual Patient Consultations', value: '25,000+', icon: '🏥' },
    { label: 'Board-Certified Specialists', value: '50+', icon: '👨‍⚕️' },
    { label: 'Emergency Triage Response Accuracy', value: '99.8%', icon: '⚡' },
    { label: 'NABH / HIPAA Compliance Quality Rating', value: '5/5 ★', icon: '🛡️' }
  ];

  return (
    <div style={{ background: 'linear-gradient(135deg, #0a2540 0%, #1e3a8a 100%)', padding: '50px 24px', borderRadius: '24px', color: '#fff', margin: '40px 0' }}>
      <div style={{ textAlign: 'center', marginBottom: '32px' }}>
        <span style={{ background: 'rgba(0, 168, 150, 0.25)', color: '#02c39a', padding: '6px 16px', borderRadius: '20px', fontWeight: 700, fontSize: '0.85rem' }}>
          NATIONAL HEALTHCARE METRICS
        </span>
        <h2 style={{ fontSize: '2rem', marginTop: '10px' }}>Excellence in Clinical Care & Patient Satisfaction</h2>
      </div>

      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', gap: '24px', textCenter: 'center' }}>
        {stats.map((item, idx) => (
          <div key={idx} style={{ background: 'rgba(255, 255, 255, 0.08)', backdropFilter: 'blur(10px)', border: '1px solid rgba(255, 255, 255, 0.15)', borderRadius: '16px', padding: '24px', textAlign: 'center' }}>
            <div style={{ fontSize: '2.5rem', marginBottom: '8px' }}>{item.icon}</div>
            <div style={{ fontSize: '2.2rem', fontWeight: 800, color: '#02c39a', letterSpacing: '-0.02em' }}>{item.value}</div>
            <div style={{ fontSize: '0.9rem', color: '#cbd5e1', marginTop: '4px', fontWeight: 600 }}>{item.label}</div>
          </div>
        ))}
      </div>
    </div>
  );
}
