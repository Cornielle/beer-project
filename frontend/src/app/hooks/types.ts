export interface Order {
    created: string;
    paid: boolean;
    subtotal: number;
    taxes: number;
    discounts: number;
    items: string[];
    rounds: {
      created: string;
      items: {
        name: string;
        quantity: number;
      }[];
    }[];
  }
