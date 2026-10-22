LEVELS = ("DEBUG", "INFO", "WARNING", "ERROR")


def parse_event(line):
    parts = line.strip().split(maxsplit=2)
    if len(parts) < 3:
        raise ValueError("в строке меньше трёх частей")
    time, level, message = parts
    if level not in LEVELS:
        raise ValueError("неизвестный уровень")
    return {"time": time, "level": level, "message": message}


def count_levels(lines):
    counts = {}
    for line in lines:
        if not line.strip():
            continue
        try:
            key = parse_event(line)["level"]
        except ValueError:
            key = "BROKEN"
        counts[key] = counts.get(key, 0) + 1
    return counts


def top_errors(lines, n):
    freq = {}
    for line in lines:
        if not line.strip():
            continue
        try:
            event = parse_event(line)
        except ValueError:
            continue
        if event["level"] == "ERROR":
            freq[event["message"]] = freq.get(event["message"], 0) + 1
    pairs = [[message, count] for message, count in freq.items()]
    pairs.sort(key=lambda p: (-p[1], p[0]))
    return pairs[:n]


def format_report(counts, errors):
    text = "Отчёт по журналу\n\n"
    for level in sorted(counts):
        text += f"{level}: {counts[level]}\n"
    text += "\nЧастые ошибки:\n"
    for message, count in errors:
        text += f"- {message} — {count}\n"
    return text
