#!/usr/bin/env python3
"""Generate stub .md files for every page listed in mkdocs.yml that doesn't exist yet."""

import os

DOCS = "/home/claude/course-site/docs"

def stub(title, path, unit_context=""):
    return f"""# {title}

## 🎯 Objective

*[One sentence: what will the student implement or understand by the end of this page?]*

---

## 🏗️ The Why

*[Explain the concept. Why does this mechanic exist? What problem does it solve?]*

---

## 🛠️ Implementation

*[Step-by-step instructions. Keep this focused on ONE node or ONE script.]*

=== "GDScript"

    ```gdscript
    # TODO: add minimal working example
    ```

=== "Notes"

    ```
    # TODO: inspector view or scene tree snapshot
    ```

!!! tip "Tip"
    *[One helpful tip or common mistake to avoid.]*

---

## 🧩 Challenge

1. *[Small modification task — beginner]*
2. *[Slightly harder variation]*
3. *[Advanced: open-ended extension]*

---

## 🚀 Explore More

- *[Link to next related page]*
- Godot Docs: *[relevant docs link]*
"""

# All pages to generate (relative to docs/, title)
PAGES = [
    # Unit 1
    ("unit1/still-life/index.md", "Still Life – Overview"),
    ("unit1/still-life/01-create-scene.md", "Create a New Scene"),
    ("unit1/still-life/03-materials.md", "Apply Materials"),
    ("unit1/still-life/04-transforms.md", "Position Objects (Transform)"),
    ("unit1/still-life/05-lighting.md", "Add Lighting"),
    ("unit1/scene-transformers/index.md", "Scene Transformers – Overview"),
    ("unit1/scene-transformers/01-light-angles.md", "Change Light Angles"),
    ("unit1/scene-transformers/02-swap-materials.md", "Swap Materials"),
    ("unit1/scene-transformers/03-remix.md", "Remix a Scene"),
    ("unit1/solar-system/index.md", "Solar System – Overview"),
    ("unit1/solar-system/02-rotation.md", "Rotation with Scripts"),
    ("unit1/solar-system/03-orbits.md", "Orbital Motion"),
    ("unit1/solar-system/04-script-reuse.md", "Reusing Scripts"),
    ("unit1/solar-system/05-camera.md", "Add a Camera"),
    ("unit1/full-control/index.md", "Full Control – Overview"),
    ("unit1/full-control/01-input-actions.md", "Input Actions"),
    ("unit1/full-control/02-forward-back.md", "Forward & Backward Movement"),
    ("unit1/full-control/03-speed.md", "Variable Speed"),
    ("unit1/full-control/04-speed-boost.md", "Speed Boost"),
    ("unit1/flying-machine/index.md", "Flying Machine – Overview"),
    ("unit1/flying-machine/01-build.md", "Build Your Machine"),
    ("unit1/flying-machine/02-obstacles.md", "Animate Obstacles"),
    ("unit1/flying-machine/03-navigation.md", "Navigation Challenge"),
    # Unit 2
    ("unit2/index.md", "Unit 2 – Physics"),
    ("unit2/staircase/index.md", "The Staircase – Overview"),
    ("unit2/staircase/01-static-body.md", "StaticBody3D"),
    ("unit2/staircase/02-collision-shape.md", "CollisionShape3D"),
    ("unit2/staircase/03-character-body.md", "CharacterBody3D"),
    ("unit2/staircase/04-gravity.md", "Gravity & Movement"),
    ("unit2/staircase/05-climb.md", "Climbing the Stairs"),
    ("unit2/crossing/index.md", "The Crossing – Overview"),
    ("unit2/crossing/01-moving-platforms.md", "Moving Platforms"),
    ("unit2/crossing/02-jumping.md", "Jumping"),
    ("unit2/crossing/03-timing.md", "Timing the Jump"),
    ("unit2/summit/index.md", "The Summit – Overview"),
    ("unit2/summit/01-area3d.md", "Area3D Setup"),
    ("unit2/summit/03-hud.md", "HUD Display"),
    # Unit 3
    ("unit3/index.md", "Unit 3 – Procedural Python"),
    ("unit3/python/index.md", "Python Crash Course – Overview"),
    ("unit3/python/01-variables.md", "Variables & Types"),
    ("unit3/python/02-conditionals.md", "Conditionals"),
    ("unit3/python/03-loops.md", "Loops"),
    ("unit3/python/04-functions.md", "Functions"),
    ("unit3/python/05-lists.md", "Lists"),
    ("unit3/python/06-dicts.md", "Dictionaries"),
    ("unit3/python/07-2d-lists.md", "2D Lists"),
    ("unit3/gridworld/index.md", "Gridworld – Overview"),
    ("unit3/gridworld/02-neighbors.md", "Mapping Neighbors"),
    ("unit3/gridworld/03-coordinates.md", "Grid Coordinates"),
    ("unit3/pil/index.md", "PIL – Overview"),
    ("unit3/pil/01-install.md", "Install & Import PIL"),
    ("unit3/pil/02-create.md", "Create an Image"),
    ("unit3/pil/03-pixels.md", "Draw Pixels"),
    ("unit3/pil/04-export.md", "Export to File"),
    ("unit3/prim/index.md", "Prim's Maze – Overview"),
    ("unit3/prim/01-grid.md", "Maze as a Grid"),
    ("unit3/prim/02-algorithm.md", "Prim's Algorithm"),
    ("unit3/prim/03-carve.md", "Carve the Maze"),
    ("unit3/prim/04-export.md", "Export to Image"),
    ("unit3/cellular-automata/index.md", "Cellular Automata – Overview"),
    ("unit3/cellular-automata/01-rules.md", "Rules of Life"),
    ("unit3/cellular-automata/02-count-neighbors.md", "Count Neighbors"),
    ("unit3/cellular-automata/03-simulate.md", "Run the Simulation"),
    ("unit3/cellular-automata/04-cave.md", "Generate a Cave"),
    # Unit 4
    ("unit4/index.md", "Unit 4 – 2D Platformer"),
    ("unit4/movement/index.md", "Movement – Overview"),
    ("unit4/movement/01-tilemap.md", "TileMapLayer"),
    ("unit4/movement/02-charbody2d.md", "CharacterBody2D"),
    ("unit4/movement/03-left-right.md", "Left & Right Movement"),
    ("unit4/movement/04-gravity.md", "Gravity"),
    ("unit4/movement/05-jumping.md", "Jumping"),
    ("unit4/collectibles/index.md", "Collectibles & HUD – Overview"),
    ("unit4/collectibles/01-area2d.md", "Area2D Pickup"),
    ("unit4/collectibles/02-signals.md", "Signals"),
    ("unit4/collectibles/03-score.md", "Score Display"),
    ("unit4/hazards/index.md", "Hazards & States – Overview"),
    ("unit4/hazards/01-gamemanager.md", "GameManager Node"),
    ("unit4/hazards/02-start-screen.md", "Start Screen"),
    ("unit4/hazards/03-fail.md", "Fail Conditions"),
    ("unit4/hazards/04-restart.md", "Restart Logic"),
    ("unit4/enemies/index.md", "Enemies – Overview"),
    ("unit4/enemies/01-enemy-body.md", "Enemy CharacterBody2D"),
    ("unit4/enemies/02-patrol.md", "Patrol Behavior"),
    ("unit4/enemies/03-groups.md", "Groups"),
    ("unit4/enemies/04-interaction.md", "Player Interaction"),
    ("unit4/platformer/index.md", "2D Platformer – Overview"),
    ("unit4/platformer/01-design.md", "Design Your Level"),
    ("unit4/platformer/02-win.md", "Win Condition"),
    ("unit4/platformer/03-polish.md", "Polish & Submit"),
]

created = 0
skipped = 0
for rel_path, title in PAGES:
    full_path = os.path.join(DOCS, rel_path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    if os.path.exists(full_path):
        skipped += 1
        continue
    with open(full_path, "w") as f:
        f.write(stub(title, rel_path))
    created += 1

print(f"Created {created} stub files, skipped {skipped} existing files.")
