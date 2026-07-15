# 5.2.2 Access

## Classification

**Type:** Design / Engineering Guide

**Category:** Computational Operations

**Difficulty:** Beginner

---

# Design Problem

Generating information is only the beginning.

Once a representation exists...

...we need to use it.

Imagine creating a game world containing one thousand tiles.

How do we find one specific tile?

Or suppose we have an image containing two million pixels.

How do we retrieve the color of just one pixel?

Or perhaps we have a dictionary describing the player.

How do we find the player's health?

The answer is through **access**.

Access is the operation of retrieving information from a representation.

---

# Why This Matters

Almost every program spends far more time reading information than creating it.

Games constantly access:

- player positions
- enemy health
- inventory items
- map tiles
- image pixels
- sound samples
- settings

Without efficient access, representations become difficult to use.

Good representations make important information easy to find.

---

# Mental Model

Think of a library.

The books already exist.

The challenge is finding the one you need.

Collections work the same way.

You already have the information.

Access is the process of locating it.

Different representations provide different ways to retrieve information.

---

# Starter Implementation

Lists are accessed by position.

```python
inventory = [
    "Sword",
    "Shield",
    "Potion"
]

inventory[1]
```

retrieves

```text
Shield
```

---

Tuples work similarly.

```python
position = (12, 8)

position[0]
```

retrieves

```text
12
```

---

Dictionaries use names instead of positions.

```python
player = {
    "health": 100,
    "coins": 25
}

player["health"]
```

retrieves

```text
100
```

Different representations.

Different methods of access.

---

# Dissecting the Operation

Notice that access does **not** change the representation.

It simply answers questions.

For example:

```text
What is the player's health?

↓

100
```

Or

```text
What color is this pixel?

↓

(255, 128, 64)
```

Or

```text
Which neighbors surround this cell?

↓

[12, 18, 19]
```

Access retrieves information.

It does not modify it.

---

# Design Principle

## Good representations make important information easy to find.

When choosing a representation, ask yourself:

> **How will I retrieve this information later?**

The easiest representation to create is not always the easiest representation to use.

---

# Experiment

Suppose you need to retrieve:

- the fifth inventory item
- the player's score
- the color of one pixel
- the position of an enemy
- the neighbors of a maze cell

For each example, ask yourself:

What information tells the computer where to look?

---

# Practical Observation

Different collections naturally support different kinds of access.

| Representation | Access By |
|----------------|-----------|
| List | Position (Index) |
| Tuple | Position (Index) |
| Set | Membership |
| Dictionary | Key |

Notice that every representation emphasizes a different relationship.

Choosing the right representation often makes retrieval much simpler.

---

# Common Misconceptions

### "Access changes the data."

No.

Access retrieves information.

The representation remains unchanged.

---

### "Every collection uses indexes."

No.

Lists and tuples use indexes.

Dictionaries use keys.

Sets are usually used to determine whether a value exists.

Different representations provide different ways of finding information.

---

### "The fastest representation is always the best."

Not necessarily.

The best representation is the one that makes your program easiest to understand while supporting the operations you perform most often.

---

### "Finding information is the same as generating it."

No.

Generation creates new representations.

Access retrieves existing information.

These are different computational operations.

---

# Reflection

Imagine you are writing a game.

How would you retrieve:

| Information | What would you use to access it? |
|--------------|----------------------------------|
| Player Health | |
| Fifth Inventory Item | |
| Pixel at (25, 18) | |
| Tile at (7, 3) | |
| Current Volume Setting | |

Now ask yourself:

Would a different representation make any of these easier to retrieve?

---

# Looking Ahead

Access allows us to retrieve information.

Eventually, however, games need to change.

The next question becomes:

> **How can we update a representation after it has been created?**