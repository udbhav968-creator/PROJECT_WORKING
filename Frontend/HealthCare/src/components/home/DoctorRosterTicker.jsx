import React from 'react';

export default function DoctorRosterTicker() {
  const doctors = [
    {
      name: 'Dr. Divit Shah',
      dept: 'General Physician & Medical Director',
      status: 'on_duty',
      statusText: 'On Duty (OPD Active)',
      room: 'OPD Room 101',
      shift: '09:00 AM - 05:00 PM',
      fee: '₹600'
    },
    {
      name: 'Dr. Rahul Mehta',
      dept: 'Senior Cardiologist & Heart Care Specialist',
      status: 'on_duty',
      statusText: 'On Duty (OPD Active)',
      room: 'OPD Room 204',
      shift: '10:00 AM - 04:00 PM',
      fee: '₹1000'
    },
    {
      name: 'Dr. Anjali Sharma',
      dept: 'Chronic Disease & Diabetes Specialist',
      status: 'in_surgery',
      statusText: 'In OT / Procedure',
      room: 'Operation Theater 2',
      shift: '02:00 PM - 08:00 PM',
      fee: '₹750'
    },
    {
      name: 'Dr. Ayesha Khan',
      dept: 'Pediatrics & Child Wellness Specialist',
      status: 'on_duty',
      statusText: 'On Duty (OPD Active)',
      room: 'OPD Room 105',
      shift: '09:00 AM - 01:00 PM',
      fee: '₹500'
    }
  ];

  return (
    <div style={{ marginTop: '40px', marginBottom: '40px' }}>
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '20px' }}>
        <div>
          <span style={{ fontSize: '0.8rem', fontWeight: 700, color: '#00a896', textTransform: 'uppercase', letterSpacing: '0.05em' }}>
            🩺 LIVE CLINICAL ROSTER
          </span>
          <h2 style={{ fontSize: '1.6rem', color: '#0a2540' }}>Attending Specialist Duty Status & OPD Shift Schedule</h2>
        </div>
        <a href="#booking" style={{ background: '#0a2540', color: '#fff', padding: '10px 20px', borderRadius: '10px', textDecoration: 'none', fontWeight: 700, fontSize: '0.9rem' }}>
          View Live Queue →
        </a>
      </div>

      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(260px, 1fr))', gap: '20px' }}>
        {doctors.map((doc, idx) => (
          <div key={idx} className="glass-panel" style={{ padding: '20px' }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start' }}>
              <h3 style={{ fontSize: '1.15rem', color: '#0a2540' }}>{doc.name}</h3>
              <span className={`duty-status-badge ${doc.status}`}>{doc.statusText}</span>
            </div>
            <p style={{ color: '#64748b', fontSize: '0.85rem', margin: '4px 0 12px' }}>{doc.dept}</p>

            <div style={{ borderTop: '1px solid #e2e8f0', paddingTop: '12px', fontSize: '0.85rem', display: 'flex', flexDirection: 'column', gap: '6px' }}>
              <div>📍 <strong>Location:</strong> {doc.room}</div>
              <div>⏰ <strong>Shift:</strong> {doc.shift}</div>
              <div>💳 <strong>Consultation Fee:</strong> {doc.fee}</div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
