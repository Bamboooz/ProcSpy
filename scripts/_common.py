def set_inline_spaces(a, b, c=None, d=None):
    biggest_len = 0
    items = [a, b, c, d]
    format_items = []
    req_spaces = []
    space_set = []

    for i in items:
        if i is not None:
            format_items.append(i)

    for i in format_items:
        if i > biggest_len:
            biggest_len = i

    for i in format_items:
        space_set.append((biggest_len - i) * ' ')

    for item in req_spaces:
        space_set.append(' ' * item)

    return space_set
