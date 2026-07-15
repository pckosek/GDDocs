# Technique 2.1 — Create a Sky Environment

## Classification

**Type:** Technique

**Category:** Visual Worldbuilding

**Difficulty:** Beginner

**Estimated Time:** 10–20 minutes

---

# Design Problem

An empty world has no atmosphere.

Without a sky, the world often feels unfinished, directionless, or artificial.

A sky provides context.

It tells the player:

* where they are
* what time it is
* what kind of world they have entered
* how the environment should feel

A useful mental model is:

> The sky is the largest object in your world.

Although players can never reach it, they are constantly experiencing it.

---

# Why This Technique Matters

The sky influences nearly every moment of gameplay.

A bright blue afternoon creates a very different experience than:

* a dark overcast storm
* a red alien sunset
* a deep star field
* a glowing fantasy sky

Remarkably, none of the gameplay has changed.

Only the atmosphere.

This is one of the first techniques that demonstrates how visual design shapes player perception.

---

# Operations Used

Required Operations:

* Add a Child Node
* Assign a Resource
* Modify Resource Properties
* Run a Scene

Helpful Supporting Operations:

* Orbit View
* Zoom View
* Align Transform to View

---

# Recipe

The general workflow is:

```text
Add WorldEnvironment
        ↓
Create Environment Resource
        ↓
Set Background Mode to Sky
        ↓
Create Procedural Sky
        ↓
Adjust Sky Properties
        ↓
Run Scene
```

Your scene should now have a complete environmental backdrop.

---

# Design Principle

## Players experience the world before they understand it.

Long before a player notices:

* mechanics
* objectives
* controls

they notice atmosphere.

The sky is often the first artistic decision the player experiences.

A thoughtfully designed sky quietly establishes expectations for everything that follows.

---

# Practical Considerations

For many projects, a **Procedural Sky** is an excellent starting point.

It allows you to adjust:

* horizon color
* sky color
* sun appearance
* atmospheric blending

without creating custom artwork.

As projects become more sophisticated, procedural skies may eventually be replaced by HDRIs or custom skyboxes.

The underlying design principle remains the same.

---

# Experiment

Create three completely different skies.

### Version A

A bright midday sky.

Try to make the world feel welcoming.

---

### Version B

A sunset.

Experiment with warm colors near the horizon.

---

### Version C

An unusual world.

Try something unrealistic:

* purple sky
* green atmosphere
* deep red horizon
* black sky with bright stars

Do not worry whether it is "correct."

Instead ask:

> What kind of world does this suggest?

---

# Reflection

Consider the following questions:

* Which sky felt the most believable?
* Which sky was the most interesting?
* Which sky would encourage you to keep exploring?
* How much changed without moving a single object?

Write down one observation.

---

# Common Mistakes

### Ignoring the Sky

Many beginners spend all of their time building objects.

Meanwhile, the entire background remains the default gray.

Remember:

The sky occupies far more of the player's vision than most individual objects.

---

### Over-Saturating Colors

Extremely bright colors can make a scene difficult to read.

Subtle changes often create stronger atmospheres.

---

### Forgetting to Test Lighting

A sky and lighting system work together.

Changing the sky may require adjusting the scene's lighting as well.

---

### Assuming There Is One "Correct" Sky

There isn't.

The appropriate sky depends on the experience you want to create.

---

# Self Check

Before moving on, ask yourself:

✓ Does the sky support the mood of my scene?

✓ Does it help establish a believable world?

✓ Does it complement my lighting?

✓ Does it encourage the player to explore?

---

# Looking Ahead

A sky is only one part of environmental storytelling.

In the next techniques you will begin shaping the world further through:

* lighting
* materials
* composition
* environmental detail

Together, these techniques transform a collection of objects into a place that feels worth exploring.
