can_create_guild = 0b1000
can_review_guild = 0b0100
can_delete_guild = 0b0010
can_edit_guild = 0b0001


def can_create_bits(user_permissions):
    result = user_permissions & can_create_guild
    return result


def can_review_bits(user_permissions):
    result = user_permissions & can_review_guild
    return result


def can_delete_bits(user_permissions):
    result = user_permissions & can_delete_guild
    return result


def can_edit_bits(user_permissions):
    result = user_permissions & can_edit_guild
    return result