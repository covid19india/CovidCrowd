import React from 'react';
import './App.css';
import axios from "axios";
import TopNav from "./components/TopNav";
import BottomFooter from "./components/BottomFooter";
import PatientTable from "./components/PatientTable";

function getTable(patients) {
  if (patients.length) {
    return <PatientTable patients={patients} />
  }
  return <h3 className="h3 my-3">Loading...</h3>
}

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
        <main className="container">
          { getTable(this.state.patients) }
        </main>
        <BottomFooter />
      </div>
    );
  }
}

export default App;
