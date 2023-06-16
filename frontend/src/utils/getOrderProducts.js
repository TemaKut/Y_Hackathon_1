import axios from 'axios';

// const URL = `${process.env.REACT_APP_API_URL}/orders/`;

// const getOrderProducts = async (query) => {
//   const reponse = await axios({
//     method: 'GET',
//     url: URL + query,
//     crossDomain: true,
//   });

//   const { results } = reponse.data;
//   return results;
// };

// export default getOrderProducts;

const getOrderProducts = async () => {
  const reponse = await axios.get(
    `http://localhost:8000/api/v1/orders/1913aa8f0023c18ba8724a234bbc987f`
  );

  // const { results } = reponse.data;
  return reponse;
};

export default getOrderProducts;

// 1913aa8f0023c18ba8724a234bbc987f
