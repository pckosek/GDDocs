# Operation 0.4.3 — Configure Physics Engine Settings

## Classification

**Type:** Operation
**Category:** Project / Editor Configuration
**Difficulty:** Intermediate
**Estimated Time:** 3 minutes

---

## Purpose

Physics Engine Settings control how the entire project simulates physical behavior.

These settings affect systems such as:

* gravity
* collision simulation
* rigid body behavior
* character controllers
* movement systems
* physics performance

Unlike most Inspector operations, Physics Engine Settings affect the entire project rather than a single object.

A useful mental model is:

> Physics settings define the laws of nature for your game world.

---

## When Would I Use This?

Use this operation whenever you need to adjust how physics behaves globally.

Examples:

* Change gravity strength
* Create a low-gravity environment
* Create a moon-like simulation
* Increase physics accuracy
* Improve performance
* Customize character movement assumptions

Many projects never need to modify these settings, but understanding them helps explain how Godot's physics systems work.

---

## Prerequisites

Before beginning:

* A Godot project exists

No scene is required.

Physics settings are configured at the project level.

---

## Procedure

### Step 1 — Open Project Settings

Select:

```text
Project
→ Project Settings
```

---

### Step 2 — Locate Physics Settings

Navigate to:

```text
Physics
```

You may see categories such as:

```text
Physics
├── 2D
└── 3D
```

depending on your project type.

---

### Step 3 — Examine Gravity

One of the most commonly modified settings is:

```text
Default Gravity
```

Example:

```text
980
```

in 2D projects.

or

```text
9.8
```

in many real-world simulations.

---

### Step 4 — Modify a Setting

Adjust the desired value.

Example:

```text
980
↓
490
```

Result:

Objects fall more slowly.

---

### Step 5 — Run the Project

Press:

```text
F5
```

or

```text
F6
```

Observe how the change affects gameplay.

---

## Success Check

You should now have:

✓ A modified physics setting

✓ A project that reflects the change

✓ An understanding of how global settings affect gameplay

---

## Common Examples

### Low Gravity World

Example:

```text
Gravity = 300
```

Result:

Objects fall slowly.

Players can remain airborne longer.

---

### High Gravity World

Example:

```text
Gravity = 2000
```

Result:

Objects fall rapidly.

Movement feels heavier.

---

### Space Simulation

Example:

```text
Gravity = 0
```

Result:

Objects no longer fall automatically.

Additional movement systems become necessary.

---

## Common Mistakes

### Mistake 1

Changing physics settings without understanding the consequences.

Result:

Character controllers suddenly feel incorrect.

Solution:

Adjust settings gradually and test frequently.

---

### Mistake 2

Modifying gravity when the real issue is movement code.

Result:

Unexpected gameplay behavior.

Solution:

Determine whether the problem is global physics or local scripting.

---

### Mistake 3

Making dramatic changes without testing.

Example:

```text
Gravity = 980
↓
Gravity = 50
```

Result:

The game behaves very differently than expected.

Solution:

Experiment incrementally.

---

### Mistake 4

Assuming all movement uses physics.

Result:

Confusion when changes appear to have no effect.

Solution:

Remember that some systems use scripted movement rather than physics simulation.

---

## Why This Matters

Physics settings influence how players perceive a world.

Consider:

```text
Moon
Earth
Jupiter
```

All three worlds could contain identical geometry.

The difference is largely determined by the rules governing motion.

Physics settings help define those rules.

---

## Design Insight

Many beginning developers think:

> Physics is realism.

Game developers often think:

> Physics is feel.

The goal is not always realism.

The goal is often creating a satisfying experience.

For example:

* Platformers frequently use exaggerated gravity.
* Racing games often use unrealistic traction.
* Space games often ignore real orbital mechanics.

Physics settings are creative tools as much as technical settings.

---

## Professional Practice

Most professional projects establish physics settings very early.

Examples:

```text
Character Controller
↓
Jump Height
↓
Gravity
↓
Movement Feel
```

These systems influence one another.

As a result, changing global physics settings late in development can require extensive retesting.

---

## Relationship to Movement Systems

Physics settings affect many common gameplay systems.

Examples:

```text
Player Movement
Enemy Movement
Projectiles
Rigid Bodies
Jumping
Vehicles
```

Understanding the relationship between global physics and local movement code is an important development skill.

---

## Earth Gravity vs Game Gravity

An important observation:

```text
Realistic Gravity
```

and

```text
Fun Gravity
```

are not always the same thing.

Many successful games intentionally modify gravity to improve responsiveness and game feel.

The best value is often the one that produces the desired experience, not necessarily the most realistic simulation.

---

## Related Operations

* 0.2.2 Run Scene
* 0.2.3 Run Project
* 0.3.1 Assign Shape
* 0.4.0 Configure Input Mapping
* 0.4.1 Configure an Autoload

---

## Related Techniques

This operation supports the following techniques:

* Physics Simulation
* Character Controllers
* Movement Systems
* Gameplay Tuning
* World Design