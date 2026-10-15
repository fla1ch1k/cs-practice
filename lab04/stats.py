def parse_record(line: str) -> dict:
    parts = line.split(";")
    if len(parts) != 3:
        raise ValueError(f"Ожидалось 3 поля, получено {len(parts)}: {line!r}")

    city = parts[0].strip()
    temp_text = parts[1].strip()
    date = parts[2].strip()

    if city == "" or date == "":
        raise ValueError(f"Пустой город или дата: {line!r}")

    try:
        temperature = float(temp_text)
    except ValueError:
        raise ValueError(f"Температура не число: {temp_text!r}")

    return {"city": city, "temperature": temperature, "date": date}
def read_valid(lines: list[str]) -> list[dict]:
    records = []
    for line in lines:
        if line.strip() == "":
            continue # пустые строки пропускаем молча
        try:
            records.append(parse_record(line))
        except ValueError:
            continue # негодную строку пропускаем, программа не падает
    return records
def average_by_city(records: list[dict]) -> dict:
    total = {}
    count = {}
    for rec in records:
        city = rec["city"]
        total[city] = total.get(city, 0) + rec["temperature"]
        count[city] = count.get(city, 0) + 1
    return {city: round(total[city] / count[city], 1) for city in total}


def warmest_city(records: list[dict]) -> str:
    averages = average_by_city(records)
    # сортируем
    best = sorted(averages, key=lambda city: (-averages[city], city))
    return best[0]
