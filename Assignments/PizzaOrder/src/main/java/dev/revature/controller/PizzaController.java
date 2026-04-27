package dev.revature.controller;

import org.springframework.web.bind.annotation.*;

import java.util.ArrayList;
import java.util.List;

@RestController
@RequestMapping("/pizza")
public class PizzaController {

    List<String> PizzaOrders = new ArrayList<>();

    @GetMapping("/orders")
    public List<String> getAllOrders() {
        return PizzaOrders;
    }

    @PostMapping("/orders")
    public void addOrder(@RequestBody String order) {
        PizzaOrders.add(order);
        System.out.println("Added order: " + order);
    }

    @DeleteMapping("/orders/{index}")
    public void deleteOrder(@PathVariable int index) {
        PizzaOrders.remove(index);
        System.out.println("Deleted " + PizzaOrders.get(index) + " at index: " + index);
    }

    @PutMapping("/orders/{index}")
    public void updateOrder(@PathVariable int index, @RequestBody String order) {
        System.out.println("Updating " + PizzaOrders.get(index) + " to " + order + " at index: " + index);
        PizzaOrders.set(index, order);
    }

}
