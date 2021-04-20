import React from 'react';
import PoliceList from './Containers/police_list'
import Navbar from './Components/navbar'
import { Provider as ReduxProvider } from "react-redux";
import configureStore from "./Redux/store";

/* (R. Friel - April 19, 2021) - All the bootstrap imports. */
import 'bootstrap/dist/css/bootstrap.min.css';


const reduxStore = configureStore(window.REDUX_INITIAL_DATA);


function App() {

    return (
      <ReduxProvider store={reduxStore}>
          <div className="App">
            <Navbar />
            <PoliceList />
          </div>
      </ReduxProvider>
  );
}

export default App;
