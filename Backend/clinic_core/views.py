from django.http import HttpResponse

def visual_frontend_home_view(request):
    """
    Renders Microsoft Enterprise Level Multi-Page Healthcare Portal with Next-Gen Features:
    - English / Hindi Multi-Language Toggle
    - AI Clinical Symptom Checker Assistant
    - Razorpay / UPI Payment Gateway Simulator
    - Live Reception OPD Token TV Display Board
    """
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Pure Health Clinic - Enterprise Next-Gen Healthcare Portal</title>
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
        <style>
            :root {
                --ms-blue: #0078d4;
                --ms-dark-navy: #002050;
                --ms-teal: #008272;
                --ms-emerald: #107c41;
                --ms-crimson: #d13438;
                --font-heading: 'Outfit', 'Segoe UI', sans-serif;
                --font-body: 'Plus Jakarta Sans', 'Segoe UI', sans-serif;
            }
            * { box-sizing: border-box; margin: 0; padding: 0; }
            body { font-family: var(--font-body); background-color: #faf9f8; color: #201f1e; line-height: 1.6; }
            h1, h2, h3, h4 { font-family: var(--font-heading); font-weight: 700; }
            
            .top-bar {
                background: linear-gradient(90deg, #002050 0%, #0078d4 100%);
                color: #ffffff; padding: 10px 32px; display: flex; justify-content: space-between;
                align-items: center; font-size: 0.88rem; border-bottom: 2px solid var(--ms-teal);
            }
            .triage-badge {
                background-color: var(--ms-crimson); color: white; font-weight: 700;
                padding: 4px 14px; border-radius: 20px; font-size: 0.78rem; text-transform: uppercase;
                animation: pulse 2s infinite;
            }
            @keyframes pulse {
                0% { box-shadow: 0 0 0 0 rgba(209, 52, 56, 0.7); }
                70% { box-shadow: 0 0 0 10px rgba(209, 52, 56, 0); }
                100% { box-shadow: 0 0 0 0 rgba(209, 52, 56, 0); }
            }
            
            .main-nav {
                background: #ffffff; padding: 16px 32px; display: flex; justify-content: space-between;
                align-items: center; box-shadow: 0 4px 20px rgba(0,0,0,0.06); sticky: top; top: 0; z-index: 100;
            }
            .logo-brand { font-size: 1.4rem; font-weight: 800; color: #002050; text-decoration: none; display: flex; align-items: center; gap: 8px; }
            .nav-links { display: flex; gap: 20px; list-style: none; align-items: center; }
            .nav-links a { color: #323130; text-decoration: none; font-weight: 600; font-size: 0.92rem; cursor: pointer; }
            .nav-links a:hover, .nav-links a.active { color: var(--ms-blue); }
            
            .lang-btn {
                background: #f3f2f1; border: 1px solid #e1dfdd; padding: 6px 14px; border-radius: 20px;
                font-weight: 700; font-size: 0.82rem; cursor: pointer; color: #002050;
            }
            
            .hero-section {
                background: linear-gradient(135deg, #002050 0%, #0078d4 60%, #008272 100%);
                color: white; padding: 60px 32px 80px; text-align: center;
            }
            
            .container { max-width: 1180px; margin: -40px auto 60px; padding: 0 24px; position: relative; z-index: 10; }
            .page-view { display: none; }
            .page-view.active { display: block; }
            
            .fluent-card {
                background: rgba(255, 255, 255, 0.95); backdrop-filter: blur(20px);
                border-radius: 20px; padding: 36px; box-shadow: 0 24px 60px rgba(0, 32, 80, 0.12);
                border: 1px solid rgba(255, 255, 255, 0.8); margin-bottom: 32px;
            }
            .input-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(230px, 1fr)); gap: 18px; margin-top: 20px; }
            .form-control {
                width: 100%; padding: 13px 18px; border: 1.5px solid #edebe9; border-radius: 12px;
                font-family: var(--font-body); font-size: 0.95rem; outline: none; background: #ffffff;
            }
            .btn-fluent {
                background: linear-gradient(135deg, var(--ms-blue) 0%, var(--ms-teal) 100%);
                color: white; font-weight: 700; font-size: 1.05rem; padding: 15px 30px;
                border: none; border-radius: 12px; cursor: pointer; width: 100%; margin-top: 20px;
            }
            .grid-3 { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 24px; margin-top: 20px; }
            
            .ai-box {
                background: #eff6fc; border: 1.5px solid #c7e0f4; padding: 20px; border-radius: 16px; margin-bottom: 24px;
            }
            .tv-display {
                background: #002050; color: white; padding: 32px; border-radius: 20px; text-align: center; margin-top: 20px;
            }
        </style>
    </head>
    <body>
        <div class="top-bar">
            <div><span class="triage-badge">🚨 24x7 EMERGENCY TRIAGE</span> &nbsp; <span id="txt-helpline">Helpline: +91 9811122233 | 1800-11-2233</span></div>
            <div style="display: flex; gap: 12px; align-items: center;">
                <button class="lang-btn" onclick="toggleLanguage()"><span id="lang-label">🌐 English / हिंदी</span></button>
                <span>🏢 Pure Health Clinic &nbsp;|&nbsp; 🛡️ NABH Certified</span>
            </div>
        </div>

        <nav class="main-nav">
            <a href="javascript:showPage('home')" class="logo-brand">🏥 Pure Health Clinic</a>
            <ul class="nav-links">
                <li><a onclick="showPage('home')" id="nav-home" class="active">Home</a></li>
                <li><a onclick="showPage('ai-triage')" id="nav-ai-triage">🤖 AI Symptom Checker</a></li>
                <li><a onclick="showPage('tv-board')" id="nav-tv-board">📺 Reception Token Board</a></li>
                <li><a onclick="showPage('about')" id="nav-about">About Us</a></li>
                <li><a onclick="showPage('services')" id="nav-services">Medical Services</a></li>
                <li><a onclick="showPage('doctors')" id="nav-doctors">Specialist Doctors</a></li>
                <li><a onclick="showPage('contact')" id="nav-contact">Contact Helpdesk</a></li>
            </ul>
        </nav>

        <section class="hero-section">
            <h1 id="hero-title" style="font-size: 3rem; margin-bottom: 12px;">Personalized Patient Care & Enterprise OPD Portal</h1>
            <p id="hero-subtitle" style="font-size: 1.15rem; color: #e2e8f0; max-width: 750px; margin: 0 auto;">
                Led by <strong>Dr. Divit Shah</strong> (Medical Director), providing AI triage, OPD tokens, and tele-consultation video rooms.
            </p>
        </section>

        <div class="container">
            <!-- PAGE 1: HOME PAGE -->
            <div id="page-home" class="page-view active">
                <div class="fluent-card">
                    <div style="text-align: center; margin-bottom: 20px;">
                        <span style="background: #002050; color: white; padding: 5px 16px; border-radius: 20px; font-size: 0.8rem; font-weight: 700;">🏥 CLINICAL OPD REGISTRATION</span>
                        <h2 style="color: #002050; margin-top: 10px;" id="hdr-booking">Instant OPD Token & Tele-Health Scheduling</h2>
                    </div>
                    <form id="opdForm">
                        <div class="input-grid">
                            <div><label style="font-weight: 600; font-size: 0.85rem;">Patient Full Name *</label><input type="text" id="patient_name" required placeholder="e.g. Rajesh Sharma" class="form-control"></div>
                            <div><label style="font-weight: 600; font-size: 0.85rem;">Mobile Phone *</label><input type="tel" id="patient_phone" required placeholder="e.g. +91 9811122233" class="form-control"></div>
                            <div>
                                <label style="font-weight: 600; font-size: 0.85rem;">Attending Specialist Doctor *</label>
                                <select id="doctor_name" class="form-control">
                                    <option value="Dr. Divit Shah">Dr. Divit Shah (Medical Director - ₹600)</option>
                                    <option value="Dr. Rahul Mehta">Dr. Rahul Mehta (Cardiology - ₹1000)</option>
                                    <option value="Dr. Anjali Sharma">Dr. Anjali Sharma (Chronic Care - ₹750)</option>
                                </select>
                            </div>
                            <div>
                                <label style="font-weight: 600; font-size: 0.85rem;">Department *</label>
                                <select id="department" class="form-control">
                                    <option value="General_Consultation">General Consultation & Preventive Care</option>
                                    <option value="Cardiology">Cardiology & Heart Care</option>
                                    <option value="Chronic_Care">Chronic Disease Care</option>
                                </select>
                            </div>
                        </div>

                        <!-- Payment Option Simulator -->
                        <div style="margin-top: 20px; background: #faf9f8; padding: 16px; border-radius: 12px; border: 1px solid #edebe9;">
                            <label style="font-weight: 700; color: #002050;">💳 Consultation Payment Method Simulator:</label>
                            <div style="display: flex; gap: 20px; margin-top: 8px;">
                                <label><input type="radio" name="payment_method" value="pay_at_clinic" checked> 🏥 Pay at Reception (Cash/Card)</label>
                                <label><input type="radio" name="payment_method" value="upi_online"> 📱 Instant UPI / Razorpay (Pay Online)</label>
                            </div>
                        </div>

                        <button type="submit" class="btn-fluent" id="submitBtn">🎟️ Book OPD Appointment & Generate Token</button>
                    </form>
                    <div id="receipt-container" style="display: none;"></div>
                </div>
            </div>

            <!-- PAGE 2: AI SYMPTOM CHECKER -->
            <div id="page-ai-triage" class="page-view">
                <div class="fluent-card">
                    <h2 style="color: #002050; font-size: 2rem;">🤖 AI Clinical Symptom Checker Assistant</h2>
                    <p style="color: #605e5c; margin-top: 6px;">Describe your health symptoms below. AI will suggest the appropriate clinical department and specialist doctor.</p>
                    
                    <div class="ai-box" style="margin-top: 20px;">
                        <label style="font-weight: 700; color: #0078d4;">Enter Symptoms or Health Concerns:</label>
                        <textarea id="symptomInput" class="form-control" style="height: 90px; margin-top: 8px;" placeholder="e.g. Chest tightness, shortness of breath, elevated blood pressure..."></textarea>
                        <button onclick="runAiCheck()" class="btn-fluent" style="margin-top: 12px; background: #0078d4;">Analyze Symptoms with AI</button>
                    </div>
                    <div id="aiResult" style="display: none; background: #dff6dd; border: 1px solid #107c41; padding: 20px; border-radius: 12px; color: #107c41;"></div>
                </div>
            </div>

            <!-- PAGE 3: RECEPTION TV TOKEN DISPLAY BOARD -->
            <div id="page-tv-board" class="page-view">
                <div class="fluent-card">
                    <h2 style="color: #002050; font-size: 2rem;">📺 Live Reception OPD Token Callout TV Board</h2>
                    <p style="color: #605e5c; margin-top: 4px;">Real-Time Digital Screen for OPD Waiting Lounges.</p>
                    
                    <div class="tv-display">
                        <div style="font-size: 1.1rem; color: #50e6ff; font-weight: 700;">NOW CALLING FOR CONSULTATION</div>
                        <div style="font-size: 4rem; font-weight: 800; color: #0078d4; margin: 10px 0; letter-spacing: 0.05em;" id="tv-token-num">PURE-GEN-101</div>
                        <div style="font-size: 1.4rem;">Patient: <strong id="tv-patient-name">Rajesh Sharma</strong> &nbsp;|&nbsp; Doctor: <strong>Dr. Divit Shah</strong></div>
                        <div style="font-size: 1.2rem; color: #dff6dd; margin-top: 8px;">Proceed to <strong>OPD Room 101</strong></div>
                    </div>
                </div>
            </div>

            <!-- PAGE 4: ABOUT US -->
            <div id="page-about" class="page-view">
                <div class="fluent-card">
                    <h2 style="color: #002050; font-size: 2rem;">About Pure Health Clinic & Hospital Systems</h2>
                    <p style="margin-top: 12px; font-size: 1.05rem; color: #484644;">
                        Founded under the vision of Medical Director <strong>Dr. Divit Shah</strong>, Pure Health Clinic provides high-availability primary care, preventive diagnostic support, chronic care, and urgent emergency triage.
                    </p>
                </div>
            </div>

            <!-- PAGE 5: SERVICES -->
            <div id="page-services" class="page-view">
                <div class="fluent-card">
                    <h2 style="color: #002050; font-size: 2rem;">Clinical Services & Specialties</h2>
                    <div class="grid-3">
                        <div class="service-item" style="background:#fff; padding:20px; border-radius:12px; border:1px solid #edebe9;">
                            <h3>🩺 General Consultation</h3>
                            <p style="font-size: 0.9rem; margin: 8px 0;">Primary care under Dr. Divit Shah.</p>
                            <div style="font-weight: 700; color: #0078d4;">Fee: ₹600</div>
                        </div>
                        <div class="service-item" style="background:#fff; padding:20px; border-radius:12px; border:1px solid #edebe9;">
                            <h3>🩸 Cardiology Care</h3>
                            <p style="font-size: 0.9rem; margin: 8px 0;">Heart health assessments led by Dr. Rahul Mehta.</p>
                            <div style="font-weight: 700; color: #0078d4;">Fee: ₹1000</div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- PAGE 6: DOCTORS -->
            <div id="page-doctors" class="page-view">
                <div class="fluent-card">
                    <h2 style="color: #002050; font-size: 2rem;">Specialist Doctors Roster</h2>
                    <div class="grid-3">
                        <div class="service-item" style="background:#fff; padding:20px; border-radius:12px; border:1px solid #edebe9;">
                            <h3>Dr. Divit Shah</h3>
                            <p style="color: #008272; font-weight: 600;">Medical Director</p>
                            <p style="font-size: 0.85rem;">📍 OPD Room 101 | ⏰ 09:00 AM - 05:00 PM</p>
                        </div>
                    </div>
                </div>
            </div>

            <!-- PAGE 7: CONTACT -->
            <div id="page-contact" class="page-view">
                <div class="fluent-card">
                    <h2 style="color: #002050; font-size: 2rem;">Contact Patient Helpdesk</h2>
                    <p style="margin-top: 8px; color: #605e5c;">Submit an inquiry or reach out to clinic administration.</p>
                </div>
            </div>
        </div>

        <footer style="background: #002050; color: #a19f9d; padding: 40px; text-align: center; border-top: 4px solid #008272;">
            <p style="color: white; font-weight: 700;">🏥 Pure Health Clinic & Hospital Systems</p>
            <p style="font-size: 0.85rem; margin-top: 6px;">Enterprise Full-Stack Deployment with Next-Gen AI & Payment Integration.</p>
        </footer>

        <script>
            let isHindi = false;
            function toggleLanguage() {
                isHindi = !isHindi;
                document.getElementById('lang-label').innerText = isHindi ? '🌐 हिंदी (Hindi Active)' : '🌐 English / हिंदी';
                document.getElementById('txt-helpline').innerText = isHindi ? 'हेल्पलाइन: +91 9811122233 | 1800-11-2233' : 'Helpline: +91 9811122233 | 1800-11-2233';
                document.getElementById('hdr-booking').innerText = isHindi ? 'त्वरित ओपीडी टोकन एवं परामर्श बुकिंग' : 'Instant OPD Token & Tele-Health Scheduling';
            }

            function showPage(pageId) {
                document.querySelectorAll('.page-view').forEach(p => p.classList.remove('active'));
                document.querySelectorAll('.nav-links a').forEach(a => a.classList.remove('active'));
                
                const target = document.getElementById('page-' + pageId);
                const navTarget = document.getElementById('nav-' + pageId);
                if (target) target.classList.add('active');
                if (navTarget) navTarget.classList.add('active');

                window.scrollTo({ top: 0, behavior: 'smooth' });
            }

            function runAiCheck() {
                const text = document.getElementById('symptomInput').value.toLowerCase();
                const res = document.getElementById('aiResult');
                res.style.display = 'block';

                if (text.includes('chest') || text.includes('heart') || text.includes('breath')) {
                    res.innerHTML = '🤖 <strong>AI Recommendation:</strong> High Priority! Recommended Department: <strong>Cardiology & Heart Care</strong> under <strong>Dr. Rahul Mehta</strong> (OPD Room 204).';
                } else if (text.includes('sugar') || text.includes('diabetes') || text.includes('bp')) {
                    res.innerHTML = '🤖 <strong>AI Recommendation:</strong> Recommended Department: <strong>Chronic Disease Care</strong> under <strong>Dr. Anjali Sharma</strong>.';
                } else {
                    res.innerHTML = '🤖 <strong>AI Recommendation:</strong> Recommended Department: <strong>General Consultation & Preventive Care</strong> under <strong>Dr. Divit Shah</strong> (OPD Room 101).';
                }
            }

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
                    priority: 'routine',
                    consultation_type: 'OPD',
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
                        document.getElementById('opdForm').style.display = 'none';
                        const receipt = document.getElementById('receipt-container');
                        receipt.style.display = 'block';
                        receipt.innerHTML = `
                            <div style="background: #ffffff; border: 2px dashed #0078d4; padding: 24px; border-radius: 16px; text-align: center;">
                                <span style="background: #dff6dd; color: #107c41; padding: 4px 14px; border-radius: 20px; font-weight: 700; font-size: 0.85rem;">✅ OPD APPOINTMENT BOOKED</span>
                                <div style="font-size: 2.2rem; font-weight: 800; color: #0078d4; margin: 10px 0;">\${data.token_number}</div>
                                <p><strong>Patient:</strong> \${data.patient_name} | <strong>Doctor:</strong> \${data.doctor_name}</p>
                                <p><strong>Fee:</strong> ₹\${data.consultation_fee_inr} | <strong>Status:</strong> \${data.status.toUpperCase()}</p>
                                <div style="margin-top: 16px;">
                                    <button onclick="window.open('/api/admin/appointments/\${data.id}/slip/', '_blank')" style="background: #0078d4; color: white; border: none; padding: 10px 20px; border-radius: 8px; font-weight: 700; cursor: pointer;">🖨️ Print Reception OPD Slip</button>
                                </div>
                            </div>
                        `;
                        // Update TV Display Board dynamically
                        document.getElementById('tv-token-num').innerText = data.token_number;
                        document.getElementById('tv-patient-name').innerText = data.patient_name;
                    }
                } catch (err) {
                    alert('Network error.');
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
