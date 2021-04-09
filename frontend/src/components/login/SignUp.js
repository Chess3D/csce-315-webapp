import React, { useState } from 'react';
import {
  Button,
  Modal,
  ModalHeader,
  ModalBody,
  ModalFooter,
  Form,
  FormGroup,
  Label,
  Input,
} from 'reactstrap';

const SignUp = (props) => {
  const {
    buttonLabel,
    className
  } = props;

  const [modal, setModal] = useState(false);

  const toggle = () => setModal(!modal);

  return (
    <div>
      <Button color="secondary" onClick={toggle}>Sign Up</Button>
      <Modal isOpen={modal} toggle={toggle} className={className}>
        <ModalHeader toggle={toggle}>Sign Up</ModalHeader>
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
          <Button color="primary" onClick={toggle}>Submit</Button>{' '}
          <Button color="secondary" onClick={toggle}>Cancel</Button>
        </ModalFooter>
      </Modal>
    </div>
  );
}

export default SignUp;