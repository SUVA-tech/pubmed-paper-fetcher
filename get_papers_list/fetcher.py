from __future__ import annotations

from typing import List
import requests


BASE_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"

def search_pubmed(query: str, max_results: int = 20) -> List[str]:
    """Fetch list of PubMed IDs matching the query."""
    response = requests.get(
        f"{BASE_URL}esearch.fcgi",
        params={
            "db": "pubmed",
            "term": query,
            "retmode": "json",
            "retmax": max_results
        }
    )
    response.raise_for_status()
    return response.json()["esearchresult"]["idlist"]

def fetch_details(pubmed_ids: List[str]) -> str:
    """Fetch XML details for given PubMed IDs."""
    ids = ",".join(pubmed_ids)
    response = requests.get(
        f"{BASE_URL}efetch.fcgi",
        params={
            "db": "pubmed",
            "id": ids,
            "retmode": "xml"
        }
    )
    response.raise_for_status()
    return response.text
