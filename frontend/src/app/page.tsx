'use client';
import { ReactElement } from 'react'
import useGetOrders from './hooks/useGetOrders'

const Page = (): ReactElement => {
  const { orders, loading, error } = useGetOrders();

  interface StatusMessageProps {
    message: string
  }
  
  const StatusMessage = ({ message }: StatusMessageProps): ReactElement => {
    return (
      <div className="flex justify-center items-center min-h-screen">
        <div>{message}</div>
      </div>
    )
  }

  if (loading) {
    return <StatusMessage message="Loading..." />
  }

  if (error) {
    return <StatusMessage message={`Error: ${error.message}`} />
  }

  if (!orders) {
    return <StatusMessage message="No orders available" />
  }


  return (
    <>
    <div className="flex justify-center items-center min-h-screen bg-gray-100">
      <div className="p-6 bg-white rounded-lg shadow-md w-full max-w-2xl">
        <h1 className="text-3xl font-bold mb-4 text-center">Status / Detalle de la orden</h1>
        <div className="border-b border-gray-200 mb-4 pb-4">
          <p><strong>Created:</strong> {new Date(orders.created).toLocaleString()}</p>
          <p><strong>Paid:</strong> {orders.paid ? 'Yes' : 'No'}</p>
          <p><strong>Subtotal:</strong> ${orders.subtotal.toFixed(2)}</p>
          <p><strong>Taxes:</strong> ${orders.taxes.toFixed(2)}</p>
          <p><strong>Discounts:</strong> ${orders.discounts.toFixed(2)}</p>
        </div>
        <h2 className="text-2xl font-bold mt-4">Rounds</h2>
        {orders.rounds.map((round, index) => (
          <div key={index} className="mt-4">
            <h3 className="font-bold">Round {index + 1}</h3>
            <p><strong>Created:</strong> {new Date(round.created).toLocaleString()}</p>
            <ul className="list-disc list-inside">
              {round.items.map((item, idx) => (
                <li key={idx}>
                  {item.quantity} x {item.name}
                </li>
              ))}
            </ul>
          </div>
        ))}
      </div>
    </div>
    </>
  );
};

export default Page;
