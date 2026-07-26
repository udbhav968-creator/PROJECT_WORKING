import { Link } from "react-router-dom";
import { ArrowRight, Clock3 } from "lucide-react";

function ServiceCard({ service }) {
  return (
    <article className="service-card">
      <Link
        to={`/services/${service.slug}`}
        className="service-card-image-link"
        aria-label={`View details for ${service.title}`}
      >
        <div className="service-card-image">
          <img
            src={service.image}
            alt={`${service.title} healthcare service`}
            loading="lazy"
            width="600"
            height="420"
          />

          <span className="service-card-number">{service.icon}</span>
        </div>
      </Link>

      <div className="service-card-content">
        <span className="service-card-category">{service.category}</span>

        <h2>
          <Link to={`/services/${service.slug}`}>{service.title}</Link>
        </h2>

        <p>{service.shortDescription}</p>

        <div className="service-card-footer">
          <Link
            to={`/services/${service.slug}`}
            className="service-card-link"
          >
            View Service
            <ArrowRight size={16} aria-hidden="true" />
          </Link>

          <span className="service-duration">
            <Clock3 size={14} aria-hidden="true" />
            {service.duration}
          </span>
        </div>
      </div>
    </article>
  );
}

export default ServiceCard;