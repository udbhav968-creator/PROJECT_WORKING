import { Link, Navigate, useParams } from "react-router-dom";

import services from "../data/services.js";

import "../styles/information-pages.css";

function ServiceDetails() {
  const { serviceSlug } = useParams();

  const service = services.find((item) => item.slug === serviceSlug);

  if (!service) {
    return <Navigate to="/services" replace />;
  }

  return (
    <main className="information-page">
      <section className="service-detail-hero">
        <div className="info-container">
          <nav className="service-breadcrumb" aria-label="Breadcrumb">
            <Link to="/">Home</Link>
            <span aria-hidden="true">/</span>
            <Link to="/services">Services</Link>
            <span aria-hidden="true">/</span>
            <span>{service.title}</span>
          </nav>

          <div className="service-detail-hero-grid">
            <div className="service-detail-content">
              <span className="info-eyebrow">{service.category}</span>

              <h1>{service.title}</h1>

              <p>{service.shortDescription}</p>

              <div className="service-detail-meta">
                <div>
                  <span>Consultation Duration</span>
                  <strong>{service.duration}</strong>
                </div>

                <div>
                  <span>Availability</span>
                  <strong>{service.availability}</strong>
                </div>
              </div>

              <div className="service-detail-actions">
                <Link
                  to="/appointment"
                  className="info-button info-button-primary"
                >
                  Book This Service
                </Link>

                <Link
                  to="/services"
                  className="info-button info-button-secondary"
                >
                  View All Services
                </Link>
              </div>
            </div>

            <div className="service-detail-image">
              <img
                src={service.image}
                alt={`${service.title} consultation`}
                width="760"
                height="600"
                fetchPriority="high"
              />

              <div className="service-detail-image-badge">
                <span aria-hidden="true">✓</span>

                <div>
                  <strong>Professional Care</strong>
                  <small>Patient-focused healthcare</small>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <section className="info-section">
        <div className="info-container service-detail-main-grid">
          <div className="service-detail-main-content">
            <article className="service-content-section">
              <span className="service-content-label">
                About This Service
              </span>

              <h2>Understanding {service.title}</h2>

              <p>{service.description}</p>

              <p>
                Every consultation is approached with attention, respect, and
                clear communication. Patients are encouraged to discuss their
                concerns openly so the healthcare professional can recommend
                appropriate next steps.
              </p>
            </article>

            <article className="service-content-section">
              <span className="service-content-label">Key Benefits</span>

              <h2>How this service can support you</h2>

              <div className="service-benefits-grid">
                {service.benefits.map((benefit, index) => (
                  <div className="service-benefit-item" key={benefit}>
                    <span>{String(index + 1).padStart(2, "0")}</span>
                    <p>{benefit}</p>
                  </div>
                ))}
              </div>
            </article>

            <article className="service-content-section">
              <span className="service-content-label">What to Expect</span>

              <h2>A clear and comfortable care process</h2>

              <div className="service-process-timeline">
                {service.process.map((step, index) => (
                  <div className="service-process-step" key={step.title}>
                    <div className="service-process-marker">
                      {String(index + 1).padStart(2, "0")}
                    </div>

                    <div>
                      <h3>{step.title}</h3>
                      <p>{step.description}</p>
                    </div>
                  </div>
                ))}
              </div>
            </article>
          </div>

          <aside className="service-detail-sidebar">
            <div className="service-sidebar-card">
              <span className="service-sidebar-label">
                Suitable For
              </span>

              <h2>Who can consider this service?</h2>

              <ul>
                {service.suitableFor.map((item) => (
                  <li key={item}>
                    <span aria-hidden="true">✓</span>
                    {item}
                  </li>
                ))}
              </ul>
            </div>

            <div className="service-sidebar-contact">
              <span className="service-sidebar-contact-icon" aria-hidden="true">
                +
              </span>

              <h2>Need more information?</h2>

              <p>
                Connect with our healthcare team for assistance before booking
                your consultation.
              </p>

              <Link to="/contact">Contact Our Team →</Link>
            </div>
          </aside>
        </div>
      </section>

      <section className="info-cta-section">
        <div className="info-container info-cta-content">
          <div>
            <span className="info-cta-eyebrow">
              Professional Healthcare Support
            </span>

            <h2>Ready to schedule your consultation?</h2>

            <p>
              Book an appointment and connect with our healthcare professionals
              for reliable guidance and personalized attention.
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
              to="/services"
              className="info-button info-button-outline-light"
            >
              Other Services
            </Link>
          </div>
        </div>
      </section>
    </main>
  );
}

export default ServiceDetails;