import React, {useState} from 'react';

// import axios from "axios";

// import { API_URL } from "../constants";

import {
  Button,
  Form,
  FormGroup,
  Label,
  Input,
  Col,
  Row
} from 'reactstrap';

import SignUp from './SignUp';

const Login = (props) => {
  // state = {
  //   email: "",
  //   password: ""
  // }
  var offset = 3

  return (
      <Form className={`m-${offset}`}>
        <FormGroup>
          <Label for="loginEmail">Email</Label>
          <Input type="email" name="email" id="loginEmail" autocomplete="off" placeholder="Please Enter Email"/>
        </FormGroup>
        <FormGroup>
          <Label for="loginEmail">Password</Label>
          <Input type="password" name="password" id="loginEmail" autocomplete="off" placeholder="Please Enter Password"/>
        </FormGroup>
        <Row>
          <Button color="primary" type="submit" className={`mx-${offset}`}>Login</Button>
          <SignUp />
        </Row>
        
      </Form>
  );
}

export default Login;
