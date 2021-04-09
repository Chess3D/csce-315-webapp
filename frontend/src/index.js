import React from 'react';
import ReactDOM from 'react-dom';
import 'bootstrap/dist/css/bootstrap.css';
import './index.css';

import TopNavbar from './components/TopNavbar';
import Login from './components/Login';


ReactDOM.render(
  <React.StrictMode>
    <TopNavbar />
    <Login />
  </React.StrictMode>,
  document.getElementById('root')
);