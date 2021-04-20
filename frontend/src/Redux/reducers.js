import Types from "./types";
const initialState = {
    policeComplaints: [],
    loading:false
};

const policeComplaintReducer = (state = initialState, action) => {
    switch (action.type) {
        case Types.GET_COMPLAINTS: {
            return {...state,policeComplaints: action.payload};
        }

        case Types.UPDATE_DATABASE: {
            return {...state,policeComplaints: action.payload};
        }

        default:
            return state;
    }
}

export default policeComplaintReducer;
