import { Link } from "react-router-dom";

function Footer() {
  return (
    <footer className="footer">
      <div className="footer-container">
        {/* Brand */}
        <div className="footer-section footer-about">
          <Link to="/" className="footer-logo">
            HealthCare
          </Link>

          <p>
            Delivering trusted, compassionate, and patient-centered healthcare
            services with experienced doctors, advanced medical facilities, and
            personalized care for every stage of life.
          </p>
        </div>

        {/* Quick Links */}
        <div className="footer-section">
          <h2>Quick Links</h2>

          <div className="footer-links">
            <Link to="/">Home</Link>
            <Link to="/about">About</Link>
            <Link to="/services">Services</Link>
            <Link to="/doctors">Doctors</Link>
            <Link to="/contact">Contact</Link>
          </div>
        </div>

        {/* Services */}
        <div className="footer-section">
          <h2>Patient Support</h2>

          <div className="footer-links">
            <Link to="/appointment">Book Appointment</Link>
            <Link to="/services">Our Services</Link>
            <Link to="/contact">Contact Us</Link>
          </div>
        </div>

        {/* Contact */}
        <div className="footer-section">
          <h2>Contact</h2>

          <address className="footer-contact">
            <a href="mailto:info@healthcare.com">
              info@healthcare.com
            </a>

            <a href="tel:+911234567890">
              +91 12345 67890
            </a>

            <p>
              Sanpada, Navi Mumbai,
              <br />
              Maharashtra, India
            </p>
          </address>
        </div>
      </div>

      <div className="footer-bottom">
        <p>
          © {new Date().getFullYear()} HealthCare. All Rights Reserved.
        </p>
      </div>
    </footer>
  );
}

export default Footer;