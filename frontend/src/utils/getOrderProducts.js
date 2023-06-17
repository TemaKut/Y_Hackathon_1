import axios from 'axios';

const URL = `${process.env.REACT_APP_API_URL}/orders/`;
// const orderkey = '46c39f23ec7f3e6ba6776d01c7edb4b9';

const getOrderProducts = async (query) => {
  // const response = await axios({
  //   method: 'GET',
  //   url: URL + query,
  //   crossDomain: true,
  // });

  // const { results } = response.data;
  // return results;
  try {
    const response = await axios({
      method: 'GET',
      url: URL + query,
      crossDomain: true,
    });
    const { data } = response;
    return data;
  } catch (err) {
    throw new Error(`Error: ${err.reponse.status}`);
  }
};

export default getOrderProducts;
