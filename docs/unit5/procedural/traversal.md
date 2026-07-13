# 5.7.3 Traversal

## Classification

**Type:** Design / Engineering Guide

**Category:** Procedural Systems

**Difficulty:** Intermediate

---

# Design Problem

Imagine standing at the entrance to a maze.

Your goal is not simply to move.

Your goal is to **explore**.

One step leads to another.

Each new location reveals new possibilities.

Eventually...

...your path begins to shape the world itself.

Many procedural algorithms work in exactly this way.

Rather than designing an entire world at once...

...they gradually build it by exploring one location after another.

This computational strategy is called **Traversal**.

---

# Why This Matters

Traversal appears throughout computer science.

Examples include:

- maze generation
- pathfinding
- graph search
- map exploration
- flood fill
- connected component analysis
- navigation systems

Although these problems appear different...

...they all involve moving through a representation while making decisions along the way.

Traversal is one of the most fundamental computational strategies.

---

# Mental Model

Imagine walking through an unexplored forest.

At every step you ask:

```text
Where can I go next?
```

You choose one path.

Then another.

Then another.

Eventually...

...the collection of decisions becomes a trail.

```text
Current Location

↓

Choose Neighbor

↓

Move

↓

Repeat
```

The structure emerges from the journey itself.

---

# Traversal Builds Structure

Notice something important.

Traversal does not begin with a finished artifact.

Instead, it begins with:

```text
One Location
```

Then repeatedly performs the same process.

```text
Explore

↓

Choose

↓

Move

↓

Explore Again
```

The path gradually grows.

Eventually...

...an entire structure emerges.

---

# Design Principle

## Exploration can become construction.

Many procedural systems build worlds by exploring them.

Rather than placing every wall or corridor directly...

...they describe how exploration should proceed.

The artifact emerges from the traversal itself.

---

# Examples

Many well-known algorithms belong to the traversal family.

| Strategy | Example Applications |
|-----------|----------------------|
| Random Walk | Exploration |
| Depth-First Search (DFS) | Graph Traversal |
| Recursive Backtracker | Maze Generation |
| Prim's Algorithm | Maze Generation |
| Wilson's Algorithm | Uniform Mazes |
| Aldous-Broder | Uniform Mazes |
| Flood Fill | Region Exploration |

Although each algorithm follows different rules...

...they all share the same underlying idea.

They explore.

---

# Practical Observation

Beginning programmers often think about drawing a maze.

Traversal algorithms rarely think that way.

Instead they ask:

> **Where should I explore next?**

The maze appears naturally as a consequence of those exploration decisions.

Changing the traversal strategy often produces dramatically different structures while keeping the representation exactly the same.

---

# Common Misconceptions

### "Traversal means moving."

Not quite.

Traversal is purposeful exploration.

The movement itself is only one part of the computational process.

---

### "Every traversal algorithm produces the same result."

No.

Different traversal strategies make different decisions.

Those decisions produce very different structures.

---

### "Traversal only applies to mazes."

Not at all.

Traversal appears throughout computing.

Whenever software explores connected information...

...some form of traversal is usually taking place.

---

### "Traversal requires randomness."

No.

Some traversal algorithms are completely deterministic.

Others use randomness only when choosing among several possible directions.

Traversal and randomness are separate ideas.

---

# Reflection

Imagine exploring one of the following.

- a maze
- a cave
- a graph
- a dungeon
- a network

How would you decide where to go next?

Would your choices always be the same?

Would different exploration strategies produce different final structures?

---

# Looking Back

Earlier we explored two important procedural strategies.

Randomness introduced variation.

Local rules introduced organization.

Traversal introduces something different.

It introduces **growth**.

Rather than constructing an artifact directly...

...the artifact gradually appears through exploration.

---

# Looking Ahead

Traversal is only one family of procedural systems.

Another family asks a different question.

Instead of exploring the world...

...how should we distribute objects throughout it?

The next strategy becomes:

> **Sampling.**