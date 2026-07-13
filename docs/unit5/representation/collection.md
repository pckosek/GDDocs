# 5.1.1 What is a Collection?

## Classification

**Type:** Design / Engineering Guide

**Category:** Computational Representation

**Difficulty:** Beginner

---

# Design Problem

Imagine writing a game where the player has collected:

- a sword
- a shield
- three potions
- a key

Should we create a separate variable for every item?

```python
item1 = "Sword"
item2 = "Shield"
item3 = "Potion"
item4 = "Potion"
item5 = "Potion"
item6 = "Key"
```

That quickly becomes difficult to manage.

Instead, we can group related information together.

A structure that stores multiple pieces of information is called a **collection**.

---

# Why This Matters

Very little information exists in isolation.

Games naturally organize information into groups.

Examples include:

- every enemy in a level
- every tile in a map
- every pixel in an image
- every sample in a sound
- every item in an inventory
- every high score

Collections allow us to treat many pieces of related information as one larger structure.

---

# Mental Model

Think of a collection as a container.

Instead of remembering one value...

```text
Player Health

↓

100
```

a collection remembers many values.

```text
Inventory

↓

Sword

Shield

Potion

Potion

Key
```

Or perhaps:

```text
Pixels

↓

255

120

90

45

...
```

Or:

```text
Terrain Heights

↓

12

14

15

11

...
```

Collections allow one variable to represent many related values.

---

# Design Principle

## Group related information together.

When several pieces of information belong together...

...representing them as a collection usually makes programs simpler to understand and easier to modify.

Collections allow programs to scale beyond just a handful of variables.

---

# Everyday Examples

Collections appear throughout computing.

| Problem | Collection |
|----------|------------|
| Player Inventory | Many Items |
| Image | Many Pixels |
| Audio | Many Samples |
| Game World | Many Cells |
| Leaderboard | Many Scores |
| Card Game | Many Cards |

Although these problems look different...

...they all involve storing many related pieces of information.

---

# Practical Observation

Beginning programmers often create many separate variables.

```python
enemy1_hp = 100
enemy2_hp = 80
enemy3_hp = 120
```

This works...

...until there are fifty enemies.

Collections allow programs to scale naturally.

Instead of creating more variables...

...we organize the information.

---

# Common Misconceptions

### "Collections are only for large programs."

No.

Even very small programs often benefit from grouping related information together.

---

### "Collections all work the same way."

No.

Different collections are designed for different purposes.

Some preserve order.

Some prevent duplicates.

Some associate names with values.

We'll explore each of these throughout this section.

---

### "A collection stores only one kind of data."

Not necessarily.

Some collections can store many different kinds of information.

Others are designed for more specific purposes.

The appropriate choice depends on the problem being solved.

---

### "Collections exist because Python has them."

No.

Almost every programming language includes ways of organizing groups of information.

The exact syntax changes.

The underlying idea remains the same.

---

# Reflection

Consider each situation below.

What collection might the program need?

| Situation | Collection of... |
|------------|------------------|
| A player's inventory | |
| Pixels in an image | |
| Samples in a sound | |
| Tiles in a map | |
| High scores | |
| Enemy positions | |

Now ask yourself:

Why would using one collection be better than creating one variable for every individual value?

---

# Looking Ahead

Collections come in many different forms.

Each is designed for a different kind of problem.

The next question becomes:

> **How can we represent information when the order of the items matters?**