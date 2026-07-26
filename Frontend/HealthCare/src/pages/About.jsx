import { Link } from "react-router-dom";

import clinicConsultationImage from "../assets/images/about/clinic-consultation.jpg";
import clinicTeamImage from "../assets/images/about/clinic-consultation1.jpg";
import patientCareImage from "../assets/images/about/clinic-consultation2.jpg";

import {
  aboutHighlights,
  clinicValues,
  healthcareStats,
} from "../data/about.js";

import siteData from "../data/siteData.js";

import "../styles/information-pages.css";

function About() {
  return (
    <main className="information-page">
      <section className="info-hero">
        <div className="info-container info-hero-grid">
          <div className="info-hero-content">
            <span className="info-eyebrow">About Our Clinic</span>

            <h1>
              Professional care built around
              <span> every patient.</span>
            </h1>

            <p>
              {siteData.clinicName} provides responsible, compassionate, and
              personalized healthcare in a safe and welcoming environment.
            </p>

            <div className="info-hero-actions">
              <Link to="/appointment" className="info-button info-button-primary">
                Book an Appointment
              </Link>

              <Link to="/services" className="info-button info-button-secondary">
                Explore Services
              </Link>
            </div>

            <div className="info-hero-trust">
              <div>
                <strong>Patient First</strong>
                <span>Personalized attention</span>
              </div>

              <div>
                <strong>Trusted Care</strong>
                <span>Responsible healthcare</span>
              </div>
            </div>
          </div>

          <div className="info-hero-visual">
            <div className="info-hero-image-wrapper">
              <img
                src={clinicConsultationImage}
                alt="Doctor consulting with a patient in a modern healthcare clinic"
                width="760"
                height="620"
                fetchPriority="high"
              />
            </div>

            <div className="info-floating-card info-floating-card-top">
              <span className="info-floating-icon" aria-hidden="true">
                ✓
              </span>

              <div>
                <strong>Quality Healthcare</strong>
                <span>Professional and reliable care</span>
              </div>
            </div>

            <div className="info-floating-card info-floating-card-bottom">
              <strong>98%</strong>
              <span>Patient Satisfaction</span>
            </div>
          </div>
        </div>
      </section>

      <section className="info-stats-section" aria-label="Clinic statistics">
        <div className="info-container info-stats-grid">
          {healthcareStats.map((stat) => (
            <article className="info-stat-card" key={stat.id}>
              <strong>{stat.value}</strong>
              <span>{stat.label}</span>
            </article>
          ))}
        </div>
      </section>

      <section className="info-section">
        <div className="info-container info-introduction-grid">
          <div className="info-image-composition">
            <div className="info-main-image">
              <img
                src={clinicTeamImage}
                alt="Healthcare professionals discussing patient care"
                loading="lazy"
                width="680"
                height="760"
              />
            </div>

            <div className="info-secondary-image">
              <img
                src={patientCareImage}
                alt="Healthcare professional providing attentive patient support"
                loading="lazy"
                width="420"
                height="360"
              />
            </div>

            <div className="info-experience-badge">
              <strong>Care</strong>
              <span>with compassion</span>
            </div>
          </div>

          <div className="info-introduction-content">
            <span className="info-eyebrow">Who We Are</span>

            <h2 className="info-section-title">
              Healthcare that begins with listening
            </h2>

            <p className="info-lead-text">{siteData.introduction}</p>

            <p>{siteData.description}</p>

            <p>
              Our approach begins by understanding each patient’s concerns,
              medical needs, and expectations. We focus on clear communication,
              responsible treatment planning, and long-term patient trust.
            </p>

            <div className="info-feature-list">
              <div>
                <span aria-hidden="true">✓</span>
                <p>
                  <strong>Personalized Attention</strong>
                  Care designed around individual patient requirements.
                </p>
              </div>

              <div>
                <span aria-hidden="true">✓</span>
                <p>
                  <strong>Clear Communication</strong>
                  Simple and honest guidance throughout every consultation.
                </p>
              </div>

              <div>
                <span aria-hidden="true">✓</span>
                <p>
                  <strong>Comfortable Environment</strong>
                  A respectful and welcoming experience for every visitor.
                </p>
              </div>
            </div>

            <Link to="/services" className="info-text-link">
              Learn more about our services
              <span aria-hidden="true">→</span>
            </Link>
          </div>
        </div>
      </section>

      <section className="info-section info-purpose-section">
        <div className="info-container">
          <header className="info-section-header">
            <span className="info-eyebrow">Our Purpose</span>

            <h2 className="info-section-title">
              Guided by a clear mission and vision
            </h2>

            <p>
              Our purpose shapes how we provide care, communicate with patients,
              and contribute to healthier communities.
            </p>
          </header>

          <div className="info-purpose-grid">
            <article className="info-purpose-card info-mission-card">
              <span className="info-purpose-label">Our Mission</span>

              <h3>Making responsible healthcare more personal</h3>

              <p>
                To provide accessible, compassionate, and high-quality
                healthcare while treating every patient with dignity, respect,
                and individual attention.
              </p>

              <span className="info-purpose-number">01</span>
            </article>

            <article className="info-purpose-card info-vision-card">
              <span className="info-purpose-label">Our Vision</span>

              <h3>Building long-term trust through better care</h3>

              <p>
                To become a trusted healthcare provider known for professional
                care, positive patient experiences, and continuous improvement
                in clinical service.
              </p>

              <span className="info-purpose-number">02</span>
            </article>
          </div>
        </div>
      </section>

      <section className="info-section">
        <div className="info-container">
          <header className="info-section-header">
            <span className="info-eyebrow">Why Choose Us</span>

            <h2 className="info-section-title">
              Care you can feel confident about
            </h2>

            <p>
              We combine professional healthcare standards with genuine
              attention to the comfort and well-being of every patient.
            </p>
          </header>

          <div className="info-highlights-grid">
            {aboutHighlights.map((highlight) => (
              <article className="info-highlight-card" key={highlight.id}>
                <span className="info-highlight-number">
                  {highlight.number}
                </span>

                <div className="info-highlight-icon" aria-hidden="true">
                  +
                </div>

                <h3>{highlight.title}</h3>

                <p>{highlight.description}</p>
              </article>
            ))}
          </div>
        </div>
      </section>

      <section className="info-section info-values-section">
        <div className="info-container info-values-layout">
          <div className="info-values-introduction">
            <span className="info-eyebrow">Our Values</span>

            <h2 className="info-section-title">
              Principles behind every patient interaction
            </h2>

            <p>
              Our values influence how we communicate, make decisions, and
              maintain long-term trust with patients and their families.
            </p>

            <Link
              to="/appointment"
              className="info-button info-button-primary"
            >
              Schedule Consultation
            </Link>
          </div>

          <div className="info-values-grid">
            {clinicValues.map((value) => (
              <article className="info-value-card" key={value.id}>
                <span className="info-value-number">
                  {String(value.id).padStart(2, "0")}
                </span>

                <h3>{value.title}</h3>

                <p>{value.description}</p>
              </article>
            ))}
          </div>
        </div>
      </section>

      <section className="info-cta-section">
        <div className="info-container info-cta-content">
          <div>
            <span className="info-cta-eyebrow">Your Health Matters</span>

            <h2>Take the next step towards better health</h2>

            <p>
              Connect with our healthcare team and receive the attention,
              guidance, and support you deserve.
            </p>
          </div>

          <div className="info-cta-actions">
            <Link
              to="/appointment"
              className="info-button info-button-light"
            >
              Book Appointment
            </Link>

            <Link
              to="/contact"
              className="info-button info-button-outline-light"
            >
              Contact Clinic
            </Link>
          </div>
        </div>
      </section>
    </main>
  );
}

export default About;