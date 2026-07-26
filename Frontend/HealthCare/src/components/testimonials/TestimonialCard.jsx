function TestimonialCard({ testimonial }) {
  const stars = Array.from(
    { length: testimonial.rating },
    (_, index) => index + 1
  );

  return (
    <article
      className={`testimonial-card ${
        testimonial.featured ? "testimonial-card-featured" : ""
      }`}
    >
      <div className="testimonial-card-header">
        <div className="testimonial-patient">
          <div
            className="testimonial-avatar"
            aria-hidden="true"
          >
            {testimonial.initials}
          </div>

          <div>
            <h2>{testimonial.patientName}</h2>

            <span>{testimonial.location}</span>
          </div>
        </div>

        <span className="testimonial-quote-icon" aria-hidden="true">
          “
        </span>
      </div>

      <div
        className="testimonial-rating"
        aria-label={`${testimonial.rating} out of 5 stars`}
      >
        {stars.map((star) => (
          <span key={star} aria-hidden="true">
            ★
          </span>
        ))}
      </div>

      <blockquote>
        <p>{testimonial.feedback}</p>
      </blockquote>

      <div className="testimonial-card-footer">
        <span>Service Used</span>
        <strong>{testimonial.service}</strong>
      </div>
    </article>
  );
}

export default TestimonialCard;