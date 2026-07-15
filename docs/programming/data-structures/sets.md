# 5.1.4 Unique Collections (Sets)

## Classification

**Type:** Design / Engineering Guide

**Category:** Computational Representation

**Difficulty:** Beginner

---

# Design Problem

Imagine a game where the player unlocks achievements.

```
Explorer

Master Builder

Treasure Hunter

Explorer
```

Should the player be allowed to unlock **Explorer** twice?

Probably not.

Now imagine storing every key the player has collected.

Or every room that has been visited.

Or every crafting recipe that has been discovered.

In these situations, the important question isn't:

> **What order are the values in?**

Instead, it's:

> **Has this value already been recorded?**

Collections designed to answer this question are called **Sets**.

---

# Why This Matters

Many programming problems involve keeping track of unique information.

Examples include:

- unlocked achievements
- visited locations
- discovered recipes
- active players
- completed quests
- available crafting materials

In these situations, duplicate values provide no additional information.

A set automatically keeps only one copy of each value.

---

# Mental Model

Think of a guest list.

```
Alice

Bob

Charlie

Alice
```

There is no reason to list Alice twice.

Instead, the list naturally becomes

```
Alice

Bob

Charlie
```

A set behaves in much the same way.

Its purpose is to answer questions like:

> Is this already here?

rather than

> Where does this appear?

---

# Starter Implementation

Creating a set is straightforward.

```python
visited_rooms = {
    "Entrance",
    "Library",
    "Dungeon"
}
```

Adding an existing value changes nothing.

```python
visited_rooms.add("Library")
```

The set still contains only one copy of **Library**.

Likewise:

```python
badges = {
    "Explorer",
    "Builder",
    "Champion"
}
```

Every value appears only once.

---

# Dissecting the Structure

Unlike lists and tuples...

...sets do **not** preserve order.

For example,

```python
{"Sword", "Shield", "Potion"}
```

does not promise that **Sword** comes before **Shield**.

Instead, the important property is:

```text
Every value is unique.
```

That makes sets especially useful when uniqueness is more important than ordering.

---

# Design Principle

## Use a set when uniqueness matters.

If your program only needs to know **whether** something exists...

...rather than **where** it appears...

...a set is often an excellent representation.

Sets naturally prevent duplicate information.

---

# Experiment

Consider the following situations.

Would a set be an appropriate representation?

| Information | Set? |
|-------------|------|
| Unlocked Achievements | |
| Player Inventory | |
| Visited Rooms | |
| RGB Color | |
| Completed Quests | |
| Cards Remaining in a Deck | |

Can you explain why?

---

# Practical Observation

Many algorithms spend a surprising amount of time asking questions like:

```text
Have I already visited this location?

Have I already processed this object?

Have I already generated this point?
```

Sets answer these questions efficiently.

As projects become larger, this simple idea becomes increasingly valuable.

You'll encounter sets again later when working with search algorithms, procedural generation, and graph traversal.

---

# Common Misconceptions

### "A set is just another kind of list."

No.

Lists preserve order.

Sets preserve uniqueness.

They solve different engineering problems.

---

### "Sets automatically sort values."

No.

Sets make no promises about the order in which values appear.

Their purpose is uniqueness, not ordering.

---

### "Duplicate values produce an error."

No.

Adding an existing value simply leaves the set unchanged.

The duplicate is ignored.

---

### "Sets are only useful for large programs."

Not at all.

Any time duplicate values have no meaning, a set may be the simplest representation.

---

# Reflection

For each situation below, decide whether a set would be appropriate.

| Situation | Set? |
|------------|------|
| Tiles visited during maze generation | |
| Enemy Spawn Locations | |
| Inventory Items | |
| Unique Bosses Defeated | |
| Pixels in an Image | |
| Sound Samples | |

Now ask yourself:

Would duplicate values make this representation more useful...

...or less useful?

---

# Looking Ahead

Lists preserve order.

Tuples preserve structure.

Sets preserve uniqueness.

Sometimes, however, the most important relationship is between a **name** and its associated value.

The next question becomes:

> **How can we store information by giving every value a meaningful name?**