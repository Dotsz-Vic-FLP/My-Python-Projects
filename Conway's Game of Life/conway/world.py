# The 'world' string represents the game world
# A '.' is an empty cell.  A '*' is a living cell.
# Every line must have the same number of symbols

# This is a simple world to start with while getting things working
__world = """
.................
.................
.................
.................
.................
.................
.................
......*****......
......*...*......
.................
.................
.................
.................
.................
.................
.................
"""

# Here is a bigger one that allows for more interesting behaviour
# Use (and change) this one to your liking
# To use it, just name it `world` instead of `__world`
world = """
..................................................
..................................................
..................................................
........................*.........................
......................*.*.........................
............**......**............**..............
...........*...*....**............**..............
**........*.....*...**............................
**........*...*.**....*.*.........................
..........*.....*.......*.........................
...........*...*..................................
............**....................................
..................................................
..................................................
..................................................
..................................................
..................................................
..................................................
..................................................
..................................................
..................................................
..................................................
..................................................
..................................................
..................................................
..........*****...................................
..........*...*...................................
..................................................
..................................................
..................................................
..................................................
..................................................
..................................................
"""


def get_world_str():
  assert world.strip() != "", "The world string must have at least one line"

  lines = world.strip().splitlines()
  for line in lines:
    assert len(line) == len(
        lines[0]), "All lines in the world string must have the same length"

    for c in line:
      assert c in ".*", "World string may contain only . or * characters"

  return world.strip()
