import React from 'react';
import Table from 'react-bootstrap/Table'
import HEADERS from '../Constants/constants'


/* (R. Friel - April 09, 2021) - Use https://react-bootstrap.github.io/components/table/ for official documentation on 
react-bootstrap table components. */
// <Table responsive striped bordered hover variant="dark">
//        {props.complaints.length}


const tableComponent = (props) => (

    <Table striped bordered hover responsive="xl" variant="dark">

        <thead>
            <tr>
                {HEADERS.map(header => {
                    return <th>{header}</th>
                })}
            </tr>
        </thead>



        {props.complaints.keys()}

        {props.complaints.length}


        {/* {props.complaints.map(complaint => {
            return <li>{complaint.first_name}</li>
        })} */}



    </Table>


)

export default tableComponent
