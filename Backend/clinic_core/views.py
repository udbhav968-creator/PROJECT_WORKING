from django.http import HttpResponse

def visual_frontend_home_view(request):
    """
    Renders the Full Visual Working Healthcare Portal Frontend Website directly at root URL '/'.
    Includes interactive OPD booking form, live doctor duty roster, emergency triage bar,
    and printable reception OPD token slips.
    """
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Pure Health Clinic - Enterprise Healthcare Portal</title>
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
        <style>
            :root {
                --primary-navy: #0a2540;
                --primary-blue: #0066cc;
                --accent-teal: #00a896;
                --accent-emerald: #02c39a;
                --emergency-red: #e63946;
                --font-heading: 'Outfit', sans-serif;
                --font-body: 'Plus Jakarta Sans', sans-serif;
            }
            * { box-sizing: border-box; margin: 0; padding: 0; }
            body { font-family: var(--font-body); background-color: #f1f5f9; color: #0f172a; line-height: 1.6; }
            h1, h2, h3, h4 { font-family: var(--font-heading); font-weight: 700; }
            
            /* Top Announcement Bar */
            .top-bar {
                background: linear-gradient(90deg, #0a2540 0%, #1e3a8a 100%);
                color: #ffffff; padding: 10px 24px; display: flex; justify-content: space-between;
                align-items: center; font-size: 0.88rem; border-bottom: 2px solid var(--accent-teal);
            }
            .triage-badge {
                background-color: var(--emergency-red); color: white; font-weight: 700;
                padding: 4px 12px; border-radius: 20px; font-size: 0.78rem; text-transform: uppercase;
                animation: pulse 2s infinite;
            }
            @keyframes pulse {
                0% { box-shadow: 0 0 0 0 rgba(230, 57, 70, 0.7); }
                70% { box-shadow: 0 0 0 10px rgba(230, 57, 70, 0); }
                100% { box-shadow: 0 0 0 0 rgba(230, 57, 70, 0); }
            }
            
            /* Hero Banner */
            .hero-section {
                background: linear-gradient(135deg, #0a2540 0%, #004080 50%, #00a896 100%);
                color: white; padding: 60px 24px 80px; text-align: center; position: relative;
            }
            .hero-badge {
                background: rgba(255,255,255,0.15); padding: 6px 18px; border-radius: 30px;
                font-size: 0.85rem; font-weight: 700; letter-spacing: 0.05em; display: inline-block;
            }
            
            /* Container & Cards */
            .container { max-width: 1140px; margin: -50px auto 50px; padding: 0 20px; position: relative; z-index: 10; }
            .card-panel {
                background: #ffffff; border-radius: 20px; padding: 32px;
                box-shadow: 0 20px 50px rgba(10, 37, 64, 0.15); border: 1px solid rgba(0, 168, 150, 0.2);
                margin-bottom: 30px;
            }
            .input-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 16px; margin-top: 20px; }
            .form-control {
                width: 100%; padding: 12px 16px; border: 1.5px solid #cbd5e1; border-radius: 10px;
                font-family: var(--font-body); font-size: 0.95rem; outline: none; transition: all 0.2s ease;
            }
            .form-control:focus { border-color: var(--primary-blue); box-shadow: 0 0 0 4px rgba(0,102,204,0.15); }
            
            .btn-submit {
                background: linear-gradient(135deg, var(--primary-blue) 0%, var(--accent-teal) 100%);
                color: white; font-weight: 700; font-size: 1.05rem; padding: 14px 28px;
                border: none; border-radius: 12px; cursor: pointer; width: 100%; margin-top: 20px;
                transition: transform 0.2s ease;
            }
            .btn-submit:hover { transform: translateY(-2px); }
            
            /* Doctor Roster Grid */
            .roster-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 20px; margin-top: 20px; }
            .roster-card {
                background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 16px; padding: 20px;
            }
            .duty-badge { padding: 4px 10px; border-radius: 12px; font-size: 0.75rem; font-weight: 700; float: right; }
            .on_duty { background: #dcfce7; color: #15803d; }
            .in_surgery { background: #fee2e2; color: #b91c1c; }
            
            /* Token Receipt */
            .receipt-box {
                background: #f8fafc; border: 2px dashed var(--primary-blue); border-radius: 16px;
                padding: 24px; margin-top: 20px; text-align: center;
            }
            .token-num { font-size: 2.2rem; font-weight: 800; color: var(--primary-blue); margin: 10px 0; }
        </style>
    </head>
    <body>
        <div class="top-bar">
            <div><span class="triage-badge">🚨 24x7 EMERGENCY TRIAGE</span> &nbsp; Helpline: +91 9811122233 | 1800-11-2233</div>
            <div>🏥 Pure Health Clinic & Hospital Systems &nbsp;|&nbsp; 🛡️ NABH Certified</div>
        </div>

        <section class="hero-section">
            <div class="hero-badge">PURE HEALTH CLINIC & HOSPITAL SYSTEMS</div>
            <h1 style="font-size: 3rem; margin: 16px 0;">Personalized Patient Care & Enterprise OPD Portal</h1>
            <p style="font-size: 1.15rem; color: #e2e8f0; max-width: 750px; margin: 0 auto 24px;">
                Led by <strong>Dr. Divit Shah</strong> (Medical Director), providing compassionate, high-quality, tailored medical OPD services, tele-consultation video rooms, and 24x7 emergency triage.
            </p>
            <div>
                <a href="#booking" style="background: #02c39a; color: #0a2540; padding: 12px 28px; border-radius: 10px; font-weight: 800; text-decoration: none; display: inline-block; margin-right: 10px;">🎟️ Book OPD Token</a>
                <a href="/api/docs/" target="_blank" style="background: rgba(255,255,255,0.2); color: white; padding: 12px 28px; border-radius: 10px; font-weight: 700; text-decoration: none; display: inline-block; border: 1px solid rgba(255,255,255,0.3);">📄 API Swagger Docs</a>
            </div>
        </section>

        <div class="container" id="booking">
            <!-- OPD Booking Widget -->
            <div class="card-panel">
                <div style="text-align: center; margin-bottom: 20px;">
                    <span style="background: #0a2540; color: white; padding: 4px 14px; border-radius: 20px; font-size: 0.8rem; font-weight: 700;">🏥 CLINICAL OPD REGISTRATION</span>
                    <h2 style="color: #0a2540; margin-top: 8px;">Instant OPD Token & Tele-Health Appointment Scheduling</h2>
                    <p style="color: #64748b; font-size: 0.95rem;">Auto-generates Clinical Tokens, Jitsi Tele-Health Links & Emergency Triage Alerts</p>
                </div>

                <div id="booking-form-container">
                    <form id="opdForm">
                        <div class="input-grid">
                            <div>
                                <label style="font-weight: 600; font-size: 0.85rem;">Patient Full Name *</label>
                                <input type="text" id="patient_name" required placeholder="e.g. Rajesh Sharma" class="form-control">
                            </div>
                            <div>
                                <label style="font-weight: 600; font-size: 0.85rem;">Mobile Phone *</label>
                                <input type="tel" id="patient_phone" required placeholder="e.g. +91 9811122233" class="form-control">
                            </div>
                            <div>
                                <label style="font-weight: 600; font-size: 0.85rem;">Attending Specialist Doctor *</label>
                                <select id="doctor_name" class="form-control">
                                    <option value="Dr. Divit Shah">Dr. Divit Shah (Medical Director - ₹600)</option>
                                    <option value="Dr. Rahul Mehta">Dr. Rahul Mehta (Cardiology - ₹1000)</option>
                                    <option value="Dr. Anjali Sharma">Dr. Anjali Sharma (Chronic Care - ₹750)</option>
                                </select>
                            </div>
                            <div>
                                <label style="font-weight: 600; font-size: 0.85rem;">Clinical Department *</label>
                                <select id="department" class="form-control">
                                    <option value="General_Consultation">General Consultation & Preventive Care</option>
                                    <option value="Cardiology">Cardiology & Heart Care</option>
                                    <option value="Chronic_Care">Chronic Disease Care</option>
                                </select>
                            </div>
                            <div>
                                <label style="font-weight: 600; font-size: 0.85rem;">Priority / Triage *</label>
                                <select id="priority" class="form-control">
                                    <option value="routine">Routine OPD Visit</option>
                                    <option value="urgent">Urgent Priority</option>
                                    <option value="emergency">🚨 Emergency Triage</option>
                                </select>
                            </div>
                            <div>
                                <label style="font-weight: 600; font-size: 0.85rem;">Mode of Consultation *</label>
                                <select id="consultation_type" class="form-control">
                                    <option value="OPD">Outpatient Department (OPD Visit)</option>
                                    <option value="Teleconsultation">📹 Tele-Health Video Consultation</option>
                                </select>
                            </div>
                        </div>

                        <button type="submit" class="btn-submit" id="submitBtn">🎟️ Book OPD Appointment & Generate Token</button>
                    </form>
                </div>

                <div id="receipt-container" style="display: none;"></div>
            </div>

            <!-- Doctor Duty Roster -->
            <div class="card-panel">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px;">
                    <div>
                        <span style="color: #00a896; font-size: 0.8rem; font-weight: 700;">🩺 LIVE DUTY ROSTER</span>
                        <h2 style="color: #0a2540;">Attending Specialist Duty Status</h2>
                    </div>
                </div>
                <div class="roster-grid">
                    <div class="roster-card">
                        <span class="duty-badge on_duty">On Duty (OPD Active)</span>
                        <h3 style="color: #0a2540;">Dr. Divit Shah</h3>
                        <p style="color: #64748b; font-size: 0.85rem;">General Physician & Medical Director</p>
                        <div style="margin-top: 10px; font-size: 0.85rem; border-top: 1px solid #e2e8f0; padding-top: 8px;">
                            📍 OPD Room 101 &nbsp;|&nbsp; ⏰ 09:00 AM - 05:00 PM &nbsp;|&nbsp; 💳 Fee: ₹600
                        </div>
                    </div>
                    <div class="roster-card">
                        <span class="duty-badge on_duty">On Duty (OPD Active)</span>
                        <h3 style="color: #0a2540;">Dr. Rahul Mehta</h3>
                        <p style="color: #64748b; font-size: 0.85rem;">Senior Cardiologist & Heart Specialist</p>
                        <div style="margin-top: 10px; font-size: 0.85rem; border-top: 1px solid #e2e8f0; padding-top: 8px;">
                            📍 OPD Room 204 &nbsp;|&nbsp; ⏰ 10:00 AM - 04:00 PM &nbsp;|&nbsp; 💳 Fee: ₹1000
                        </div>
                    </div>
                    <div class="roster-card">
                        <span class="duty-badge in_surgery">In Surgery</span>
                        <h3 style="color: #0a2540;">Dr. Anjali Sharma</h3>
                        <p style="color: #64748b; font-size: 0.85rem;">Chronic Care & Diabetes Specialist</p>
                        <div style="margin-top: 10px; font-size: 0.85rem; border-top: 1px solid #e2e8f0; padding-top: 8px;">
                            📍 Operation Theater 2 &nbsp;|&nbsp; ⏰ 02:00 PM - 08:00 PM &nbsp;|&nbsp; 💳 Fee: ₹750
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <footer style="background: #0a2540; color: #94a3b8; padding: 30px; text-align: center; border-top: 4px solid #00a896;">
            <p style="color: white; font-weight: 700;">🏥 Pure Health Clinic & Hospital Systems</p>
            <p style="font-size: 0.85rem; margin-top: 4px;">© 2026 Pure Health Clinic. Full-Stack Enterprise Deployment.</p>
        </footer>

        <script>
            document.getElementById('opdForm').addEventListener('submit', async function(e) {
                e.preventDefault();
                const btn = document.getElementById('submitBtn');
                btn.innerHTML = '⏳ Generating OPD Token...';
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
                                <span style="background: #dcfce7; color: #15803d; padding: 4px 14px; border-radius: 20px; font-weight: 700; font-size: 0.85rem;">
                                    ✅ OPD APPOINTMENT BOOKED SUCCESSFULLY
                                </span>
                                <div class="token-num">\${data.token_number}</div>
                                <p><strong>Patient:</strong> \${data.patient_name} &nbsp;|&nbsp; <strong>Phone:</strong> \${data.patient_phone}</p>
                                <p><strong>Doctor:</strong> \${data.doctor_name} &nbsp;|&nbsp; <strong>Department:</strong> \${data.department}</p>
                                <p><strong>Consultation Fee:</strong> ₹\${data.consultation_fee_inr} &nbsp;|&nbsp; <strong>Status:</strong> \${data.status.toUpperCase()}</p>
                                \${data.video_room_url ? `<div style="background: #e0f2fe; padding: 10px; border-radius: 8px; margin-top: 12px;">📹 <strong>Tele-Health Video Link:</strong> <a href="\${data.video_room_url}" target="_blank" style="color: #0284c7; font-weight: 700;">\${data.video_room_url}</a></div>` : ''}
                                \${data.emergency_escalation_code ? `<div style="background: #fee2e2; color: #b91c1c; padding: 10px; border-radius: 8px; margin-top: 12px; font-weight: 700;">🚨 EMERGENCY ALERT CODE: \${data.emergency_escalation_code}</div>` : ''}
                                <div style="margin-top: 20px; display: flex; gap: 10px; justify-content: center;">
                                    <button onclick="window.open('/api/admin/appointments/\${data.id}/slip/', '_blank')" style="background: #0a2540; color: white; border: none; padding: 10px 20px; border-radius: 8px; font-weight: 700; cursor: pointer;">🖨️ Print Reception OPD Slip</button>
                                    <button onclick="location.reload()" style="background: #e2e8f0; border: none; padding: 10px 20px; border-radius: 8px; font-weight: 700; cursor: pointer;">Book Another OPD</button>
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
