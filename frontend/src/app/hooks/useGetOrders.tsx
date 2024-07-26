import { useEffect, useState } from 'react';
import { Order } from './types';

const DOMAIN = process.env.NEXT_PUBLIC_BACKEND_BEER_STATUS_DOMAIN || ''

const useGetOrders = () => {
  const [orders, setOrders] = useState<Order | null>(null);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | unknown>(null);

  useEffect(() => {
    const fetchOrders = async () => {
      try {
        const response = await fetch(DOMAIN , {
            method:'get',
            headers:{
                "Content-Type": "application/json"
            }
        })
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        const data = await response.json();
        setOrders(data);
      } catch (error) {
        setError(error);
      } finally {
        setLoading(false);
      }
    };

    fetchOrders();
  }, []);

  return { orders, loading, error };
};

export default useGetOrders;
