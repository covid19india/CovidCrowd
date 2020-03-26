import React from "react";
import PatientTable from "../components/PatientTable";

function getTable(patients) {
  if (patients.length) {
    return <PatientTable patients={patients} />
  }
  return <h3 className="h3 my-3">Loading...</h3>
}

function HomePage(props) {
  return (
    <main className="container">
      <h3 className="h3 text-uppercase my-3">Affected Patients</h3>
      { getTable(props.patients) }
    </main>
  );
}

export default HomePage