import { Navigate, Route, Routes } from "react-router-dom";

import PageLayout from "./components/layout/PageLayout.jsx";
import ScrollToTop from "./components/common/ScrollToTop.jsx";
import Home from "./pages/Home.jsx";
import About from "./pages/About.jsx";
import Services from "./pages/Services.jsx";
import ServiceDetails from "./pages/ServiceDetails.jsx";
import Doctors from "./pages/Doctors.jsx";
import Testimonials from "./pages/Testimonials.jsx";

import "./styles/layout.css";


function PlaceholderPage({ title }) {
  return (
    <main className="integration-placeholder">
      <div className="integration-placeholder-container">
        <h1>{title}</h1>

        <p>
          This page is currently being developed by the assigned team member.
        </p>
      </div>
    </main>
  );
}

function App() {
  return (
    <>
      <ScrollToTop />

      <PageLayout>
        <Routes>
          <Route path="/" element={<Home />} />

          <Route path="/about" element={<About />} />

          <Route path="/services" element={<Services />} />

          <Route
            path="/services/:serviceSlug"
            element={<ServiceDetails />}
          />

          <Route path="/doctors" element={<Doctors />} />

          <Route
            path="/testimonials"
            element={<Testimonials />}
          />

          <Route
            path="/appointment"
            element={<PlaceholderPage title="Appointment Page" />}
          />

          <Route
            path="/contact"
            element={<PlaceholderPage title="Contact Page" />}
          />

          <Route path="*" element={<Navigate to="/" replace />} />
        </Routes>
      </PageLayout>
    </>
  );
}

export default App;