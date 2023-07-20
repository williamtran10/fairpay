export type Item = {
  id: number;
  name: string;
  cost: number;
};

export type Customer = {
  id: number;
  table_id: number;
  tip: number;
};

export type Order = {
  customer_id: number;
  item_id: number;
  amount: number;
};

export type Bill = {
  table_id: number;
  customer_id: number;
  cost: number;
};
