import React, { Component } from "react";
import Table from  "../Components/table";
import { getPoliceComplaints, updatePoliceComplaintsDatabase } from '../Redux/actions.js'



class PoliceComplaintsList extends Component {

    constructor(props) {
        super(props);
        this.state = {
            policeComplaints: 0
        }
    }


    componentDidMount() {
        getPoliceComplaints();
    }


    render() {

        const complaints = this.props
        console.log(complaints)


        return (
            <div>
                <ul>This works!</ul>
                <Table />
            </div>
        );
    }


}

export default PoliceComplaintsList
