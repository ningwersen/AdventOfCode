import math
from collections import deque

class Monkey1():
   def __init__(self, items: deque[int], operation: str, test: int, true: int, false: int):
      self.items = items
      self.operation = operation
      self.test = test
      self.true = true
      self.false = false
      self.inspections = 0
   
   def inspect_items(self) -> list[tuple]:
      transfers = []

      while len(self.items) > 0:
         item = self.items.popleft()
         new_item = eval(self.operation.replace('old', 'item'))
         item = math.floor(new_item / 3)

         transfer = (self.true, item) if item % self.test == 0 else (self.false, item)
         transfers.append(transfer)

         self.inspections += 1
      
      return transfers
   
class Monkey2():
    def __init__(self, items: deque[int], operation: str, test: int, true: int, false: int):
      self.items = items
      self.operation = operation
      self.test = test
      self.true = true
      self.false = false
      self.inspections = 0
      # Set this after all Monkeys are initialized
      self.lcm = None

    def inspect_items(self) -> list[tuple]:
        transfers = []

        while len(self.items) > 0:
            item = self.items.popleft()
            # Reduce number by taking modulus of least common multiple of all monkey tests
            item %= self.lcm
            new_item = eval(self.operation.replace('old', 'item'))
            item = new_item

            transfer = (self.true, item) if item % self.test == 0 else (self.false, item)
            transfers.append(transfer)

            self.inspections += 1

        return transfers
