def set_inline_spaces(a, b, c, d):
    biggest_len = 0
    items = [a, b, c, d]

    for i in items:
        if i > biggest_len:
            biggest_len = i

    req_spaces = [biggest_len - a, biggest_len - b, biggest_len - c, biggest_len - d]
    space_set = []

    for item in req_spaces:
        space_set.append(' ' * item)

    return space_set
