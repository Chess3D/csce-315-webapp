import React, {useState} from 'react';

// import axios from "axios";

// import { API_URL } from "../constants";

import {
  Button,
  Form,
  FormGroup,
  Label,
  Input
} from 'reactstrap';

const Login = (props) => {
  // state = {
  //   email: "",
  //   password: ""
  // }

  return (
      <Form className='m-3'>
        <FormGroup>
          <Label for="loginEmail">Email</Label>
          <Input type="email" name="email" id="loginEmail" autocomplete="off" placeholder="Please Enter Email"/>
        </FormGroup>
        <FormGroup>
          <Label for="loginEmail">Password</Label>
          <Input type="password" name="password" id="loginEmail" autocomplete="off" placeholder="Please Enter Password"/>
        </FormGroup>
        <Button color="primary" type="submit">Login</Button>
      </Form>
  );
}

export default Login;
