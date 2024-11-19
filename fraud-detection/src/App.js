import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Navbar from './components/Navbar';
import Home from './components/Home';
import Overview from './components/Overview';
import MakeTransaction from './components/MakeTransaction';
import Footer from './components/Footer'

const App = () => {
  return (
    <Router>
      <Navbar />
      <Routes>
        <Route exact path="/" element={<Home />} />
        <Route path="/overview" element={<Overview />} />
        <Route path="/make-transaction" element={<MakeTransaction />} />
      </Routes>
      <Footer />
    </Router>
  );
};

export default App;
