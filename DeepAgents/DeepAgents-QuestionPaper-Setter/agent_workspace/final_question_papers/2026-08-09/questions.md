# Combined Entrance Examination Question Paper

Date: 2026-08-09
Duration: 120 Minutes
Total Questions: 45

---

## Section A: Aptitude and Programming (Questions 1 - 15)

### Question 1
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

### Question 2
An in-order traversal of a Binary Search Tree (BST) produces which of the following sequences?
A. Sorted in ascending order
B. Sorted in descending order
C. Level-by-level order
D. Root node followed by left and right subtrees

### Question 3
Consider the database table `Employees` with columns `DepartmentID` and `Salary`. Which of the following SQL queries will return the `DepartmentID` and the average salary of departments having an average salary greater than 50,000?
A. `SELECT DepartmentID, AVG(Salary) FROM Employees WHERE AVG(Salary) > 50000 GROUP BY DepartmentID;`
B. `SELECT DepartmentID, AVG(Salary) FROM Employees GROUP BY DepartmentID HAVING AVG(Salary) > 50000;`
C. `SELECT DepartmentID, AVG(Salary) FROM Employees HAVING AVG(Salary) > 50000 GROUP BY DepartmentID;`
D. `SELECT DepartmentID, AVG(Salary) FROM Employees GROUP BY DepartmentID WHERE AVG(Salary) > 50000;`

### Question 4
Which OOP concept refers to the ability of different classes to respond to the same message (method call) in different ways?
A. Encapsulation
B. Inheritance
C. Polymorphism
D. Abstraction

### Question 5
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

### Question 6
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

### Question 7
What is the worst-case time complexity of inserting an element into a balanced Binary Search Tree (like an AVL tree) with $N$ nodes?
A. $O(1)$
B. $O(\log N)$
C. $O(N)$
D. $O(N \log N)$

### Question 8
In Java, which of the following statements about Garbage Collection is correct?
A. Developers must manually free memory using the `delete` keyword.
B. Calling `System.gc()` guarantees that the JVM will immediately run the garbage collector.
C. Objects are eligible for garbage collection when they are no longer reachable by any active thread.
D. Garbage collection runs in the main thread of execution and pauses all other threads permanently.

### Question 9
Which of the following data structures operates on a Last-In, First-Out (LIFO) basis?
A. Queue
B. Stack
C. Heap
D. Linked List

### Question 10
Which design pattern ensures that a class has only one instance and provides a global point of access to it?
A. Factory Pattern
B. Singleton Pattern
C. Observer Pattern
D. Decorator Pattern

### Question 11
A person travels from town A to town B at a speed of 40 km/h and returns from B to A at a speed of 60 km/h. What is the average speed for the entire journey?
A. 48 km/h
B. 50 km/h
C. 52 km/h
D. 45 km/h

### Question 12
An item is marked up by 40% above its cost price. A discount of 20% is then offered on this marked price. What is the net profit percentage?
A. 20%
B. 15%
C. 12%
D. 18%

### Question 13
A bag contains 5 red, 4 blue, and 3 green marbles. If two marbles are drawn at random one after another without replacement, what is the probability that both are of the same color?
A. 19/66
B. 5/12
C. 7/22
D. 3/11

### Question 14
Worker A can complete a job in 12 days and Worker B can complete the same job in 18 days. They work together for 4 days, after which Worker A leaves. How many days will it take Worker B to finish the remaining work alone?
A. 6 days
B. 8 days
C. 5 days
D. 10 days

### Question 15
How many liters of a 30% acid solution must be mixed with 10 liters of a 60% acid solution to obtain a final mixture that is a 40% acid solution?
A. 15 liters
B. 25 liters
C. 20 liters
D. 12 liters

---

## Section B: Reasoning (Questions 16 - 30)

### Question 16
Today is Sunday, August 9, 2026. What day of the week will it be on August 9, 2032?
A. Sunday
B. Monday
C. Tuesday
D. Wednesday

### Question 17
Pointing to a photograph of a woman, Amit says, "She is the only daughter-in-law of the grandmother of my father's only son." How is the woman in the photograph related to Amit?
A. Mother
B. Aunt
C. Sister-in-law
D. Grandmother

