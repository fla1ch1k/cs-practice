import json


def csv_to_records(text):
    lines = [line for line in text.splitlines() if line.strip() != ""]
    if not lines:
        return []
    header = [name.strip() for name in lines[0].split(",")]
    records = []
    for line in lines[1:]:
        values = [value.strip() for value in line.split(",")]
        records.append(dict(zip(header, values)))
    return records
def convert_value(text):
    low = text.lower()
    if low in ("true", "yes"):
        return True
    if low in ("false", "no"):
        return False
    try:
        return int(text)
    except ValueError:
        pass
    try:
        return float(text.replace(",", "."))
    except ValueError:
        pass
    return text


def parse_settings(lines):
    result = {}
    current_list = None
    for line in lines:
        line = line.split("#")[0].strip()
        if line == "":
            continue
        if line.startswith("-"):
            if current_list is not None:
                current_list.append(convert_value(line[1:].strip()))
            continue
        if ":" in line:
            key, value = line.split(":", 1)
            key = key.strip()
            value = value.strip()
            if value == "":
                current_list = []
                result[key] = current_list
            else:
                current_list = None
                result[key] = convert_value(value)
    return result

def merge_by_key(rows, extra, key="id"):
    result = []
    for row in rows:
        merged = {}
        info = extra.get(row.get(key))
        if info:
            merged.update(info)
        merged.update(row)
        result.append(merged)
    return result


def records_to_json(records):
    return json.dumps(records, indent=2, sort_keys=True, ensure_ascii=False)
