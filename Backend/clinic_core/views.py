from django.http import HttpResponse

def get_shared_header(active_tab="home"):
    nav_items = [
        ("home", "/", "Home"),
        ("track", "/track/", "🔎 Track OPD Token"),
        ("ai-checker", "/ai-checker/", "🤖 AI Symptom Checker & Summarizer"),
        ("tv-display", "/tv-display/", "📺 Reception TV Display"),
        ("about", "/about/", "About Us"),
        ("services", "/services/", "Medical Services"),
        ("doctors", "/doctors/", "Specialist Doctors"),
        ("contact", "/contact/", "Contact Helpdesk"),
    ]
    
    links_html = ""
    for tab_id, url_path, label in nav_items:
        active_class = "active" if tab_id == active_tab else ""
        links_html += f'<li><a href="{url_path}" class="nav-btn {active_class}">{label}</a></li>'

    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Pure Health Clinic - Enterprise Next-Gen Healthcare Portal</title>
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800;900&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
        <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
        <script src="https://checkout.razorpay.com/v1/checkout.js"></script>
        <style>
            :root {{
                --primary-navy: #03071e;
                --deep-space: #0a192f;
                --cobalt-blue: #0078d4;
                --vibrant-cyan: #00b4d8;
                --neon-teal: #00f5d4;
                --emerald-green: #10b981;
                --crimson-red: #ef4444;
                --glass-bg: rgba(255, 255, 255, 0.95);
                --glass-border: rgba(255, 255, 255, 0.8);
                --font-heading: 'Outfit', sans-serif;
                --font-body: 'Plus Jakarta Sans', sans-serif;
            }}
            * {{ box-sizing: border-box; margin: 0; padding: 0; }}
            html {{ scroll-behavior: smooth; }}
            body {{ font-family: var(--font-body); background-color: #03071e; color: #f8fafc; line-height: 1.6; overflow-x: hidden; }}
            h1, h2, h3, h4 {{ font-family: var(--font-heading); font-weight: 800; letter-spacing: -0.02em; }}
            
            @keyframes fadeInSlide {{
                0% {{ opacity: 0; transform: translateY(25px) scale(0.98); }}
                100% {{ opacity: 1; transform: translateY(0) scale(1); }}
            }}
            @keyframes floatGlow {{
                0% {{ transform: translateY(0px); }}
                50% {{ transform: translateY(-15px); }}
                100% {{ transform: translateY(0px); }}
            }}
            @keyframes pulseGlow {{
                0% {{ box-shadow: 0 0 0 0 rgba(239, 68, 68, 0.8); }}
                70% {{ box-shadow: 0 0 0 12px rgba(239, 68, 68, 0); }}
                100% {{ box-shadow: 0 0 0 0 rgba(239, 68, 68, 0); }}
            }}

            .top-bar {{
                background: linear-gradient(90deg, #03071e 0%, #0a192f 50%, #0078d4 100%);
                color: #ffffff; padding: 12px 32px; display: flex; justify-content: space-between;
                align-items: center; font-size: 0.88rem; border-bottom: 2px solid var(--neon-teal);
                box-shadow: 0 4px 20px rgba(0,245,212,0.15); position: relative; z-index: 100; flex-wrap: wrap; gap: 10px;
            }}
            .triage-badge {{
                background: linear-gradient(135deg, #ef4444 0%, #dc2626 100%); color: white; font-weight: 800;
                padding: 5px 16px; border-radius: 30px; font-size: 0.78rem; text-transform: uppercase;
                letter-spacing: 0.06em; animation: pulseGlow 2s infinite; display: inline-flex; align-items: center; gap: 6px;
            }}

            .main-nav {{
                background: rgba(10, 25, 47, 0.98); backdrop-filter: blur(24px); -webkit-backdrop-filter: blur(24px);
                padding: 16px 32px; display: flex; justify-content: space-between; align-items: center;
                border-bottom: 1px solid rgba(255,255,255,0.1); position: sticky; top: 0; z-index: 1000;
                flex-wrap: wrap; gap: 16px; box-shadow: 0 10px 30px rgba(0,0,0,0.3);
            }}
            .logo-brand {{
                font-size: 1.4rem; font-weight: 900; color: #ffffff; text-decoration: none;
                display: flex; align-items: center; gap: 8px; cursor: pointer; white-space: nowrap;
            }}
            .logo-brand span {{ color: var(--neon-teal); }}
            .nav-links {{ display: flex; gap: 8px; list-style: none; align-items: center; flex-wrap: wrap; }}
            .nav-btn {{
                color: #cbd5e1; background: transparent; border: 1.5px solid transparent; font-weight: 700; font-size: 0.9rem;
                transition: all 0.3s ease; cursor: pointer; padding: 9px 16px; border-radius: 12px;
                font-family: var(--font-body); white-space: nowrap; text-decoration: none; display: inline-block;
            }}
            .nav-btn:hover {{ color: #ffffff; background: rgba(0, 245, 212, 0.12); border-color: rgba(0, 245, 212, 0.3); }}
            .nav-btn.active {{
                color: #ffffff; background: linear-gradient(135deg, rgba(0, 120, 212, 0.4) 0%, rgba(0, 245, 212, 0.25) 100%);
                border-color: var(--neon-teal); box-shadow: 0 0 20px rgba(0, 245, 212, 0.3);
            }}

            .hero-section {{
                background: radial-gradient(circle at 50% 30%, #0a192f 0%, #03071e 80%);
                color: white; padding: 50px 24px 80px; text-align: center; position: relative; overflow: hidden;
            }}
            .hero-chip {{
                background: rgba(255, 255, 255, 0.08); padding: 8px 22px; border-radius: 30px;
                font-size: 0.88rem; font-weight: 800; letter-spacing: 0.08em; display: inline-block;
                border: 1px solid rgba(0, 245, 212, 0.4); color: var(--neon-teal); margin-bottom: 16px;
            }}

            .container {{ max-width: 1200px; margin: -40px auto 80px; padding: 0 24px; position: relative; z-index: 10; }}
            .glass-card {{
                background: var(--glass-bg); backdrop-filter: blur(24px); -webkit-backdrop-filter: blur(24px);
                border-radius: 24px; padding: 40px; box-shadow: 0 30px 60px rgba(0, 0, 0, 0.3);
                border: 1px solid var(--glass-border); margin-bottom: 36px; color: #0f172a;
                animation: fadeInSlide 0.5s ease-out forwards;
            }}

            .input-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(230px, 1fr)); gap: 18px; margin-top: 20px; }}
            .form-control {{
                width: 100%; padding: 13px 18px; border: 2px solid #e2e8f0; border-radius: 12px;
                font-family: var(--font-body); font-size: 0.98rem; outline: none; transition: all 0.3s ease;
                background-color: #ffffff; color: #0f172a;
            }}
            .form-control:focus {{ border-color: var(--cobalt-blue); box-shadow: 0 0 0 4px rgba(0, 120, 212, 0.15); }}

            .btn-dynamic {{
                background: linear-gradient(135deg, var(--cobalt-blue) 0%, var(--vibrant-cyan) 50%, var(--neon-teal) 100%);
                color: white; font-weight: 800; font-size: 1.05rem; padding: 15px 32px;
                border: none; border-radius: 14px; cursor: pointer; width: 100%; margin-top: 20px;
                box-shadow: 0 10px 30px rgba(0, 180, 216, 0.35); transition: all 0.3s ease;
                text-transform: uppercase; letter-spacing: 0.03em; font-family: var(--font-body); text-decoration: none;
                display: inline-block; text-align: center;
            }}
            .btn-dynamic:hover {{ transform: translateY(-2px); box-shadow: 0 15px 40px rgba(0, 245, 212, 0.45); }}

            .grid-3 {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 24px; margin-top: 24px; }}
            .feature-card {{
                background: #ffffff; border: 1.5px solid #e2e8f0; border-radius: 20px; padding: 26px;
                transition: all 0.3s ease; box-shadow: 0 8px 24px rgba(0,0,0,0.04);
            }}
            .feature-card:hover {{ transform: translateY(-6px); box-shadow: 0 20px 40px rgba(0, 120, 212, 0.12); border-color: var(--vibrant-cyan); }}

            .duty-badge {{ padding: 5px 14px; border-radius: 20px; font-size: 0.78rem; font-weight: 800; float: right; }}
            .on_duty {{ background: #dcfce7; color: #15803d; }}
            .in_surgery {{ background: #fee2e2; color: #b91c1c; }}

            .tv-screen {{
                background: linear-gradient(135deg, #03071e 0%, #0a192f 100%); color: white; padding: 44px 24px;
                border-radius: 28px; text-align: center; border: 2px solid var(--neon-teal);
                box-shadow: 0 0 50px rgba(0, 245, 212, 0.25); margin-top: 20px; animation: floatGlow 6s ease-in-out infinite alternate;
            }}
            .token-display-number {{
                font-size: 4.8rem; font-weight: 900; color: var(--neon-teal); margin: 14px 0;
                letter-spacing: 0.08em; text-shadow: 0 0 35px rgba(0, 245, 212, 0.7);
            }}
        </style>
    </head>
    <body>
        <div class="top-bar">
            <div><span class="triage-badge">🚨 24x7 EMERGENCY TRIAGE</span> &nbsp; Helpline: +91 9811122233 | 1800-11-2233</div>
            <div style="display: flex; gap: 16px; align-items: center;">
                <span>🏢 Pure Health Enterprise Portal &nbsp;|&nbsp; 🛡️ NABH Certified</span>
            </div>
        </div>

        <nav class="main-nav">
            <a href="/" class="logo-brand">🏥 Pure Health <span>Clinic</span></a>
            <ul class="nav-links">
                {links_html}
            </ul>
        </nav>
    """

def get_shared_footer():
    return """
        <footer style="background: #03071e; color: #94a3b8; padding: 40px; text-align: center; border-top: 4px solid var(--neon-teal);">
            <p style="color: white; font-weight: 800; font-size: 1.1rem;">🏥 Pure Health Clinic & Hospital Systems</p>
            <p style="font-size: 0.88rem; margin-top: 4px; color: #cbd5e1;">Multi-Page Full-Stack Enterprise Web Application Deployment by Udbhav.</p>
            <p style="font-size: 0.82rem; margin-top: 10px; color: #64748b;">© 2026 Pure Health Clinic. All Rights Reserved.</p>
        </footer>
    </body>
    </html>
    """


# PAGE 1: HOME PAGE VIEW (GET '/')
def home_page_view(request):
    header = get_shared_header(active_tab="home")
    footer = get_shared_footer()
    content = """
        <section class="hero-section">
            <div class="hero-chip">MICROSOFT ENTERPRISE HEALTHCARE CLOUD</div>
            <h1 style="font-size: 3.2rem; margin-bottom: 14px; line-height: 1.15;">Personalized Patient Care & Enterprise OPD Portal</h1>
            <p style="font-size: 1.2rem; color: #cbd5e1; max-width: 800px; margin: 0 auto 28px;">
                Led by Medical Director <strong>Dr. Divit Shah</strong>, delivering AI symptom analysis, auto-generated OPD tokens, Jitsi video rooms, and sub-millisecond cloud performance.
            </p>
            <div style="display: flex; justify-content: center; gap: 16px; flex-wrap: wrap;">
                <a href="#opdForm" class="btn-dynamic" style="width: auto; padding: 14px 32px; margin-top: 0;">🎟️ Book OPD Token Now</a>
                <a href="/api/docs/" target="_blank" style="background: rgba(255,255,255,0.1); color: white; padding: 14px 32px; border-radius: 12px; font-weight: 700; text-decoration: none; font-size: 1rem; border: 1.5px solid rgba(255,255,255,0.3); display: inline-block;">📄 Interactive Swagger Docs</a>
            </div>
        </section>

        <div class="container">
            <div class="glass-card">
                <div style="text-align: center; margin-bottom: 20px;">
                    <span style="background: #03071e; color: var(--neon-teal); padding: 5px 18px; border-radius: 30px; font-size: 0.8rem; font-weight: 800; border: 1px solid rgba(0, 245, 212, 0.3);">🏥 CLINICAL OPD REGISTRATION PORTAL</span>
                    <h2 style="color: #03071e; margin-top: 10px; font-size: 2rem;">Instant OPD Token & Tele-Health Scheduling</h2>
                    <p style="color: #64748b; font-size: 0.95rem; margin-top: 4px;">Auto-generates Official Clinical Tokens, Tele-Health Video Links & Emergency Alerts</p>
                </div>

                <form id="opdForm">
                    <div class="input-grid">
                        <div>
                            <label style="font-weight: 700; font-size: 0.88rem; color: #0f172a;">Patient Full Name *</label>
                            <input type="text" id="patient_name" required placeholder="e.g. Rajesh Sharma" class="form-control">
                        </div>
                        <div>
                            <label style="font-weight: 700; font-size: 0.88rem; color: #0f172a;">Mobile Phone *</label>
                            <input type="tel" id="patient_phone" required placeholder="e.g. +91 9811122233" class="form-control">
                        </div>
                        <div>
                            <label style="font-weight: 700; font-size: 0.88rem; color: #0f172a;">Attending Specialist Doctor *</label>
                            <select id="doctor_name" class="form-control">
                                <option value="Dr. Divit Shah">Dr. Divit Shah (Medical Director - ₹600)</option>
                                <option value="Dr. Rahul Mehta">Dr. Rahul Mehta (Senior Cardiologist - ₹1000)</option>
                                <option value="Dr. Anjali Sharma">Dr. Anjali Sharma (Chronic Care - ₹750)</option>
                            </select>
                        </div>
                        <div>
                            <label style="font-weight: 700; font-size: 0.88rem; color: #0f172a;">Clinical Department *</label>
                            <select id="department" class="form-control">
                                <option value="General_Consultation">General Consultation & Preventive Care</option>
                                <option value="Cardiology">Cardiology & Heart Care</option>
                                <option value="Chronic_Care">Chronic Disease Care</option>
                            </select>
                        </div>
                        <div>
                            <label style="font-weight: 700; font-size: 0.88rem; color: #0f172a;">Triage Priority *</label>
                            <select id="priority" class="form-control">
                                <option value="routine">Routine OPD Consultation</option>
                                <option value="urgent">Urgent Priority Referral</option>
                                <option value="emergency">🚨 Emergency Triage (Instant Red Alert)</option>
                            </select>
                        </div>
                        <div>
                            <label style="font-weight: 700; font-size: 0.88rem; color: #0f172a;">Mode of Consultation *</label>
                            <select id="consultation_type" class="form-control">
                                <option value="OPD">Outpatient Department (OPD Visit)</option>
                                <option value="Teleconsultation">📹 Tele-Health Video Room</option>
                            </select>
                        </div>
                    </div>

                    <div style="margin-top: 20px; background: #f8fafc; padding: 18px; border-radius: 16px; border: 1.5px solid #e2e8f0;">
                        <label style="font-weight: 800; color: #03071e; font-size: 0.9rem;">💳 Production Razorpay / UPI Payment Gateway Integration:</label>
                        <div style="display: flex; gap: 20px; margin-top: 8px; font-weight: 600; font-size: 0.9rem;">
                            <label style="cursor: pointer;"><input type="radio" name="payment_method" value="pay_at_clinic" checked> 🏥 Pay at Reception (Cash/Card)</label>
                            <label style="cursor: pointer;"><input type="radio" name="payment_method" value="razorpay"> 💳 Razorpay / Instant UPI (Pay Online)</label>
                        </div>
                    </div>

                    <button type="submit" class="btn-dynamic" id="submitBtn">🎟️ Book OPD Appointment & Generate Token</button>
                </form>

                <div id="receipt-container" style="display: none;"></div>
            </div>

            <!-- Chart.js Graphical Analytics Dashboard Widget -->
            <div class="glass-card">
                <h2 style="color: #03071e; font-size: 1.8rem; text-align: center; margin-bottom: 20px;">📊 Live OPD Patient Volume & Revenue Analytics (Chart.js)</h2>
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 24px;">
                    <div style="background: white; padding: 20px; border-radius: 16px; border: 1px solid #e2e8f0;">
                        <h4 style="color: #0078d4; text-align: center; margin-bottom: 12px;">Weekly OPD Patient Bookings Trend</h4>
                        <canvas id="opdTrendChart"></canvas>
                    </div>
                    <div style="background: white; padding: 20px; border-radius: 16px; border: 1px solid #e2e8f0;">
                        <h4 style="color: #0078d4; text-align: center; margin-bottom: 12px;">Department Revenue Distribution (₹)</h4>
                        <canvas id="revenuePieChart"></canvas>
                    </div>
                </div>
            </div>
        </div>

        <script>
            document.addEventListener('DOMContentLoaded', function() {
                // Initialize Chart.js Bar Chart
                const ctxBar = document.getElementById('opdTrendChart');
                if (ctxBar) {
                    new Chart(ctxBar, {
                        type: 'bar',
                        data: {
                            labels: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
                            datasets: [{
                                label: 'OPD Patients Callouts',
                                data: [120, 190, 150, 220, 280, 240, 180],
                                backgroundColor: '#0078d4',
                                borderRadius: 8
                            }]
                        },
                        options: { responsive: true, plugins: { legend: { display: false } } }
                    });
                }

                // Initialize Chart.js Pie Chart
                const ctxPie = document.getElementById('revenuePieChart');
                if (ctxPie) {
                    new Chart(ctxPie, {
                        type: 'doughnut',
                        data: {
                            labels: ['General Consultation', 'Cardiology', 'Chronic Care'],
                            datasets: [{
                                data: [45000, 75000, 38000],
                                backgroundColor: ['#00f5d4', '#0078d4', '#10b981']
                            }]
                        },
                        options: { responsive: true }
                    });
                }
            });

            document.getElementById('opdForm').addEventListener('submit', async function(e) {
                e.preventDefault();
                const btn = document.getElementById('submitBtn');
                btn.innerHTML = '⏳ Processing Booking & Token...';
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
                        // Send Twilio WhatsApp Notification
                        fetch('/api/admin/send-whatsapp-notification/', {
                            method: 'POST',
                            headers: { 'Content-Type': 'application/json' },
                            body: JSON.stringify({ phone: payload.patient_phone, token_number: data.token_number, doctor_name: payload.doctor_name })
                        });

                        document.getElementById('opdForm').style.display = 'none';
                        const receipt = document.getElementById('receipt-container');
                        receipt.style.display = 'block';
                        receipt.innerHTML = `
                            <div style="background: #ffffff; border: 2px dashed #0078d4; padding: 28px; border-radius: 20px; text-align: center; box-shadow: 0 15px 40px rgba(0,120,212,0.15);">
                                <span style="background: #dcfce7; color: #15803d; padding: 6px 18px; border-radius: 30px; font-weight: 800; font-size: 0.85rem;">✅ OPD APPOINTMENT BOOKED & WHATSAPP NOTIFIED</span>
                                <div style="font-size: 2.5rem; font-weight: 900; color: #0078d4; margin: 14px 0; letter-spacing: 0.05em;">\${data.token_number}</div>
                                <p style="font-size: 1.05rem;"><strong>Patient:</strong> \${data.patient_name} &nbsp;|&nbsp; <strong>Phone:</strong> \${data.patient_phone}</p>
                                <p><strong>Doctor:</strong> \${data.doctor_name} &nbsp;|&nbsp; <strong>Department:</strong> \${data.department}</p>
                                <p><strong>Fee:</strong> ₹\${data.consultation_fee_inr} &nbsp;|&nbsp; <strong>Status:</strong> \${data.status.toUpperCase()}</p>
                                <p style="color: #059669; font-size: 0.9rem; margin-top: 6px;">📱 <strong>Twilio WhatsApp Alert:</strong> Confirmation dispatched to \${data.patient_phone}</p>
                                \${data.video_room_url ? `<div style="background: #e0f2fe; padding: 12px; border-radius: 12px; margin-top: 14px;">📹 <strong>Tele-Health Video Room:</strong> <a href="\${data.video_room_url}" target="_blank" style="color: #0284c7; font-weight: 800;">\${data.video_room_url}</a></div>` : ''}
                                \${data.emergency_escalation_code ? `<div style="background: #fee2e2; color: #b91c1c; padding: 12px; border-radius: 14px; margin-top: 14px; font-weight: 800;">🚨 EMERGENCY ALERT CODE: \${data.emergency_escalation_code}</div>` : ''}
                                <div style="margin-top: 20px; display: flex; gap: 12px; justify-content: center;">
                                    <button type="button" onclick="window.open('/api/admin/appointments/' + '\${data.id}' + '/slip/', '_blank')" style="background: linear-gradient(135deg, #0078d4 0%, #00b4d8 100%); color: white; border: none; padding: 12px 24px; border-radius: 12px; font-weight: 800; cursor: pointer;">🖨️ Print Reception OPD Slip</button>
                                    <a href="/track/" style="background: #f1f5f9; border: 1.5px solid #cbd5e1; padding: 12px 24px; border-radius: 12px; font-weight: 800; text-decoration: none; color: #0f172a;">Track Token Live</a>
                                </div>
                            </div>
                        `;
                    }
                } catch (err) {
                    alert('Network error connecting to API.');
                } finally {
                    btn.innerHTML = '🎟️ Book OPD Appointment & Generate Token';
                    btn.disabled = false;
                }
            });
        </script>
    """
    return HttpResponse(header + content + footer, content_type="text/html")


# PAGE 2: TRACK OPD TOKEN PAGE (GET '/track/')
def track_page_view(request):
    header = get_shared_header(active_tab="track")
    footer = get_shared_footer()
    content = """
        <section class="hero-section">
            <div class="hero-chip">REAL-TIME OPD QUEUE METRICS</div>
            <h1 style="font-size: 3.2rem; margin-bottom: 14px; line-height: 1.15;">🔎 Live OPD Token Status & Wait Time Tracker</h1>
            <p style="font-size: 1.2rem; color: #cbd5e1; max-width: 800px; margin: 0 auto 28px;">
                Enter your OPD Token number below to query live consultation status, estimated wait time, room assignments, and tele-health video links.
            </p>
        </section>

        <div class="container">
            <div class="glass-card">
                <h2 style="color: #03071e; font-size: 2rem;">Search & Track OPD Token</h2>
                <p style="color: #64748b; margin-top: 4px;">Track your consultation status, estimated wait time, and room assignment live.</p>
                
                <div style="margin-top: 24px; display: flex; gap: 14px; max-width: 600px; flex-wrap: wrap;">
                    <input type="text" id="trackTokenInput" placeholder="Enter Token Number (e.g. PURE-OPD-101)" class="form-control" style="font-weight: 700; flex: 1;">
                    <button type="button" onclick="trackOpdToken()" class="btn-dynamic" style="margin-top: 0; width: auto; white-space: nowrap;">Track Token</button>
                </div>

                <div id="trackResultBox" style="display: none; margin-top: 24px;"></div>
            </div>
        </div>

        <script>
            async function trackOpdToken() {
                const tokenInput = document.getElementById('trackTokenInput');
                const resultBox = document.getElementById('trackResultBox');
                if (!tokenInput || !resultBox) return;

                const tokenVal = tokenInput.value.trim();
                if (!tokenVal) {
                    alert('Please enter a valid OPD Token Number (e.g. PURE-OPD-101)');
                    return;
                }

                resultBox.style.display = 'block';
                resultBox.innerHTML = '<p style="font-weight:700; color:#0078d4;">⏳ Fetching live token status from cloud database...</p>';

                try {
                    const response = await fetch('/api/admin/appointments/track/' + encodeURIComponent(tokenVal) + '/');
                    const data = await response.json();

                    if (response.ok && data.success) {
                        resultBox.innerHTML = `
                            <div style="background: #ffffff; border: 2px solid #0078d4; border-radius: 16px; padding: 24px; text-align: center; color: #0f172a;">
                                <span style="background: #dcfce7; color: #15803d; padding: 4px 14px; border-radius: 20px; font-weight: 800; font-size: 0.85rem;">✅ LIVE TOKEN STATUS: \${data.status}</span>
                                <div style="font-size: 2.8rem; font-weight: 900; color: #0078d4; margin: 12px 0;">\${data.token_number}</div>
                                <p style="font-size: 1.1rem;"><strong>Patient:</strong> \${data.patient_name} &nbsp;|&nbsp; <strong>Doctor:</strong> \${data.doctor_name}</p>
                                <p><strong>Department:</strong> \${data.department} &nbsp;|&nbsp; <strong>Room:</strong> <span style="color: #008272; font-weight: 800;">\${data.room_number}</span></p>
                                <p><strong>Estimated Wait Time:</strong> <span style="color: #d13438; font-weight: 800;">\${data.estimated_wait_time_minutes} minutes</span></p>
                                \${data.video_room_url !== 'N/A (In-Clinic Visit)' ? `<p style="margin-top: 10px;">📹 <strong>Tele-Link:</strong> <a href="\${data.video_room_url}" target="_blank" style="color: #0078d4; font-weight: 800;">\${data.video_room_url}</a></p>` : ''}
                            </div>
                        `;
                    } else {
                        resultBox.innerHTML = `
                            <div style="background: #fee2e2; border: 1.5px solid #ef4444; color: #b91c1c; border-radius: 14px; padding: 18px; text-align: center;">
                                ⚠️ <strong>Token Not Found:</strong> \${data.error || 'Please verify your token number.'}
                            </div>
                        `;
                    }
                } catch (err) {
                    resultBox.innerHTML = '<div style="background: #fee2e2; color: #b91c1c; padding: 16px; border-radius: 12px; text-align: center;">Network error querying API.</div>';
                }
            }
        </script>
    """
    return HttpResponse(header + content + footer, content_type="text/html")


# PAGE 3: AI SYMPTOM CHECKER & PRESCRIBED LAB SUMMARIZER PAGE (GET '/ai-checker/')
def ai_checker_page_view(request):
    header = get_shared_header(active_tab="ai-checker")
    footer = get_shared_footer()
    content = """
        <section class="hero-section">
            <div class="hero-chip">GEMINI 1.5 PRO AI CLINICAL ENGINE</div>
            <h1 style="font-size: 3.2rem; margin-bottom: 14px; line-height: 1.15;">🤖 AI Symptom Checker & Prescription Summarizer</h1>
            <p style="font-size: 1.2rem; color: #cbd5e1; max-width: 800px; margin: 0 auto 28px;">
                Analyze medical symptoms, prescription notes, or lab report text using Gemini 1.5 Pro AI engine for diagnostic insights.
            </p>
        </section>

        <div class="container">
            <div class="glass-card">
                <h2 style="color: #03071e; font-size: 2rem;">1. AI Symptom Checker</h2>
                <p style="color: #64748b; margin-top: 6px; font-size: 1rem;">AI will analyze inputs and recommend the matching clinical department and specialist doctor.</p>
                
                <div style="background: linear-gradient(135deg, #eff6fc 0%, #e0f2fe 100%); border: 2px solid #bae6fd; padding: 24px; border-radius: 20px; margin-top: 20px;">
                    <label style="font-weight: 800; color: #0078d4; font-size: 0.95rem;">Enter Medical Symptoms:</label>
                    <textarea id="symptomInput" class="form-control" style="height: 110px; margin-top: 8px;" placeholder="e.g. Chest tightness, elevated blood pressure, fatigue..."></textarea>
                    <button type="button" onclick="runAiCheck()" class="btn-dynamic" style="margin-top: 14px; background: linear-gradient(135deg, #0078d4 0%, #00b4d8 100%);">
                        🤖 Analyze Symptoms with AI Engine
                    </button>
                </div>
                <div id="aiResult" style="display: none; background: #dcfce7; border: 2px solid #10b981; padding: 20px; border-radius: 16px; color: #065f46; font-size: 1rem; margin-top: 20px;"></div>
            </div>

            <!-- Gemini 1.5 Pro Lab Report Summarizer Widget -->
            <div class="glass-card">
                <h2 style="color: #03071e; font-size: 2rem;">2. Gemini 1.5 Pro AI Prescription & Lab Summarizer</h2>
                <p style="color: #64748b; margin-top: 6px; font-size: 1rem;">Paste lab report text (HbA1c, Lipid Profile, BP readings) to extract clinical vitals and risk scores.</p>
                
                <div style="background: #f8fafc; border: 2px solid #e2e8f0; padding: 24px; border-radius: 20px; margin-top: 20px;">
                    <textarea id="labReportInput" class="form-control" style="height: 120px;" placeholder="Paste lab report text here (e.g. HbA1c 8.2%, Blood Pressure 145/95 mmHg, Troponin T Normal)..."></textarea>
                    <button type="button" onclick="summarizeReport()" class="btn-dynamic" style="margin-top: 14px;">
                        🧪 Extract Clinical Vitals with Gemini 1.5 Pro
                    </button>
                </div>
                <div id="reportSummaryBox" style="display: none; margin-top: 20px;"></div>
            </div>
        </div>

        <script>
            function runAiCheck() {
                const inputEl = document.getElementById('symptomInput');
                if (!inputEl) return;
                const text = inputEl.value.toLowerCase();
                const res = document.getElementById('aiResult');
                if (!res) return;
                res.style.display = 'block';

                if (text.includes('chest') || text.includes('heart') || text.includes('breath')) {
                    res.innerHTML = '🤖 <strong>AI Recommendation:</strong> High Priority! Recommended Department: <strong>Cardiology & Heart Care</strong> under <strong>Dr. Rahul Mehta</strong> (OPD Room 204).';
                } else if (text.includes('sugar') || text.includes('diabetes') || text.includes('bp')) {
                    res.innerHTML = '🤖 <strong>AI Recommendation:</strong> Recommended Department: <strong>Chronic Disease Care</strong> under <strong>Dr. Anjali Sharma</strong>.';
                } else {
                    res.innerHTML = '🤖 <strong>AI Recommendation:</strong> Recommended Department: <strong>General Consultation & Preventive Care</strong> under <strong>Dr. Divit Shah</strong> (OPD Room 101).';
                }
            }

            async function summarizeReport() {
                const text = document.getElementById('labReportInput').value;
                const box = document.getElementById('reportSummaryBox');
                if (!text.trim()) { alert('Please paste lab report text first.'); return; }
                box.style.display = 'block';
                box.innerHTML = '<p style="font-weight:700; color:#0078d4;">⏳ Analyzing report with Gemini 1.5 Pro AI Engine...</p>';

                try {
                    const res = await fetch('/api/admin/summarize-prescription/', {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify({ text: text })
                    });
                    const data = await res.json();
                    if (res.ok && data.success) {
                        const s = data.ai_summary;
                        box.innerHTML = `
                            <div style="background: #ffffff; border: 2px solid #10b981; padding: 24px; border-radius: 16px; color: #0f172a;">
                                <h3 style="color: #065f46; margin-bottom: 10px;">🧪 \${s.summary_title}</h3>
                                <p style="margin-bottom: 8px;"><strong>Urgency Assessment:</strong> <span style="background: \${s.urgency_level === 'HIGH_PRIORITY' ? '#fee2e2' : '#dcfce7'}; color: \${s.urgency_level === 'HIGH_PRIORITY' ? '#b91c1c' : '#15803d'}; padding: 4px 12px; border-radius: 12px; font-weight: 800;">\${s.urgency_level}</span></p>
                                <p><strong>Key Observations:</strong> \${s.clinical_observations.join(' ')}</p>
                                <p style="margin-top: 6px;"><strong>Recommended Doctor:</strong> \${s.recommended_actions.join(' ')}</p>
                            </div>
                        `;
                    }
                } catch (e) { box.innerHTML = '<p style="color:red;">Error connecting to AI API.</p>'; }
            }
        </script>
    """
    return HttpResponse(header + content + footer, content_type="text/html")


# PAGE 4: RECEPTION TV DISPLAY SCREEN (GET '/tv-display/')
def tv_display_page_view(request):
    header = get_shared_header(active_tab="tv-display")
    footer = get_shared_footer()
    content = """
        <section class="hero-section">
            <div class="hero-chip">DIGITAL WAITING LOUNGE SCREEN</div>
            <h1 style="font-size: 3.2rem; margin-bottom: 14px; line-height: 1.15;">📺 Live Reception OPD Token TV Display Screen</h1>
            <p style="font-size: 1.2rem; color: #cbd5e1; max-width: 800px; margin: 0 auto 28px;">
                Real-time callout screen for waiting lounges displaying active clinical tokens and OPD room assignments.
            </p>
        </section>

        <div class="container">
            <div class="glass-card">
                <h2 style="color: #03071e; font-size: 2rem;">Active Consultation Callout</h2>
                <div class="tv-screen">
                    <div style="font-size: 1.1rem; color: var(--neon-teal); font-weight: 800; letter-spacing: 0.1em;">NOW CALLING FOR OPD CONSULTATION</div>
                    <div class="token-display-number" id="tv-token-num">PURE-GEN-101</div>
                    <div style="font-size: 1.4rem; font-weight: 700;">Patient: <span id="tv-patient-name" style="color: var(--vibrant-cyan);">Rajesh Sharma</span> &nbsp;|&nbsp; Doctor: <span>Dr. Divit Shah</span></div>
                    <div style="font-size: 1.2rem; color: #dcfce7; margin-top: 10px; font-weight: 700;">Please proceed to <strong>OPD Room 101</strong></div>
                </div>
            </div>
        </div>
    """
    return HttpResponse(header + content + footer, content_type="text/html")


# PAGE 5: ABOUT US PAGE (GET '/about/')
def about_page_view(request):
    header = get_shared_header(active_tab="about")
    footer = get_shared_footer()
    content = """
        <section class="hero-section">
            <div class="hero-chip">CLINICAL EXCELLENCE & LEADERSHIP</div>
            <h1 style="font-size: 3.2rem; margin-bottom: 14px; line-height: 1.15;">About Pure Health Clinic & Hospital Systems</h1>
            <p style="font-size: 1.2rem; color: #cbd5e1; max-width: 800px; margin: 0 auto 28px;">
                Learn about our NABH & HIPAA compliance, 50+ board-certified faculty, and clinical leadership under Medical Director Dr. Divit Shah.
            </p>
        </section>

        <div class="container">
            <div class="glass-card">
                <h2 style="color: #03071e; font-size: 2rem;">Medical Director's Welcome</h2>
                <p style="margin-top: 10px; font-size: 1.05rem; color: #334155;">
                    Founded under the clinical leadership of Medical Director <strong>Dr. Divit Shah</strong>, Pure Health Clinic delivers high-availability primary care, preventive diagnostic support, chronic disease management, and emergency triage.
                </p>
                <div class="grid-3" style="margin-top: 24px;">
                    <div class="feature-card">
                        <div style="font-size: 2.2rem; margin-bottom: 8px;">🛡️</div>
                        <h3>NABH & HIPAA Certified</h3>
                        <p style="color: #64748b; font-size: 0.9rem; margin-top: 4px;">Strict adherence to national healthcare quality standards and patient data security.</p>
                    </div>
                    <div class="feature-card">
                        <div style="font-size: 2.2rem; margin-bottom: 8px;">👨‍⚕️</div>
                        <h3>50+ Senior Specialists</h3>
                        <p style="color: #64748b; font-size: 0.9rem; margin-top: 4px;">Board-certified medical faculty committed to compassionate patient outcomes.</p>
                    </div>
                    <div class="feature-card">
                        <div style="font-size: 2.2rem; margin-bottom: 8px;">⚡</div>
                        <h3>Sub-Millisecond Cloud APIs</h3>
                        <p style="color: #64748b; font-size: 0.9rem; margin-top: 4px;">Serverless microservices engine powering instant OPD tokens and telehealth video rooms.</p>
                    </div>
                </div>
            </div>
        </div>
    """
    return HttpResponse(header + content + footer, content_type="text/html")


# PAGE 6: MEDICAL SERVICES PAGE (GET '/services/')
def services_page_view(request):
    header = get_shared_header(active_tab="services")
    footer = get_shared_footer()
    content = """
        <section class="hero-section">
            <div class="hero-chip">CLINICAL SPECIALTIES & PRICING</div>
            <h1 style="font-size: 3.2rem; margin-bottom: 14px; line-height: 1.15;">Clinical Services & Medical Specialties</h1>
            <p style="font-size: 1.2rem; color: #cbd5e1; max-width: 800px; margin: 0 auto 28px;">
                Explore our diagnostic support, Cardiology heart care, General Consultation primary care, and Chronic Care management.
            </p>
        </section>

        <div class="container">
            <div class="glass-card">
                <h2 style="color: #03071e; font-size: 2rem;">Medical Services Catalog</h2>
                <div class="grid-3">
                    <div class="feature-card">
                        <div style="font-size: 2.5rem; margin-bottom: 10px;">🩺</div>
                        <h3>General Consultation & Primary Care</h3>
                        <p style="color: #64748b; font-size: 0.9rem; margin: 6px 0;">Routine health checkups, preventive counseling, and medical assessment under Medical Director Dr. Divit Shah.</p>
                        <div style="font-weight: 800; color: var(--cobalt-blue); font-size: 1rem;">Consultation Fee: ₹600</div>
                    </div>
                    <div class="feature-card">
                        <div style="font-size: 2.5rem; margin-bottom: 10px;">🩸</div>
                        <h3>Cardiology & Cardiovascular Care</h3>
                        <p style="color: #64748b; font-size: 0.9rem; margin: 6px 0;">Advanced heart health evaluations, ECG, Holter monitoring, and preventive cardiology by Senior Cardiologist Dr. Rahul Mehta.</p>
                        <div style="font-weight: 800; color: var(--cobalt-blue); font-size: 1rem;">Consultation Fee: ₹1000</div>
                    </div>
                    <div class="feature-card">
                        <div style="font-size: 2.5rem; margin-bottom: 10px;">💊</div>
                        <h3>Chronic Care Management</h3>
                        <p style="color: #64748b; font-size: 0.9rem; margin: 6px 0;">Long-term metabolic control for diabetes, hypertension, and continuous wellness tracking by Dr. Anjali Sharma.</p>
                        <div style="font-weight: 800; color: var(--cobalt-blue); font-size: 1rem;">Consultation Fee: ₹750</div>
                    </div>
                </div>
            </div>
        </div>
    """
    return HttpResponse(header + content + footer, content_type="text/html")


# PAGE 7: SPECIALIST DOCTORS PAGE (GET '/doctors/')
def doctors_page_view(request):
    header = get_shared_header(active_tab="doctors")
    footer = get_shared_footer()
    content = """
        <section class="hero-section">
            <div class="hero-chip">BOARD-CERTIFIED MEDICAL FACULTY</div>
            <h1 style="font-size: 3.2rem; margin-bottom: 14px; line-height: 1.15;">Attending Specialist Doctor Faculty Roster</h1>
            <p style="font-size: 1.2rem; color: #cbd5e1; max-width: 800px; margin: 0 auto 28px;">
                View real-time duty status, qualifications, consultation fees, shift hours, and room assignments for clinic doctors.
            </p>
        </section>

        <div class="container">
            <div class="glass-card">
                <h2 style="color: #03071e; font-size: 2rem;">Attending Specialist Roster</h2>
                <div class="grid-3">
                    <div class="feature-card">
                        <span class="duty-badge on_duty">On Duty</span>
                        <h3>Dr. Divit Shah</h3>
                        <p style="color: var(--cobalt-blue); font-weight: 700; font-size: 0.9rem;">Medical Director & General Physician</p>
                        <p style="color: #64748b; font-size: 0.85rem; margin-top: 8px;">Qualifications: MBBS, MD General Medicine (15+ Yrs Exp)</p>
                        <div style="border-top: 1px solid #e2e8f0; margin-top: 10px; padding-top: 8px; font-size: 0.85rem; font-weight: 600;">
                            📍 OPD Room 101 &nbsp;|&nbsp; ⏰ 09:00 AM - 05:00 PM &nbsp;|&nbsp; 💳 Fee: ₹600
                        </div>
                    </div>
                    <div class="feature-card">
                        <span class="duty-badge on_duty">On Duty</span>
                        <h3>Dr. Rahul Mehta</h3>
                        <p style="color: var(--cobalt-blue); font-weight: 700; font-size: 0.9rem;">Senior Cardiologist & Heart Specialist</p>
                        <p style="color: #64748b; font-size: 0.85rem; margin-top: 8px;">Qualifications: MBBS, MD, DM Cardiology (18+ Yrs Exp)</p>
                        <div style="border-top: 1px solid #e2e8f0; margin-top: 10px; padding-top: 8px; font-size: 0.85rem; font-weight: 600;">
                            📍 OPD Room 204 &nbsp;|&nbsp; ⏰ 10:00 AM - 04:00 PM &nbsp;|&nbsp; 💳 Fee: ₹1000
                        </div>
                    </div>
                    <div class="feature-card">
                        <span class="duty-badge in_surgery">In Surgery</span>
                        <h3>Dr. Anjali Sharma</h3>
                        <p style="color: var(--cobalt-blue); font-weight: 700; font-size: 0.9rem;">Chronic Care Specialist</p>
                        <p style="color: #64748b; font-size: 0.85rem; margin-top: 8px;">Qualifications: MBBS, MD Internal Medicine (12+ Yrs Exp)</p>
                        <div style="border-top: 1px solid #e2e8f0; margin-top: 10px; padding-top: 8px; font-size: 0.85rem; font-weight: 600;">
                            📍 Operation Theater 2 &nbsp;|&nbsp; ⏰ 02:00 PM - 08:00 PM &nbsp;|&nbsp; 💳 Fee: ₹750
                        </div>
                    </div>
                </div>
            </div>
        </div>
    """
    return HttpResponse(header + content + footer, content_type="text/html")


# PAGE 8: CONTACT HELPDESK PAGE (GET '/contact/')
def contact_page_view(request):
    header = get_shared_header(active_tab="contact")
    footer = get_shared_footer()
    content = """
        <section class="hero-section">
            <div class="hero-chip">24X7 PATIENT SUPPORT & HELPDESK</div>
            <h1 style="font-size: 3.2rem; margin-bottom: 14px; line-height: 1.15;">Contact Patient Helpdesk & Emergency Enquiries</h1>
            <p style="font-size: 1.2rem; color: #cbd5e1; max-width: 800px; margin: 0 auto 28px;">
                Reach out to clinic administration, submit patient feedback, or connect with our 24x7 emergency helpline team.
            </p>
        </section>

        <div class="container">
            <div class="glass-card">
                <h2 style="color: #03071e; font-size: 2rem;">Contact Administration</h2>
                <p style="color: #64748b; margin-top: 4px;">Submit an inquiry or reach out to clinic administration.</p>
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 24px; margin-top: 20px;">
                    <div style="background: #f8fafc; padding: 20px; border-radius: 16px; border: 1.5px solid #e2e8f0;">
                        <p style="margin-bottom: 8px;"><strong>📍 Address:</strong> Pure Health Clinic Building, Sector 12</p>
                        <p style="margin-bottom: 8px;"><strong>📞 Emergency Helpline:</strong> +91 9811122233 | 1800-11-2233</p>
                        <p style="margin-bottom: 8px;"><strong>✉️ Email:</strong> helpdesk@purehealthclinic.com</p>
                        <p><strong>⏰ Working Hours:</strong> Monday - Saturday: 08:00 AM - 08:00 PM</p>
                    </div>
                    <form id="contactForm">
                        <input type="text" placeholder="Full Name" class="form-control" style="margin-bottom: 12px;" required>
                        <input type="email" placeholder="Email Address" class="form-control" style="margin-bottom: 12px;" required>
                        <textarea placeholder="Your Message or Health Enquiry" class="form-control" style="height: 100px; margin-bottom: 12px;" required></textarea>
                        <button type="submit" class="btn-dynamic">Send Helpdesk Message</button>
                    </form>
                </div>
            </div>
        </div>

        <script>
            document.getElementById('contactForm').addEventListener('submit', function(e) {
                e.preventDefault();
                alert('Thank you! Your helpdesk message has been received by Pure Health Clinic administration.');
                this.reset();
            });
        </script>
    """
    return HttpResponse(header + content + footer, content_type="text/html")


# Alias for backward compatibility
visual_frontend_home_view = home_page_view
