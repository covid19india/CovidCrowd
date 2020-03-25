import React from 'react';
import logo from './img/covidcrowd.svg'
import home from './home'
import {BrowserRouter as Router, Route, Switch} from 'react-router-dom';
import './css/font-awesome.css'
import './css/app.css';
import './css/argon-design-system.min.css'

function App() {
  return (
    <div>
      <nav className="navbar navbar-expand-lg">
        <a className="navbar-brand" href="/">
          <img src={logo} className="d-inline-block" alt="" width="30" height="30"/>
          Covid-19 India
        </a>
        <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbar-primary"
                aria-controls="navbar-primary" aria-expanded="false" aria-label="Toggle navigation">
        <span className="navbar-toggler-icon text-primary">
          <i className="fa fa-bars"/>
        </span>
        </button>
        <div className="collapse navbar-collapse" id="navbar-primary">
          <div className="navbar-collapse-header">
            <div className="row">
              <div className="col-6 collapse-brand">
                <a className="navbar-brand" href="/">Covid-19 India</a>
              </div>
              <div className="col-6 collapse-close">
                <button type="button" className="navbar-toggler" data-toggle="collapse" data-target="#navbar-primary"
                        aria-controls="navbar-primary" aria-expanded="false" aria-label="Toggle navigation">
                  <span/>
                  <span/>
                </button>
              </div>
            </div>
          </div>
          <div className="navbar-nav">
            <a className="nav-item nav-link" href="/report">Report New Patient</a>
          </div>
          <ul className="navbar-nav ml-auto">

            <li className="nav-item">
              <a className="nav-link" href="/login-form">Login</a>
            </li>

          </ul>

        </div>
      </nav>
      <main>
        <Router>
          <Switch>
            <Route exact path='/' component={home}/>
          </Switch>
        </Router>
      </main>
      <footer className="mt-5 p-5 border-top bg-lighter">
        <div className="row text-gray-dark text-center">
          <div className="col">
            <small>
              The data on this site is curated by a team of volunteers under the umbrella of <a
              href="http://covid19india.org">Covid19India.org</a> from multiple sources
              including news reports, Twitter posts and official Govt Websites like the <a
              href="https://www.mohfw.gov.in/">MoFHW</a> site.
            </small>
          </div>
        </div>
        <div className="row mt-2">
          <div className="col text-center">
            <span></span>
            <a href="https://twitter.com/share?ref_src=twsrc%5Etfw" className="twitter-share-button" data-size="large"
               data-via="covid19indiaorg" data-hashtags="covid19india" data-dnt="true" data-show-count="false">
              Tweet
            </a>
          </div>
        </div>
      </footer>
    </div>
  );
}

export default App;
