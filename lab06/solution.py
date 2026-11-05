def count_by_extension(paths):
    result = {}
    for path in paths:
        name = path.split("/")[-1]
        if "." in name:
            ext = name.split(".")[-1].lower()
        else:
            ext = ""
        if ext in result:
            result[ext] += 1
        else:
            result[ext] = 1
    return result
