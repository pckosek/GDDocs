# 5.1 Representing Information

## Big Question

> **How do computers organize information?**

---

# Design Problem

Everything a computer creates begins with information.

A game world.

An image.

A sound effect.

A maze.

A character inventory.

A high score table.

Before a computer can transform any of these things...

...it must first **represent** them.

Representation is one of the most fundamental ideas in computer science.

---

# Why This Matters

Imagine asking a computer to create a forest.

Before it can place a single tree, it must answer questions like:

- Where are the trees?
- How many trees are there?
- Which trees have already been visited?
- Which locations are empty?
- Which trees are connected by a path?

None of these questions involve graphics.

They involve **information**.

The computer cannot reason about a world until that world has been represented.

---

# Mental Model

Think about a map.

A paper map is not the real world.

It is a **representation** of the real world.

Likewise, a computer never stores the real thing.

Instead, it stores representations.

For example:

```text
A Player
```

might become

```text
Health = 85

Coins = 12

Position = (17, 4)
```

An image might become

```text
255
120
18
...
```

A game world might become

```text
. . . # #
# . . . #
...
```

Different kinds of information require different representations.

---

# Design Principle

## Good representations make good algorithms possible.

Choosing how information is represented is one of the most important design decisions in software engineering.

A poor representation often makes simple problems difficult.

A good representation often makes difficult problems surprisingly simple.

---

# Representation Questions

Whenever we create software, we should begin by asking questions like:

- How many things am I storing?
- Does the order matter?
- Can values repeat?
- Do I need names?
- How will I find information later?
- Will this information change?

The answers help determine the best representation.

---

# Practical Observation

Beginning programmers often believe there is one "correct" way to store information.

Professional programmers ask a different question.

> **Which representation makes this problem easiest to solve?**

There is rarely one perfect representation.

Instead, there are representations that are better suited to particular problems.

Throughout this unit, we'll learn several different ways to organize information, each with its own strengths and weaknesses.

---

# Common Misconceptions

### "Computers store the real object."

No.

Computers store representations of objects.

A player, an image, or a sound all become collections of data.

---

### "There is one best way to organize information."

Usually not.

Different problems benefit from different representations.

The best choice depends on what you need to accomplish.

---

### "Representations are only important for large programs."

No.

Even the smallest programs depend on choosing appropriate representations.

Good habits learned early continue to help as projects become more complex.

---

# Reflection

Consider the following digital artifacts.

What information might a computer need to represent for each one?

| Artifact | Possible Information |
|-----------|----------------------|
| A Player | |
| An Image | |
| A Sound Effect | |
| A Maze | |
| A Deck of Cards | |
| A Tile Map | |

Now ask yourself:

How might different representations make some operations easier than others?

---

# Looking Ahead

Computers have many different ways of organizing information.

The next question becomes:

> **What is the simplest way to represent an ordered collection of information?**