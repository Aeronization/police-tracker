import React from 'react';
import Table from 'react-bootstrap/Table'
import HEADERS from '../Constants/constants'


/* (R. Friel - April 09, 2021) - Use https://react-bootstrap.github.io/components/table/ for official documentation on 
react-bootstrap table components. */

const tableComponent = (props) => (

    <Table striped bordered hover responsive="xl" variant="dark">

        <thead>
            <tr>
                {HEADERS.map(header => {
                    return <th>{header}</th>
                })}
            </tr>
        </thead>

        {/* {props.complaints.length} */}

        {/* (R. Friel - April 21, 2021) - Iterate over the json data that is returned. */}
        <tbody>
            {props.complaints.map( (complaint, index) => {
                let values = Object.values(complaint)
                return (
                    <tr>
                        {values.map( value => {
                            return(
                                <td>{value}</td>
                            )
                        })}
                    </tr>
                )
            })}
        </tbody>



    </Table>


)

export default tableComponent
