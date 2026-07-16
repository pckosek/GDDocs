# Techniques

Techniques is where reusable implementation recipes live — Coyote Time, Checkpoints, Dialogue, Inventory, Moving Platforms, Patrols, and everything like them. Each page teaches one specific, named technique you can drop into a project, independent of which conceptual domain it happens to build on. Come here when you already know *what* you want to build and just need the recipe for it.

If you want to understand *why* a technique works — the physics, architecture, or presentation concept underneath it — that material lives in [Building Games](../building-games/index.md) instead. Techniques assumes you'll come back to that section when a recipe references a concept you haven't seen yet, rather than re-explaining it here.

## What you'll learn

- How to implement dozens of specific, reusable gameplay features rather than general concepts
- Which techniques form families worth reading together (like the 2D/3D coyote time pair, or the three patrol variants)
- Where a technique's underlying concept lives, when you need the deeper explanation

## Recommended prerequisites

[Editor](../editor/index.md) and at least the relevant subsection of [Building Games](../building-games/index.md) — most techniques assume you can already create a scene, attach a script, and understand the physics body or architecture pattern the technique is built on.

## Categories in this section

- [Movement & Platforming](movement-and-platforming/index.md) — jumping, dashing, moving platforms, and patrol movement.
- [Triggers & World Interaction](triggers-and-world-interaction/index.md) — checkpoints, doors, switches, and area-based triggers.
- [Inventory & Progression](inventory-and-progression/index.md) — collecting items, tracking inventory, damage, and death.
- [Dialogue & Narrative Delivery](dialogue-and-narrative-delivery/index.md) — the conversation system itself, beyond just triggering it.
- [Enemies & Combat](enemies-and-combat/index.md) — patrol, chase, investigation, combat, and boss design.
- [Tile-World Population](tile-world-population/index.md) — spawning and procedurally populating a tile-based level.

## Where to go next

[Building Games](../building-games/index.md) is where every technique's underlying concept lives — if a technique page references CharacterBody, signals, or a state machine and you want the deeper explanation, that's where to find it. [Game Design Theory](../game-design-theory/understanding-games/index.md) is a good companion once you're comfortable with the implementation side and want to reason about which techniques actually serve your game's design.

---

## Full Technique Index (searchable by tag)

Every technique page below also carries `tags` in its own front matter, so a tag-based search will find it even if you don't know which category above it's filed under. This flat list exists specifically so no technique is ever more than one click away, regardless of the category structure above.

### Movement & Platforming

- [Walking Into a Wall](movement-and-platforming/character-hits-wall.md)
- [Conveyor Belt](movement-and-platforming/conveyor-belt.md)
- [Coyote Time](movement-and-platforming/coyote-time-2d.md)
- [Coyote Time](movement-and-platforming/coyote-time.md)
- [Dash](movement-and-platforming/dash.md)
- [Detect the Ceiling](movement-and-platforming/detect-ceiling.md)
- [Detect the Floor](movement-and-platforming/detect-floor.md)
- [Double Jump](movement-and-platforming/double-jump.md)
- [Face Movement Direction](movement-and-platforming/face-movement-direction.md)
- [Crossing a Finish Line](movement-and-platforming/finish-line.md)
- [Follow the Player](movement-and-platforming/follow-the-player.md)
- [Four-Way Movement](movement-and-platforming/four-way-movement.md)
- [Jump Buffering](movement-and-platforming/jump-buffer-2d.md)
- [Jump Buffer](movement-and-platforming/jump-buffer.md)
- [Variable Jump Height](movement-and-platforming/jump-variations.md)
- [Jump](movement-and-platforming/jump.md)
- [Jumping](movement-and-platforming/jumping-2d.md)
- [Knockback](movement-and-platforming/knockback.md)
- [Detect a Ledge](movement-and-platforming/ledge-detect.md)
- [Change Animations Based on Movement](movement-and-platforming/movement-driven-animation.md)
- [Ride a Moving Platform](movement-and-platforming/moving-platform.md)
- [One-Way Platforms](movement-and-platforming/one-way-platforms.md)
- [Patrol Between Points](movement-and-platforming/patrol-between-points.md)
- [Patrol Between Walls](movement-and-platforming/patrol-between-walls.md)
- [Push a RigidBody](movement-and-platforming/push-objects.md)
- [Rotating Platform](movement-and-platforming/rotating-platform.md)
- [Slopes](movement-and-platforming/slopes-and-ramps.md)
- [NPC Stops at a Wall](movement-and-platforming/stop-at-wall.md)
- [Identify Which Side I Collided With](movement-and-platforming/which-side-collision.md)

