import React from 'react';
import Navbar from './components/Navbar';
import Mat from './components/Mat';
import './App.css';
import Home from './components/pages/Home';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Services from './components/pages/Services';
import Products from './components/pages/Products';
import SignUp from './components/pages/SignUp';


function sl_web() {
  return (
    <>
      <Router>
        <div>
        <Navbar />
        <Routes>
          <Route path='/' exact element={< Home />}/>
          <Route path='/services' element={< Services />} />
          <Route path='/products' element={< Products />} />
          <Route path='/sign-up' element={< SignUp />} />
        </Routes>
        </div>
      <Mat />
      </Router>
    </>
  );
}

export default sl_web;
