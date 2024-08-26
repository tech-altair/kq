import React from 'react';
import { Nav } from 'react-bootstrap';
import './App.css'; 

function Sidebar() {
  return (
    <div className="sidebar">
      <Nav className="flex-column">
        <Nav.Link href="#">Dashboard</Nav.Link>
        <Nav.Link href="#">Flights</Nav.Link>
        <Nav.Link href="#">Customers</Nav.Link>
        <Nav.Link href="#">Bookings</Nav.Link>
        <Nav.Link href="#">Services</Nav.Link>
        <Nav.Link href="#">Brands</Nav.Link>
      </Nav>
    </div>
  );
}

export default Sidebar;
