import React from 'react';
import ReactDOM from 'react-dom';
import { library } from "@fortawesome/fontawesome-svg-core";
import {
  faArrowCircleRight, faSort, faSortAmountDown, faSortAmountUp,
  faChevronLeft, faAngleDoubleLeft, faChevronRight, faAngleDoubleRight,
  faBullhorn, faVenusMars, faUserPlus, faHeartbeat, faMapMarkerAlt, faGlobeAsia,
  faExclamationCircle, faArrowAltCircleRight
} from '@fortawesome/free-solid-svg-icons';

import 'bootstrap/dist/css/bootstrap.min.css';
import './index.css';
import App from './App';
import * as serviceWorker from './serviceWorker';

library.add(faArrowCircleRight, faSort, faSortAmountDown, faSortAmountUp,
  faChevronLeft, faAngleDoubleLeft, faChevronRight, faAngleDoubleRight,
  faBullhorn, faVenusMars, faUserPlus, faHeartbeat, faMapMarkerAlt, faGlobeAsia,
  faExclamationCircle, faArrowAltCircleRight
);


ReactDOM.render(
  <App />,
  document.getElementById('root')
);

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
