def get_most_common_enemy(enemies_dict):
    if len(enemies_dict) == 0:
        return None

    max_count = 0
    for enemy in enemies_dict:
        if max_count < enemies_dict[enemy]:
            max_count = enemies_dict[enemy]
            enemy_name = enemy
    return enemy_name
