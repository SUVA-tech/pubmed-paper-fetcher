from __future__ import annotations

import argparse
from typing import NoReturn

from get_papers_list.fetcher import search_pubmed, fetch_details
from get_papers_list.filters import extract_paper_data
from get_papers_list.writer import write_to_csv


def main() -> NoReturn:
    parser = argparse.ArgumentParser(
        description="Fetch PubMed papers with non-academic authors from biotech/pharma companies."
    )
    parser.add_argument("query", type=str, help="Search query for PubMed")
    parser.add_argument("-f", "--file", type=str, help="Output CSV filename")
    parser.add_argument("-d", "--debug", action="store_true", help="Print debug info")
    
    args = parser.parse_args()

    if args.debug:
        print(f"🔍 Query: {args.query}")
        if args.file:
            print(f"📄 Output file: {args.file}")

    try:
        ids = search_pubmed(args.query)
        if args.debug:
            print(f"🔎 Found {len(ids)} PubMed IDs")

        xml_data = fetch_details(ids)
        results = extract_paper_data(xml_data)

        if not results:
            print("⚠️ No non-academic authors found.")
        else:
            write_to_csv(results, args.file)

    except Exception as e:
        print(f"❌ Error: {e}")


if __name__ == "__main__":
    main()
