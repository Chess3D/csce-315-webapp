import React from 'react';
import ReactDOM from 'react-dom';
import 'bootstrap/dist/css/bootstrap.css';
import './index.css';

import TopNavbar from './components/TopNavbar';
import Login from './components/login/Login';
import SignUp from './components/login/SignUp';


ReactDOM.render(
  <React.StrictMode>
    <TopNavbar />
    <Login />
    {/* <SignUp /> */}
  </React.StrictMode>,
  document.getElementById('root')
);