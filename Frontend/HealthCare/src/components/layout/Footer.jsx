import { Link } from "react-router-dom";

function Footer() {
  return (
    <footer className="footer">
      <div className="footer-container">
        <div className="footer-section footer-about">
          <Link to="/" className="footer-logo">
            HealthCare
          </Link>

          <p>
            Providing reliable healthcare services with professional guidance,
            personalized attention, care, trust, and dedication.
          </p>
        </div>

        <div className="footer-section">
          <h2>Quick Links</h2>

          <div className="footer-links">
            <Link to="/">Home</Link>
            <Link to="/about">About</Link>
            <Link to="/doctors">Doctors</Link>
            <Link to="/services">Services</Link>
            <Link to="/testimonials">Testimonials</Link>
          </div>
        </div>

        <div className="footer-section">
          <h2>Patient Support</h2>

          <div className="footer-links">
            <Link to="/appointment">Book Appointment</Link>
            <Link to="/contact">Contact Us</Link>
            <Link to="/services">Healthcare Services</Link>
          </div>
        </div>

        <div className="footer-section">
          <h2>Contact</h2>

          <address className="footer-contact">
            <a href="mailto:doctors@healthcare.com">
              doctors@healthcare.com
            </a>

            <a href="tel:+917861861902">
              +91 7861861902
            </a>

            <p>Sanpada, Navi Mumbai, Maharashtra 400705</p>
          </address>
        </div>
      </div>

      <div className="footer-bottom">
        <p>
          © {new Date().getFullYear()} HealthCare. All rights reserved.
        </p>
      </div>
    </footer>
  );
}

export default Footer;