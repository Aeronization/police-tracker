import React, { Component } from "react";
import {connect} from 'react-redux'
import Table from  "../Components/table";
import { getPoliceComplaints, updatePoliceComplaintsDatabase } from '../Redux/actions.js'



class PoliceComplaintsList extends Component {

    constructor(props) {
        super(props);
        this.state = {
            policeComplaints: []
        }
    }


    componentDidMount() {
        this.props.getPoliceComplaints();
    }


    render() {

        return (
            <div>
                <Table complaints={Object.values(this.props.policeComplaints)}/>
            </div>
        );
    }


}

const mapStateToProps = (state) => ({
    policeComplaints: state.policeComplaints
})

const mapDispatchToProps = {
    getPoliceComplaints, updatePoliceComplaintsDatabase
}


export default connect(mapStateToProps, mapDispatchToProps)(PoliceComplaintsList)
