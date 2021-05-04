import src.data_structures.heap
from src.algorithms.misc import powerfulIntegers

class Solution:
   def balancedStringSplit(self, s: str) -> int:
      bal = 0
      stack = []
      for c in s:
         if c not in stack:
            stack.append(c)
         else:
            stack.pop()
            bal += 1
      return bal


if __name__ == "__main__":
   x = powerfulIntegers(2,3,10)
   print(x)
else:
   print("File one executed when imported")