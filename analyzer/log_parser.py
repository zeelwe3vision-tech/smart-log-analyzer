import pandas as pd
import re

def parse_logs(file_path):
    data = []

    with open(file_path, "r") as file:
        for line in file:
            parsed = parse_line(line)
            if parsed:
                data.append(parsed)

    return pd.DataFrame(data)

def parse_line(line):
    pattern = r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (\w+) (.*)'
    match = re.match(pattern, line)

    if match:
        return {
            "timestamp": match.group(1),
            "level": match.group(2),
            "message": match.group(3)
        }
    return None