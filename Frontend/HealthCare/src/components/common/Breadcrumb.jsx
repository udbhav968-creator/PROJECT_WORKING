import { Link } from "react-router-dom";

const Breadcrumb = ({ currentPage }) => {
  return (
    <div className="breadcrumb">
      <Link to="/">Home</Link>
      <span> / </span>
      <span>{currentPage}</span>
    </div>
  );
};

export default Breadcrumb;