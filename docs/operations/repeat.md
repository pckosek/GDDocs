# 5.2.7 Repeat

## Classification

**Type:** Design / Engineering Guide

**Category:** Computational Operations

**Difficulty:** Beginner

---

# Design Problem

Suppose we know how to update **one** pixel.

How do we update one million pixels?

Or perhaps we know how to generate **one** audio sample.

How do we create forty-four thousand samples for one second of sound?

Or maybe we know how to process **one** tile in a game world.

How do we process an entire map?

The answer is not to write the same code thousands of times.

Instead, we repeat the same operation.

---

# Why This Matters

Computers excel at repetition.

Once we describe an operation once...

...the computer can perform it again and again.

Examples include:

- generating every pixel in an image
- processing every tile in a grid
- updating every enemy
- creating every audio sample
- smoothing every cell in a cave
- examining every frontier cell in a maze

Many computational systems are simply one operation repeated many times.

---

# Mental Model

Think of laying bricks.

You don't invent a new technique for every brick.

You repeat the same action.

```text
One Brick

↓

Repeat

↓

Wall
```

Computation works the same way.

```text
One Operation

↓

Repeat

↓

Artifact
```

The complexity comes from repetition.

Not from making every step different.

---

# Starter Implementation

Suppose we wish to generate ten values.

```python
values = [
    x
    for x in range(10)
]
```

Although the code is short...

...the computer performs the same operation ten times.

---

Or perhaps we want every value doubled.

```python
result = [
    x * 2
    for x in values
]
```

Again...

the rule remains the same.

Only the current value changes.

---

Repetition also appears in more familiar forms.

```python
for value in values:
    print(value)
```

The computer performs the same instructions once for every element in the collection.

---

# Dissecting the Operation

Every repetition has three parts.

```text
Choose One Value

↓

Perform One Operation

↓

Move To The Next Value
```

Eventually...

```text
No More Values

↓

Stop
```

This pattern appears throughout computing.

---

# Design Principle

## Describe the process once.

Let the computer repeat it.

The power of computation comes from automation.

Rather than solving one hundred similar problems...

...solve one problem and repeat the solution.

---

# Experiment

Imagine each of the following tasks.

What operation is being repeated?

| Task | Repeated Operation |
|------|--------------------|
| Draw an image | |
| Generate a sound | |
| Update every enemy | |
| Search a maze | |
| Smooth a cave | |
| Build a height map | |

Notice that the overall artifact emerges from many repeated applications of one simple rule.

---

# Practical Observation

Many beginners believe that repetition exists only because programming languages have loops.

In reality...

loops exist because repetition is one of the fundamental operations of computation.

Whether you use:

- a loop
- a comprehension
- recursion
- a library function

the underlying idea remains the same.

Something is being repeated.

---

# Common Misconceptions

### "Repeating means copying code."

No.

Repeating means applying the same operation multiple times.

Good programs avoid duplicated code.

Instead, they automate repetition.

---

### "Every repetition performs a different task."

Usually not.

Most repetitions perform the same task on different values.

The rule remains constant.

The input changes.

---

### "Loops are the goal."

No.

Loops are one way to express repetition.

Repetition is the computational idea.

---

### "Repetition is only useful for large programs."

Even simple programs rely heavily on repetition.

Drawing ten pixels, printing five values, or checking three enemies are all examples of repeated computation.

---

# Reflection

Think about one computational artifact.

- an image
- a sound
- a maze
- a tile map

What operation must be repeated to create it?

Could the artifact exist without repetition?

Why or why not?

---

# Looking Ahead

Repeating an operation creates structure.

Sometimes, however, we don't want every repetition to produce exactly the same result.

The next question becomes:

> **How can we introduce variation while still following a rule?**