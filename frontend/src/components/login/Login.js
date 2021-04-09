import React from 'react'

import {
  Form,
  FormGroup,
  Label,
  Input,
  Row,
  Button,
} from 'reactstrap';

import SignUp from './SignUp'

class Login extends React.Component {
    render() {
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
}

export default Login