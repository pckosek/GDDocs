# Technique 3.7 — Following, Orbiting, and Relative Motion

## Classification

**Type:** Transform Systems Technique

**Category:** Transform Systems

**Difficulty:** Advanced

**Estimated Time:** 30–45 minutes

---

# Design Problem

Many interesting systems do not move independently.

Instead, they move **relative to something else.**

Examples include:

* a moon orbiting a planet
* a camera following a player
* a drone escorting a vehicle
* a companion following a character
* a satellite circling a space station

These systems appear very different.

Yet they all rely on the same underlying idea:

> Movement is often defined relative to another object.

---

# Why This Technique Matters

Beginning programmers often think about moving objects independently.

Experienced developers often think about relationships.

Instead of asking:

> "Where should this object move?"

they ask:

> "Who should this object follow?"

or

> "What should this object orbit?"

That change in perspective makes many systems dramatically simpler.

---

# Mental Model

Imagine walking through a city with a friend.

Your friend is not trying to maintain a specific world position.

Instead, they are trying to remain:

> "Three steps behind you."

That position changes constantly.

Not because the relationship changes...

...but because **you** are moving.

Relative motion works exactly the same way.

---

# Core Idea

Relative motion defines movement using another object as the reference.

Examples:

```text id="jlwm9t"
Planet
└── Moon
```

The Moon moves relative to the Planet.

---

```text id="jlwm7h"
Player
└── Camera
```

The Camera moves relative to the Player.

---

```text id="jlwm4m"
Vehicle
└── Turret
```

The Turret moves relative to the Vehicle.

---

The relationship matters more than the absolute coordinates.

---

# Experiment

Build a simple hierarchy.

```text id="6kjlwm"
Planet

└── Moon
```

Rotate the Planet.

Observe the Moon.

Questions:

* Is the Moon moving?
* Is the Planet moving?
* Which object actually changed?

Now repeat using:

```text
Player

└── Camera
```

Move the Player.

Observe the Camera.

---

# Investigation

Create three versions of the same scene.

### Version A

The Camera exists independently.

Move the Player.

Observe.

---

### Version B

The Camera is parented to the Player.

Move the Player.

Observe.

---

### Version C

The Camera follows using code.

Move the Player.

Observe.

Questions:

* Which systems behave similarly?
* Which behave differently?
* Why might a developer choose one approach over another?

---

# Design Principle

## Relationships often matter more than positions.

Many game systems are not trying to reach a location.

They are trying to maintain a relationship.

Examples:

* Stay behind the player.
* Stay above the vehicle.
* Stay ten meters away.
* Orbit at a constant distance.
* Follow with a slight delay.

Those relationships create behavior that feels natural.

---

# Practical Applications

Relative motion appears throughout game development.

Examples include:

### Solar Systems

Planets orbit stars.

Moons orbit planets.

---

### Third-Person Cameras

The camera remains behind the player.

---

### Companion Characters

Followers maintain a comfortable distance.

---

### Orbiting Weapons

Weapons circle the player.

---

### Decorative Animation

Objects rotate around a central point.

---

Nearly every game contains systems based on relative motion.

---

# Common Misconceptions

### "Orbiting requires complicated mathematics."

Not always.

Simple parent-child hierarchies can produce convincing orbiting behavior.

---

### "Following means copying another object's position."

Sometimes.

More often, following means maintaining a relationship.

---

### "Everything should be parented."

Not necessarily.

Some relationships are better expressed through code than through hierarchy.

Choosing the appropriate approach is part of system design.

---

# Challenge

Create two moons.

Moon A:

Use hierarchy.

Moon B:

Use code.

Both should orbit the same planet.

Before testing:

Predict:

* Which will be easier to build?
* Which will be easier to modify?
* Which gives you greater flexibility?

Test your predictions.

Discuss your observations.

---

# Reflection

Complete the sentence:

> Relative motion allows me to...

Now answer:

Which systems in games are really relationships disguised as movement?

Try to think of three examples.

---

# Self Check

Before moving on, ask yourself:

✓ Can I distinguish between independent motion and relative motion?

✓ Can I explain why orbiting works?

✓ Can I recognize when hierarchy simplifies a problem?

✓ Can I decide whether a relationship belongs in hierarchy or code?

---

# Looking Ahead

The Transform Systems explored in this section form the foundation for many of the projects you will build throughout the remainder of the course.

Whether creating:

* flying machines
* procedural worlds
* enemy AI
* particle systems
* camera rigs

the same ideas continue to appear.

The mathematics becomes more sophisticated.

The underlying question remains surprisingly simple:

> **What relationship should these objects have to one another?**

Learning to answer that question is one of the defining habits of computational worldbuilding.
