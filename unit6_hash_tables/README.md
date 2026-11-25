# Unit 6 Discussion: Dictionaries as Hash Tables

## Overview

This assignment uses Python dictionaries to demonstrate hash table behavior.

## Learning Objectives

- Insert key-value pairs
- Retrieve values efficiently
- Update existing values
- Remove entries
- Understand hashing concepts

## Requirements

1. Create and populate a dictionary.
2. Demonstrate lookup operations.
3. Demonstrate update operations.
4. Demonstrate delete operations.
5. Test edge cases.
6. Create a real-world scenario.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain how hash tables behave, what collisions are, and how hash tables can improve efficiency.

## Reflection

According to GeeksforGeeks, HashMap uses hashing to make searching and adding/removing items faster. In this lab, 
I used a HashMap to store inventory items using key value pairs. The SKU is the key, and the quantity is the value. 
For example, I was recently asked to share a SKU number of a product I was interested in purchasing online while 
speaking with a representative. These work well as keys because each product has its own unique code, which makes it 
easier to find these items online for the representative. A collision, according to GeeksforGeeks, occurs when two 
different keys end up being assigned to the same location in a hash table. in my programming assignment, this would 
happen if two products with the different SKU numbers were assigned to the same location, even though each product has 
its own unique code. Python dictionaries handle this through open addressing. This is important as this could make the 
process of looking up products slow. For context, the average lookup time is O(1), but in the worst case it could be 
O(n). In my program, I accounted for situations where a SKU did not exist, while this program also showed the ability 
to add products, update inventory quantities, and more. 

## References

GeeksforGeeks. (2025, July 23). Collision resolution techniques. https://www.geeksforgeeks.org/dsa/collision-resolution-techniques/
GeeksforGeeks. (2026a, March 3). Hashing in data structure. https://www.geeksforgeeks.org/dsa/hashing-data-structure/