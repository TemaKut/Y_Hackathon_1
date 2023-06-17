import axios from 'axios';

const URL = `${process.env.REACT_APP_API_URL}/orders/`;

const getOrderProducts = async (query) => {
  const response = await axios({
    method: 'GET',
    url: URL + query,
    crossDomain: true,
  });

  const { results } = response.data;
  return results;
};

export default getOrderProducts;
