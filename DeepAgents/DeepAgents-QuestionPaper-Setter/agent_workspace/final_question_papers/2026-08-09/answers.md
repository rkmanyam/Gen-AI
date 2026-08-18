# Combined Entrance Examination Answer Key

Date: 2026-08-09
Total Questions: 45

---

## Section A: Aptitude and Programming (Questions 1 - 15)

### Question 1
- **Correct Answer:** C
- **Explanation:** `my_list` is initialized to `[1, 2, 3]`. Inside the function, the re-assignment `lst = lst + [4]` binds the local variable `lst` to a new object. Modifying index 0 of this new list does not affect the outer list `my_list`.
- **Difficulty:** Medium
- **Concept:** Python List Mutability & Scoping

### Question 2
- **Correct Answer:** A
- **Explanation:** In-order traversal (Left, Root, Right) of a Binary Search Tree (BST) visits nodes in strictly increasing sorted order.
- **Difficulty:** Medium
- **Concept:** BST Traversal

### Question 3
- **Correct Answer:** B
- **Explanation:** Standard SQL syntax requires grouping by non-aggregated fields first, and then using the `HAVING` clause to filter based on aggregates (e.g., `AVG()`).
- **Difficulty:** Medium
- **Concept:** SQL Grouping and Aggregation

### Question 4
- **Correct Answer:** C
- **Explanation:** Polymorphism allows child classes to implement identical interfaces (methods) in distinct ways.
- **Difficulty:** Easy
- **Concept:** OOP Concepts

### Question 5
- **Correct Answer:** D
- **Explanation:** Since reference `b` is an alias for `a`, and pointer `c` points to the address of `b` (which is `a`), changing the dereferenced pointer `*c` updates the underlying memory location of `a` to 20.
- **Difficulty:** Hard
- **Concept:** C++ Pointers and References

### Question 6
- **Correct Answer:** C
- **Explanation:** The function sums up the remainders of modulo-2 operations while shifting `n` to the right recursively (dividing by 2), which effectively computes the Hamming weight (number of set bits).
- **Difficulty:** Medium
- **Concept:** Recursion and Binary Logic

### Question 7
- **Correct Answer:** B
- **Explanation:** Balanced binary search trees maintain a maximum depth of $O(\log N)$. Thus, worst-case insertions take time proportional to the height, which is logarithmic.
- **Difficulty:** Medium
- **Concept:** Time Complexity of Balanced Trees

### Question 8
- **Correct Answer:** C
- **Explanation:** An object is eligible for garbage collection in Java once there are no valid reference paths starting from root threads that can reach it.
- **Difficulty:** Easy
- **Concept:** Java Garbage Collection Principles

### Question 9
- **Correct Answer:** B
- **Explanation:** A Stack operates on a LIFO (Last-In, First-Out) mechanism.
- **Difficulty:** Easy
- **Concept:** Linear Data Structures

### Question 10
- **Correct Answer:** B
- **Explanation:** The Singleton design pattern restricts instantiation to a single object and provides global access to it.
- **Difficulty:** Medium
- **Concept:** Software Design Patterns

### Question 11
- **Correct Answer:** A
- **Explanation:** The average speed of a round trip of equal distance is the harmonic mean: $\frac{2 \times 40 \times 60}{40 + 60} = 48\text{ km/h}$.
- **Difficulty:** Medium
- **Concept:** Time, Speed, and Distance

### Question 12
- **Correct Answer:** C
- **Explanation:** Let cost price be 100. Markup = 140. 20% discount on 140 = 28. Selling price = 112. Net profit = 12%.
- **Difficulty:** Medium
- **Concept:** Profit and Loss

### Question 13
- **Correct Answer:** A
- **Explanation:** Total outcomes = 132. Favorable outcomes = $5 \times 4$ (both Red) + $4 \times 3$ (both Blue) + $3 \times 2$ (both Green) = 38. Probability = $38 / 132 = 19 / 66$.
- **Difficulty:** Medium
- **Concept:** Probability

