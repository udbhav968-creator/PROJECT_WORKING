import { Link } from "react-router-dom";

import testimonials from "../../data/testimonials.js";
import TestimonialCard from "./TestimonialCard.jsx";

function TestimonialsSection({
  eyebrow = "Patient Stories",
  title = "Trusted by patients and their families",
  description = "Read what our patients say about their consultation, treatment, comfort, and overall healthcare experience.",
  limit,
  showViewAll = true,
}) {
  const visibleTestimonials =
    typeof limit === "number"
      ? testimonials.slice(0, limit)
      : testimonials;

  return (
    <section className="info-section testimonials-list-section">
      <div className="info-container">
        <header className="testimonials-section-heading">
          <div>
            <span className="info-eyebrow">{eyebrow}</span>

            <h2 className="info-section-title">{title}</h2>
          </div>

          <p>{description}</p>
        </header>

        <div className="testimonials-card-grid">
          {visibleTestimonials.map((testimonial) => (
            <TestimonialCard
              key={testimonial.id}
              testimonial={testimonial}
            />
          ))}
        </div>

        {showViewAll && (
          <div className="testimonials-section-action">
            <Link to="/testimonials" className="info-text-link">
              View all patient stories
              <span aria-hidden="true">→</span>
            </Link>
          </div>
        )}
      </div>
    </section>
  );
}

export default TestimonialsSection;