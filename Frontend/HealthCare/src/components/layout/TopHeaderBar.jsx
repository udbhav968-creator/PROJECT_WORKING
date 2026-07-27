import React from 'react';

export default function TopHeaderBar() {
  return (
    <div className="top-announcement-bar">
      <div style={{ display: 'flex', alignItems: 'center', gap: '12px' }}>
        <span className="triage-badge-red pulse-emergency">🚨 24x7 EMERGENCY TRIAGE</span>
        <span style={{ fontWeight: 600 }}>Helpline: +91 9811122233 | 1800-11-2233</span>
      </div>

      <div style={{ display: 'flex', alignItems: 'center', gap: '20px', fontSize: '0.85rem' }}>
        <span>🏥 Pure Health Clinic & Hospital Systems</span>
        <span>🛡️ NABH Certified</span>
        <a href="https://project-working-snojkumar968-9939s-projects.vercel.app/api/docs/" target="_blank" rel="noopener noreferrer" style={{ color: '#02c39a', textDecoration: 'none', fontWeight: 700 }}>
          ⚡ API Portal (Swagger UI)
        </a>
      </div>
    </div>
  );
}
