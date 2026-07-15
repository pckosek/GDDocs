# 5.6.1 Sound as Data

## Classification

**Type:** Design / Engineering Guide

**Category:** Digital Audio

**Difficulty:** Beginner

---

# Design Problem

When you hear a sound...

...you hear music.

Or speech.

Or footsteps.

Or an explosion.

A computer does not.

The computer hears none of these things.

Instead, it stores:

- numbers
- time
- amplitudes

Nothing more.

Every digital sound is simply a representation of information changing over time.

Understanding this idea changes the way we think about sound.

Instead of asking:

> **How do I play a sound?**

we begin asking:

> **What information describes the sound?**

---

# Why This Matters

Digital audio appears throughout game development.

Examples include:

- music
- footsteps
- explosions
- ambient sound
- user interface effects
- dialogue
- procedural sound effects

Although these sounds feel very different...

...they all share the same underlying representation.

They are simply collections of numerical values arranged through time.

Once we understand that representation...

...we can begin creating sounds ourselves.

---

# Mental Model

Earlier in this unit we represented an image as many pixels.

```text
Pixel

Pixel

Pixel

Pixel
```

Digital audio works almost exactly the same way.

Instead of pixels arranged through space...

...audio stores **samples** arranged through time.

```text
Sample

Sample

Sample

Sample

Sample
```

An image answers:

> What value belongs at this location?

A sound answers:

> What value belongs at this moment?

The representation changes.

The underlying idea does not.

---

# Representation

Imagine one second of sound.

Rather than storing one continuous waveform...

...the computer stores many individual measurements.

```text
0.18

0.22

0.19

0.10

...

```

Individually, these numbers mean very little.

Together...

they become a sound.

The computer never stores "music."

It stores many individual samples.

---

# Design Principle

## Sounds are representations before they are experiences.

The computer does not understand melodies.

It does not understand instruments.

It understands numerical values.

Our ears interpret those values as sound.

Separating representation from perception is one of the most important ideas in computational media.

---

# Comparing Media

Notice the remarkable similarity.

| Medium | Smallest Unit |
|----------|---------------|
| Image | Pixel |
| Sound | Sample |
| Gridworld | Cell |
| Tile Map | Tile |

Every computational medium is built from many simple units.

Complex artifacts emerge from the relationships between those units.

---

# Practical Observation

Beginning programmers often think about recording sounds.

Computational audio begins somewhere different.

Instead of recording...

...we generate the samples ourselves.

Later in this unit we'll build:

- tones
- chords
- fades
- noise
- sound effects

Not by editing recordings...

...but by generating numerical representations directly.

---

# Common Misconceptions

### "A sound file stores sound."

Not exactly.

It stores numerical values.

The sound is produced later when speakers convert those values into physical vibrations.

---

### "Audio is completely different from images."

Structurally, they are surprisingly similar.

Images store values across space.

Audio stores values across time.

Both are representations.

---

### "Computers understand music."

No.

Computers manipulate numerical representations.

Meaning emerges when people interpret those representations.

---

### "Digital audio requires microphones."

Not at all.

Many sounds are synthesized entirely through computation.

No recording is required.

---

# Reflection

Earlier we discovered that images are collections of pixels.

Now we've discovered that sounds are collections of samples.

How are these ideas similar?

How are they different?

Now ask yourself:

Is the computer storing a sound...

...or a representation that eventually becomes sound?

---

# Looking Back

Earlier in this unit we explored computational images.

Now we've discovered that digital audio follows the same philosophy.

Images are representations across space.

Sounds are representations across time.

The medium has changed.

The computational thinking has not.

---

# Looking Ahead

Now that we understand what digital audio really is...

...the next question becomes:

> **What exactly is one sample, and what information does it store?**