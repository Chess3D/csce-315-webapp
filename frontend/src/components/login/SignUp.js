import React from 'react'

import {
  Button,
  Modal,
  ModalHeader,
  ModalBody,
  Form,
  Label,
  Input,
  FormGroup,
  ModalFooter,
} from 'reactstrap';

class SignUp extends React.Component {
  state = {
    username: "",
    email: "",
    password: "",
    modal: false
  }

  toggle = (e) => {
    this.setState({ modal: !this.state.modal})
  };

  submit = (e) => {

  }

  render() {
    return (
      <div>
        <Button color="secondary" onClick={this.toggle}>Sign Up</Button>
        <Modal isOpen={this.state.modal} toggle={this.toggle} className="signUp">
          <ModalHeader toggle={this.toggle}>Sign Up</ModalHeader>
          <ModalBody>
            <Form>
            <FormGroup>
              <Label for="Username">Username</Label>
              <Input type="username" name="email" id="username" autocomplete="off" placeholder="Enter Username"/>
            </FormGroup>
            <FormGroup>
              <Label for="signUpEmail">Email</Label>
              <Input type="email" name="email" id="signUpEmail" autocomplete="off" placeholder="Enter Email"/>
            </FormGroup>
            <FormGroup>
              <Label for="signUpPassword">Password</Label>
              <Input type="password" name="password" id="signUpPassword" autocomplete="off" placeholder="Enter Password"/>
            </FormGroup>
            <FormGroup>
              <Input type="passwordConfirm" name="passwordConfirm" id="passwordConfirm" autocomplete="off" placeholder="Confirm Password"/>
            </FormGroup>
          </Form>
          </ModalBody>
          <ModalFooter>
            <Button color="primary" onClick={this.submit}>Submit</Button>{' '}
            <Button color="secondary" onClick={this.toggle}>Cancel</Button>
          </ModalFooter>
        </Modal>
      </div>
    );   
  }
}

export default SignUp