import { createStore } from "redux";

export const ADD_PATIENTS = "ADD_PATIENTS";

export function addPatients(patients) {
  return {
    type: ADD_PATIENTS,
    patients
  }
}

const initialState = {
  currentPatient: null,
  patients: []
};

function patientsApp(state = initialState, action) {
  switch (action.type) {
    case ADD_PATIENTS:
      return Object.assign({}, state, {patients: action.patients});
    default:
      return state
  }
}

const store = createStore(patientsApp);
export default store;