#!/usr/bin/env python3
 
class CashRegister:
    def __init__(self, discount=0):
        self.items = []
        self.discount = discount
        self.last_transaction = 0
        self.total = 0

    def add_item(self, title, price, quantity=1):
        for _ in range(quantity):
            self.items.append((title, price))
            self.total += price 
        self.last_transaction = price

    def apply_discount(self):
        if self.discount > 0:
            self.total = self.total * (100 - self.discount) / 100
            return f"After the discount, the total comes to ${self.total:.2f}."
        else:
            return "There is no discount to apply."

    def void_last_transaction(self):
        if self.items:
            title, price = self.items.pop()
            self.total -= price
            self.last_transaction = price
  
