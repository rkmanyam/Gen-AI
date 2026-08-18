# Aptitude and Programming Questions

## Question 1
What is the output of the following Python code?
```python
def modify_list(lst):
    lst = lst + [4]
    lst[0] = 99

my_list = [1, 2, 3]
modify_list(my_list)
print(my_list)
```
A. `[1, 2, 3, 4]`
B. `[99, 2, 3]`
C. `[1, 2, 3]`
D. `[99, 2, 3, 4]`

## Question 2
An in-order traversal of a Binary Search Tree (BST) produces which of the following sequences?
A. Sorted in ascending order
B. Sorted in descending order
C. Level-by-level order
D. Root node followed by left and right subtrees

## Question 3
Consider the database table `Employees` with columns `DepartmentID` and `Salary`. Which of the following SQL queries will return the `DepartmentID` and the average salary of departments having an average salary greater than 50,000?
A. `SELECT DepartmentID, AVG(Salary) FROM Employees WHERE AVG(Salary) > 50000 GROUP BY DepartmentID;`
B. `SELECT DepartmentID, AVG(Salary) FROM Employees GROUP BY DepartmentID HAVING AVG(Salary) > 50000;`
C. `SELECT DepartmentID, AVG(Salary) FROM Employees HAVING AVG(Salary) > 50000 GROUP BY DepartmentID;`
D. `SELECT DepartmentID, AVG(Salary) FROM Employees GROUP BY DepartmentID WHERE AVG(Salary) > 50000;`

## Question 4
Which OOP concept refers to the ability of different classes to respond to the same message (method call) in different ways?
A. Encapsulation
B. Inheritance
C. Polymorphism
D. Abstraction

## Question 5
What is the output of the following C++ code?
```cpp
#include <iostream>
using namespace std;

int main() {
    int a = 10;
    int &b = a;
    int *c = &b;
    *c = 20;
    cout << a << " " << b;
    return 0;
}
```
A. `10 10`
B. `20 10`
C. `10 20`
D. `20 20`

## Question 6
What does the following Python function compute for a non-negative integer `n`?
```python
def func(n):
    if n == 0:
        return 0
    return (n % 2) + func(n // 2)
```
A. The factorial of `n`
B. The number of digits in the decimal representation of `n`
C. The number of set bits (1s) in the binary representation of `n`
D. The sum of all integers from 1 to `n`

## Question 7
What is the worst-case time complexity of inserting an element into a balanced Binary Search Tree (like an AVL tree) with $N$ nodes?
A. $O(1)$
B. $O(\log N)$
C. $O(N)$
D. $O(N \log N)$

## Question 8
In Java, which of the following statements about Garbage Collection is correct?
A. Developers must manually free memory using the `delete` keyword.
B. Calling `System.gc()` guarantees that the JVM will immediately run the garbage collector.
C. Objects are eligible for garbage collection when they are no longer reachable by any active thread.
D. Garbage collection runs in the main thread of execution and pauses all other threads permanently.

## Question 9
Which of the following data structures operates on a Last-In, First-Out (LIFO) basis?
A. Queue
B. Stack
C. Heap
D. Linked List

## Question 10
Which design pattern ensures that a class has only one instance and provides a global point of access to it?
A. Factory Pattern
B. Singleton Pattern
C. Observer Pattern
D. Decorator Pattern

## Question 11
A person travels from town A to town B at a speed of 40 km/h and returns from B to A at a speed of 60 km/h. What is the average speed for the entire journey?
A. 48 km/h
B. 50 km/h
C. 52 km/h
D. 45 km/h

## Question 12
An item is marked up by 40% above its cost price. A discount of 20% is then offered on this marked price. What is the net profit percentage?
A. 20%
B. 15%
C. 12%
D. 18%

## Question 13
A bag contains 5 red, 4 blue, and 3 green marbles. If two marbles are drawn at random one after another without replacement, what is the probability that both are of the same color?
A. 19/66
B. 5/12
C. 7/22
D. 3/11

## Question 14
Worker A can complete a job in 12 days and Worker B can complete the same job in 18 days. They work together for 4 days, after which Worker A leaves. How many days will it take Worker B to finish the remaining work alone?
A. 6 days
B. 8 days
C. 5 days
D. 10 days

## Question 15
How many liters of a 30% acid solution must be mixed with 10 liters of a 60% acid solution to obtain a final mixture that is a 40% acid solution?
A. 15 liters
B. 25 liters
C. 20 liters
D. 12 liters
