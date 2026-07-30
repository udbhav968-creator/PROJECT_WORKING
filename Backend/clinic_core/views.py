from django.http import HttpResponse

def visual_frontend_home_view(request):
    """
    Renders Microsoft Fluent Design Level Multi-Page Enterprise Healthcare Web Portal at root URL '/'.
    Includes navigation for Home, About Us, Clinical Services, Doctors Directory, Health Blogs, Testimonials & Contact Helpdesk.
    """
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Pure Health Clinic - Enterprise Multi-Page Healthcare Portal</title>
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
                --ms-acrylic-bg: rgba(255, 255, 255, 0.95);
                --font-heading: 'Outfit', 'Segoe UI', sans-serif;
                --font-body: 'Plus Jakarta Sans', 'Segoe UI', sans-serif;
            }
            * { box-sizing: border-box; margin: 0; padding: 0; }
            body { font-family: var(--font-body); background-color: #faf9f8; color: #201f1e; line-height: 1.6; }
            h1, h2, h3, h4 { font-family: var(--font-heading); font-weight: 700; }
            
            /* Top Announcement Bar */
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
            
            /* Navigation Header */
            .main-nav {
                background: #ffffff; padding: 16px 32px; display: flex; justify-content: space-between;
                align-items: center; box-shadow: 0 4px 20px rgba(0,0,0,0.06); sticky: top; top: 0; z-index: 100;
            }
            .logo-brand { font-size: 1.4rem; font-weight: 800; color: #002050; text-decoration: none; display: flex; align-items: center; gap: 8px; }
            .nav-links { display: flex; gap: 24px; list-style: none; }
            .nav-links a { color: #323130; text-decoration: none; font-weight: 600; font-size: 0.95rem; transition: color 0.2s ease; cursor: pointer; }
            .nav-links a:hover, .nav-links a.active { color: var(--ms-blue); }
            
            /* Hero Banner */
            .hero-section {
                background: linear-gradient(135deg, #002050 0%, #0078d4 60%, #008272 100%);
                color: white; padding: 60px 32px 80px; text-align: center; position: relative;
            }
            
            /* Page Views Container */
            .container { max-width: 1180px; margin: -40px auto 60px; padding: 0 24px; position: relative; z-index: 10; }
            .page-view { display: none; }
            .page-view.active { display: block; }
            
            .fluent-card {
                background: var(--ms-acrylic-bg); backdrop-filter: blur(20px);
                border-radius: 20px; padding: 36px; box-shadow: 0 24px 60px rgba(0, 32, 80, 0.12);
                border: 1px solid rgba(255, 255, 255, 0.8); margin-bottom: 32px;
            }
            .input-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(230px, 1fr)); gap: 18px; margin-top: 20px; }
            .form-control {
                width: 100%; padding: 13px 18px; border: 1.5px solid #edebe9; border-radius: 12px;
                font-family: var(--font-body); font-size: 0.95rem; outline: none; background: #ffffff;
            }
            .form-control:focus { border-color: var(--ms-blue); box-shadow: 0 0 0 4px rgba(0, 120, 212, 0.15); }
            
            .btn-fluent {
                background: linear-gradient(135deg, var(--ms-blue) 0%, var(--ms-teal) 100%);
                color: white; font-weight: 700; font-size: 1.05rem; padding: 15px 30px;
                border: none; border-radius: 12px; cursor: pointer; width: 100%; margin-top: 20px;
            }
            
            .grid-3 { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 24px; margin-top: 20px; }
            .service-item, .doctor-item, .blog-item {
                background: #ffffff; border: 1px solid #edebe9; border-radius: 16px; padding: 24px;
                box-shadow: 0 4px 16px rgba(0,0,0,0.04);
            }
            .duty-badge { padding: 4px 12px; border-radius: 14px; font-size: 0.75rem; font-weight: 700; float: right; }
            .on_duty { background: #dff6dd; color: #107c41; }
            .in_surgery { background: #fde7e9; color: #d13438; }
        </style>
    </head>
    <body>
        <div class="top-bar">
            <div><span class="triage-badge">🚨 24x7 EMERGENCY TRIAGE</span> &nbsp; Helpline: +91 9811122233 | 1800-11-2233</div>
            <div>🏢 Pure Health Clinic Enterprise Portal &nbsp;|&nbsp; 🛡️ NABH Certified</div>
        </div>

        <nav class="main-nav">
            <a href="javascript:showPage('home')" class="logo-brand">🏥 Pure Health Clinic</a>
            <ul class="nav-links">
                <li><a onclick="showPage('home')" id="nav-home" class="active">Home</a></li>
                <li><a onclick="showPage('about')" id="nav-about">About Us</a></li>
                <li><a onclick="showPage('services')" id="nav-services">Medical Services</a></li>
                <li><a onclick="showPage('doctors')" id="nav-doctors">Specialist Doctors</a></li>
                <li><a onclick="showPage('blogs')" id="nav-blogs">Health Blogs</a></li>
                <li><a onclick="showPage('testimonials')" id="nav-testimonials">Testimonials</a></li>
                <li><a onclick="showPage('contact')" id="nav-contact">Contact Helpdesk</a></li>
            </ul>
        </nav>

        <section class="hero-section">
            <h1 id="hero-title" style="font-size: 3rem; margin-bottom: 12px;">Personalized Patient Care & Enterprise OPD Portal</h1>
            <p id="hero-subtitle" style="font-size: 1.15rem; color: #e2e8f0; max-width: 750px; margin: 0 auto;">
                Led by <strong>Dr. Divit Shah</strong> (Medical Director), delivering compassionate clinical care, auto-generated OPD tokens, and 24x7 emergency triage.
            </p>
        </section>

        <div class="container">
            <!-- PAGE 1: HOME PAGE -->
            <div id="page-home" class="page-view active">
                <div class="fluent-card">
                    <div style="text-align: center; margin-bottom: 20px;">
                        <span style="background: #002050; color: white; padding: 5px 16px; border-radius: 20px; font-size: 0.8rem; font-weight: 700;">🏥 CLINICAL OPD REGISTRATION</span>
                        <h2 style="color: #002050; margin-top: 10px;">Instant OPD Token & Tele-Health Scheduling</h2>
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
                        <button type="submit" class="btn-fluent" id="submitBtn">🎟️ Book OPD Appointment & Generate Token</button>
                    </form>
                    <div id="receipt-container" style="display: none;"></div>
                </div>
            </div>

            <!-- PAGE 2: ABOUT US -->
            <div id="page-about" class="page-view">
                <div class="fluent-card">
                    <h2 style="color: #002050; font-size: 2rem;">About Pure Health Clinic & Hospital Systems</h2>
                    <p style="margin-top: 12px; font-size: 1.05rem; color: #484644;">
                        Founded under the vision of Medical Director <strong>Dr. Divit Shah</strong>, Pure Health Clinic is dedicated to providing personalized primary care, preventive diagnostic support, chronic disease management, and urgent emergency triage.
                    </p>
                    <div class="grid-3" style="margin-top: 24px;">
                        <div class="service-item"><h3>🛡️ NABH & HIPAA Certified</h3><p style="font-size: 0.9rem; margin-top: 8px;">Adhering strictly to national clinical audit standards and patient data privacy guidelines.</p></div>
                        <div class="service-item"><h3>👨‍⚕️ Board-Certified Faculty</h3><p style="font-size: 0.9rem; margin-top: 8px;">50+ senior specialist doctors dedicated to compassionate patient outcomes.</p></div>
                        <div class="service-item"><h3>⚡ Sub-Millisecond APIs</h3><p style="font-size: 0.9rem; margin-top: 8px;">Enterprise serverless infrastructure powering real-time OPD tokens and telehealth video rooms.</p></div>
                    </div>
                </div>
            </div>

            <!-- PAGE 3: MEDICAL SERVICES -->
            <div id="page-services" class="page-view">
                <div class="fluent-card">
                    <h2 style="color: #002050; font-size: 2rem;">Clinical Services & Medical Specialties</h2>
                    <div class="grid-3">
                        <div class="service-item">
                            <div style="font-size: 2.5rem;">🩺</div>
                            <h3>General Consultation</h3>
                            <p style="font-size: 0.9rem; margin: 8px 0;">Comprehensive primary care and preventive screenings under Dr. Divit Shah.</p>
                            <div style="font-weight: 700; color: var(--ms-blue);">Consultation Fee: ₹600</div>
                        </div>
                        <div class="service-item">
                            <div style="font-size: 2.5rem;">🩸</div>
                            <h3>Cardiology & Heart Care</h3>
                            <p style="font-size: 0.9rem; margin: 8px 0;">Advanced cardiovascular assessments, 24-hr Holter monitoring, and ECG led by Dr. Rahul Mehta.</p>
                            <div style="font-weight: 700; color: var(--ms-blue);">Consultation Fee: ₹1000</div>
                        </div>
                        <div class="service-item">
                            <div style="font-size: 2.5rem;">💊</div>
                            <h3>Chronic Care Management</h3>
                            <p style="font-size: 0.9rem; margin: 8px 0;">Diabetes and hypertension long-term control under Dr. Anjali Sharma.</p>
                            <div style="font-weight: 700; color: var(--ms-blue);">Consultation Fee: ₹750</div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- PAGE 4: DOCTORS DIRECTORY -->
            <div id="page-doctors" class="page-view">
                <div class="fluent-card">
                    <h2 style="color: #002050; font-size: 2rem;">Attending Specialist Doctor Faculty</h2>
                    <div class="grid-3">
                        <div class="doctor-item">
                            <span class="duty-badge on_duty">On Duty</span>
                            <h3>Dr. Divit Shah</h3>
                            <p style="color: #008272; font-weight: 600; font-size: 0.9rem;">Medical Director & General Physician</p>
                            <p style="font-size: 0.85rem; margin-top: 8px;">Qualifications: MBBS, MD General Medicine (15+ Yrs Exp)</p>
                            <p style="font-size: 0.85rem;">📍 Room 101 | ⏰ 09:00 AM - 05:00 PM</p>
                        </div>
                        <div class="doctor-item">
                            <span class="duty-badge on_duty">On Duty</span>
                            <h3>Dr. Rahul Mehta</h3>
                            <p style="color: #008272; font-weight: 600; font-size: 0.9rem;">Senior Cardiologist</p>
                            <p style="font-size: 0.85rem; margin-top: 8px;">Qualifications: MBBS, MD, DM Cardiology (18+ Yrs Exp)</p>
                            <p style="font-size: 0.85rem;">📍 Room 204 | ⏰ 10:00 AM - 04:00 PM</p>
                        </div>
                        <div class="doctor-item">
                            <span class="duty-badge in_surgery">In Surgery</span>
                            <h3>Dr. Anjali Sharma</h3>
                            <p style="color: #008272; font-weight: 600; font-size: 0.9rem;">Chronic Care Specialist</p>
                            <p style="font-size: 0.85rem; margin-top: 8px;">Qualifications: MBBS, MD Internal Medicine (12+ Yrs Exp)</p>
                            <p style="font-size: 0.85rem;">📍 OT 2 | ⏰ 02:00 PM - 08:00 PM</p>
                        </div>
                    </div>
                </div>
            </div>

            <!-- PAGE 5: BLOGS -->
            <div id="page-blogs" class="page-view">
                <div class="fluent-card">
                    <h2 style="color: #002050; font-size: 2rem;">Medical Blogs & Health Education</h2>
                    <div class="grid-3">
                        <div class="blog-item">
                            <span style="color: #008272; font-size: 0.8rem; font-weight: 700;">PREVENTIVE HEALTH</span>
                            <h3 style="margin-top: 4px;">Understanding Cardiovascular Risk Factors</h3>
                            <p style="font-size: 0.88rem; margin: 8px 0;">Key preventive measures to maintain optimal heart health and blood pressure.</p>
                            <span style="font-size: 0.8rem; color: #605e5c;">By Dr. Rahul Mehta</span>
                        </div>
                        <div class="blog-item">
                            <span style="color: #008272; font-size: 0.8rem; font-weight: 700;">CHRONIC CARE</span>
                            <h3 style="margin-top: 4px;">Effective Glucose Management Guidelines</h3>
                            <p style="font-size: 0.88rem; margin: 8px 0;">Dietary adjustments and continuous tracking for diabetic patient wellness.</p>
                            <span style="font-size: 0.8rem; color: #605e5c;">By Dr. Anjali Sharma</span>
                        </div>
                    </div>
                </div>
            </div>

            <!-- PAGE 6: TESTIMONIALS -->
            <div id="page-testimonials" class="page-view">
                <div class="fluent-card">
                    <h2 style="color: #002050; font-size: 2rem;">Patient Testimonials & Reviews</h2>
                    <div class="grid-3">
                        <div class="service-item">
                            <div style="color: #f59e0b; font-size: 1.2rem;">★★★★★</div>
                            <p style="font-size: 0.95rem; margin: 8px 0;">"The instant OPD token booking system and tele-health link saved us so much time. Excellent care by Dr. Divit Shah!"</p>
                            <strong>— Rajesh Sharma</strong>
                        </div>
                        <div class="service-item">
                            <div style="color: #f59e0b; font-size: 1.2rem;">★★★★★</div>
                            <p style="font-size: 0.95rem; margin: 8px 0;">"Outstanding cardiology consultation with Dr. Rahul Mehta. Very professional clinic staff."</p>
                            <strong>— Priya Verma</strong>
                        </div>
                    </div>
                </div>
            </div>

            <!-- PAGE 7: CONTACT HELPDESK -->
            <div id="page-contact" class="page-view">
                <div class="fluent-card">
                    <h2 style="color: #002050; font-size: 2rem;">Contact Patient Helpdesk</h2>
                    <p style="margin-top: 8px; color: #605e5c;">Submit an inquiry or reach out to clinic administration.</p>
                    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 24px; margin-top: 20px;">
                        <div>
                            <p><strong>📍 Address:</strong> Pure Health Clinic Building, Sector 12</p>
                            <p><strong>📞 Emergency Line:</strong> +91 9811122233</p>
                            <p><strong>✉️ Email:</strong> helpdesk@purehealthclinic.com</p>
                            <p><strong>⏰ Working Hours:</strong> Mon - Sat: 08:00 AM - 08:00 PM</p>
                        </div>
                        <form id="contactForm">
                            <input type="text" placeholder="Full Name" class="form-control" style="margin-bottom: 12px;" required>
                            <input type="email" placeholder="Email Address" class="form-control" style="margin-bottom: 12px;" required>
                            <textarea placeholder="Your Message" class="form-control" style="height: 100px; margin-bottom: 12px;" required></textarea>
                            <button type="submit" class="btn-fluent">Send Helpdesk Message</button>
                        </form>
                    </div>
                </div>
            </div>
        </div>

        <footer style="background: #002050; color: #a19f9d; padding: 40px; text-align: center; border-top: 4px solid #008272;">
            <p style="color: white; font-weight: 700;">🏥 Pure Health Clinic & Hospital Systems</p>
            <p style="font-size: 0.85rem; margin-top: 6px;">Multi-Page Enterprise Web Application Deployment by Udbhav.</p>
        </footer>

        <script>
            function showPage(pageId) {
                document.querySelectorAll('.page-view').forEach(p => p.classList.remove('active'));
                document.querySelectorAll('.nav-links a').forEach(a => a.classList.remove('active'));
                
                const target = document.getElementById('page-' + pageId);
                const navTarget = document.getElementById('nav-' + pageId);
                if (target) target.classList.add('active');
                if (navTarget) navTarget.classList.add('active');

                const titles = {
                    home: 'Personalized Patient Care & Enterprise OPD Portal',
                    about: 'About Pure Health Clinic & Clinical Leadership',
                    services: 'Clinical Services & Medical Specialties',
                    doctors: 'Attending Specialist Doctor Faculty Roster',
                    blogs: 'Medical Health Blogs & Patient Education',
                    testimonials: 'Patient Feedback, Reviews & Testimonials',
                    contact: 'Contact Patient Helpdesk & Emergency Enquiries'
                };
                document.getElementById('hero-title').innerText = titles[pageId] || titles.home;
                window.scrollTo({ top: 0, behavior: 'smooth' });
            }

            document.getElementById('opdForm').addEventListener('submit', async function(e) {
                e.preventDefault();
                const btn = document.getElementById('submitBtn');
                btn.innerHTML = '⏳ Generating Token...';
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
                                <p><strong>Consultation Fee:</strong> ₹\${data.consultation_fee_inr} | <strong>Status:</strong> \${data.status.toUpperCase()}</p>
                                <div style="margin-top: 16px;">
                                    <button onclick="window.open('/api/admin/appointments/\${data.id}/slip/', '_blank')" style="background: #0078d4; color: white; border: none; padding: 10px 20px; border-radius: 8px; font-weight: 700; cursor: pointer;">🖨️ Print Reception OPD Slip</button>
                                </div>
                            </div>
                        `;
                    }
                } catch (err) {
                    alert('Network error.');
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