### Question 14
- **Correct Answer:** B
- **Explanation:** Worker A efficiency = 3 units/day, Worker B = 2 units/day. In 4 days they do 20 units. B completes the remaining 16 units in $16 / 2 = 8$ days.
- **Difficulty:** Medium
- **Concept:** Time and Work

### Question 15
- **Correct Answer:** C
- **Explanation:** Set up concentration equality: $0.3x + 0.6(10) = 0.4(x + 10) \implies 0.1x = 2 \implies x = 20\text{ liters}$.
- **Difficulty:** Medium
- **Concept:** Mixtures and Alligations

---

## Section B: Reasoning (Questions 16 - 30)

### Question 16
- **Correct Answer:** B
- **Explanation:** Across 6 years (2026-2032), there are 2 leap days included (Feb 2028 and Feb 2032) and 4 ordinary days, creating 8 odd days, which is equal to 1 odd day. Sunday + 1 = Monday.
- **Difficulty:** Medium
- **Concept:** Calendar and Dates

### Question 17
- **Correct Answer:** A
- **Explanation:** "Father's only son" is Amit. His grandmother's only daughter-in-law is Amit's mother.
- **Difficulty:** Medium
- **Concept:** Blood Relations

### Question 18
- **Correct Answer:** B
- **Explanation:** Divide the 8-letter word in halves ("COMP", "ILER") and reverse both halves individually: "PMOC", "RELI" $\rightarrow$ "PMOCRELI".
- **Difficulty:** Medium
- **Concept:** Coding-Decoding

### Question 19
- **Correct Answer:** A
- **Explanation:** Pattern is $(T_n \times 3) - \text{odd numbers} = T_{n+1}$. So $248 \times 3 - 9 = 735$.
- **Difficulty:** Medium
- **Concept:** Number Series

### Question 20
- **Correct Answer:** B
- **Explanation:** Some computers are phones, and no phone is a tablet, which means those computers that are phones can never be tablets.
- **Difficulty:** Medium
- **Concept:** Syllogisms

### Question 21
- **Correct Answer:** B
- **Explanation:** Using coordinate tracking, the final point B is at (20, 21). The shortest distance is $\sqrt{20^2 + 21^2} = 29\text{ meters}$.
- **Difficulty:** Medium
- **Concept:** Directions

### Question 22
- **Correct Answer:** D
- **Explanation:** The linear ordering must be: R, P, Q, T, S, U. The person immediately to the right of S is U.
- **Difficulty:** Hard
- **Concept:** Linear Seating Arrangement

### Question 23
- **Correct Answer:** A
- **Explanation:** Principle of Inclusion-Exclusion yields 115 who like at least one language. 120 - 115 = 5 who like none.
- **Difficulty:** Medium
- **Concept:** Set Theory & Venn Diagrams

### Question 24
- **Correct Answer:** B
- **Explanation:** Replacing the symbols gives $36 / 4 \times 7 - 8 + 10 = 65$.
- **Difficulty:** Easy
- **Concept:** Mathematical Operations

### Question 25
- **Correct Answer:** C
- **Explanation:** Order is $E < D < C < A < B$. Runner E finished first.
- **Difficulty:** Hard
- **Concept:** Analytical Reasoning

### Question 26
- **Correct Answer:** A
- **Explanation:** Alphabetical opposites are used (Position sum = 27). G(7) $\rightarrow$ T(20), A(1) $\rightarrow$ Z(26), etc. Resulting code is "TZIWVM".
- **Difficulty:** Medium
- **Concept:** Coding-Decoding

### Question 27
- **Correct Answer:** A
- **Explanation:** Using coordinate tracking, final point is (0, 15). The distance from start is 15 meters to the North.
- **Difficulty:** Medium
- **Concept:** Directions

### Question 28
- **Correct Answer:** B
- **Explanation:** "Only daughter of my father" refers to the female speaker. Thus, the speaker is the man's wife, making the man her husband.
- **Difficulty:** Medium
- **Concept:** Blood Relations

