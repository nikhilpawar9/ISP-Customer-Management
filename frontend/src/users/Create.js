import React, { useState } from "react";
import {
  FormGroup,
  FormControl,
  InputLabel,
  Input,
  Button,
  makeStyles,
  Typography,
} from "@material-ui/core";
import addCustomer from "../components/APIcalls";
import { useNavigate } from "react-router-dom";

import Axios from "axios";
import { addUserDetails } from "../components/APIcalls";

const Create = () => {
  const navigate = useNavigate();

  const [customers, setCustomers] = useState({
    name: "",
    email: "",
    primary_mobile: "",
  });

  const { name, email, primary_mobile } = customers;

  const onValueChange = (e) => {
    console.log(e.target.value);

    setCustomers({ ...customers, [e.target.name]: e.target.value });
    console.log(customers)
  };
  const addCust = async() =>{
    return await Axios.post(`http://127.0.0.1:8000/customers/`, customers) 
  }

  return (
    <FormGroup className="container">
      <Typography variant="h4">Add User</Typography>
      <FormControl>
        <InputLabel htmlFor="my-input">Name</InputLabel>
        <Input
          onChange={(e) => onValueChange(e)}
          name="name"
          value={name}
          id="my-input"
        />
      </FormControl>
      <FormControl>
        <InputLabel htmlFor="my-input">Email</InputLabel>
        <Input
          onChange={(e) => onValueChange(e)}
          name="email"
          value={email}
          id="my-input"
        />
      </FormControl>
      <FormControl>
        <InputLabel htmlFor="my-input">Phone</InputLabel>
        <Input
          onChange={(e) => onValueChange(e)}
          name="primary_mobile"
          value={primary_mobile}
          id="my-input"
        />
      </FormControl>
      <FormControl>
        <Button
          variant="contained"
          color="primary"
          onClick={() => addCust()}
        >
          Add User
        </Button>
      </FormControl>
    </FormGroup>
  );
};

export default Create;
