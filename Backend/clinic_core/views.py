from django.http import HttpResponse

def visual_frontend_home_view(request):
    """
    Renders Microsoft Fluent Design Level Enterprise Healthcare Portal directly at root URL '/'.
    Inspired by Microsoft Healthcare Cloud Systems & Fluent UI Design Standards.
    """
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Pure Health Clinic - Microsoft Enterprise Healthcare Cloud Portal</title>
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
        <style>
            :root {
                /* Microsoft Fluent UI Palette */
                --ms-blue: #0078d4;
                --ms-dark-navy: #002050;
                --ms-teal: #008272;
                --ms-emerald: #107c41;
                --ms-crimson: #d13438;
                --ms-neutral-light: #f3f2f1;
                --ms-acrylic-bg: rgba(255, 255, 255, 0.85);
                --font-heading: 'Outfit', 'Segoe UI', sans-serif;
                --font-body: 'Plus Jakarta Sans', 'Segoe UI', sans-serif;
            }
            * { box-sizing: border-box; margin: 0; padding: 0; }
            body { font-family: var(--font-body); background-color: #faf9f8; color: #201f1e; line-height: 1.6; }
            h1, h2, h3, h4 { font-family: var(--font-heading); font-weight: 700; letter-spacing: -0.01em; }
            
            /* Microsoft Top Bar */
            .top-bar {
                background: linear-gradient(90deg, #002050 0%, #0078d4 100%);
                color: #ffffff; padding: 12px 32px; display: flex; justify-content: space-between;
                align-items: center; font-size: 0.88rem; border-bottom: 2px solid var(--ms-teal);
            }
            .triage-badge {
                background-color: var(--ms-crimson); color: white; font-weight: 700;
                padding: 4px 14px; border-radius: 20px; font-size: 0.78rem; text-transform: uppercase;
                letter-spacing: 0.05em; animation: pulse 2s infinite;
            }
            @keyframes pulse {
                0% { box-shadow: 0 0 0 0 rgba(209, 52, 56, 0.7); }
                70% { box-shadow: 0 0 0 10px rgba(209, 52, 56, 0); }
                100% { box-shadow: 0 0 0 0 rgba(209, 52, 56, 0); }
            }
            
            /* Microsoft Fluent Hero Section */
            .hero-section {
                background: linear-gradient(135deg, #002050 0%, #0078d4 60%, #008272 100%);
                color: white; padding: 70px 32px 90px; text-align: center; position: relative;
            }
            .fluent-chip {
                background: rgba(255,255,255,0.18); padding: 6px 20px; border-radius: 30px;
                font-size: 0.85rem; font-weight: 700; letter-spacing: 0.05em; display: inline-block;
                border: 1px solid rgba(255,255,255,0.3); backdrop-filter: blur(10px);
            }
            
            /* Acrylic Container & Fluent Cards */
            .container { max-width: 1180px; margin: -50px auto 60px; padding: 0 24px; position: relative; z-index: 10; }
            .fluent-card {
                background: var(--ms-acrylic-bg); backdrop-filter: blur(20px); -webkit-backdrop-filter: blur(20px);
                border-radius: 20px; padding: 36px; box-shadow: 0 24px 60px rgba(0, 32, 80, 0.12);
                border: 1px solid rgba(255, 255, 255, 0.8); margin-bottom: 32px;
            }
            .input-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(230px, 1fr)); gap: 18px; margin-top: 24px; }
            .form-control {
                width: 100%; padding: 13px 18px; border: 1.5px solid #e1dfdd; border-radius: 12px;
                font-family: var(--font-body); font-size: 0.95rem; outline: none; transition: all 0.2s ease;
                background-color: #ffffff;
            }
            .form-control:focus { border-color: var(--ms-blue); box-shadow: 0 0 0 4px rgba(0, 120, 212, 0.15); }
            
            .btn-fluent {
                background: linear-gradient(135deg, var(--ms-blue) 0%, var(--ms-teal) 100%);
                color: white; font-weight: 700; font-size: 1.05rem; padding: 15px 30px;
                border: none; border-radius: 12px; cursor: pointer; width: 100%; margin-top: 24px;
                box-shadow: 0 8px 24px rgba(0, 120, 212, 0.25); transition: all 0.2s ease;
            }
            .btn-fluent:hover { transform: translateY(-2px); box-shadow: 0 12px 32px rgba(0, 120, 212, 0.35); }
            
            /* Roster Grid */
            .roster-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 24px; margin-top: 24px; }
            .roster-card {
                background: #ffffff; border: 1px solid #edebe9; border-radius: 16px; padding: 24px;
                box-shadow: 0 4px 16px rgba(0, 0, 0, 0.04);
            }
            .duty-badge { padding: 4px 12px; border-radius: 14px; font-size: 0.75rem; font-weight: 700; float: right; }
            .on_duty { background: #dff6dd; color: #107c41; }
            .in_surgery { background: #fde7e9; color: #d13438; }
            
            /* Receipt Slip */
            .receipt-box {
                background: #ffffff; border: 2px dashed var(--ms-blue); border-radius: 20px;
                padding: 28px; margin-top: 24px; text-align: center; box-shadow: 0 12px 36px rgba(0, 120, 212, 0.1);
            }
            .token-num { font-size: 2.5rem; font-weight: 800; color: var(--ms-blue); margin: 12px 0; letter-spacing: 0.05em; }
        </style>
    </head>
    <body>
        <div class="top-bar">
            <div><span class="triage-badge">🚨 24x7 EMERGENCY TRIAGE</span> &nbsp; Helpline: +91 9811122233 | 1800-11-2233</div>
            <div>🏢 Microsoft Enterprise Certified Healthcare Cloud Systems &nbsp;|&nbsp; 🛡️ HIPAA & NABH Compliant</div>
        </div>

        <section class="hero-section">
            <div class="fluent-chip">MICROSOFT HEALTHCARE CLOUD & CLINICAL CORE</div>
            <h1 style="font-size: 3.2rem; margin: 18px 0; line-height: 1.15;">
                Enterprise Healthcare Portal & OPD Scheduling System
            </h1>
            <p style="font-size: 1.2rem; color: #e2e8f0; max-width: 800px; margin: 0 auto 28px;">
                Led by <strong>Dr. Divit Shah</strong> (Medical Director), delivering high-availability clinical care, auto-generated OPD tokens, secure tele-health video rooms, and real-time emergency triage escalation.
            </p>
            <div>
                <a href="#booking" style="background: #008272; color: white; padding: 14px 32px; border-radius: 12px; font-weight: 800; text-decoration: none; display: inline-block; margin-right: 12px; box-shadow: 0 8px 24px rgba(0, 130, 114, 0.3);">
                  🎟️ Book OPD Token
                </a>
                <a href="/api/docs/" target="_blank" style="background: rgba(255,255,255,0.2); color: white; padding: 14px 32px; border-radius: 12px; font-weight: 700; text-decoration: none; display: inline-block; border: 1px solid rgba(255,255,255,0.3);">
                  📄 Swagger API Docs
                </a>
            </div>
        </section>

        <div class="container" id="booking">
            <!-- OPD Booking Card -->
            <div class="fluent-card">
                <div style="text-align: center; margin-bottom: 24px;">
                    <span style="background: #002050; color: white; padding: 5px 16px; border-radius: 20px; font-size: 0.8rem; font-weight: 700;">
                      🏥 CLINICAL OPD REGISTRATION PORTAL
                    </span>
                    <h2 style="color: #002050; margin-top: 10px; font-size: 2rem;">Instant Clinical OPD Token & Tele-Health Scheduling</h2>
                    <p style="color: #605e5c; font-size: 0.98rem;">Enterprise Token Generator, Teams/Jitsi Video Room Links & Emergency Triage Alerts</p>
                </div>

                <div id="booking-form-container">
                    <form id="opdForm">
                        <div class="input-grid">
                            <div>
                                <label style="font-weight: 600; font-size: 0.88rem; color: #323130;">Patient Full Name *</label>
                                <input type="text" id="patient_name" required placeholder="e.g. Rajesh Sharma" class="form-control">
                            </div>
                            <div>
                                <label style="font-weight: 600; font-size: 0.88rem; color: #323130;">Mobile Phone *</label>
                                <input type="tel" id="patient_phone" required placeholder="e.g. +91 9811122233" class="form-control">
                            </div>
                            <div>
                                <label style="font-weight: 600; font-size: 0.88rem; color: #323130;">Attending Specialist Doctor *</label>
                                <select id="doctor_name" class="form-control">
                                    <option value="Dr. Divit Shah">Dr. Divit Shah (Medical Director - ₹600)</option>
                                    <option value="Dr. Rahul Mehta">Dr. Rahul Mehta (Senior Cardiologist - ₹1000)</option>
                                    <option value="Dr. Anjali Sharma">Dr. Anjali Sharma (Chronic Care - ₹750)</option>
                                </select>
                            </div>
                            <div>
                                <label style="font-weight: 600; font-size: 0.88rem; color: #323130;">Clinical Department *</label>
                                <select id="department" class="form-control">
                                    <option value="General_Consultation">General Consultation & Preventive Care</option>
                                    <option value="Cardiology">Cardiology & Heart Care</option>
                                    <option value="Chronic_Care">Chronic Disease Care</option>
                                </select>
                            </div>
                            <div>
                                <label style="font-weight: 600; font-size: 0.88rem; color: #323130;">Priority / Triage *</label>
                                <select id="priority" class="form-control">
                                    <option value="routine">Routine OPD Visit</option>
                                    <option value="urgent">Urgent Priority Referral</option>
                                    <option value="emergency">🚨 Emergency Triage (Instant Red Alert)</option>
                                </select>
                            </div>
                            <div>
                                <label style="font-weight: 600; font-size: 0.88rem; color: #323130;">Mode of Consultation *</label>
                                <select id="consultation_type" class="form-control">
                                    <option value="OPD">Outpatient Department (OPD Visit)</option>
                                    <option value="Teleconsultation">📹 Tele-Health Video Consultation</option>
                                </select>
                            </div>
                        </div>

                        <button type="submit" class="btn-fluent" id="submitBtn">🎟️ Book OPD Appointment & Generate Token</button>
                    </form>
                </div>

                <div id="receipt-container" style="display: none;"></div>
            </div>

            <!-- Doctor Duty Roster Card -->
            <div class="fluent-card">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px;">
                    <div>
                        <span style="color: #008272; font-size: 0.8rem; font-weight: 700; text-transform: uppercase;">🩺 LIVE CLINICAL DUTY ROSTER</span>
                        <h2 style="color: #002050; font-size: 1.8rem;">Attending Specialist Duty Status & OPD Shift Schedule</h2>
                    </div>
                </div>
                <div class="roster-grid">
                    <div class="roster-card">
                        <span class="duty-badge on_duty">On Duty (OPD Active)</span>
                        <h3 style="color: #002050; font-size: 1.2rem;">Dr. Divit Shah</h3>
                        <p style="color: #605e5c; font-size: 0.88rem;">General Physician & Medical Director</p>
                        <div style="margin-top: 12px; font-size: 0.85rem; border-top: 1px solid #edebe9; padding-top: 10px;">
                            📍 <strong>Location:</strong> OPD Room 101<br>
                            ⏰ <strong>Shift:</strong> 09:00 AM - 05:00 PM<br>
                            💳 <strong>Fee:</strong> ₹600
                        </div>
                    </div>
                    <div class="roster-card">
                        <span class="duty-badge on_duty">On Duty (OPD Active)</span>
                        <h3 style="color: #002050; font-size: 1.2rem;">Dr. Rahul Mehta</h3>
                        <p style="color: #605e5c; font-size: 0.88rem;">Senior Cardiologist & Heart Specialist</p>
                        <div style="margin-top: 12px; font-size: 0.85rem; border-top: 1px solid #edebe9; padding-top: 10px;">
                            📍 <strong>Location:</strong> OPD Room 204<br>
                            ⏰ <strong>Shift:</strong> 10:00 AM - 04:00 PM<br>
                            💳 <strong>Fee:</strong> ₹1000
                        </div>
                    </div>
                    <div class="roster-card">
                        <span class="duty-badge in_surgery">In Surgery</span>
                        <h3 style="color: #002050; font-size: 1.2rem;">Dr. Anjali Sharma</h3>
                        <p style="color: #605e5c; font-size: 0.88rem;">Chronic Care & Diabetes Specialist</p>
                        <div style="margin-top: 12px; font-size: 0.85rem; border-top: 1px solid #edebe9; padding-top: 10px;">
                            📍 <strong>Location:</strong> Operation Theater 2<br>
                            ⏰ <strong>Shift:</strong> 02:00 PM - 08:00 PM<br>
                            💳 <strong>Fee:</strong> ₹750
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <footer style="background: #002050; color: #a19f9d; padding: 40px; text-align: center; border-top: 4px solid #008272;">
            <p style="color: white; font-weight: 700; font-size: 1.1rem;">🏥 Pure Health Clinic & Hospital Systems</p>
            <p style="font-size: 0.9rem; margin-top: 6px;">Microsoft Enterprise Certified Cloud Architecture | PY Digital Services Pvt. Ltd.</p>
            <p style="font-size: 0.85rem; margin-top: 12px;">© 2026 Pure Health Clinic. Full-Stack Enterprise Deployment by Udbhav.</p>
        </footer>

        <script>
            document.getElementById('opdForm').addEventListener('submit', async function(e) {
                e.preventDefault();
                const btn = document.getElementById('submitBtn');
                btn.innerHTML = '⏳ Generating Clinical OPD Token...';
                btn.disabled = true;

                const payload = {
                    patient_name: document.getElementById('patient_name').value,
                    patient_phone: document.getElementById('patient_phone').value,
                    doctor_name: document.getElementById('doctor_name').value,
                    department: document.getElementById('department').value,
                    priority: document.getElementById('priority').value,
                    consultation_type: document.getElementById('consultation_type').value,
                    consultation_fee_inr: 600,
                    appointment_date: new Date().toISOString()
                };

                try {
                    const response = await fetch('/api/admin/appointments/', {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify(payload)
                    });
                    const data = await response.json();

                    if (response.ok) {
                        document.getElementById('booking-form-container').style.display = 'none';
                        const receipt = document.getElementById('receipt-container');
                        receipt.style.display = 'block';
                        receipt.innerHTML = `
                            <div class="receipt-box">
                                <span style="background: #dff6dd; color: #107c41; padding: 6px 18px; border-radius: 20px; font-weight: 700; font-size: 0.85rem;">
                                    ✅ OPD APPOINTMENT BOOKED SUCCESSFULLY
                                </span>
                                <div class="token-num">\${data.token_number}</div>
                                <p style="font-size: 1.05rem;"><strong>Patient:</strong> \${data.patient_name} &nbsp;|&nbsp; <strong>Phone:</strong> \${data.patient_phone}</p>
                                <p><strong>Doctor:</strong> \${data.doctor_name} &nbsp;|&nbsp; <strong>Department:</strong> \${data.department}</p>
                                <p><strong>Consultation Fee:</strong> ₹\${data.consultation_fee_inr} &nbsp;|&nbsp; <strong>Status:</strong> \${data.status.toUpperCase()}</p>
                                \${data.video_room_url ? `<div style="background: #eff6fc; padding: 12px; border-radius: 10px; margin-top: 14px;">📹 <strong>Tele-Health Video Link:</strong> <a href="\${data.video_room_url}" target="_blank" style="color: #0078d4; font-weight: 700;">\${data.video_room_url}</a></div>` : ''}
                                \${data.emergency_escalation_code ? `<div style="background: #fde7e9; color: #d13438; padding: 12px; border-radius: 10px; margin-top: 14px; font-weight: 700;">🚨 EMERGENCY ALERT CODE: \${data.emergency_escalation_code}</div>` : ''}
                                <div style="margin-top: 24px; display: flex; gap: 12px; justify-content: center;">
                                    <button onclick="window.open('/api/admin/appointments/\${data.id}/slip/', '_blank')" style="background: #0078d4; color: white; border: none; padding: 12px 24px; border-radius: 10px; font-weight: 700; cursor: pointer;">🖨️ Print Reception OPD Slip</button>
                                    <button onclick="location.reload()" style="background: #f3f2f1; border: 1px solid #e1dfdd; padding: 12px 24px; border-radius: 10px; font-weight: 700; cursor: pointer;">Book Another OPD</button>
                                </div>
                            </div>
                        `;
                    } else {
                        alert('Booking failed. Please check inputs.');
                    }
                } catch (err) {
                    alert('Network error connecting to API.');
                } finally {
                    btn.innerHTML = '🎟️ Book OPD Appointment & Generate Token';
                    btn.disabled = false;
                }
            });
        </script>
    </body>
    </html>
    """
    return HttpResponse(html_content, content_type="text/html")
