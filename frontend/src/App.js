import React from 'react';
import './App.css';
import axios from "axios";
import TopNav from "./components/TopNav";
import BottomFooter from "./components/BottomFooter";
import { Route, Switch, BrowserRouter as Router } from "react-router-dom";
import PatientDetail from "./pages/patient-detail";
import NewPatient from "./pages/new-patient";
import HomePage from "./pages/home-page";

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      isLoading: true,
      patients: []
    }
  }

  componentDidMount() {
    axios.get("/api/patients")
      .then(res => {
        this.setState({patients: res.data, isLoading: false});
      })
      .catch(err => console.log(err));
  }


  render() {
    return (
      <div className="App">
        <TopNav />
        { this.state.isLoading ?
          <h3 className="my-3">Loading ....</h3> :
          <Router>
            <Switch>
              <Route path="/patient/:id">
                <PatientDetail patients={this.state.patients}/>
              </Route>
              <Route path="/new-patient" component={NewPatient}/>
              <Route exact path="/">
                <HomePage patients={this.state.patients}/>
              </Route>
            </Switch>
          </Router>
        }
        <BottomFooter />
      </div>
    );
  }
}

export default App;
