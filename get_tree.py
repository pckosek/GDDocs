#!/usr/bin/env python3
import sys
from pathlib import Path

# String constants for tree drawing
# SPACE = "    "
# BRANCH = "│   "
# TEE = "├── "
# LAST = "└── "

SPACE = "    "
BRANCH = "|   "
TEE = "|-- "
LAST = "\\-- "

def build_tree(dir_path: Path, prefix: str = ""):
    """Recursively yields tree lines for a given directory."""
    try:
        # Fetch entries and sort them (directories first, then files alphabetically)
        entries = sorted(
            list(dir_path.iterdir()),
            key=lambda p: (p.is_file(), p.name.lower())
        )
    except PermissionError:
        # Handle cases where you don't have read permissions
        return

    entries_count = len(entries)
    for index, path in enumerate(entries):
        is_last = (index == entries_count - 1)
        
        # Choose the correct connector
        connector = LAST if is_last else TEE
        yield f"{prefix}{connector}{path.name}"
        
        # If it's a directory, recurse into it
        if path.is_dir():
            # Adjust the prefix for the next level deep
            next_prefix = prefix + (SPACE if is_last else BRANCH)
            yield from build_tree(path, next_prefix)

def main():
    # sys.stdout.reconfigure(encoding='utf-8')

    # Use the provided argument, or default to the current directory '.'
    target_str = sys.argv[1] if len(sys.argv) > 1 else "."
    target_path = Path(target_str)

    if not target_path.exists():
        print(f"Error: Path '{target_str}' does not exist.")
        sys.exit(1)

    # Print the root directory name
    print(target_str)
    
    # Generate and print the rest of the tree
    for line in build_tree(target_path):
        print(line)

if __name__ == "__main__":
    main()