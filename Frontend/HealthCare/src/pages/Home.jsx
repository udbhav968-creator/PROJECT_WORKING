import Hero from "../components/home/Hero.jsx";
import AboutPreview from "../components/home/AboutPreview.jsx";
import TestimonialsSection from "../components/testimonials/TestimonialsSection";
function Home() {
  return (
    <main>
      <Hero />
      <AboutPreview />
      <TestimonialsSection
  limit={3}
  showViewAllButton={true}
  title="What Our Patients Say"
  subtitle="Real experiences shared by patients who trusted us with their healthcare."
/>
    </main>
  );
}

export default Home;