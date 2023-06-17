import axios from 'axios';

const URL = `${process.env.REACT_APP_API_URL}/orders/cell-to-work`;

const getOrderCell = async () => {
  try {
    const response = await axios({
      method: 'GET',
      url: URL,
      crossDomain: true,
    });
    const { data } = response;
    return data;
  } catch (err) {
    throw new Error(`Error: ${err.reponse.status}`);
  }
};

export default getOrderCell;
