# Technique 2.2 — Light a Scene

## Classification

**Type:** Technique

**Category:** Visual Worldbuilding

**Difficulty:** Beginner

**Estimated Time:** 15–20 minutes

---

# Design Problem

A world without light is difficult to understand.

Even if every object is modeled correctly, players cannot appreciate a scene if they cannot clearly perceive its form, depth, and atmosphere.

Lighting serves two purposes:

* it allows players to see the world
* it tells players how the world should feel

A useful mental model is:

> Geometry creates the world.
>
> Lighting reveals it.

---

# Why This Technique Matters

Lighting is one of the fastest ways to change the emotional tone of a scene.

Without changing a single object, lighting can make the same environment feel:

* peaceful
* mysterious
* dangerous
* lonely
* hopeful
* dramatic

Good lighting does not simply illuminate.

It communicates.

---

# Operations Used

Required Operations:

* Add a Child Node
* Assign a Resource
* Modify Resource Properties
* Rotate Object
* Run a Scene

Helpful Supporting Operations:

* Orbit View
* Focus Selected Object
* Align Transform to View

---

# Recipe

The general workflow is:

```text id="swwc4m"
Add DirectionalLight3D
        ↓
Rotate Light
        ↓
Enable Shadows
        ↓
Adjust Intensity
        ↓
Run Scene
        ↓
Observe
        ↓
Adjust Again
```

Unlike many operations, lighting almost always requires iteration.

---

# Design Principle

## Light guides attention.

Players naturally look toward areas that are:

* brighter
* higher contrast
* more visually interesting

As a designer, you can use light to guide the player's eye without saying a single word.

Good lighting quietly answers questions like:

> Where should I look?

> Where should I go?

> What is important?

---

# Practical Considerations

For most outdoor scenes, a single:

```text
DirectionalLight3D
```

is an excellent starting point.

Remember:

The **position** of a DirectionalLight3D is largely irrelevant.

Its **rotation** determines the direction of the light, much like the angle of the sun.

If your scene feels flat, one of the first things to check is whether **shadows** are enabled. Shadows often add depth and make it easier to perceive the shapes in a scene.

---

# Experiment

Build one simple scene.

Perhaps:

* a tree
* a rock
* a small building

Now create three different lighting setups.

---

### Version A

High noon.

Place the light nearly overhead.

What does the scene feel like?

---

### Version B

Late afternoon.

Lower the light toward the horizon.

Observe how the shadows change.

---

### Version C

Extreme angle.

Move the light very low.

What details suddenly become visible?

What disappears?

---

Do not change the objects.

Only change the light.

---

# Reflection

Consider the following questions:

* Which lighting setup felt the most believable?
* Which felt the most dramatic?
* How did shadows change the scene?
* Where did your eyes naturally focus?

Write down one observation.

---

# Common Mistakes

### Forgetting Shadows

Many beginning developers add a light but leave shadows disabled.

The scene becomes brighter but still feels flat.

Whenever appropriate, experiment with shadows.

---

### Rotating the Object Instead of the Light

If the shadows are changing in unexpected ways, verify that you rotated the light—not the environment.

---

### Using Extremely Bright Lighting

Brighter is not always better.

Overexposed scenes often lose visual detail.

---

### Trying to Perfect the Lighting Immediately

Lighting is an iterative process.

Small adjustments often produce better results than dramatic ones.

---

# Self Check

Before moving on, ask yourself:

✓ Can I clearly see the important parts of my scene?

✓ Do the shadows add depth?

✓ Does the lighting support the mood I want?

✓ Does the scene feel intentional?

---

# Looking Ahead

Lighting is only one part of visual storytelling.

Combined with:

* materials
* sky environments
* object placement
* composition

lighting transforms simple geometry into a believable world.

As your projects become more sophisticated, you will find yourself returning to lighting repeatedly—not because something is broken, but because every adjustment changes how the player experiences your world.
