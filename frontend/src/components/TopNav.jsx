import React, { useState } from 'react';
import {
  Collapse,
  Navbar,
  NavbarToggler,
  NavbarBrand,
  Nav,
  NavItem,
  NavLink,
} from 'reactstrap';
import logo from './covidcrowd.svg';

const Example = (props) => {
  const [isOpen, setIsOpen] = useState(false);

  const toggle = () => setIsOpen(!isOpen);

  return (
    <div>
      <Navbar color="white" light expand="md">
        <NavbarBrand href="/" className="text-primary">
          <img src={logo} alt="" width={30} height={30} className="mr-2"/>
          Covid-19 India
        </NavbarBrand>
        <NavbarToggler onClick={toggle} />
        <Collapse isOpen={isOpen} navbar>
          <Nav navbar>
            <NavItem>
              <NavLink href="http://covid19india.org">Dashboard</NavLink>
            </NavItem>
            <NavItem>
              <NavLink href="https://www.covid19india.org/clusters">Clusters</NavLink>
            </NavItem>
            <NavItem>
              <NavLink href="https://www.covid19india.org/links">Helpful Links</NavLink>
            </NavItem>
            <NavItem>
              <NavLink href="https://www.covid19india.org/faq">FAQ</NavLink>
            </NavItem>
          </Nav>
        </Collapse>
      </Navbar>
    </div>
  );
};

export default Example;