def count_turns(defender_health: int, defender_armor: int, attacker_damage: int) -> int:
    turns = 0
    while defender_health > 0:
        defender_health -= max(1, attacker_damage - defender_armor)
        turns += 1
    return turns

def get_weapons() -> list:
    return [
        ("Dagger", 8, 4, 0),
        ("Shortsword", 10, 5, 0),
        ("Warhammer", 25, 6, 0),
        ("Longsword", 40, 7, 0),
        ("Greataxe", 74, 8, 0)
    ]

def get_armors() -> list:
    return [
        ("None", 0, 0, 0),
        ("Leather", 13, 0, 1),
        ("Chainmail", 31, 0, 2),
        ("Splintmail", 53, 0, 3),
        ("Bandedmail", 75, 0, 4),
        ("Platemail", 102, 0, 5)
    ]

def get_rings() -> list:
    return [
        ("None", 0, 0, 0),
        ("Damage +1", 25, 1, 0),
        ("Damage +2", 50, 2, 0),
        ("Damage +3", 100, 3, 0),
        ("Defense +1", 20, 0, 1),
        ("Defense +2", 40, 0, 2),
        ("Defense +3", 80, 0, 3)
    ]

def part1(boss_health: int,
          boss_damage: int,
          boss_armor: int,
          player_health: int,
          player_damage: int,
          player_armor: int) -> None:
    weapons = get_weapons()
    armors = get_armors()
    rings = get_rings()

    ring_combos = [("", 0, 0, 0)]
    for i in range(0, len(rings)):
        for j in range(i + 1, len(rings)):
            ring_combos.append(("", rings[i][1] + rings[j][1], rings[i][2] + rings[j][2], rings[i][3] + rings[j][3]))

    g_gold = 1000000
    for weapon in weapons:
        for armor in armors:
            for ring_combo in ring_combos:
                player_gold = weapon[1] + armor[1] + ring_combo[1]
                player_damage = weapon[2] + armor[2] + ring_combo[2]
                player_armor = weapon[3] + armor[3] + ring_combo[3]

                if count_turns(boss_health, boss_armor, player_damage) <= count_turns(player_health, player_armor, boss_damage):
                    g_gold = min(g_gold, player_gold)

    print("Solution Part 1: ", g_gold)

def part2(boss_health: int,
          boss_damage: int,
          boss_armor: int,
          player_health: int,
          player_damage: int,
          player_armor: int) -> None:
    weapons = get_weapons()
    armors = get_armors()
    rings = get_rings()

    ring_combos = [("", 0, 0, 0)]
    for i in range(0, len(rings)):
        for j in range(i + 1, len(rings)):
            ring_combos.append(("", rings[i][1] + rings[j][1], rings[i][2] + rings[j][2], rings[i][3] + rings[j][3]))

    g_gold = 0
    for weapon in weapons:
        for armor in armors:
            for ring_combo in ring_combos:
                player_gold = weapon[1] + armor[1] + ring_combo[1]
                player_damage = weapon[2] + armor[2] + ring_combo[2]
                player_armor = weapon[3] + armor[3] + ring_combo[3]

                if count_turns(boss_health, boss_armor, player_damage) > count_turns(player_health, player_armor, boss_damage):
                    g_gold = max(g_gold, player_gold)

    print("Solution Part 2: ", g_gold)

if __name__ == "__main__":
    part1(109, 8, 2, 100, 0, 0)
    part2(109, 8, 2, 100, 0, 0)

