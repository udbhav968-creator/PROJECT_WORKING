import Navbar from "./Navbar.jsx";
import Footer from "./Footer.jsx";

function PageLayout({ children }) {
  return (
    <div className="app-layout">
      <Navbar />

      <div className="page-content">
        {children}
      </div>

      <Footer />
    </div>
  );
}

export default PageLayout;