### Question 29
- **Correct Answer:** C
- **Explanation:** Placing B at 1, A is at 2 (left), C is at 4 (opposite A), and D is at 3. The immediate right of D is position 2, which is A.
- **Difficulty:** Medium
- **Concept:** Circular Seating Arrangement

### Question 30
- **Correct Answer:** B
- **Explanation:** Using clock angle formula: $|30(3) - 5.5(15)| = |90 - 82.5| = 7.5^\circ$.
- **Difficulty:** Medium
- **Concept:** Clocks

---

## Section C: Communication Skills (Questions 31 - 45)

### Question 31
- **Correct Answer:** C
- **Explanation:** Routing of datagrams and logical addressing is the primary function of Layer 3 (Network Layer) of the OSI model.
- **Difficulty:** Medium
- **Concept:** OSI Model Layers

### Question 32
- **Correct Answer:** B
- **Explanation:** With a /26 prefix, there are 6 bits for host IDs. $2^6 - 2 = 62$ usable host addresses.
- **Difficulty:** Hard
- **Concept:** IP Addressing & Subnetting

### Question 33
- **Correct Answer:** C
- **Explanation:** Paraphrasing ideas, clarifying concepts, and focusing entirely on the speaker define active listening.
- **Difficulty:** Easy
- **Concept:** Verbal Communication & Listening Skills

### Question 34
- **Correct Answer:** B
- **Explanation:** "Bcc" stands for Blind Carbon Copy. It is used to distribute emails to multiple addresses without showing those addresses to others.
- **Difficulty:** Easy
- **Concept:** Professional Written Communication

### Question 35
- **Correct Answer:** B
- **Explanation:** User Datagram Protocol (UDP) is a connectionless, low-overhead protocol preferred for real-time traffic like streaming.
- **Difficulty:** Medium
- **Concept:** Transport Layer Protocols

### Question 36
- **Correct Answer:** B
- **Explanation:** Differences in wording, local idioms, or technical jargon cause semantic communication barriers.
- **Difficulty:** Medium
- **Concept:** Barriers to Communication

### Question 37
- **Correct Answer:** C
- **Explanation:** Sending private messages securely requires encrypting with the recipient's public key (Bob's public key).
- **Difficulty:** Hard
- **Concept:** Network Security & Cryptography

### Question 38
- **Correct Answer:** B
- **Explanation:** Maintaining natural eye contact and nodding signal engagement, interest, and confidence.
- **Difficulty:** Easy
- **Concept:** Non-verbal Communication

### Question 39
- **Correct Answer:** C
- **Explanation:** MAC addresses are physical 48-bit hex addresses burned into the NIC. IP addresses are logical Layer 3 routing addresses.
- **Difficulty:** Medium
- **Concept:** Network Addressing Fundamentals

### Question 40
- **Correct Answer:** B
- **Explanation:** The 7x7 rule limits slides to a maximum of 7 lines and 7 words per line to maintain legibility.
- **Difficulty:** Medium
- **Concept:** Professional Presentation Skills

### Question 41
- **Correct Answer:** B
- **Explanation:** When using "neither... nor", the verb agrees with the closer subject. Since "employees" is plural, "were prepared" is correct.
- **Difficulty:** Medium
- **Concept:** Subject-Verb Agreement

### Question 42
- **Correct Answer:** C
- **Explanation:** "Cogent" means clear, logical, and highly convincing (persuasive).
- **Difficulty:** Medium
- **Concept:** Vocabulary in Context

### Question 43
- **Correct Answer:** C
- **Explanation:** Proxemics is the study of how people use space and distance to communicate.
- **Difficulty:** Medium
- **Concept:** Communication Theory

### Question 44
- **Correct Answer:** B
- **Explanation:** An indirect buffer strategy cushions bad news with neutral framing first, preserving professional relationships.
- **Difficulty:** Medium
- **Concept:** Professional Written Communication Strategy

### Question 45
- **Correct Answer:** B
- **Explanation:** "Cut corners" means doing something quickly or cheaply, usually at the expense of quality.
- **Difficulty:** Medium
- **Concept:** Idioms and Phrases
