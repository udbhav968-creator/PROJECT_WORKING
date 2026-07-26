import { NavLink } from "react-router-dom";

const navigationLinks = [
  { label: "Home", path: "/" },
  { label: "About", path: "/about" },
  { label: "Services", path: "/services" },
  { label: "Doctors", path: "/doctors" },
  { label: "Gallery", path: "/gallery" },
  { label: "Blog", path: "/blog" },
  { label: "Contact", path: "/contact" },
];

function Navbar() {
  return (
    <header className="navbar">
      <div className="navbar-container">
        <NavLink to="/" className="navbar-logo">
          HealthCare
        </NavLink>

        <nav className="navbar-links" aria-label="Primary Navigation">
          {navigationLinks.map((link) => (
            <NavLink
              key={link.path}
              to={link.path}
              end={link.path === "/"}
              className={({ isActive }) =>
                isActive ? "navbar-link active" : "navbar-link"
              }
            >
              {link.label}
            </NavLink>
          ))}

          <NavLink
            to="/appointment"
            className={({ isActive }) =>
              isActive
                ? "navbar-link navbar-cta active"
                : "navbar-link navbar-cta"
            }
          >
            Book Appointment
          </NavLink>
        </nav>
      </div>
    </header>
  );
}

export default Navbar;