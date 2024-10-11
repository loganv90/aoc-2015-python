def get_spells() -> dict[str, tuple[int, int]]:
    return {
        # name, cost (mana), effect (turns)
        "Magic Missile": (53, 1),
        "Drain": (73, 1),
        "Shield": (113, 6),
        "Poison": (173, 6),
        "Recharge": (229, 5)
    }

def dfs(boss_health: int,
        boss_damage: int,

        player_health: int,
        player_mana: int,
        player_turn: bool,

        spells: dict[str, tuple[int, int]],
        cast_spells: dict[str, int],

        mana_spent: int,
        min_mana: int,
        level: int,
        hard: bool) -> int:
    # spaces = " " * level
    # print(f"{spaces}Boss: {boss_health}, Player: {player_health}, Mana: {mana_spent}, Min: {min_mana}")

    if hard and player_turn:
        player_health -= 1
        if player_health <= 0:
            return -1

    player_armor = 0

    to_remove = []
    for spell_name in cast_spells:
        if spell_name == "Shield":
            player_armor = 7
        elif spell_name == "Poison":
            boss_health -= 3
        elif spell_name == "Recharge":
            player_mana += 101
        elif spell_name == "Drain":
            player_health += 2
            boss_health -= 2
        elif spell_name == "Magic Missile":
            boss_health -= 4
        else:
            raise ValueError("Unknown effect")

        cast_spells[spell_name] -= 1
        effect = cast_spells[spell_name]
        if effect <= 0:
            to_remove.append(spell_name)
            continue
    for spell_name in to_remove:
        del cast_spells[spell_name]

    if boss_health <= 0:
        return mana_spent

    if player_turn:
        for spell_name in spells:
            if spell_name in cast_spells:
                continue

            cost, effect = spells[spell_name]
            if player_mana < cost:
                continue

            new_mana_spent = mana_spent + cost
            if new_mana_spent >= min_mana:
                continue

            new_cast_spells = cast_spells.copy()
            new_cast_spells[spell_name] = effect
            new_player_mana = player_mana - cost

            mana = dfs(boss_health,
                       boss_damage,

                       player_health,
                       new_player_mana,
                       False,

                       spells,
                       new_cast_spells,

                       new_mana_spent,
                       min_mana,
                       level + 1,
                       hard)
            if mana < 0:
                continue
            min_mana = min(min_mana, mana)
        return min_mana
    else:
        player_health -= max(1, boss_damage - player_armor)
        if player_health <= 0:
            return -1

        mana = dfs(boss_health,
                   boss_damage,

                   player_health,
                   player_mana,
                   True,

                   spells,
                   cast_spells,

                   mana_spent,
                   min_mana,
                   level + 1,
                   hard)
        if mana < 0:
            return -1
        return min(min_mana, mana)


def part1(boss_health: int,
          boss_damage: int,
          player_health: int,
          player_mana: int) -> None:
    spells = get_spells()

    mana = dfs(boss_health,
               boss_damage,

               player_health,
               player_mana,
               True,

               spells,
               {},

               0,
               1000000,
               0,
               False)

    print("Solution Part 1: ", mana)

def part2(boss_health: int,
          boss_damage: int,
          player_health: int,
          player_mana: int) -> None:
    spells = get_spells()

    mana = dfs(boss_health,
               boss_damage,

               player_health,
               player_mana,
               True,

               spells,
               {},

               0,
               1000000,
               0,
               True)

    print("Solution Part 2: ", mana)

if __name__ == "__main__":
    part1(13, 8, 10, 250)
    part1(51, 9, 50, 500)
    part2(51, 9, 50, 500)

