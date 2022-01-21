import * as React from 'react';
import { Link } from "react-router-dom";
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';
import { Button } from '@mui/material';


const Tables = ({ customers, searchCustomer, Sorting,deleteCust }) => {


  return (
    <TableContainer component={Paper} className='container' >
      <Table sx={{ minWidth: 650 }} aria-label="simple table">
        <TableHead style={{cursor:"pointer"}} >
          <TableRow>
            <TableCell onClick={() => Sorting("id")}><h4>Sr No</h4></TableCell>
            <TableCell align="center" onClick={() => Sorting("name")}><h4>Name</h4></TableCell>
            <TableCell align="center" onClick={() => Sorting("email")}><h4>Email</h4></TableCell>
            <TableCell align="center" onClick={() => Sorting("primary_mobile")}><h4>Mobile</h4></TableCell>
            <TableCell align="center"  ><h4>Delete</h4></TableCell>
            <TableCell align="center" ><h4>Update</h4></TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
        {customers
            .filter((val) => {
              if (searchCustomer == "") {
                return val;
              } else if (
                val.name
                  .toLowerCase()
                  .includes(searchCustomer.toLowerCase())
              ) {
                return val;
              }
            })
            .map((val, key) =>{
                return(
            <TableRow
              key={key}
              sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
            >
              <TableCell component="tr" scope="row">
                {val.id}
              </TableCell>
              <TableCell align="center">
              <Link to={`/customers/${val.id}`} target='_blank' className="page-link">
                      {val.name}
                    </Link>
              </TableCell>
              <TableCell align="center">{val.email}</TableCell>
              <TableCell align="center">{val.primary_mobile}</TableCell>
              <TableCell align="center" ><Button onClick={() => {deleteCust(val.id)}} >Delete</Button></TableCell>
              <TableCell align="center">
              <Link to={`/customers/update/${val.id}`}  className="page-link"  >
                      <Button>Update</Button>
                    </Link>
              </TableCell>
              
              
            </TableRow>
            );
            })}
        </TableBody>
      </Table>
    </TableContainer>
  );
}

export default Tables;