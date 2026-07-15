# 6.6.3 Camera Limits

## Classification

**Type:** Engineering Technique

**Category:** World Presentation

**Difficulty:** Beginner

**Estimated Time:** 15–20 minutes

---

# Design Problem

Suppose your platformer level is only twenty screens wide.

The player reaches the edge.

Should the camera continue moving?

If it does...

...the player begins seeing empty space outside the world.

Although the gameplay is still correct...

the illusion of the world is broken.

The camera needs to understand where the world ends.

Godot provides **Camera Limits** for exactly this purpose.

---

# Why This Matters

Camera Limits define the boundaries of the visible world.

Instead of allowing the camera to move infinitely...

...they restrict it to a meaningful area.

This prevents players from seeing:

- empty space
- unfinished regions
- objects outside the level

The camera remains focused on the playable world.

---

# Starter Workflow

Select your:

```text
Camera2D
```

Open the:

```text
Limit
```

section.

Configure:

```text
Left

Top

Right

Bottom
```

These values define the furthest positions the camera may travel.

As the player approaches the edge of the level...

the camera stops.

The player continues moving normally.

---

# Dissecting the System

Notice what changes.

Without limits:

```text
Player

↓

Camera

↓

Outside World
```

With limits:

```text
Player

↓

Camera

↓

World Edge

↓

Stop
```

The camera respects the boundaries of the level.

The world feels complete.

---

# Mental Model

Think about watching a stage performance.

The audience sees only the stage.

They do not see:

- backstage
- lighting equipment
- storage areas

The camera performs a similar role.

It frames only the part of the world intended for the player.

---

# Design Principle

## Present only the playable world.

The player should remain focused on meaningful gameplay.

Camera Limits prevent accidental distractions and preserve the illusion that the world extends naturally to its edges.

Good presentation often comes from deciding what **not** to show.

---

# Practical Observation

Many students configure the player correctly...

...but forget to configure the camera.

The result is often:

```text
Grey Background

↓

Beyond Level
```

The movement code is perfectly correct.

The presentation simply lacks boundaries.

Whenever a camera appears to move "too far," Camera Limits are one of the first settings worth checking.

---

# Common Misconceptions

### "Camera Limits stop the player."

No.

They stop the camera.

The player continues moving normally.

---

### "The camera should always stay centred."

Not at the edge of a level.

Once a camera reaches a limit...

the player naturally moves away from the centre of the screen.

This is expected behavior.

---

### "Limits change the size of the world."

No.

They change only the area the camera is allowed to display.

The world itself remains unchanged.

---

### "Every game needs camera limits."

Many large scrolling games do.

Some games with infinite or procedurally generated worlds may intentionally avoid fixed limits.

The appropriate choice depends on the design of the game.

---

# Reflection

Imagine the following games.

Would Camera Limits be useful?

| Game | Camera Limits? |
|------|----------------|
| Platformer | |
| Infinite Endless Runner | |
| Procedurally Generated World | |
| One-Screen Puzzle Game | |
| Zelda-Style Dungeon | |

Now ask yourself:

What should the player never be allowed to see?

---

# Looking Back

Earlier we learned how the camera follows the player.

Now we've discovered that following has limits.

The camera is not responsible for showing everything.

It is responsible for showing the part of the world that creates the best player experience.

Carefully chosen limits help maintain the illusion that the game world is complete.

---

# Looking Ahead

So far, our world has been completely flat.

Many games, however, create the illusion of depth by allowing different layers of the world to move at different speeds.

The next lesson explores one of the oldest and most effective visual techniques in 2D games:

> **Parallax**