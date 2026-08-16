import React from "react";
import "../assets/style.css";
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap/dist/js/bootstrap.bundle.min.js";

const Header = () => {
  const logout = async (e) => {
    e.preventDefault();

    const logoutUrl = window.location.origin + "/djangoapp/logout";

    try {
      const res = await fetch(logoutUrl, {
        method: "GET",
      });

      const json = await res.json();

      if (json) {
        const username = sessionStorage.getItem("username");

        sessionStorage.removeItem("username");

        alert("Logging out " + username + "...");

        window.location.href = window.location.origin;
      } else {
        alert("The user could not be logged out.");
      }
    } catch (error) {
      console.error("Logout error:", error);
      alert("An error occurred while logging out.");
    }
  };

  // Get the username from the current session
  const curr_user = sessionStorage.getItem("username");

  // Default home page items
  let home_page_items = <div></div>;

  // If the user is logged in, show username and logout option
  if (curr_user !== null && curr_user !== "") {
    home_page_items = (
      <div className="input_panel">
        <span className="username">
          {curr_user}
        </span>

        <a
          className="nav_item"
          href="/djangoapp/logout"
          onClick={logout}
        >
          Logout
        </a>
      </div>
    );
  }

  return (
    <div>
      <nav
  className="navbar navbar-expand-lg navbar-light"
  style={{
    backgroundColor: "rgb(232, 245, 237)",
    position: "relative",
    zIndex: 1050,
  }}
>
  <div className="container-fluid">

    <h2 style={{ paddingRight: "5%" }}>
      Dealerships
    </h2>

    <button
      className="navbar-toggler"
      type="button"
      data-bs-toggle="collapse"
      data-bs-target="#navbarText"
      aria-controls="navbarText"
      aria-expanded="false"
      aria-label="Toggle navigation"
    >
      <span className="navbar-toggler-icon"></span>
    </button>

    <div
      className="collapse navbar-collapse"
      id="navbarText"
    >
      <ul className="navbar-nav me-auto mb-2 mb-lg-0">

        <li className="nav-item">
          <a
            className="nav-link active"
            href="/"
          >
            Home
          </a>
        </li>

        <li className="nav-item">
          <a
            className="nav-link"
            href="/about"
          >
            About Us
          </a>
        </li>

        <li className="nav-item">
          <a
            className="nav-link"
            href="/contact"
          >
            Contact Us
          </a>
        </li>

      </ul>

      <span className="navbar-text">
        <div
          className="loginlink"
          id="loginlogout"
        >
          {home_page_items}
        </div>
      </span>

    </div>
  </div>
</nav>
    
    </div>
  );
};
export default Header;