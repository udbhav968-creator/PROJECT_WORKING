const Footer = () => {
  return (
    <footer className="footer">
      <div className="footer-container">
        <div className="footer-section">
          <h3>HealthCare</h3>
          <p>
            Providing quality healthcare services with care, trust, and
            dedication.
          </p>
        </div>

        <div className="footer-section">
          <h4>Quick Links</h4>
          <a href="/">Home</a>
          <a href="/about">About</a>
          <a href="/doctors">Doctors</a>
          <a href="/services">Services</a>
        </div>

        <div className="footer-section">
          <h4>Contact</h4>
          <p>Email: info@healthcare.com</p>
          <p>Phone: +1 234 567 890</p>
          <p>Location: Bangalore, India</p>
        </div>
      </div>

      <div className="footer-bottom">
        <p>© 2026 HealthCare. All rights reserved.</p>
      </div>
    </footer>
  );
};

export default Footer;