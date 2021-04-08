import React from 'react';
import ReactDOM from 'react-dom';
import 'bootstrap/dist/css/bootstrap.css';
import './index.css';

import TopNavbar from './components/TopNavbar';


ReactDOM.render(
  <React.StrictMode>
    <TopNavbar />
  </React.StrictMode>,
  document.getElementById('root')
);