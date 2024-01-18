def body_parts(num_heads, num_arms, num_fingers):
    return int(num_heads, 2), int(num_arms, 2), int(num_fingers, 2)

print(body_parts("101", "110", "001"))
