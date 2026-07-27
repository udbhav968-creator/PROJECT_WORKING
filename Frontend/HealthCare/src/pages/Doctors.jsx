import { Link } from "react-router-dom";
import {
  ArrowDown,
  ArrowRight,
  CalendarDays,
  Ear,
  HeartPulse,
  MessagesSquare,
  UserRoundCheck,
} from "lucide-react";

import DoctorCard from "../components/doctors/DoctorCard.jsx";

import doctors, {
  carePrinciples,
  doctorHighlights,
} from "../data/doctors.js";

import "../styles/information-pages.css";

const carePrincipleIcons = {
  1: Ear,
  2: MessagesSquare,
  3: UserRoundCheck,
};

function Doctors() {
  return (
    <main className="information-page">
      <section className="doctors-hero">
        <div className="info-container doctors-hero-grid">
          <div className="doctors-hero-content">
            <span className="info-eyebrow">Meet Our Medical Team</span>

            <h1>
              Trusted doctors.
              <span> Thoughtful care.</span>
            </h1>

            <p>
              Meet experienced healthcare professionals committed to clear
              communication, responsible medical guidance, and personalized
              attention throughout every consultation.
            </p>

            <div className="doctors-hero-actions">
              <Link
                to="/appointment"
                className="info-button info-button-primary"
              >
                <CalendarDays size={18} aria-hidden="true" />
                Book an Appointment
              </Link>

              <a
                href="#medical-team"
                className="info-button info-button-secondary"
              >
                Meet the Doctors
                <ArrowDown size={18} aria-hidden="true" />
              </a>
            </div>

            <div className="doctors-trust-line">
              <div className="doctor-avatar-stack" aria-hidden="true">
                {doctors.map((doctor) => (
                  <img
                    key={doctor.id}
                    src={doctor.image}
                    alt=""
                    width="48"
                    height="48"
                  />
                ))}
              </div>

              <div>
                <strong>Experienced medical professionals</strong>
                <span>Patient-focused consultation and support</span>
              </div>
            </div>
          </div>

          <div className="doctors-hero-visual">
            <div className="doctors-hero-image-main">
              <img
                src={doctors[0].image}
                alt={`${doctors[0].name}, ${doctors[0].specialization}`}
                width="720"
                height="840"
                fetchPriority="high"
              />

              <div className="doctors-hero-experience-card">
                <strong>25+</strong>
                <span>Years of combined medical experience</span>
              </div>
            </div>

            <div className="doctors-hero-mini-card">
              <span className="doctors-mini-icon" aria-hidden="true">
                <HeartPulse size={21} strokeWidth={2.1} />
              </span>

              <div>
                <strong>Personalized Care</strong>
                <span>Guidance designed around every patient</span>
              </div>
            </div>

            <div className="doctors-hero-decoration doctors-decoration-one" />
            <div className="doctors-hero-decoration doctors-decoration-two" />
          </div>
        </div>
      </section>

      <section className="doctor-highlights-section">
        <div className="info-container doctor-highlights-grid">
          {doctorHighlights.map((item) => (
            <article className="doctor-highlight-item" key={item.id}>
              <strong>{item.number}</strong>
              <span>{item.label}</span>
            </article>
          ))}
        </div>
      </section>

      <section
        id="medical-team"
        className="info-section doctors-list-section"
      >
        <div className="info-container">
          <header className="doctors-section-heading">
            <div>
              <span className="info-eyebrow">
                Our Healthcare Professionals
              </span>

              <h2 className="info-section-title">
                Meet the doctors behind your care
              </h2>
            </div>

            <p>
              Our doctors combine medical experience with a patient-first
              approach to make every consultation clear, comfortable, and
              meaningful.
            </p>
          </header>

          <div className="doctors-card-grid">
            {doctors.map((doctor) => (
              <DoctorCard key={doctor.id} doctor={doctor} />
            ))}
          </div>
        </div>
      </section>

      <section className="info-section doctors-care-section">
        <div className="info-container doctors-care-grid">
          <div className="doctors-care-intro">
            <span className="info-eyebrow">How We Care</span>

            <h2 className="info-section-title">
              Medical expertise with a human approach
            </h2>

            <p>
              Good healthcare is not limited to diagnosis and treatment. It
              also requires listening carefully, explaining clearly, and
              helping patients feel confident about their next steps.
            </p>

            <Link
              to="/about"
              className="info-button info-button-secondary"
            >
              Learn About Our Clinic
              <ArrowRight size={18} aria-hidden="true" />
            </Link>
          </div>

          <div className="doctors-care-principles">
            {carePrinciples.map((principle) => {
              const PrincipleIcon =
                carePrincipleIcons[principle.id] || HeartPulse;

              return (
                <article
                  className="doctor-care-principle"
                  key={principle.id}
                >
                  <span className="doctor-care-icon" aria-hidden="true">
                    <PrincipleIcon size={22} strokeWidth={2} />
                  </span>

                  <div>
                    <small>{principle.number}</small>
                    <h3>{principle.title}</h3>
                    <p>{principle.description}</p>
                  </div>
                </article>
              );
            })}
          </div>
        </div>
      </section>

      <section className="doctors-appointment-section">
        <div className="info-container doctors-appointment-grid">
          <div>
            <span className="doctors-appointment-label">
              Schedule Your Consultation
            </span>

            <h2>Connect with the right doctor for your healthcare needs.</h2>

            <p>
              Choose a convenient appointment time and receive professional
              guidance from our experienced medical team.
            </p>
          </div>

          <div className="doctors-appointment-actions">
            <Link
              to="/appointment"
              className="info-button info-button-light"
            >
              <CalendarDays size={18} aria-hidden="true" />
              Book Appointment
            </Link>

            <Link
              to="/services"
              className="info-button info-button-outline-light"
            >
              Explore Services
              <ArrowRight size={18} aria-hidden="true" />
            </Link>
          </div>
        </div>
      </section>
    </main>
  );
}

export default Doctors;