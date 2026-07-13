# 5.1.5 Associative Collections (Dictionaries)

## Classification

**Type:** Design / Engineering Guide

**Category:** Computational Representation

**Difficulty:** Beginner

---

# Design Problem

Imagine creating a player.

The player has several pieces of information.

- Health
- Coins
- Lives
- Score

One approach might be:

```python
player = [100, 25, 3, 800]
```

But now ask yourself:

Which number represents the player's health?

Which one is the score?

Without additional information, the values have lost their meaning.

Instead of remembering positions...

...we can give each value a name.

Collections that associate names with values are called **Dictionaries**.

---

# Why This Matters

Many kinds of information naturally have names.

Examples include:

- player statistics
- game settings
- inventory quantities
- level information
- configuration values

In these situations, remembering that

```text
Health is position 0
```

is unnecessary.

Instead, we can simply ask for:

```text
Health
```

The name becomes part of the representation.

---

# Mental Model

Think of a dictionary as a collection of labeled boxes.

```text
Health

↓

100

----------------

Coins

↓

25

----------------

Lives

↓

3

----------------

Score

↓

800
```

Instead of searching by position...

...we search by name.

Each name is called a **key**.

Each associated piece of information is called a **value**.

---

# Starter Implementation

Creating a dictionary is straightforward.

```python
player = {
    "health": 100,
    "coins": 25,
    "lives": 3,
    "score": 800
}
```

Now we can access information by name.

```python
player["health"]
```

or

```python
player["score"]
```

The names explain what the values represent.

---

# Dissecting the Structure

Notice that every entry has two parts.

```text
Key

↓

Value
```

For example,

```python
"coins" : 25
```

The key

```text
"coins"
```

describes the meaning.

The value

```text
25
```

stores the information.

Together, they create an association.

---

# Design Principle

## Use names when meaning matters more than position.

If the identity of the information is more important than its location...

...a dictionary is often the most natural representation.

Names make programs easier to read and easier to understand.

---

# Experiment

Consider each situation.

Would a dictionary be an appropriate representation?

| Information | Dictionary? |
|-------------|-------------|
| Player Statistics | |
| Graphics Settings | |
| RGB Color | |
| High Scores by Level | |
| Inventory Quantities | |
| Animation Frames | |

Can you explain why?

---

# Practical Observation

Dictionaries appear throughout game development.

For example:

```python
enemy = {
    "name": "Skeleton",
    "health": 50,
    "damage": 12,
    "speed": 3
}
```

Or

```python
settings = {
    "volume": 0.75,
    "difficulty": "Normal",
    "fullscreen": True
}
```

Notice that each value has a clear meaning without requiring comments or documentation.

The keys explain the structure.

---

# Common Misconceptions

### "Dictionaries replace lists."

No.

Lists organize information by position.

Dictionaries organize information by name.

Each solves a different problem.

---

### "Dictionary keys must always be words."

No.

Many different kinds of values can serve as keys.

Strings are simply one of the most common choices because they are easy for people to read.

---

### "Dictionaries preserve meaning because of their order."

No.

The meaning comes from the keys, not their position.

The key identifies what each value represents.

---

### "Everything should be stored in a dictionary."

Not necessarily.

If information has no meaningful names, another representation may be simpler.

Good software chooses the representation that best matches the problem.

---

# Reflection

Suppose you are creating each of the following.

Would a dictionary be an appropriate representation?

| Problem | Dictionary? |
|----------|-------------|
| Player Statistics | |
| Inventory Quantities | |
| Pixel Coordinates | |
| Game Settings | |
| Boss Information | |
| Sequence of Animation Frames | |

Now ask yourself:

Would the information become easier to understand if each value had a meaningful name?

---

# Looking Ahead

We've now explored four different ways to organize information.

- Lists preserve order.
- Tuples preserve structure.
- Sets preserve uniqueness.
- Dictionaries associate names with values.

The final question becomes:

> **How do we choose the best representation for a particular problem?**