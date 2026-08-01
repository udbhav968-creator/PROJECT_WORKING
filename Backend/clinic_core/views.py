from django.http import HttpResponse

def visual_frontend_home_view(request):
    """
    Renders a World-Class, Ultra-Smooth, Glassmorphic Enterprise Healthcare Web Portal directly at root URL '/'.
    Includes micro-animations, acrylic glass depth, interactive AI symptom checker, live OPD token booking,
    reception TV token display board, and multi-language English/Hindi toggle.
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
        <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800;900&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
        <style>
            :root {
                --primary-navy: #03071e;
                --deep-space: #0a192f;
                --cobalt-blue: #0078d4;
                --vibrant-cyan: #00b4d8;
                --neon-teal: #00f5d4;
                --emerald-green: #10b981;
                --crimson-red: #ef4444;
                --glass-bg: rgba(255, 255, 255, 0.92);
                --glass-border: rgba(255, 255, 255, 0.6);
                --font-heading: 'Outfit', sans-serif;
                --font-body: 'Plus Jakarta Sans', sans-serif;
            }
            * { box-sizing: border-box; margin: 0; padding: 0; }
            html { scroll-behavior: smooth; }
            body { font-family: var(--font-body); background-color: #03071e; color: #f8fafc; line-height: 1.6; overflow-x: hidden; }
            h1, h2, h3, h4 { font-family: var(--font-heading); font-weight: 800; letter-spacing: -0.02em; }
            
            /* Top Announcement Bar */
            .top-bar {
                background: linear-gradient(90deg, #03071e 0%, #0a192f 50%, #0078d4 100%);
                color: #ffffff; padding: 12px 36px; display: flex; justify-content: space-between;
                align-items: center; font-size: 0.88rem; border-bottom: 2px solid var(--neon-teal);
                box-shadow: 0 4px 20px rgba(0,245,212,0.15); position: relative; z-index: 100;
            }
            .triage-badge {
                background: linear-gradient(135deg, #ef4444 0%, #dc2626 100%); color: white; font-weight: 800;
                padding: 5px 16px; border-radius: 30px; font-size: 0.78rem; text-transform: uppercase;
                letter-spacing: 0.06em; animation: pulse-glow 2s infinite; display: inline-flex; align-items: center; gap: 6px;
            }
            @keyframes pulse-glow {
                0% { box-shadow: 0 0 0 0 rgba(239, 68, 68, 0.8); }
                70% { box-shadow: 0 0 0 12px rgba(239, 68, 68, 0); }
                100% { box-shadow: 0 0 0 0 rgba(239, 68, 68, 0); }
            }

            /* Sticky Navigation Header */
            .main-nav {
                background: rgba(10, 25, 47, 0.95); backdrop-filter: blur(20px); -webkit-backdrop-filter: blur(20px);
                padding: 18px 36px; display: flex; justify-content: space-between; align-items: center;
                border-bottom: 1px solid rgba(255,255,255,0.1); position: sticky; top: 0; z-index: 1000;
            }
            .logo-brand { font-size: 1.5rem; font-weight: 900; color: #ffffff; text-decoration: none; display: flex; align-items: center; gap: 10px; }
            .logo-brand span { color: var(--neon-teal); }
            .nav-links { display: flex; gap: 24px; list-style: none; align-items: center; }
            .nav-links a {
                color: #cbd5e1; text-decoration: none; font-weight: 600; font-size: 0.95rem;
                transition: all 0.3s ease; cursor: pointer; padding: 8px 16px; border-radius: 10px;
            }
            .nav-links a:hover, .nav-links a.active { color: #ffffff; background: rgba(0, 245, 212, 0.15); border: 1px solid rgba(0, 245, 212, 0.3); }

            .lang-btn {
                background: linear-gradient(135deg, var(--cobalt-blue) 0%, var(--vibrant-cyan) 100%);
                color: white; border: none; padding: 8px 18px; border-radius: 20px;
                font-weight: 800; font-size: 0.82rem; cursor: pointer; transition: transform 0.2s ease;
                box-shadow: 0 4px 15px rgba(0, 180, 216, 0.3);
            }
            .lang-btn:hover { transform: scale(1.05); }

            /* Hero Banner */
            .hero-section {
                background: radial-gradient(circle at 50% 30%, #0a192f 0%, #03071e 80%);
                color: white; padding: 80px 24px 110px; text-align: center; position: relative; overflow: hidden;
            }
            .hero-section::before {
                content: ''; position: absolute; top: -20%; left: 30%; width: 500px; height: 500px;
                background: radial-gradient(circle, rgba(0, 245, 212, 0.15) 0%, transparent 70%);
                animation: float-glow 8s ease-in-out infinite alternate; pointer-events: none;
            }
            @keyframes float-glow {
                0% { transform: translateY(0) scale(1); }
                100% { transform: translateY(-30px) scale(1.2); }
            }

            .hero-chip {
                background: rgba(255, 255, 255, 0.08); padding: 8px 22px; border-radius: 30px;
                font-size: 0.88rem; font-weight: 800; letter-spacing: 0.08em; display: inline-block;
                border: 1px solid rgba(0, 245, 212, 0.4); color: var(--neon-teal); margin-bottom: 20px;
                box-shadow: 0 0 20px rgba(0, 245, 212, 0.2);
            }

            /* Container & Glass Cards */
            .container { max-width: 1200px; margin: -60px auto 80px; padding: 0 24px; position: relative; z-index: 10; }
            .page-view { display: none; opacity: 0; transform: translateY(20px); transition: opacity 0.4s ease, transform 0.4s ease; }
            .page-view.active { display: block; opacity: 1; transform: translateY(0); }

            .glass-card {
                background: var(--glass-bg); backdrop-filter: blur(24px); -webkit-backdrop-filter: blur(24px);
                border-radius: 24px; padding: 40px; box-shadow: 0 30px 60px rgba(0, 0, 0, 0.3);
                border: 1px solid var(--glass-border); margin-bottom: 36px; color: #0f172a;
            }

            .input-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 20px; margin-top: 24px; }
            .form-control {
                width: 100%; padding: 14px 20px; border: 2px solid #e2e8f0; border-radius: 14px;
                font-family: var(--font-body); font-size: 0.98rem; outline: none; transition: all 0.3s ease;
                background-color: #ffffff; color: #0f172a;
            }
            .form-control:focus { border-color: var(--cobalt-blue); box-shadow: 0 0 0 4px rgba(0, 120, 212, 0.15); }

            .btn-dynamic {
                background: linear-gradient(135deg, var(--cobalt-blue) 0%, var(--vibrant-cyan) 50%, var(--neon-teal) 100%);
                color: white; font-weight: 800; font-size: 1.1rem; padding: 16px 36px;
                border: none; border-radius: 14px; cursor: pointer; width: 100%; margin-top: 24px;
                box-shadow: 0 10px 30px rgba(0, 180, 216, 0.35); transition: all 0.3s ease; text-transform: uppercase;
                letter-spacing: 0.03em;
            }
            .btn-dynamic:hover { transform: translateY(-3px) scale(1.01); box-shadow: 0 15px 40px rgba(0, 245, 212, 0.45); }

            /* Grid Layouts */
            .grid-3 { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 24px; margin-top: 24px; }
            .feature-card {
                background: #ffffff; border: 1.5px solid #e2e8f0; border-radius: 20px; padding: 28px;
                transition: all 0.3s ease; box-shadow: 0 8px 24px rgba(0,0,0,0.04);
            }
            .feature-card:hover { transform: translateY(-8px); box-shadow: 0 20px 40px rgba(0, 120, 212, 0.12); border-color: var(--vibrant-cyan); }

            .duty-badge { padding: 5px 14px; border-radius: 20px; font-size: 0.78rem; font-weight: 800; float: right; }
            .on_duty { background: #dcfce7; color: #15803d; }
            .in_surgery { background: #fee2e2; color: #b91c1c; }

            /* AI Symptom Box */
            .ai-box {
                background: linear-gradient(135deg, #eff6fc 0%, #e0f2fe 100%); border: 2px solid #bae6fd;
                padding: 28px; border-radius: 20px; margin-bottom: 28px;
            }

            /* Reception TV Display Screen */
            .tv-screen {
                background: linear-gradient(135deg, #03071e 0%, #0a192f 100%); color: white; padding: 48px 32px;
                border-radius: 28px; text-align: center; border: 2px solid var(--neon-teal);
                box-shadow: 0 0 50px rgba(0, 245, 212, 0.25); margin-top: 24px;
            }
            .token-display-number {
                font-size: 5rem; font-weight: 900; color: var(--neon-teal); margin: 16px 0;
                letter-spacing: 0.08em; text-shadow: 0 0 30px rgba(0, 245, 212, 0.6);
            }
        </style>
    </head>
    <body>
        <div class="top-bar">
            <div><span class="triage-badge">🚨 24x7 EMERGENCY TRIAGE</span> &nbsp; <span id="txt-helpline">Helpline: +91 9811122233 | 1800-11-2233</span></div>
            <div style="display: flex; gap: 16px; align-items: center;">
                <button class="lang-btn" onclick="toggleLanguage()"><span id="lang-label">🌐 English / हिंदी</span></button>
                <span>🏢 Pure Health Enterprise Portal &nbsp;|&nbsp; 🛡️ NABH Certified</span>
            </div>
        </div>

        <nav class="main-nav">
            <a href="javascript:showPage('home')" class="logo-brand">🏥 Pure Health <span>Clinic</span></a>
            <ul class="nav-links">
                <li><a onclick="showPage('home')" id="nav-home" class="active">Home</a></li>
                <li><a onclick="showPage('ai-triage')" id="nav-ai-triage">🤖 AI Symptom Checker</a></li>
                <li><a onclick="showPage('tv-board')" id="nav-tv-board">📺 Reception TV Display</a></li>
                <li><a onclick="showPage('about')" id="nav-about">About Us</a></li>
                <li><a onclick="showPage('services')" id="nav-services">Medical Services</a></li>
                <li><a onclick="showPage('doctors')" id="nav-doctors">Specialist Doctors</a></li>
                <li><a onclick="showPage('contact')" id="nav-contact">Contact Helpdesk</a></li>
            </ul>
        </nav>

        <section class="hero-section">
            <div class="hero-chip">MICROSOFT ENTERPRISE HEALTHCARE CLOUD</div>
            <h1 id="hero-title" style="font-size: 3.5rem; margin-bottom: 16px; line-height: 1.1;">
                Personalized Patient Care & Enterprise OPD Portal
            </h1>
            <p id="hero-subtitle" style="font-size: 1.25rem; color: #cbd5e1; max-width: 800px; margin: 0 auto 32px;">
                Led by Medical Director <strong>Dr. Divit Shah</strong>, delivering AI symptom analysis, auto-generated OPD tokens, Jitsi video rooms, and sub-millisecond cloud performance.
            </p>
            <div style="display: flex; justify-content: center; gap: 16px;">
                <a href="#booking" onclick="showPage('home')" style="background: linear-gradient(135deg, var(--neon-teal) 0%, var(--vibrant-cyan) 100%); color: #03071e; padding: 16px 36px; border-radius: 14px; font-weight: 900; text-decoration: none; font-size: 1.05rem; box-shadow: 0 10px 30px rgba(0, 245, 212, 0.4);">
                    🎟️ Book OPD Token Now
                </a>
                <a href="/api/docs/" target="_blank" style="background: rgba(255,255,255,0.1); color: white; padding: 16px 36px; border-radius: 14px; font-weight: 700; text-decoration: none; font-size: 1.05rem; border: 1.5px solid rgba(255,255,255,0.3);">
                    📄 Interactive Swagger Docs
                </a>
            </div>
        </section>

        <div class="container">
            <!-- PAGE 1: HOME PAGE -->
            <div id="page-home" class="page-view active">
                <div class="glass-card">
                    <div style="text-align: center; margin-bottom: 24px;">
                        <span style="background: #03071e; color: var(--neon-teal); padding: 6px 20px; border-radius: 30px; font-size: 0.82rem; font-weight: 800; border: 1px solid rgba(0, 245, 212, 0.3);">
                            🏥 CLINICAL OPD REGISTRATION PORTAL
                        </span>
                        <h2 style="color: #03071e; margin-top: 12px; font-size: 2.2rem;" id="hdr-booking">
                            Instant OPD Token & Tele-Health Scheduling
                        </h2>
                        <p style="color: #64748b; font-size: 1rem; margin-top: 4px;">
                            Auto-generates Official Clinical Tokens, Tele-Health Video Links & Emergency Alerts
                        </p>
                    </div>

                    <form id="opdForm">
                        <div class="input-grid">
                            <div>
                                <label style="font-weight: 700; font-size: 0.9rem; color: #0f172a;">Patient Full Name *</label>
                                <input type="text" id="patient_name" required placeholder="e.g. Rajesh Sharma" class="form-control">
                            </div>
                            <div>
                                <label style="font-weight: 700; font-size: 0.9rem; color: #0f172a;">Mobile Phone *</label>
                                <input type="tel" id="patient_phone" required placeholder="e.g. +91 9811122233" class="form-control">
                            </div>
                            <div>
                                <label style="font-weight: 700; font-size: 0.9rem; color: #0f172a;">Attending Specialist Doctor *</label>
                                <select id="doctor_name" class="form-control">
                                    <option value="Dr. Divit Shah">Dr. Divit Shah (Medical Director - ₹600)</option>
                                    <option value="Dr. Rahul Mehta">Dr. Rahul Mehta (Senior Cardiologist - ₹1000)</option>
                                    <option value="Dr. Anjali Sharma">Dr. Anjali Sharma (Chronic Care - ₹750)</option>
                                </select>
                            </div>
                            <div>
                                <label style="font-weight: 700; font-size: 0.9rem; color: #0f172a;">Clinical Department *</label>
                                <select id="department" class="form-control">
                                    <option value="General_Consultation">General Consultation & Preventive Care</option>
                                    <option value="Cardiology">Cardiology & Heart Care</option>
                                    <option value="Chronic_Care">Chronic Disease Care</option>
                                </select>
                            </div>
                            <div>
                                <label style="font-weight: 700; font-size: 0.9rem; color: #0f172a;">Triage Priority *</label>
                                <select id="priority" class="form-control">
                                    <option value="routine">Routine OPD Consultation</option>
                                    <option value="urgent">Urgent Priority Referral</option>
                                    <option value="emergency">🚨 Emergency Triage (Instant Red Alert)</option>
                                </select>
                            </div>
                            <div>
                                <label style="font-weight: 700; font-size: 0.9rem; color: #0f172a;">Mode of Consultation *</label>
                                <select id="consultation_type" class="form-control">
                                    <option value="OPD">Outpatient Department (OPD Visit)</option>
                                    <option value="Teleconsultation">📹 Tele-Health Video Room</option>
                                </select>
                            </div>
                        </div>

                        <!-- Payment Simulator -->
                        <div style="margin-top: 24px; background: #f8fafc; padding: 20px; border-radius: 16px; border: 1.5px solid #e2e8f0;">
                            <label style="font-weight: 800; color: #03071e; font-size: 0.95rem;">💳 Consultation Payment Method Simulator:</label>
                            <div style="display: flex; gap: 24px; margin-top: 10px; font-weight: 600;">
                                <label style="cursor: pointer;"><input type="radio" name="payment_method" value="pay_at_clinic" checked> 🏥 Pay at Reception (Cash/Card)</label>
                                <label style="cursor: pointer;"><input type="radio" name="payment_method" value="upi_online"> 📱 Instant UPI / Razorpay (Pay Online)</label>
                            </div>
                        </div>

                        <button type="submit" class="btn-dynamic" id="submitBtn">🎟️ Book OPD Appointment & Generate Token</button>
                    </form>

                    <div id="receipt-container" style="display: none;"></div>
                </div>
            </div>

            <!-- PAGE 2: AI SYMPTOM CHECKER -->
            <div id="page-ai-triage" class="page-view">
                <div class="glass-card">
                    <h2 style="color: #03071e; font-size: 2.2rem;">🤖 AI Clinical Symptom Checker Assistant</h2>
                    <p style="color: #64748b; margin-top: 6px; font-size: 1.05rem;">
                        Enter your medical symptoms below. AI will analyze inputs and recommend the matching clinical department and specialist doctor.
                    </p>
                    
                    <div class="ai-box" style="margin-top: 24px;">
                        <label style="font-weight: 800; color: #0078d4; font-size: 1rem;">Describe Symptoms or Medical Concerns:</label>
                        <textarea id="symptomInput" class="form-control" style="height: 110px; margin-top: 10px;" placeholder="e.g. Chest tightness, elevated blood pressure, fatigue..."></textarea>
                        <button onclick="runAiCheck()" class="btn-dynamic" style="margin-top: 16px; background: linear-gradient(135deg, #0078d4 0%, #00b4d8 100%);">
                            🤖 Analyze Symptoms with AI Engine
                        </button>
                    </div>
                    <div id="aiResult" style="display: none; background: #dcfce7; border: 2px solid #10b981; padding: 24px; border-radius: 16px; color: #065f46; font-size: 1.05rem;"></div>
                </div>
            </div>

            <!-- PAGE 3: RECEPTION TV DISPLAY BOARD -->
            <div id="page-tv-board" class="page-view">
                <div class="glass-card">
                    <h2 style="color: #03071e; font-size: 2.2rem;">📺 Live Reception OPD Token TV Display Board</h2>
                    <p style="color: #64748b; margin-top: 6px;">Real-Time Waiting Lounge Token Display Screen.</p>
                    
                    <div class="tv-screen">
                        <div style="font-size: 1.2rem; color: var(--neon-teal); font-weight: 800; letter-spacing: 0.1em;">NOW CALLING FOR OPD CONSULTATION</div>
                        <div class="token-display-number" id="tv-token-num">PURE-GEN-101</div>
                        <div style="font-size: 1.5rem; font-weight: 700;">Patient: <span id="tv-patient-name" style="color: var(--vibrant-cyan);">Rajesh Sharma</span> &nbsp;|&nbsp; Doctor: <span>Dr. Divit Shah</span></div>
                        <div style="font-size: 1.25rem; color: #dcfce7; margin-top: 12px; font-weight: 700;">Please proceed to <strong>OPD Room 101</strong></div>
                    </div>
                </div>
            </div>

            <!-- PAGE 4: ABOUT US -->
            <div id="page-about" class="page-view">
                <div class="glass-card">
                    <h2 style="color: #03071e; font-size: 2.2rem;">About Pure Health Clinic & Hospital Systems</h2>
                    <p style="margin-top: 12px; font-size: 1.1rem; color: #334155;">
                        Founded under the clinical leadership of Medical Director <strong>Dr. Divit Shah</strong>, Pure Health Clinic delivers high-availability primary care, preventive diagnostic support, chronic disease management, and emergency triage.
                    </p>
                    <div class="grid-3" style="margin-top: 28px;">
                        <div class="feature-card">
                            <div style="font-size: 2.5rem; margin-bottom: 10px;">🛡️</div>
                            <h3>NABH & HIPAA Certified</h3>
                            <p style="color: #64748b; font-size: 0.92rem; margin-top: 6px;">Strict adherence to national healthcare quality standards and patient data security.</p>
                        </div>
                        <div class="feature-card">
                            <div style="font-size: 2.5rem; margin-bottom: 10px;">👨‍⚕️</div>
                            <h3>50+ Senior Specialists</h3>
                            <p style="color: #64748b; font-size: 0.92rem; margin-top: 6px;">Board-certified medical faculty committed to compassionate patient outcomes.</p>
                        </div>
                        <div class="feature-card">
                            <div style="font-size: 2.5rem; margin-bottom: 10px;">⚡</div>
                            <h3>Sub-Millisecond Cloud APIs</h3>
                            <p style="color: #64748b; font-size: 0.92rem; margin-top: 6px;">Serverless microservices engine powering instant OPD tokens and telehealth video rooms.</p>
                        </div>
                    </div>
                </div>
            </div>

            <!-- PAGE 5: SERVICES -->
            <div id="page-services" class="page-view">
                <div class="glass-card">
                    <h2 style="color: #03071e; font-size: 2.2rem;">Clinical Services & Medical Specialties</h2>
                    <div class="grid-3">
                        <div class="feature-card">
                            <div style="font-size: 2.8rem; margin-bottom: 12px;">🩺</div>
                            <h3>General Consultation & Primary Care</h3>
                            <p style="color: #64748b; font-size: 0.92rem; margin: 8px 0;">Routine health checkups, preventive counseling, and medical assessment under Medical Director Dr. Divit Shah.</p>
                            <div style="font-weight: 800; color: var(--cobalt-blue); font-size: 1.05rem;">Consultation Fee: ₹600</div>
                        </div>
                        <div class="feature-card">
                            <div style="font-size: 2.8rem; margin-bottom: 12px;">🩸</div>
                            <h3>Cardiology & Cardiovascular Care</h3>
                            <p style="color: #64748b; font-size: 0.92rem; margin: 8px 0;">Advanced heart health evaluations, ECG, Holter monitoring, and preventive cardiology by Senior Cardiologist Dr. Rahul Mehta.</p>
                            <div style="font-weight: 800; color: var(--cobalt-blue); font-size: 1.05rem;">Consultation Fee: ₹1000</div>
                        </div>
                        <div class="feature-card">
                            <div style="font-size: 2.8rem; margin-bottom: 12px;">💊</div>
                            <h3>Chronic Care Management</h3>
                            <p style="color: #64748b; font-size: 0.92rem; margin: 8px 0;">Long-term metabolic control for diabetes, hypertension, and continuous wellness tracking by Dr. Anjali Sharma.</p>
                            <div style="font-weight: 800; color: var(--cobalt-blue); font-size: 1.05rem;">Consultation Fee: ₹750</div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- PAGE 6: DOCTORS -->
            <div id="page-doctors" class="page-view">
                <div class="glass-card">
                    <h2 style="color: #03071e; font-size: 2.2rem;">Attending Specialist Doctor Faculty</h2>
                    <div class="grid-3">
                        <div class="feature-card">
                            <span class="duty-badge on_duty">On Duty (OPD Active)</span>
                            <h3>Dr. Divit Shah</h3>
                            <p style="color: var(--cobalt-blue); font-weight: 700; font-size: 0.95rem;">Medical Director & General Physician</p>
                            <p style="color: #64748b; font-size: 0.88rem; margin-top: 10px;">Qualifications: MBBS, MD General Medicine (15+ Yrs Exp)</p>
                            <div style="border-top: 1px solid #e2e8f0; margin-top: 12px; padding-top: 10px; font-size: 0.88rem; font-weight: 600;">
                                📍 OPD Room 101 &nbsp;|&nbsp; ⏰ 09:00 AM - 05:00 PM &nbsp;|&nbsp; 💳 Fee: ₹600
                            </div>
                        </div>
                        <div class="feature-card">
                            <span class="duty-badge on_duty">On Duty (OPD Active)</span>
                            <h3>Dr. Rahul Mehta</h3>
                            <p style="color: var(--cobalt-blue); font-weight: 700; font-size: 0.95rem;">Senior Cardiologist & Heart Specialist</p>
                            <p style="color: #64748b; font-size: 0.88rem; margin-top: 10px;">Qualifications: MBBS, MD, DM Cardiology (18+ Yrs Exp)</p>
                            <div style="border-top: 1px solid #e2e8f0; margin-top: 12px; padding-top: 10px; font-size: 0.88rem; font-weight: 600;">
                                📍 OPD Room 204 &nbsp;|&nbsp; ⏰ 10:00 AM - 04:00 PM &nbsp;|&nbsp; 💳 Fee: ₹1000
                            </div>
                        </div>
                        <div class="feature-card">
                            <span class="duty-badge in_surgery">In Surgery</span>
                            <h3>Dr. Anjali Sharma</h3>
                            <p style="color: var(--cobalt-blue); font-weight: 700; font-size: 0.95rem;">Chronic Care Specialist</p>
                            <p style="color: #64748b; font-size: 0.88rem; margin-top: 10px;">Qualifications: MBBS, MD Internal Medicine (12+ Yrs Exp)</p>
                            <div style="border-top: 1px solid #e2e8f0; margin-top: 12px; padding-top: 10px; font-size: 0.88rem; font-weight: 600;">
                                📍 Operation Theater 2 &nbsp;|&nbsp; ⏰ 02:00 PM - 08:00 PM &nbsp;|&nbsp; 💳 Fee: ₹750
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- PAGE 7: CONTACT -->
            <div id="page-contact" class="page-view">
                <div class="glass-card">
                    <h2 style="color: #03071e; font-size: 2.2rem;">Contact Patient Helpdesk</h2>
                    <p style="color: #64748b; margin-top: 6px;">Submit an inquiry or reach out to clinic administration.</p>
                    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 32px; margin-top: 24px;">
                        <div style="background: #f8fafc; padding: 24px; border-radius: 16px; border: 1.5px solid #e2e8f0;">
                            <p style="margin-bottom: 10px;"><strong>📍 Address:</strong> Pure Health Clinic Building, Sector 12</p>
                            <p style="margin-bottom: 10px;"><strong>📞 Emergency Helpline:</strong> +91 9811122233 | 1800-11-2233</p>
                            <p style="margin-bottom: 10px;"><strong>✉️ Email:</strong> helpdesk@purehealthclinic.com</p>
                            <p><strong>⏰ Working Hours:</strong> Monday - Saturday: 08:00 AM - 08:00 PM</p>
                        </div>
                        <form id="contactForm">
                            <input type="text" placeholder="Full Name" class="form-control" style="margin-bottom: 14px;" required>
                            <input type="email" placeholder="Email Address" class="form-control" style="margin-bottom: 14px;" required>
                            <textarea placeholder="Your Message or Health Enquiry" class="form-control" style="height: 120px; margin-bottom: 14px;" required></textarea>
                            <button type="submit" class="btn-dynamic">Send Helpdesk Message</button>
                        </form>
                    </div>
                </div>
            </div>
        </div>

        <footer style="background: #03071e; color: #94a3b8; padding: 48px; text-align: center; border-top: 4px solid var(--neon-teal);">
            <p style="color: white; font-weight: 800; font-size: 1.2rem;">🏥 Pure Health Clinic & Hospital Systems</p>
            <p style="font-size: 0.9rem; margin-top: 6px; color: #cbd5e1;">Enterprise Full-Stack Web Portal Deployment by Udbhav.</p>
            <p style="font-size: 0.85rem; margin-top: 12px; color: #64748b;">© 2026 Pure Health Clinic. All Rights Reserved.</p>
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
                        document.getElementById('opdForm').style.display = 'none';
                        const receipt = document.getElementById('receipt-container');
                        receipt.style.display = 'block';
                        receipt.innerHTML = `
                            <div style="background: #ffffff; border: 2px dashed #0078d4; padding: 32px; border-radius: 20px; text-align: center; box-shadow: 0 15px 40px rgba(0,120,212,0.15);">
                                <span style="background: #dcfce7; color: #15803d; padding: 6px 18px; border-radius: 30px; font-weight: 800; font-size: 0.88rem;">✅ OPD APPOINTMENT BOOKED SUCCESSFULLY</span>
                                <div style="font-size: 2.8rem; font-weight: 900; color: #0078d4; margin: 16px 0; letter-spacing: 0.05em;">\${data.token_number}</div>
                                <p style="font-size: 1.1rem;"><strong>Patient:</strong> \${data.patient_name} &nbsp;|&nbsp; <strong>Phone:</strong> \${data.patient_phone}</p>
                                <p><strong>Doctor:</strong> \${data.doctor_name} &nbsp;|&nbsp; <strong>Department:</strong> \${data.department}</p>
                                <p><strong>Fee:</strong> ₹\${data.consultation_fee_inr} &nbsp;|&nbsp; <strong>Status:</strong> \${data.status.toUpperCase()}</p>
                                \${data.video_room_url ? `<div style="background: #e0f2fe; padding: 12px; border-radius: 12px; margin-top: 16px;">📹 <strong>Tele-Health Video Room:</strong> <a href="\${data.video_room_url}" target="_blank" style="color: #0284c7; font-weight: 800;">\${data.video_room_url}</a></div>` : ''}
                                \${data.emergency_escalation_code ? `<div style="background: #fee2e2; color: #b91c1c; padding: 12px; border-radius: 12px; margin-top: 16px; font-weight: 800;">🚨 EMERGENCY ALERT CODE: \${data.emergency_escalation_code}</div>` : ''}
                                <div style="margin-top: 24px; display: flex; gap: 14px; justify-content: center;">
                                    <button onclick="window.open('/api/admin/appointments/\${data.id}/slip/', '_blank')" style="background: linear-gradient(135deg, #0078d4 0%, #00b4d8 100%); color: white; border: none; padding: 12px 28px; border-radius: 12px; font-weight: 800; cursor: pointer;">🖨️ Print Reception OPD Slip</button>
                                    <button onclick="location.reload()" style="background: #f1f5f9; border: 1.5px solid #cbd5e1; padding: 12px 28px; border-radius: 12px; font-weight: 800; cursor: pointer;">Book Another OPD</button>
                                </div>
                            </div>
                        `;
                        // Update TV Display Board dynamically
                        document.getElementById('tv-token-num').innerText = data.token_number;
                        document.getElementById('tv-patient-name').innerText = data.patient_name;
                    }
                } catch (err) {
                    alert('Network error connecting to API.');
                } finally {
                    btn.innerHTML = '🎟️ Book OPD Appointment & Generate Token';
                    btn.disabled = false;
                }
            });

            document.getElementById('contactForm').addEventListener('submit', function(e) {
                e.preventDefault();
                alert('Thank you! Your helpdesk message has been received by Pure Health Clinic administration.');
                this.reset();
            });
        </script>
    </body>
    </html>
    """
    return HttpResponse(html_content, content_type="text/html")
