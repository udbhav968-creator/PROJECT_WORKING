import { Link } from "react-router-dom";

import aboutImage from "../../assets/images/about/clinic-consultation.jpg";

function AboutPreview() {
  return (
    <section className="about-preview-section">
      <div className="about-preview-container">
        <div className="about-preview-image">
          <img
            src={aboutImage}
            alt="Healthcare professional consulting with a patient"
          />
        </div>

        <div className="about-preview-content">
          <span className="about-preview-eyebrow">
            About Our Healthcare Clinic
          </span>

          <h2>Compassionate Care You Can Trust</h2>

          <p>
            We are committed to providing reliable, patient-focused healthcare
            services in a comfortable and welcoming environment.
          </p>

          <p>
            Our experienced healthcare professionals focus on understanding
            every patient's needs and delivering quality care with compassion.
          </p>

          <Link to="/about" className="about-preview-button">
            Learn More About Us
          </Link>
        </div>
      </div>
    </section>
  );
}

export default AboutPreview;