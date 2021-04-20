import React from 'react';
import Navbar from 'react-bootstrap/Navbar'
import Nav from 'react-bootstrap/Nav'



const navbarComponent = (props) => (

    <Navbar bg="dark" expand="lg" variant="dark">
        <Navbar.Brand href="#home">Police Accountability</Navbar.Brand>
        <Navbar.Toggle aria-controls="basic-navbar-nav" />
        <Navbar.Collapse id="basic-navbar-nav">
            <Nav className="mr-auto">
                <Nav.Link href="#home">Home</Nav.Link>
                <Nav.Link href="#link">Police Complaint Records</Nav.Link>
            </Nav>

        </Navbar.Collapse>
    </Navbar>
)

export default navbarComponent
