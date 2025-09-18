import pandas as pd
import os
import csv
import json
from collections import Counter

def sportfest():
    # Path to the Excel file
    excel_path = 'Sportfest 2025.xlsx'

    # Output directory for CSV files
    output_dir = 'sportfest_csv'
    os.makedirs(output_dir, exist_ok=True)

    # Read all sheets from the Excel file
    sheets = pd.read_excel(excel_path, sheet_name=None)

    # Export each sheet to a separate CSV file
    for sheet_name, df in sheets.items():
        csv_path = os.path.join(output_dir, f"{sheet_name}.csv")
        df.to_csv(csv_path, index=False)
        print(f"Exported {sheet_name} to {csv_path}")

def count_names():
    csv_path = 'sportfest_csv/Tabelle1.csv'
    json_path = 'name_counts.json'

    name_counter = Counter()

    with open(csv_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader, None)  # Skip the first row (headers)
        for row in reader:
            for name in row:
                name = name.strip()
                # Skip empty, 'Mattis Jung', and anything that is a number
                if name and name != 'Mattis Jung':
                    try:
                        float(name)
                        continue  # skip numbers
                    except ValueError:
                        name_counter[name] += 1

            # Sort by count (descending), then by first letter of name (ascending)
            sorted_counts = dict(sorted(
                name_counter.items(),
                key=lambda item: (-item[1], item[0][0])
            ))

            with open(json_path, 'w', encoding='utf-8') as jsonfile:
                json.dump(sorted_counts, jsonfile, ensure_ascii=False, indent=2)

    print(f"Saved name counts to {json_path}")

def main():
    sportfest()
    count_names()

main()
