function TestimonialCard({ testimonial }) {
  const {
    patientName,
    initials,
    location,
    rating,
    feedback,
    service,
    featured,
  } = testimonial;

  const stars = Array.from({ length: 5 }, (_, index) => index + 1);

  return (
    <article
      className={`testimonial-card ${
        featured ? "testimonial-card-featured" : ""
      }`}
    >
      <div className="testimonial-card-header">
        <div className="testimonial-patient">
          <div className="testimonial-avatar" aria-hidden="true">
            {initials}
          </div>

          <div>
            <h3>{patientName}</h3>
            <span>{location}</span>
          </div>
        </div>

        <span className="testimonial-quote-icon" aria-hidden="true">
          “
        </span>
      </div>

      <div
        className="testimonial-rating"
        aria-label={`${rating} out of 5 stars`}
      >
        {stars.map((star) => (
          <span
            key={star}
            className={star <= rating ? "testimonial-star-active" : ""}
            aria-hidden="true"
          >
            ★
          </span>
        ))}
      </div>

      <blockquote>
        <p>“{feedback}”</p>
      </blockquote>

      <div className="testimonial-card-footer">
        <span>Service Used</span>
        <strong>{service}</strong>
      </div>
    </article>
  );
}

export default TestimonialCard;