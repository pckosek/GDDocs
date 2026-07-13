# 4.3.6 Decoupling Systems

## Classification

**Type:** Design / Engineering Guide

**Category:** Game Architecture

**Difficulty:** Intermediate

---

# Design Problem

Imagine a player collects a coin.

Without signals, the Player might need to tell every other object what to do.

```text
Player

↓

Increase Score

↓

Update HUD

↓

Play Sound

↓

Check Achievement

↓

Save Progress

↓

Unlock Door
```

The Player now knows about nearly every important system in the game.

As the project grows, this becomes increasingly difficult to manage.

Can we design our game so that objects don't need to know so much about one another?

---

# Why This Matters

Large software projects become difficult to maintain when every object depends on every other object.

Imagine changing the HUD.

Would you also need to edit the Player?

What if you add a new achievement?

Do you need to modify every gameplay script?

When systems depend heavily on one another, even small changes can ripple throughout the project.

Signals help reduce these dependencies.

---

# Mental Model

Think about a school intercom.

The principal makes an announcement.

```text
"The buses have arrived."
```

Who responds?

- Teachers dismiss students.
- Students gather their belongings.
- Office staff prepare dismissal.
- Custodians continue cleaning.

The principal doesn't tell each person exactly what to do.

Everyone simply responds according to their own responsibility.

Signals work the same way.

---

# Before Signals

Without signals, communication often looks like this.

```text
Player

├── HUD
├── Sound Manager
├── Achievement Manager
├── Save System
├── Door
├── Enemy Manager
└── ...
```

Every new feature creates another connection.

The Player gradually becomes responsible for too many systems.

---

# With Signals

Instead:

```text
Player

↓

player_died
```

Each system decides whether to listen.

```text
HUD

Game Manager

Achievement Manager

Music Manager

Game Over Screen
```

The Player only announces the event.

It no longer needs to know who is responding.

---

# Design Principle

## Objects should know as little as possible about one another.

Each object should focus on its own responsibility.

Communication should happen through well-defined events rather than direct control.

Reducing unnecessary dependencies makes software easier to understand, modify, and extend.

---

# Practical Observation

One way to recognize tightly coupled code is to ask:

> **How many other objects does this script know about?**

If a single object directly references dozens of unrelated systems...

...it may be taking on too much responsibility.

Signals often help reduce those connections.

---

# Experiment

Imagine adding a brand-new feature to your game.

```text
Statistics Screen
```

It wants to record:

- enemies defeated
- coins collected
- time played

If your game already broadcasts those events...

...the Statistics Screen can simply begin listening.

No existing gameplay objects need to change.

Now imagine your game does **not** use signals.

How many scripts would need to be modified?

---

# Common Misconceptions

### "Decoupled means objects never communicate."

No.

Objects still communicate.

They simply communicate through well-defined events instead of directly controlling one another.

---

### "Signals remove all dependencies."

No.

Some objects naturally depend on others.

Signals simply reduce unnecessary dependencies.

---

### "Direct function calls are always bad."

Not at all.

Sometimes one object genuinely needs another.

Signals are most useful when many independent systems need to react to the same event.

---

### "Decoupling makes programs more complicated."

At first, perhaps.

As projects grow, however, decoupled systems are usually much easier to modify and maintain.

---

# Reflection

Think about a game you've built.

Can you identify one object that seems responsible for "too many things"?

How might signals allow some of those responsibilities to move into other objects?

Now ask yourself:

If you wanted to add one completely new feature...

How many existing scripts would need to change?

---

# Looking Ahead

We've now explored how independent systems communicate through events.

The next challenge is different.

Communication tells us **what happened.**

The next question asks:

> **How do we control what an object is currently doing?**

We'll answer that by introducing another important architectural tool:

> **State Machines.**