# Aptitude and Programming Answers

## Question 1
Correct Answer: C
Explanation:
`my_list` is initialized to `[1, 2, 3]`. Inside `modify_list`, the statement `lst = lst + [4]` creates a brand new list in memory (`[1, 2, 3, 4]`) and reassigns the local variable `lst` to it. The subsequent modification `lst[0] = 99` only changes this new local list. The outer original list `my_list` remains unaffected and remains `[1, 2, 3]`.
Difficulty: Medium
Concept: Python List Mutability & Scoping

## Question 2
Correct Answer: A
Explanation:
In-order traversal visits nodes in the order: Left Subtree, Root, Right Subtree. In a Binary Search Tree (BST), this always visits the keys in sorted, ascending order.
Difficulty: Medium
Concept: BST Traversal

## Question 3
Correct Answer: B
Explanation:
Aggregate functions like `AVG()` cannot be used in a `WHERE` clause. To filter group results based on aggregates, the `HAVING` clause must be used. It must follow the `GROUP BY` clause.
Difficulty: Medium
Concept: SQL Grouping and Aggregation

## Question 4
Correct Answer: C
Explanation:
Polymorphism is the OOP principle that allows different classes to implement the same method interface in their own unique ways.
Difficulty: Easy
Concept: OOP Concepts

## Question 5
Correct Answer: D
Explanation:
`b` is a reference (alias) to `a`. `c` is a pointer pointing to `b` (and hence to `a`). Accessing `*c` and modifying it to 20 directly updates `a` to 20. Since `b` is an alias of `a`, `b` is also 20.
Difficulty: Hard
Concept: C++ Pointers and References

## Question 6
Correct Answer: C
Explanation:
`n % 2` gets the least significant bit of `n`, and `n // 2` shifts the binary representation to the right by dividing by 2. Thus, the recursive function counts and returns the number of set bits (1s) in the binary representation of `n` (Hamming weight).
Difficulty: Medium
Concept: Recursion and Binary Logic

## Question 7
Correct Answer: B
Explanation:
In a balanced Binary Search Tree (such as AVL or Red-Black Tree), the height is maintained at $O(\log N)$. Traversal from root to leaf takes time proportional to height, which is $O(\log N)$.
Difficulty: Medium
Concept: Time Complexity of Balanced Trees

## Question 8
Correct Answer: C
Explanation:
Objects in Java become eligible for garbage collection when there are no active threads that can reach them. `System.gc()` is only a hint/suggestion to the JVM, not a guarantee.
Difficulty: Easy
Concept: Java Garbage Collection Principles

## Question 9
Correct Answer: B
Explanation:
A Stack is a Last-In, First-Out (LIFO) linear data structure. A Queue is a First-In, First-Out (FIFO) structure.
Difficulty: Easy
Concept: Linear Data Structures

## Question 10
Correct Answer: B
Explanation:
The Singleton pattern restricts a class to a single instance and provides a global access point to that instance.
Difficulty: Medium
Concept: Software Design Patterns

## Question 11
Correct Answer: A
Explanation:
The average speed is given by the harmonic mean:
$\text{Average Speed} = \frac{2 \cdot v_1 \cdot v_2}{v_1 + v_2} = \frac{2 \cdot 40 \cdot 60}{100} = 48\text{ km/h}$.
Difficulty: Medium
Concept: Time, Speed, and Distance

## Question 12
Correct Answer: C
Explanation:
Let CP = 100. Markup is 40%, so MP = 140. Discount is 20%, so SP = $140 \times 0.80 = 112$. Profit = 12%.
Difficulty: Medium
Concept: Profit and Loss

## Question 13
Correct Answer: A
Explanation:
Total marbles = 12. Ways to draw two = $12 \times 11 = 132$.
Favorable ways:
- Both Red: $5 \times 4 = 20$
- Both Blue: $4 \times 3 = 12$
- Both Green: $3 \times 2 = 6$
Total favorable ways = $20 + 12 + 6 = 38$.
$\text{Probability} = \frac{38}{132} = \frac{19}{66}$.
Difficulty: Medium
Concept: Probability

## Question 14
Correct Answer: B
Explanation:
Total work = LCM(12, 18) = 36 units. Efficiency of A = 3 units/day. Efficiency of B = 2 units/day.
In 4 days together, they complete $4 \times 5 = 20$ units.
Remaining work = $36 - 20 = 16$ units.
B takes $16 / 2 = 8$ days to complete the remaining work alone.
Difficulty: Medium
Concept: Time and Work

## Question 15
Correct Answer: C
Explanation:
Let $x$ be the volume of the 30% solution.
$0.3x + 0.6 \times 10 = 0.4(x + 10)$
$0.3x + 6 = 0.4x + 4$
$0.1x = 2 \implies x = 20\text{ liters}$.
Difficulty: Medium
Concept: Mixtures and Alligations
