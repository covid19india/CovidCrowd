import React from 'react';
import './App.css';
import axios from "axios";
import TopNav from "./components/TopNav";
import BottomFooter from "./components/BottomFooter";
import PatientTable from "./components/PatientTable";
import { addPatients } from "./store";
import { connect } from "react-redux";

function getTable(patients) {
  if (patients.length) {
    return <PatientTable patients={patients} />
  }
  return <h3 className="h3 my-3">Loading...</h3>
}

const mapStateToProps = function(state) {
  return {
    patients: state.patients
  }
};

const mapDispatchToProps = {
  addPatients: addPatients
};

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      isLoading: true,
      patients: props.patients
    }
  }

  componentDidMount() {
    if (!this.patients) {
      axios.get("/api/patients")
        .then(res => {
          this.setState({patients: res.data, isLoading: false});
          this.props.dispatch(addPatients(res.data));
        })
        .catch(err => console.log(err));
    }
  }


  render() {
    return (
      <div className="App">
        <TopNav />
        <main className="container">
          { getTable(this.state.patients) }
        </main>
        <BottomFooter />
      </div>
    );
  }
}

const AppContainer = connect(mapStateToProps, mapDispatchToProps)(App);

export default AppContainer;
