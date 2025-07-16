from __future__ import annotations

from typing import List, Tuple, Optional
import xml.etree.ElementTree as ET
import re


# Heuristics for non-academic affiliation detection
NON_ACADEMIC_KEYWORDS = [
    "pharma", "biotech", "inc", "ltd", "llc", "corporation", "corp",
    "gmbh", "company", "therapeutics", "laboratories", "labs"
]

ACADEMIC_KEYWORDS = [
    "university", "college", "school", "institute", "hospital",
    "faculty", "department", "centre", "center"
]

def is_non_academic(affiliation: str) -> bool:
    """Check if an affiliation seems non-academic based on heuristics."""
    affil_lower = affiliation.lower()
    return (
        any(word in affil_lower for word in NON_ACADEMIC_KEYWORDS) and
        not any(word in affil_lower for word in ACADEMIC_KEYWORDS)
    )

def extract_paper_data(xml_data: str) -> List[Dict[str, str]]:

    """Extract paper info including non-academic authors from XML."""
    root = ET.fromstring(xml_data)
    papers = []

    for article in root.findall(".//PubmedArticle"):
        pmid = article.findtext(".//PMID")
        title = article.findtext(".//ArticleTitle")
        pub_date_elem = article.find(".//PubDate")
        pub_date = (
            pub_date_elem.findtext("Year") or
            pub_date_elem.findtext("MedlineDate") or
            "Unknown"
        )

        authors = []
        companies = []
        email = None

        for author in article.findall(".//Author"):
            affiliation_info = author.find(".//AffiliationInfo")
            if affiliation_info is not None:
                affil_text = affiliation_info.findtext("Affiliation", default="")
                if is_non_academic(affil_text):
                    last = author.findtext("LastName", "")
                    fore = author.findtext("ForeName", "")
                    full_name = f"{fore} {last}".strip()
                    authors.append(full_name)
                    companies.append(affil_text)

                    # Try to extract email
                    match = re.search(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", affil_text)
                    if match and not email:
                        email = match.group(0)

        if authors:
            papers.append({
                "PubmedID": pmid,
                "Title": title,
                "Publication Date": pub_date,
                "Non-academic Author(s)": "; ".join(authors),
                "Company Affiliation(s)": "; ".join(companies),
                "Corresponding Author Email": email or "Not found"
            })

    return papers
