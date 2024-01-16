def take_magic_damage(health, resist, amp, spell_power):
    max_dmg = spell_power * amp
    actual_dmg = max_dmg - resist
    health -= actual_dmg
    return health
