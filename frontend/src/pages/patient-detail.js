import React from "react";
import { useParams } from "react-router-dom";

function PatientDetail() {
  const { id } = useParams();
  return (
    <h3>Patient {id}</h3>
  );
}

export  default PatientDetail
