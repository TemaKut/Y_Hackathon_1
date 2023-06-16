/* eslint-disable react/jsx-no-bind */
import React, { useState } from 'react';
import { Routes, Route, useNavigate, useLocation } from 'react-router-dom';

import Style from './App.module.scss';

import Header from './components/Header/Header';
import Main from './components/Main/Main';
import Keyboard from './components/Keyboard/Keyboard';
import Footer from './components/Footer/Footer';

import Products from './components/Products/Products';
import Package from './components/Package/Package';
import Final from './components/Final/Final';

import LeftSide from './components/LeftSide/LeftSide';
// import RightSide from './components/RightSide/RightSide';

function App() {
  const navigate = useNavigate();
  const location = useLocation();
  const [isKeyboardOpen, setIsKeyboardOpen] = useState(false);
  const [keyboardTitleText, setKeyboardTitleText] = useState('');
  // const [showRightSide, setShowRightSide] = useState(false);
  const showLefSide = ['/products', '/package'].includes(location.pathname);

  const isStart = ['/'].includes(location.pathname);
  const isFinal = ['/final'].includes(location.pathname);
  const isPackage = ['/package'].includes(location.pathname);
  // const isProducts = ['/products'].includes(location.pathname);

  // useEffect(() => {
  //   if (isStart || isFinal) {
  //     setShowRightSide(true);
  //   }
  //   if (isProducts) {
  //     setShowRightSide(true);
  //   }
  //   if (isPackage) {
  //     setShowRightSide(false);
  //   }
  // }, [isStart, isProducts, isFinal, isPackage]);

  function keyboardClick() {
    if (['/'].includes(location.pathname)) {
      setKeyboardTitleText('Введите код ячейки');
      setIsKeyboardOpen(true);
    } else if (['/products'].includes(location.pathname)) {
      navigate('/package');
    } else if (['/package'].includes(location.pathname)) {
      navigate('/final');
    }
  }

  function goBack() {
    navigate(-1);
  }

  function rightSideClick() {
    if (['/'].includes(location.pathname)) {
      setIsKeyboardOpen(true);
    } else if (['/products'].includes(location.pathname)) {
      navigate('/package');
    } else if (['/final'].includes(location.pathname)) {
      navigate('/');
    }
  }

  return (
    <div className={Style.app}>
      <Header />
      <main className={Style.content}>
        {showLefSide && <LeftSide isPackage={isPackage} />}
        <Routes>
          <Route exact path="/" element={<Main isStart={isStart} />} />
          <Route exact path="/products" element={<Products />} />
          <Route exact path="/package" element={<Package />} />
          <Route exact path="/final" element={<Final />} />
        </Routes>
        {/* {showRightSide && (
          <RightSide
            rightSideClick={rightSideClick}
            isFinal={isFinal}
            isStart={isStart}
            isProducts={isProducts}
            isKeyboardOpen={isKeyboardOpen}
          />
        )} */}
      </main>
      <Keyboard isKeyboardOpen={isKeyboardOpen} titleText={keyboardTitleText} />
      <Footer
        goBack={goBack}
        keyboardClick={keyboardClick}
        isFinal={isFinal}
        isStart={isStart}
      />
    </div>
  );
}

export default App;
