import Types from "./types";
const initialState = {
    posts: [],
    loading:false
};

const policeComplaintReducer = (state = initialState, action) => {
    switch (action.type) {
        case Types.GET_COMPLAINTS: {
            console.log("create_item");
            return {...state,loading: action.payload};
        }

        case Types.UPDATE_DATABASE: {
            return {...state,posts: action.payload};
        }

        default:
            return state;
    }
}

export default policeComplaintReducer;
