import Navbar from "./Navbar";
import Footer from "./Footer";

const PageLayout = ({ children }) => {
  return (
    <>
      <Navbar />

      <main className="page-content">
        {children}
      </main>

      <Footer />
    </>
  );
};

export default PageLayout;