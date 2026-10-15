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
