import axios from "axios";
import { Item, Customer, Order, Bill } from "./types";

const baseAPIClient = axios.create({
  baseURL: "http://localhost:8000",
});

const getBill = async (customerId: number): Promise<Bill> => {
  try {
    const { data } = await baseAPIClient.get(`/bill/${customerId}/`);
    return data;
  } catch (error) {
    return error as Bill;
  }
};

const getAllCustomers = async (): Promise<Customer[]> => {
  try {
    const { data } = await baseAPIClient.get(`/customer/`);
    return data;
  } catch (error) {
    return error as Customer[];
  }
};

const getCustomerOrders = async (customerId: number): Promise<Order[]> => {
  try {
    const { data } = await baseAPIClient.get(`/orders/${customerId}/`);
    return data;
  } catch (error) {
    return error as Order[];
  }
};

const getAllItems = async (): Promise<Item[]> => {
  try {
    const { data } = await baseAPIClient.get(`/items/`);
    return data;
  } catch (error) {
    return error as Item[];
  }
};

export default {
  getBill,
  getAllCustomers,
  getCustomerOrders,
  getAllItems,
};
