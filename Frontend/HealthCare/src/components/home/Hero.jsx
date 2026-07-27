import { Link } from "react-router-dom";

function Hero() {
  return (
    <section className="hero-section">
      <div className="hero-container">
        <div className="hero-content">
          <span className="hero-eyebrow">
            Trusted Healthcare for Your Family
          </span>

          <h1>
            Professional Healthcare
            <br />
            for Every Family
          </h1>

          <p>
            Quality medical care delivered by experienced healthcare
            professionals with compassion, trust, and modern facilities.
          </p>

          <div className="hero-actions">
            <Link to="/appointment" className="hero-primary-button">
              Book an Appointment
            </Link>

            <Link to="/services" className="hero-secondary-button">
              Explore Our Services
            </Link>
          </div>
        </div>
      </div>
    </section>
  );
}

export default Hero;