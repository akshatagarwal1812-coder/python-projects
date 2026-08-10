def sortlist(ls, item, path=None):
    if path is None:
        path = []
    result = []
    for index, value in enumerate(ls):
        current_path = path + [index]
        if value == item:
            result.append(current_path)
        elif isinstance(value, list):
            result.extend(sortlist(value, item, current_path))
    return result

print(sortlist([4, [4, [4, 5, 4], [7, 9, 4]]], 4))