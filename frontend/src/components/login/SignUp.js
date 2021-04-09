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
    username: '',
    email: '',

    password: '',
    confirm: '',

    modal: false
  }

  onToggle = () => {
    this.setState({ modal: !this.state.modal});
  };

  onChange = (e) => {
    this.setState({ [e.target.name]: e.target.value });
  }

  onSubmit = (e) => {
    e.preventDefault();
    const { username, email, password, confirm } = this.state;

    if (password !== confirm) {
      // this.props.createMessage({ passwordNotMatch: 'Passwords do not match' });
    } else {
      const user = {
        username,
        password,
        email,
      };

      // this.props.register(user);
    }

    this.onToggle();
  }

  render() {
    const { username, email, password, confirm } = this.state;

    return (
      <div>
        <Button color="secondary" onClick={this.onToggle}>Sign Up</Button>
        <Modal isOpen={this.state.modal} toggle={this.onToggle} className="signUp">
          <ModalHeader toggle={this.onToggle}>Sign Up</ModalHeader>
          <ModalBody>
            <Form>
            <FormGroup className="form-group">
              <Label for="username">Username</Label>
              <Input
                autocomplete="off"
                placeholder="Enter Username"

                type="username"
                className="form-control"
                name="username"

                onChange={this.onChange}
                value={username}
              />
            </FormGroup>
            <FormGroup className="form-group">
              <Label for="email">Email</Label>
              <Input
                autocomplete="off"
                placeholder="Enter Email"

                type="email"
                className="form-control"
                name="email"

                onChange={this.onChange}
                value={email}
              />
            </FormGroup>
            <FormGroup className="form-group">
              <Label for="password">Password</Label>
              <Input
                autocomplete="off"
                placeholder="Enter Password"

                type="password"
                className="form-control"
                name="password"

                onChange={this.onChange}
                value={password}
              />
            </FormGroup>
            <FormGroup className="form-group">
              <Input
                autocomplete="off"
                placeholder="Confirm Password"

                type="password"
                className="form-control"
                name="confirm"

                onChange={this.onChange}
                value={confirm}
              />
            </FormGroup>
          </Form>
          </ModalBody>
          <ModalFooter>
            <Button color="primary" onClick={this.onSubmit}>Submit</Button>
            <Button color="secondary" onClick={this.onToggle}>Cancel</Button>
          </ModalFooter>
        </Modal>
      </div>
    );
  }
}

export default SignUp