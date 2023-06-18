import axios from 'axios';

const URL = `${process.env.REACT_APP_API_URL}/orders/`;

const getOrderPackage = async (query) => {
  try {
    const response = await axios({
      method: 'GET',
      url: `${URL + query}/predict`,
      crossDomain: true,
    });
    const { data } = response;
    return data;
  } catch (err) {
    throw new Error(`Error: ${err.reponse.status}`);
  }
};

export default getOrderPackage;
