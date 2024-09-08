import React from "react";
import { Link } from "react-router-dom";
import Logo from "../assets/Logo.jpeg";

const Navbar = () => {
    return (
        <header className="navbar">
            <div className="logo-container">
                <img src={Logo} alt="WalterLustWays" /> 
            </div> 
            <nav>
                <ul className="nav">
                    <li>
                        <Link to="/" className="nav-link">
                            Home
                        </Link>
                    </li>
                    <li>
                        <Link to="/hotels" className="nav-link">
                            Hotels
                        </Link>
                    </li>
                    <li>
                        <Link to="/travels" className="nav-link">
                            Travels
                        </Link>
                    </li>
                    <li>
                        <Link to="/touristdestinations" className="nav-link">
                            Tourist
                        </Link>
                    </li>
                    <li>
                        <Link to="/login" className="login">
                            Login
                        </Link>
                    </li>
                </ul>
            </nav>
        </header>
    );
};

export default Navbar;