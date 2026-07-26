import { Link } from "react-router-dom";

import ServiceCard from "../components/services/ServiceCard.jsx";

import services, { serviceFeatures } from "../data/services.js";

import "../styles/information-pages.css";

function Services() {
  return (
    <main className="information-page">
      <section className="services-hero">
        <div className="info-container services-hero-grid">
          <div className="services-hero-content">
            <span className="info-eyebrow">Our Healthcare Services</span>

            <h1>
              Thoughtful healthcare for
              <span> every stage of life.</span>
            </h1>

            <p>
              Explore reliable healthcare services designed to support routine
              medical needs, preventive care, ongoing health management, and
              long-term well-being.
            </p>

            <div className="services-hero-actions">
              <Link
                to="/appointment"
                className="info-button info-button-primary"
              >
                Book an Appointment
              </Link>

              <a
                href="#services-list"
                className="info-button info-button-secondary"
              >
                Explore Services
              </a>
            </div>
          </div>

          <div className="services-hero-summary">
            <div className="services-summary-card">
              <span className="services-summary-label">Patient Support</span>

              <strong>Reliable care when you need it</strong>

              <p>
                Our healthcare services are designed around clear
                communication, professional consultation, and patient comfort.
              </p>

              <div className="services-summary-meta">
                <div>
                  <strong>6+</strong>
                  <span>Core Services</span>
                </div>

                <div>
                  <strong>7 Days</strong>
                  <span>Weekly Support</span>
                </div>
              </div>
            </div>

            <div className="services-hero-shape services-shape-one" />
            <div className="services-hero-shape services-shape-two" />
          </div>
        </div>
      </section>

      <section
        id="services-list"
        className="info-section services-list-section"
      >
        <div className="info-container">
          <header className="services-section-heading">
            <div>
              <span className="info-eyebrow">What We Provide</span>

              <h2 className="info-section-title">
                Care designed around your needs
              </h2>
            </div>

            <p>
              From routine consultation to long-term health guidance, our
              services are structured to make healthcare clear, accessible, and
              comfortable.
            </p>
          </header>

          <div className="services-card-grid">
            {services.map((service) => (
              <ServiceCard key={service.id} service={service} />
            ))}
          </div>
        </div>
      </section>

      <section className="info-section services-process-section">
        <div className="info-container">
          <header className="info-section-header">
            <span className="info-eyebrow">Our Care Approach</span>

            <h2 className="info-section-title">
              A better healthcare experience
            </h2>

            <p>
              Our approach focuses on understanding the patient, communicating
              clearly, and providing responsible guidance throughout the care
              journey.
            </p>
          </header>

          <div className="service-features-grid">
            {serviceFeatures.map((feature, index) => (
              <article className="service-feature-card" key={feature.id}>
                <span className="service-feature-number">
                  {String(index + 1).padStart(2, "0")}
                </span>

                <div className="service-feature-icon" aria-hidden="true">
                  +
                </div>

                <h3>{feature.title}</h3>

                <p>{feature.description}</p>
              </article>
            ))}
          </div>
        </div>
      </section>

      <section className="services-assistance-section">
        <div className="info-container services-assistance-grid">
          <div>
            <span className="services-assistance-label">
              Need medical guidance?
            </span>

            <h2>Not sure which service is right for you?</h2>

            <p>
              Speak with our healthcare team and receive guidance about the
              most suitable consultation based on your concerns.
            </p>
          </div>

          <div className="services-assistance-actions">
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

export default Services;