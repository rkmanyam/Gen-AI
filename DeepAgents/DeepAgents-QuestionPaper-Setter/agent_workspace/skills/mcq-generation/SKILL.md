---
name: mcq-generation
description: Generate high-quality multiple-choice questions on a given topic. Use this skill when the user requests MCQs, quizzes, multiple-choice questions, practice questions, or assessment questions for a specified topic.
---

# Multiple Choice Question Generation

## Purpose

Generate accurate, clear, and useful multiple-choice questions based on the topic and requirements provided by the user.

## Input

Use the user's prompt to determine:

- Topic
- Number of questions
- Difficulty level
- Target audience
- Specific subtopics
- Question style
- Output format
- Additional constraints

If the number of questions is not specified, generate 10 questions.

If the difficulty is not specified, generate a balanced mix of Easy, Medium, and Hard questions.

## Question Generation

For each question:

- Generate exactly four options.
- Provide exactly one correct answer.
- Make incorrect options plausible.
- Ensure the question directly relates to the requested topic.
- Avoid ambiguous wording.
- Avoid duplicate questions.
- Avoid duplicate options.
- Do not use trick questions unless explicitly requested.
- Randomize the position of the correct answer.

Each question should test meaningful knowledge, understanding, application, or reasoning rather than simple memorization whenever appropriate.

## Difficulty

Use the difficulty requested by the user.

Supported levels:

- Easy
- Medium
- Hard

If no difficulty is specified, use approximately:

- 30% Easy
- 50% Medium
- 20% Hard

For small question sets, use the closest practical distribution.

## Target Audience

Adjust the complexity of questions, vocabulary, concepts, and distractors according to the requested audience.

Examples:

- Primary school → simple language and age-appropriate concepts
- High school → moderate conceptual depth
- College → deeper conceptual understanding
- Professional → practical and scenario-based questions
- Technical → terminology, concepts, implementation, and troubleshooting

## Question Types

Use a suitable mixture when the user does not specify a particular type:

- Conceptual questions
- Definition-based questions
- Application-based questions
- Scenario-based questions
- Comparison questions
- Cause-and-effect questions
- Problem-solving questions
- Practical questions

Do not force a mixture when the topic or user's requirements call for a specific question type.

## Output Format

Unless the user specifies another format, use:

### Question 1

**Difficulty:** Medium

What is the primary purpose of ...?

A. Option A  
B. Option B  
C. Option C  
D. Option D

**Correct Answer:** B

**Explanation:**  
Provide a concise explanation of why the correct answer is correct.

---

### Question 2

**Difficulty:** Easy

Question text...

A. Option A  
B. Option B  
C. Option C  
D. Option D

**Correct Answer:** D

**Explanation:**  
Provide a concise explanation.

## JSON Output

If the user explicitly requests JSON, return the questions using this structure:

{
  "topic": "<topic>",
  "total_questions": 10,
  "questions": [
    {
      "question": "<question>",
      "options": {
        "A": "<option A>",
        "B": "<option B>",
        "C": "<option C>",
        "D": "<option D>"
      },
      "correct_answer": "B",
      "explanation": "<explanation>",
      "difficulty": "Medium"
    }
  ]
}

Follow any JSON schema explicitly provided by the user instead of this default schema.

## Validation

Before returning the questions, validate the complete set.

Verify that:

1. The requested number of questions has been generated.
2. Every question has exactly four options.
3. Every question has exactly one correct answer.
4. The correct answer exists among the options.
5. The explanation supports the correct answer.
6. Questions are relevant to the requested topic.
7. Questions are not duplicated.
8. Options are not duplicated within a question.
9. The difficulty matches the user's requirements.
10. The questions are appropriate for the target audience.
11. The correct-answer positions are reasonably distributed.

If any question fails validation, revise it before returning the final output.

## Accuracy

Do not fabricate facts.

For topics involving potentially changing information, use the available `web_search` tool to verify current information.

When web search is used:

- Base the question on information actually retrieved.
- Prefer authoritative sources.
- Do not fabricate references.
- Clearly distinguish researched information from general knowledge when required.

## Important Rules

- Follow the user's requested topic exactly.
- Respect the requested number of questions.
- Respect the requested difficulty.
- Respect the requested audience.
- Respect the requested output format.
- Do not reveal internal reasoning or chain-of-thought.
- Do not include unnecessary commentary.
- Return only the generated questions and the information required by the requested format.


  ##  INDIVIDUAL SUBAGENT FILES


  - After receiving the output from a subagent, persist its output immediately.

  - Do not wait until the entire workflow is complete.

  - For aptitude:

    /workspace/questions/aptitude/<today-date>/questions.md

    /workspace/questions/aptitude/<today-date>/answers.md

  - For reasoning:

    /workspace/questions/reasoning/<today-date>/questions.md

    /workspace/questions/reasoning/<today-date>/answers.md

  - For communication:

    /workspace/questions/communication_skills/<today-date>/questions.md

    /workspace/questions/communication_skills/<today-date>/answers.md

    Only create directories for categories that were actually requested.