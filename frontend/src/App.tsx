import React, { useState, useEffect } from "react";
import {
  ChakraProvider,
  Box,
  Button,
  Heading,
  HStack,
  Modal,
  ModalOverlay,
  ModalContent,
  ModalHeader,
  ModalFooter,
  ModalBody,
  ModalCloseButton,
  VStack,
  Grid,
  theme,
  Text,
  useDisclosure,
  useToast,
} from "@chakra-ui/react";
import { ColorModeSwitcher } from "./ColorModeSwitcher";
import APIClient from "./APIClient";
import { Item, Customer } from "./types";

export const App = () => {
  const toast = useToast();
  const { isOpen, onOpen, onClose } = useDisclosure();
  const [customers, setCustomers] = useState<Customer[]>([]);
  const [items, setItems] = useState<Item[]>([]);

  useEffect(() => {
    const getInfo = async () => {
      let [customersResponse, itemsResponse] = await Promise.all([
        APIClient.getAllCustomers(),
        APIClient.getAllItems(),
      ]);
      console.log(customersResponse);
      console.log(itemsResponse);

      if (customersResponse && itemsResponse) {
        setCustomers(customersResponse);
        setItems(itemsResponse);
      } else {
        toast({
          description: `Unable to retrieve info.`,
          status: "error",
          duration: 3000,
          variant: "subtle",
        });
      }
    };
    getInfo();
  }, [toast]);

  return (
    <ChakraProvider theme={theme}>
      <Box textAlign="center" fontSize="xl">
        <Grid minH="100vh" p={3}>
          <ColorModeSwitcher justifySelf="flex-end" />

          <Modal isOpen={isOpen} onClose={onClose}>
            <ModalOverlay />
            <ModalContent>
              <ModalHeader>Todo</ModalHeader>
              <ModalCloseButton />
              <ModalBody></ModalBody>

              <ModalFooter>
                <Button colorScheme="blue" mr={3} onClick={onClose}>
                  Todo
                </Button>
                <Button variant="ghost">Todo</Button>
              </ModalFooter>
            </ModalContent>
          </Modal>
          <Heading>Customers</Heading>
          <VStack spacing={8}>
            {customers.map((customer) => (
              <Button p={10} onClick={onOpen}>
                <Heading>{`Customer ${customer.id}`}</Heading>
              </Button>
            ))}
          </VStack>
          <Heading>Menu</Heading>
          <VStack spacing={2}>
            {items.map((item) => (
              <HStack spacing={2}>
                <Heading>{item.name}</Heading>
                <Text>{item.cost}</Text>
              </HStack>
            ))}
          </VStack>
        </Grid>
      </Box>
    </ChakraProvider>
  );
};
