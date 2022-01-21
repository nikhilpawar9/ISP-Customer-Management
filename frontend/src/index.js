import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import { BrowserRouter as Router, Routes,  Route } from 'react-router-dom';
import Details from './components/Details';
import Dashboard from './components/Dashboard';
import Update from './users/Update'
import Create from './users/Create'







ReactDOM.render(
<Router>
<Routes>
<Route path="/" element={<Dashboard/>} />
<Route path="/customers" element={<App/>} />
<Route path="/customers/create/" element={<Create/>} />
<Route path="/customers/update/:id" element={<Update/>} />

<Route path="/customers/:id" element={<Details />} />
</Routes>
</Router>,
  document.getElementById('root')
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
