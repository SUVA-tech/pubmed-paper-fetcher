from __future__ import annotations

import csv
from typing import List, Dict, Optional


def write_to_csv(data: List[Dict], filename: Optional[str] = None) -> None:
    """Write the extracted paper data to CSV or print to console if no filename."""
    fieldnames = [
        "PubmedID",
        "Title",
        "Publication Date",
        "Non-academic Author(s)",
        "Company Affiliation(s)",
        "Corresponding Author Email"
    ]

    if filename:
        with open(filename, mode="w", encoding="utf-8", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
        print(f"\n✅ Results written to {filename}")
    else:
        print("\n--- PubMed Papers with Non-Academic Authors ---\n")
        writer = csv.DictWriter(
            open("CON", "w", encoding="utf-8", newline=""),
            fieldnames=fieldnames
        )
        writer.writeheader()
        writer.writerows(data)
