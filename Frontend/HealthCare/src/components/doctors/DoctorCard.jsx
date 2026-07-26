import { Link } from "react-router-dom";

function DoctorCard({ doctor }) {
  const isLimited = doctor.status === "Limited Slots";

  return (
    <article className="doctor-card">
      <div className="doctor-card-image">
        <img
          src={doctor.image}
          alt={`${doctor.name}, ${doctor.specialization}`}
          loading="lazy"
          width="600"
          height="720"
        />

        <span
          className={`doctor-status ${
            isLimited ? "doctor-status-limited" : ""
          }`}
        >
          <span aria-hidden="true" />
          {doctor.status}
        </span>

        <div className="doctor-image-overlay">
          <span>{doctor.experience}</span>
        </div>
      </div>

      <div className="doctor-card-content">
        <span className="doctor-specialization">
          {doctor.specialization}
        </span>

        <h2>{doctor.name}</h2>

        <p className="doctor-qualification">
          {doctor.qualification}
        </p>

        <p className="doctor-bio">{doctor.shortBio}</p>

        <div className="doctor-expertise-list">
          {doctor.expertise.map((item) => (
            <span key={item}>{item}</span>
          ))}
        </div>

        <div className="doctor-schedule">
          <div>
            <span>Available</span>
            <strong>{doctor.availability}</strong>
          </div>

          <div>
            <span>Consultation</span>
            <strong>{doctor.consultationTime}</strong>
          </div>
        </div>

        <div className="doctor-card-actions">
          <Link
            to={`/appointment?doctor=${doctor.slug}`}
            className="info-button info-button-primary doctor-book-button"
          >
            Book Appointment
          </Link>

          <Link
            to="/contact"
            className="doctor-contact-link"
            aria-label={`Contact clinic regarding ${doctor.name}`}
          >
            Ask a Question
            <span aria-hidden="true">→</span>
          </Link>
        </div>
      </div>
    </article>
  );
}

export default DoctorCard;