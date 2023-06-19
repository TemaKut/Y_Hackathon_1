import React, { useState, useEffect } from 'react';
import { Routes, Route, useNavigate, useLocation } from 'react-router-dom';

import Style from './App.module.scss';
import getOrderCell from './utils/getOrderCell';
import getOrderProducts from './utils/getOrderProducts';
import Header from './components/Header/Header';
import Main from './components/Main/Main';
import Popup from './components/Popup/Popup';
import Footer from './components/Footer/Footer';
import Products from './components/Products/Products';
import Package from './components/Package/Package';
import Final from './components/Final/Final';

function App() {
  const navigate = useNavigate();
  const location = useLocation();
  const [loading, setLoading] = useState(false);
  // eslint-disable-next-line no-unused-vars
  const [error, setError] = useState(false);
  const [isKeyboardOpen, setIsKeyboardOpen] = useState(false);
  const [isPopupOpen, setIsPopupOpen] = useState(false);
  const [orderData, setOrderData] = useState({
    cell: '',
    orderkey: '',
    suggestedPackage: '',
    chosenPackage: '',
  });
  const [productsCell, setProductsCell] = useState([]);

  const isStart = ['/'].includes(location.pathname);
  const isFinal = ['/final'].includes(location.pathname);
  const isPackage = ['/package'].includes(location.pathname);
  const isProducts = ['/product'].includes(location.pathname);

  const getOrderData = () => {
    getOrderCell()
      .then(setLoading(true))
      .then((response) => {
        setOrderData(response);
        localStorage.setItem('orderData', JSON.stringify(response));
      })
      .catch((err) => setError(err))
      .finally(() => setLoading(false));
  };

  const getProducts = () => {
    getOrderProducts(orderData.orderkey)
      .then(setLoading(true))
      .then((response) => {
        setProductsCell(response);
      })
      .catch((err) => setError(err))
      .finally(() => setLoading(false));
  };

  useEffect(() => {
    const storedOrderData = localStorage.getItem('orderData');

    if (storedOrderData) {
      setOrderData(JSON.parse(storedOrderData));
    } else {
      getOrderData();
    }
  }, []);

  useEffect(() => {
    if (orderData) {
      getProducts();
    }
  }, [orderData]);

  useEffect(() => {
    if (loading) {
      setIsPopupOpen(true);
      setTimeout(setIsPopupOpen, 2000, false);
    } else setIsPopupOpen(false);
  }, [loading]);

  const keyboardClick = () => {
    if (['/'].includes(location.pathname)) {
      setIsKeyboardOpen((prev) => !prev);
    } else if (['/products'].includes(location.pathname)) {
      setIsKeyboardOpen((prev) => !prev);
    } else if (['/package'].includes(location.pathname)) {
      setIsKeyboardOpen((prev) => !prev);
    }
  };

  const footerButtonClick = () => {
    if (isStart) {
      setIsPopupOpen(true);
      setTimeout(setIsPopupOpen, 2000, false);
    } else {
      navigate(-1);
    }
  };

  // left the console.log for the convenience of testing
  // eslint-disable-next-line no-console
  console.log('orderData.orderkey', orderData.orderkey);

  return (
    <div className={Style.app}>
      <Header />
      <main className={Style.content}>
        <Routes>
          <Route
            exact
            path="/"
            element={
              <Main
                isStart={isStart}
                cellName={orderData.cell}
                handleClickBtn={getOrderData}
                isKeyboardOpen={isKeyboardOpen}
                setIsKeyboardOpen={setIsKeyboardOpen}
                orderKey={orderData.orderkey}
                setIsPopupOpen={setIsPopupOpen}
              />
            }
          />
          <Route
            exact
            path="/products"
            element={
              <Products
                productsCell={productsCell}
                cellName={orderData.cell}
                isKeyboardOpen={isKeyboardOpen}
                setIsKeyboardOpen={setIsKeyboardOpen}
                setIsPopupOpen={setIsPopupOpen}
              />
            }
          />
          <Route
            exact
            path="/package"
            element={
              <Package
                orderKey={orderData.orderkey}
                setSuggestedPackage={(suggestedPackage) => {
                  setOrderData((prevOrderData) => ({
                    ...prevOrderData,
                    suggestedPackage,
                  }));
                }}
                setError={setError}
                setLoading={setLoading}
                isKeyboardOpen={isKeyboardOpen}
                setIsKeyboardOpen={setIsKeyboardOpen}
                setChosenPackage={(chosenPackage) => {
                  setOrderData((prevOrderData) => ({
                    ...prevOrderData,
                    chosenPackage,
                  }));
                }}
              />
            }
          />
          <Route exact path="/final" element={<Final />} />
        </Routes>
      </main>
      <Popup
        isStart={isStart}
        isPackage={isPackage}
        isProducts={isProducts}
        isPopupOpen={isPopupOpen}
        isKeyboardOpen={isKeyboardOpen}
        loading={loading}
      />
      <Footer
        goBack={footerButtonClick}
        keyboardClick={keyboardClick}
        isFinal={isFinal}
        isStart={isStart}
      />
    </div>
  );
}

export default App;