### Triggers & World Interaction

- [Enter an Area](triggers-and-world-interaction/area-enter.md)
- [Exit an Area](triggers-and-world-interaction/area-exit.md)
- [Trigger a Checkpoint](triggers-and-world-interaction/checkpoint.md)
- [Collect an Item](triggers-and-world-interaction/collect-item.md)
- [Count Objects Inside an Area](triggers-and-world-interaction/count-objects-in-area.md)
- [Scoring a Goal](triggers-and-world-interaction/goal-trigger.md)
- [Interact](triggers-and-world-interaction/interact-with-object.md)
- [Keys & Doors](triggers-and-world-interaction/keys-and-locks.md)
- [Open a Door](triggers-and-world-interaction/open-a-door.md)
- [Play a Sound](triggers-and-world-interaction/play-sound-on-trigger.md)
- [Require Multiple Objects Inside an Area](triggers-and-world-interaction/require-multiple-triggers.md)
- [Start a Dialogue](triggers-and-world-interaction/start-a-dialogue.md)
- [Switches & Events](triggers-and-world-interaction/switches.md)
- [World Interaction](triggers-and-world-interaction/tile-based-interaction.md)

### Inventory & Progression

- [Area2D](inventory-and-progression/2d-area-trigger.md)
- [Collectibles](inventory-and-progression/collectibles.md)
- [Connecting Gameplay Systems](inventory-and-progression/connecting-collectibles-to-state.md)
- [Damage Systems](inventory-and-progression/damage.md)
- [Death & Destruction](inventory-and-progression/death-and-respawn.md)
- [Inventory](inventory-and-progression/inventory.md)
- [Quests](inventory-and-progression/quests.md)

### Dialogue & Narrative Delivery

- [Dialogue](dialogue-and-narrative-delivery/dialogue-system.md)

### Enemies & Combat

- [Boss Design](enemies-and-combat/boss-encounters.md)
- [Chase](enemies-and-combat/chase.md)
- [Combat](enemies-and-combat/combat.md)
- [Navigation](enemies-and-combat/enemy-navigation.md)
- [Investigation](enemies-and-combat/investigation.md)
- [Patrol](enemies-and-combat/patrol.md)

### Tile-World Population

- [Procedural Population](tile-world-population/populating-a-level.md)
- [Spawn Systems](tile-world-population/spawning.md)

---

**59 technique pages** across 6 categories.

A few of these form related **technique families** worth reading together rather than in isolation:

- **Jump-timing forgiveness:** [Coyote Time](movement-and-platforming/coyote-time.md) / [Coyote Time (2D)](movement-and-platforming/coyote-time-2d.md), and [Jump Buffer](movement-and-platforming/jump-buffer.md) / [Jump Buffer (2D)](movement-and-platforming/jump-buffer-2d.md).
- **Patrol variants:** [Patrol Between Points](movement-and-platforming/patrol-between-points.md), [Patrol Between Walls](movement-and-platforming/patrol-between-walls.md), and the enemy-specific [Patrol](enemies-and-combat/patrol.md).
- **The two "elevator" pages, disambiguated:** [Rotating Platform](movement-and-platforming/rotating-platform.md) and [Moving Platform](movement-and-platforming/moving-platform.md) used to share the filename `elevator.md` — they're different techniques, now named for what they actually do.
- **Dialogue, in two parts:** [Start a Dialogue](triggers-and-world-interaction/start-a-dialogue.md) covers the *trigger*; [Dialogue System](dialogue-and-narrative-delivery/dialogue-system.md) covers the *conversation system* itself.
