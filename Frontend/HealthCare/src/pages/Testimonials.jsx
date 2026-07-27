import { Link } from "react-router-dom";

import TestimonialsSection from "../components/testimonials/TestimonialsSection.jsx";

import testimonials, {
  feedbackPrinciples,
  testimonialStats,
} from "../data/testimonials.js";

import "../styles/information-pages.css";

function Testimonials() {
  const featuredTestimonials = testimonials
    .filter((testimonial) => testimonial.featured)
    .slice(0, 2);

  return (
    <main className="information-page">
      <section className="testimonials-hero">
        <div className="info-container testimonials-hero-grid">
          <div className="testimonials-hero-content">
            <span className="info-eyebrow">Patient Experiences</span>

            <h1>
              Real experiences.
              <span> Meaningful care.</span>
            </h1>

            <p>
              Discover how patients describe their consultation,
              communication, comfort, and overall healthcare experience with
              our medical team.
            </p>

            <div className="testimonials-hero-actions">
              <Link
                to="/appointment"
                className="info-button info-button-primary"
              >
                Book an Appointment
              </Link>

              <a
                href="#patient-stories"
                className="info-button info-button-secondary"
              >
                Read Patient Stories
              </a>
            </div>

            <div className="testimonials-hero-rating">
              <div
                className="testimonials-rating-stars"
                aria-hidden="true"
              >
                ★★★★★
              </div>

              <div>
                <strong>4.9 out of 5</strong>
                <span>Based on patient feedback</span>
              </div>
            </div>
          </div>

          <div className="testimonials-hero-visual">
            {featuredTestimonials.map((testimonial, index) => (
              <article
                className={`testimonial-hero-card testimonial-hero-card-${
                  index + 1
                }`}
                key={testimonial.id}
              >
                <div className="testimonial-hero-card-top">
                  <div
                    className="testimonial-avatar"
                    aria-hidden="true"
                  >
                    {testimonial.initials}
                  </div>

                  <div>
                    <strong>{testimonial.patientName}</strong>
                    <span>{testimonial.service}</span>
                  </div>
                </div>

                <div
                  className="testimonial-rating"
                  aria-label={`${testimonial.rating} out of 5 stars`}
                >
                  {Array.from(
                    { length: testimonial.rating },
                    (_, starIndex) => (
                      <span key={starIndex} aria-hidden="true">
                        ★
                      </span>
                    ),
                  )}
                </div>

                <p>“{testimonial.feedback}”</p>
              </article>
            ))}

            <div className="testimonial-hero-summary">
              <strong>98%</strong>
              <span>
                Patients report a positive consultation experience
              </span>
            </div>

            <div
              className="testimonial-decoration testimonial-decoration-one"
              aria-hidden="true"
            />

            <div
              className="testimonial-decoration testimonial-decoration-two"
              aria-hidden="true"
            />
          </div>
        </div>
      </section>

      <section
        className="testimonial-stats-section"
        aria-label="Patient feedback statistics"
      >
        <div className="info-container testimonial-stats-grid">
          {testimonialStats.map((stat) => (
            <article className="testimonial-stat-item" key={stat.id}>
              <strong>{stat.value}</strong>
              <span>{stat.label}</span>
            </article>
          ))}
        </div>
      </section>

      <div id="patient-stories">
        <TestimonialsSection
          eyebrow="Patient Stories"
          title="What patients say about their care"
          description="Every patient experience helps us understand how clearly, comfortably, and responsibly we are delivering healthcare."
          showViewAll={false}
        />
      </div>

      <section className="info-section testimonials-feedback-section">
        <div className="info-container testimonials-feedback-grid">
          <div className="testimonials-feedback-intro">
            <span className="info-eyebrow">
              Your Feedback Matters
            </span>

            <h2 className="info-section-title">
              Better healthcare starts by listening
            </h2>

            <p>
              We use responsible patient feedback to improve communication,
              consultation quality, clinic comfort, and the overall healthcare
              experience.
            </p>

            <Link
              to="/contact"
              className="info-button info-button-secondary"
            >
              Share Your Feedback
            </Link>
          </div>

          <div className="testimonials-feedback-principles">
            {feedbackPrinciples.map((principle) => (
              <article
                className="testimonial-feedback-card"
                key={principle.id}
              >
                <span>{principle.number}</span>

                <div>
                  <h3>{principle.title}</h3>
                  <p>{principle.description}</p>
                </div>
              </article>
            ))}
          </div>
        </div>
      </section>

      <section className="testimonials-cta-section">
        <div className="info-container testimonials-cta-grid">
          <div>
            <span className="testimonials-cta-label">
              Start Your Care Journey
            </span>

            <h2>
              Experience professional, thoughtful, and patient-focused care.
            </h2>

            <p>
              Schedule a consultation with our medical team and receive clear
              guidance designed around your healthcare needs.
            </p>
          </div>

          <div className="testimonials-cta-actions">
            <Link
              to="/appointment"
              className="info-button info-button-light"
            >
              Book Appointment
            </Link>

            <Link
              to="/doctors"
              className="info-button info-button-outline-light"
            >
              Meet Our Doctors
            </Link>
          </div>
        </div>
      </section>
    </main>
  );
}

export default Testimonials;