### Question 18
In a certain code language, "SYSTEM" is coded as "SYSMET" and "NEARER" is coded as "AENRER". How is "COMPILER" coded in that language?
A. RELIPMOC
B. PMOCRELI
C. PMOCILER
D. COMPRELI

### Question 19
Find the missing number in the following sequence: 4, 11, 30, 85, 248, ?
A. 735
B. 744
C. 753
D. 726

### Question 20
Statements:
1. All laptops are computers.
2. Some computers are phones.
3. No phone is a tablet.

Conclusions:
I. Some laptops are phones.
II. No tablet is a computer.
III. Some computers are not tablets.

Which of the conclusions logically follow(s) from the statements?
A. Only I follows
B. Only III follows
C. Only II and III follow
D. None of the conclusions follow

### Question 21
A person starts from point A and walks 12 meters East, then turns right and walks 5 meters. He then turns left and walks 8 meters, and finally turns left and walks 26 meters to reach point B. What is the shortest distance between point A and point B?
A. 25 meters
B. 29 meters
C. 31 meters
D. 35 meters

### Question 22
Six friends—P, Q, R, S, T, and U—are sitting in a row facing North.
1. P is sitting third to the left of S.
2. R is sitting at one of the extreme ends.
3. Q is sitting to the immediate right of P.
4. T is sitting to the immediate left of S.
5. U is not sitting at the extreme left end.

Who is sitting to the immediate right of S?
A. P
B. Q
C. R
D. U

### Question 23
In a survey of 120 college students, 70 students like Python, 60 students like Java, and 45 students like C++. If 30 students like both Python and Java, 25 students like both Java and C++, 20 students like both Python and C++, and 15 students like all three languages, how many students do not like any of these three programming languages?
A. 5
B. 10
C. 15
D. 20

### Question 24
If '+' means 'multiplied by', '-' means 'divided by', '*' means 'add', and '/' means 'subtract', what is the value of the expression: $36 - 4 + 7 / 8 * 10$?
A. 54
B. 65
C. 71
D. 48

### Question 25
Five runners—A, B, C, D, and E—participated in a race.
1. No two runners finished at the same time.
2. A finished before B but after C.
3. D finished after E but before C.

Who won the race (finished first)?
A. C
B. D
C. E
D. A

### Question 26
If "FLOWER" is coded as "UOLDVI" in a certain language, how is "GARDEN" coded in that language?
A. TZIWVM
B. SZIVMN
C. TZIWUN
D. UYJVUN

### Question 27
Rohan walks 10 meters North, then turns Right and walks 15 meters. From there, he turns Left and walks 5 meters. Finally, he turns Left and walks 15 meters. How far and in which direction is he now relative to his starting point?
A. 15 meters, North
B. 15 meters, South
C. 25 meters, East
D. 10 meters, North

### Question 28
Introducing a man, a woman says, "His wife is the only daughter of my father." How is the man related to the woman?
A. Brother
B. Husband
C. Father-in-law
D. Brother-in-law

### Question 29
Four people—A, B, C, and D—are sitting around a circular table facing the center.
1. A is sitting to the immediate left of B.
2. C is sitting opposite to A.

Who is sitting to the immediate right of D?
A. B
B. C
C. A
D. Cannot be determined

### Question 30
If a wall clock shows exactly 3:15 PM, what is the angle between the hour hand and the minute hand?
A. $0^\circ$
B. $7.5^\circ$
C. $15^\circ$
D. $11.25^\circ$

---

## Section C: Communication Skills (Questions 31 - 45)

### Question 31
At which layer of the OSI reference model does routing (determining the best path for data packets across networks) take place?
A. Transport Layer
B. Data Link Layer
C. Network Layer
D. Physical Layer

### Question 32
An organization is allocated the IP address block `192.168.1.0/26`. What is the maximum number of usable host IP addresses that can be assigned to devices in this subnet?
A. 64
B. 62
C. 30
D. 126

