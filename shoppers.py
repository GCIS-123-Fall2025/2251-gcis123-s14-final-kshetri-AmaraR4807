"""
Course: GCIS 123 (2251)
Exam: Final Exam
Question: Question #1 (25 points)
Filename: shoppers.py

An item has an item code (e.g. "ABCD-1234"), a name (e.g. "Silky Camisole"), 
and a price (e.g. $24). 
A partially completed item class has been provided to you below. You must 
complete the class by making the following enhancements:
- Write accessors for all fields.
- Two items are considered equal if they have the same item code.
- Items should be capable of being used with hashing data structures.
- The string representation of an item is its its code, name, and price
  seperated by commmas in a parenthesis, e.g. "(ABCD-1234, Silky Camisole, 24)"
- Items can be sorted based on the item code.
Write down the manual test by creating at least two items.
"""

class Item:
  __slots__ = ['__code', '__name', '__price']
  def __init__(self, code, name, price):
    self.__code = code
    self.__name = name
    self.__price = price

    def get_code(self):
      return self.__code
    def get_name(self):
      return self.__name
    def get_price(self):
      return self.__price
    
    def set_code(self, code):
      self.__code = code
    def set_name(self, name):
      self.__name = name
    def set_price(self, price):
      self.__price = price
    
    def print_item(self):
      print(self.__code, "\t", self.__name, "\t", self.__price, sep="")
    def __repr__(self):
      return "item(code=" + self.__code + "name=" + self.__name + "price=" + str(self.__price) + ")"
    def __str__(self):
      return self.__name + " [" + self.__code + "] - $" + str(self.__price)
    
# manual test from main() method
def main():
  item1 = "ABCD-1234", "Pencil", "1.10"
  item2 = "CDEF-4567", "Binder", "3.55"
  item1.print_item()
  item2.print_item()
  print(item1) # output from __str__
  print(repr(item2)) # uses repr

if __name__ == "__main__":    main()