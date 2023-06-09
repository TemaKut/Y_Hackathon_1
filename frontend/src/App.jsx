/* eslint-disable react/jsx-no-bind */
/* eslint-disable prettier/prettier */
import React from 'react';
import { Routes, Route, useNavigate, useLocation } from 'react-router-dom';

import Style from './App.module.scss';

import Header from './components/Header/Header';
import Main from './components/Main/Main';
import Footer from './components/Footer/Footer';

import Products from './components/Products/Products';
import Package from './components/Package/Package';
import Final from './components/Final/Final';

import LeftSide from './components/LeftSide/LeftSide';
import RightSide from './components/RightSide/RightSide';

function App() {
  const navigate = useNavigate();
  const location = useLocation();
  const showLefSide = ['/products', '/package'].includes(location.pathname);
  const showRightSide = ['/products', '/final', '/'].includes(
    location.pathname
  );

  const isStart = ['/'].includes(location.pathname);
  const isFinal = ['/final'].includes(location.pathname);

  function keyboardClick() {
    if (['/'].includes(location.pathname)) {
      navigate('/products');
    }
    else if (['/products'].includes(location.pathname)) {
      navigate('/package');
    }
    else if (['/package'].includes(location.pathname)) {
      navigate('/final');
    }
  }

  function goBack() {
    navigate(-1);
  }

  function rightSideClick() {
    navigate('/package');
    if (['/'].includes(location.pathname)) {
      navigate('/');
    }
    else if (['/products'].includes(location.pathname)) {
      navigate('/package');
    }
    else if (['/final'].includes(location.pathname)) {
      navigate('/');
    }
  }

  return (
    <div className="App">
      <Header />
      <main className={Style.content}>
        {showLefSide && <LeftSide />}
        <Routes>
          <Route exact path="/" element={<Main />} />
          <Route exact path="/products" element={<Products />} />
          <Route exact path="/package" element={<Package />} />
          <Route exact path="/final" element={<Final />} />
        </Routes>
        {showRightSide && <RightSide rightSideClick={rightSideClick} isFinal={isFinal} isStart={isStart} />}
      </main>
      <Footer goBack={goBack} keyboardClick={keyboardClick} isFinal={isFinal} isStart={isStart} />
    </div>
  );
}

export default App;
