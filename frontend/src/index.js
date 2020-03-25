import React from 'react';
import ReactDOM from 'react-dom';
import { Route, Switch, BrowserRouter as Router } from 'react-router-dom';
import { library } from "@fortawesome/fontawesome-svg-core";
import {
  faArrowCircleRight, faSort, faSortAmountDown, faSortAmountUp,
  faChevronLeft, faAngleDoubleLeft, faChevronRight, faAngleDoubleRight
} from '@fortawesome/free-solid-svg-icons';

import 'bootstrap/dist/css/bootstrap.min.css';
import './extras/css/argon-design-system.min.css';
import './index.css';
import App from './App';
import NewPatient from "./pages/new-patient";
import PatientDetail from "./pages/patient-detail";
import * as serviceWorker from './serviceWorker';

library.add(faArrowCircleRight, faSort, faSortAmountDown, faSortAmountUp,
  faChevronLeft, faAngleDoubleLeft, faChevronRight, faAngleDoubleRight);

const routing = (
  <Router>
    <Switch>
      <Route path="/new-patient" component={NewPatient} />
      <Route path="/patient" component={PatientDetail} />
      <Route exact path="/" component={App} />
    </Switch>
  </Router>
);


ReactDOM.render(
  routing,
  document.getElementById('root')
);

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
