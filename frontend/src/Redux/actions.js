import Types from "./types";
import axios from "axios";


/* (R. Friel - April 09, 2021) - Will return the current police complaints stored in the database. */
export const getPoliceComplaints = () => {
    return dispatch => {
        dispatch({type:Types.GET_COMPLAINTS, payload:true})
        axios.get(`${process.env.REACT_APP_HOST_IP_ADDRESS}/api/police-complaints`)
            .then(response => {
                    dispatch({type:Types.GET_COMPLAINTS, payload:response.data})
                }
            )
            .catch(err => {
                    console.log(err)
                    dispatch({type:Types.GET_COMPLAINTS, payload:false})
            }
            );
    }
}


/* (R. Friel - April 09, 2021) - This will prompt the backend to refresh the database with new official data. */
export const updatePoliceComplaintsDatabase = () => {
    return dispatch => {
        dispatch({type:Types.UPDATE_DATABASE, payload:true})
        axios.get(`${process.env.REACT_APP_HOST_IP_ADDRESS}/api/police-complaints-update`)
            .then(response => {
                    dispatch({type:Types.UPDATE_DATABASE, payload:response.data})
                }
            )
            .catch(err => {
                    console.log(err)
                    dispatch({type:Types.UPDATE_DATABASE, payload:false})
            }
            );
    }
}