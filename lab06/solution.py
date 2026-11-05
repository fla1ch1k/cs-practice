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
def deepest_path(paths):
    if not paths:
        return ""
    return min(paths, key=lambda p: (-p.count("/"), p))


def human_size(n_bytes):
    if n_bytes < 1024:
        return f"{n_bytes} Б"
    size = n_bytes
    for unit in ["КБ", "МБ", "ГБ", "ТБ"]:
        size = size / 1024
        if size < 1024 or unit == "ТБ":
            return f"{size:.1f} {unit}"
