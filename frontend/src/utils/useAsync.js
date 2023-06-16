import { useCallback, useEffect, useState } from 'react';

const useAsync = (callback, query) => {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(false);
  const [value, setValue] = useState([]);

  const callbackMemoized = useCallback(() => {
    setLoading(true);
    setError(false);
    setValue([]);
    Promise.resolve(callback(query))
      .then((response) => setValue(response))
      .catch((err) => setError(err))
      .finally(() => setLoading(false));
  }, [callback, query]);

  useEffect(() => {
    callbackMemoized();
  }, [callbackMemoized]);

  return { loading, error, value };
};

export default useAsync;
