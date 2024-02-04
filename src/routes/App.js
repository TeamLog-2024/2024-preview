import React from 'react';
import '../styles/App.css';
import { HashRouter, Route, Routes } from 'react-router-dom';
import Home from './home';
import Login from './login'
import Signup from './signup'

function App() {
  return (
    <HashRouter>
      <Routes>
      <Route path="/" exact={true} element={<Home/>} />
      <Route path="/login" element={<Login/>} />
      <Route path="/signup" element={<Signup/>} />
      </Routes>
    </HashRouter>
  );
}

export default App;
