# 5.6.2 Samples

## Classification

**Type:** Design / Engineering Guide

**Category:** Digital Audio

**Difficulty:** Beginner

---

# Design Problem

If a digital sound is a collection of information...

...what exactly is being stored?

Suppose we pause a sound at one exact instant.

At that precise moment, the computer stores one numerical value.

That value is called a **sample**.

Every digital sound is built from many individual samples.

Understanding samples means understanding how computers represent sound.

---

# Why This Matters

Samples are one of the most fundamental representations in digital audio.

Examples include:

- music
- speech
- footsteps
- explosions
- ambient sound
- procedural sound effects

Although these sounds feel very different...

...they are all collections of samples.

The only difference is the values those samples contain.

---

# Mental Model

Think about a flipbook.

Each page captures one moment.

Viewed individually...

...each page is just a picture.

Viewed together...

...they become animation.

Digital audio works similarly.

```text
Sound

↓

Samples

↓

Values
```

Each sample stores the sound at one instant in time.

Together...

they become a continuous listening experience.

---

# Representation

Imagine a very short sound.

Instead of one continuous waveform...

the computer stores:

```text
0.00

0.18

0.42

0.61

0.57

0.31

0.02

...
```

Each value represents one instant.

No single sample sounds interesting.

The sound emerges from the relationship between many neighboring samples.

---

# Design Principle

## Complex sounds emerge from many simple samples.

A single sample tells us almost nothing.

Thousands of neighboring samples together describe pitch, loudness, rhythm, and timbre.

Like pixels in an image...

the pattern matters more than the individual value.

---

# Comparing Media

Notice the similarity.

| Medium | Smallest Unit | Organized Across |
|----------|---------------|-----------------|
| Image | Pixel | Space |
| Sound | Sample | Time |
| Gridworld | Cell | Space |
| Tile Map | Tile | Space |

Although the media are different...

they are all built from many small units arranged within some larger structure.

---

# Practical Observation

Beginning programmers often think of a sound as one object.

Computers think differently.

They see:

```text
Sample

Sample

Sample

Sample

...
```

Everything we hear is reconstructed from those individual values.

Later in this unit we'll generate those values ourselves rather than recording them.

---

# Common Misconceptions

### "One sample is one sound."

No.

One sample represents one instant.

A complete sound requires many samples working together.

---

### "Samples store musical notes."

No.

Samples store numerical amplitudes.

Notes emerge from patterns across many samples.

---

### "Samples know about one another."

No.

Each sample stores only its own value.

Relationships between neighboring samples create recognizable sounds.

---

### "Audio is continuous inside the computer."

Not exactly.

The computer stores many individual samples.

The illusion of continuity emerges because those samples occur very rapidly.

---

# Reflection

Suppose one sample stores:

```text
0.25
```

Can you hear that sample by itself?

Probably not.

Now imagine forty-four thousand neighboring samples.

What has changed?

Now ask yourself:

Is a sound really one thing...

...or is it a pattern formed by many moments?

---

# Looking Back

Earlier we discovered that an image is built from pixels.

Now we've discovered that sound is built from samples.

The pattern is becoming familiar.

Large computational artifacts emerge from many simple components.

The representation changes.

The underlying computational idea remains remarkably similar.

---

# Looking Ahead

Every sample stores one numerical value.

The next question becomes:

> **What do those numbers actually represent, and how do they become audible sound?**