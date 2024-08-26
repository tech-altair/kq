import React from "react";
import "./index.css";
import { Box } from "@chakra-ui/react";
const NavBar = () => {
  return (
    <Box as="nav" p={4}>
        <nav className="navbar navbar-expand-lg bg-body-tertiary">
      <div className="container-nav">
        <a href="#">Home</a>
        <a href="/dashboard">Comments</a>
      </div>
    </nav>
    </Box>
  );
};

export default NavBar;
