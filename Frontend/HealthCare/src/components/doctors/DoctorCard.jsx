import { Link } from "react-router-dom";
import {
  ArrowRight,
  CalendarDays,
  Clock3,
  MessageCircleMore,
} from "lucide-react";

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
            <span className="doctor-schedule-label">
              <CalendarDays size={14} aria-hidden="true" />
              Available
            </span>
            <strong>{doctor.availability}</strong>
          </div>

          <div>
            <span className="doctor-schedule-label">
              <Clock3 size={14} aria-hidden="true" />
              Consultation
            </span>
            <strong>{doctor.consultationTime}</strong>
          </div>
        </div>

        <div className="doctor-card-actions">
          <Link
            to={`/appointment?doctor=${doctor.slug}`}
            className="info-button info-button-primary doctor-book-button"
          >
            <CalendarDays size={16} aria-hidden="true" />
            Book Appointment
          </Link>

          <Link
            to="/contact"
            className="doctor-contact-link"
            aria-label={`Contact clinic regarding ${doctor.name}`}
          >
            <MessageCircleMore size={16} aria-hidden="true" />
            Ask a Question
            <ArrowRight size={15} aria-hidden="true" />
          </Link>
        </div>
      </div>
    </article>
  );
}

export default DoctorCard;