### Question 33
In professional communication, "active listening" is best characterized by which of the following behaviors?
A. Formulating your response while the other person is still speaking.
B. Interrupting the speaker to correct factual errors immediately.
C. Paraphrasing the speaker's words and asking clarifying questions to confirm understanding.
D. Multi-tasking to show that you can handle multiple tasks efficiently.

### Question 34
When writing a formal professional email, what does the abbreviation "Bcc" stand for, and what is its primary purpose?
A. Business Carbon Copy; used to copy the main recipient's supervisor.
B. Blind Carbon Copy; used to send the email to multiple recipients without sharing their email addresses with each other.
C. Brief Content Copy; used to summarize the email for busy executives.
D. Backup Client Copy; used to save a copy of the email on a backup server.

### Question 35
Which of the following transport layer protocols is connectionless, does not guarantee delivery, and is preferred for real-time applications like video streaming and online gaming?
A. TCP (Transmission Control Protocol)
B. UDP (User Datagram Protocol)
C. HTTP (Hypertext Transfer Protocol)
D. FTP (File Transfer Protocol)

### Question 36
During a global project meeting, a team member from Germany uses highly technical local idioms that cause confusion among team members from Japan and Brazil. This is an example of which type of communication barrier?
A. Physical Barrier
B. Semantic Barrier
C. Psychological Barrier
D. Organizational Barrier

### Question 37
In asymmetric (public-key) cryptography, if Alice wants to send a confidential (encrypted) message to Bob that only Bob can read, which key should Alice use to encrypt the message?
A. Alice's Public Key
B. Alice's Private Key
C. Bob's Public Key
D. Bob's Private Key

### Question 38
Which of the following is considered a positive and encouraging non-verbal communication cue during a job interview?
A. Keeping arms crossed tightly over the chest.
B. Maintaining consistent, natural eye contact and nodding occasionally.
C. Fidgeting with a pen or looking frequently at the clock.
D. Leaning back deeply into the chair with an expressionless face.

### Question 39
Which of the following statements correctly distinguishes between a MAC address and an IP address?
A. A MAC address is dynamic and assigned by an ISP, whereas an IP address is physical and burned into the network interface card (NIC).
B. A MAC address operates at the Network Layer (Layer 3), whereas an IP address operates at the Data Link Layer (Layer 2).
C. A MAC address is a 48-bit physical address unique to the hardware, whereas an IP address is a logical address (32-bit for IPv4) used for network-layer routing.
D. A MAC address is written in decimal notation, whereas an IP address is always written in hexadecimal notation.

### Question 40
When delivering a slide presentation to an audience, what is the "7x7 rule" often recommended by communication experts?
A. Use exactly 7 slides, each containing 7 images.
B. Limit each slide to a maximum of 7 lines of text, with no more than 7 words per line.
C. Change the slide every 7 seconds for a total of 7 minutes.
D. Use a font size of 7 points for body text and 70 points for headers.

### Question 41
Choose the correct alternative to replace the underlined part of the sentence to make it grammatically correct:
"Neither the manager nor the employees <u>was prepared</u> for the sudden audit."
A. was prepared
B. were prepared
C. are preparing
D. has prepared

### Question 42
Choose the word that is closest in meaning to the bold word in the following sentence:
"The CEO's **cogent** argument convinced the board members to approve the merger immediately."
A. redundant
B. vague
C. persuasive
D. offensive

### Question 43
In the study of professional communication, the analysis of how human beings use space and distance to communicate messages is known as:
A. Kinesics
B. Haptics
C. Proxemics
D. Chronemics

### Question 44
When drafting a negative-news message (such as a job rejection or business claim denial), which written communication strategy is generally recommended to maintain goodwill?
A. Stating the negative decision in the first sentence to save the reader's time.
B. Using an indirect buffer strategy to build common ground before stating the bad news.
C. Writing in an extremely formal, passive voice to avoid taking responsibility.
D. Omitting the explanation entirely and only delivering the final decision.

### Question 45
Identify the correct meaning of the underlined idiom in the following sentence:
"We had to <u>cut corners</u> to complete the software development project within our tight budget."
A. expand the scope of the project
B. perform tasks in a fast, cheap, and potentially substandard way
C. work overtime without extra pay
D. hire external consultants to speed up the process
