# get-papers-list

[![Python Version](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)

Fetch PubMed research papers with non-academic authors affiliated with pharmaceutical or biotech companies.

---

## 🚀 Overview

This Python command-line tool fetches research papers from the PubMed API based on a user-provided search query. It filters results to include only papers where **at least one author is affiliated with a non-academic pharmaceutical or biotech company**, using heuristic keyword matching on author affiliations.

The results are output as a CSV file or printed to the console, including key metadata such as PubMed ID, paper title, publication date, company affiliations, and corresponding author email addresses.

---

## ⚙️ Features

- Full support for PubMed's rich query syntax.
- Identification of non-academic authors using affiliation heuristics.
- Outputs clean, well-formatted CSV files.
- CLI options for debug info and output filename specification.
- Modular code with strict type annotations.
- Dependency management and packaging via Poetry.

---

## 📦 Installation

Make sure you have **Python 3.10+** installed.  
Then clone the repo and install dependencies:

```bash
git clone https://github.com/yourusername/pubmed-paper-fetcher.git
cd pubmed-paper-fetcher
poetry install
```

---

## 🛠 Usage

Run the CLI tool with:

```bash
poetry run get-papers-list "your search query" [options]
```

### Arguments

| Argument  | Description                            |
| --------- | ------------------------------------ |
| `query`   | Required. PubMed search query string.|

### Options

| Flag          | Description                             |
| ------------- | ------------------------------------- |
| `-f`, `--file`| Output CSV filename. If omitted, prints to console.|
| `-d`, `--debug`| Enable debug output during execution.|
| `-h`, `--help`| Show usage instructions.               |

### Example

```bash
poetry run get-papers-list "cancer immunotherapy" -f results.csv -d
```

---

## 🧠 How It Works

1. Uses PubMed **`esearch.fcgi`** API to find paper IDs matching your query.
2. Fetches detailed XML metadata using **`efetch.fcgi`**.
3. Parses XML to extract paper info, authors, affiliations, and emails.
4. Applies heuristics to detect **non-academic pharmaceutical/biotech affiliations**:
   - Keywords like `"pharma"`, `"biotech"`, `"labs"`, `"inc"`, `"therapeutics"`.
   - Filters out academic institutions with keywords like `"university"`, `"institute"`.
5. Outputs data to CSV or prints to console.

---

## 🛠 Development & Packaging

- Written in Python with full **type hints** (`mypy` compatible).
- Uses **requests** for HTTP calls.
- Packaged and dependency-managed using **Poetry**.
- Modularized with separate files for fetching, filtering, writing, and CLI.
- Exception handling for network issues and missing data.

---

## 🧪 Tools & Resources Used

- [Python 3.10+](https://www.python.org/)
- [Poetry](https://python-poetry.org/)
- [Requests](https://docs.python-requests.org/en/latest/)
- [NCBI E-utilities API](https://www.ncbi.nlm.nih.gov/books/NBK25501/)
- Large Language Models (e.g., ChatGPT) for code generation and design assistance

---

## 📂 Output Format

The output CSV contains the following columns:

| Column                 | Description                                   |
|------------------------|-----------------------------------------------|
| PubmedID               | Unique PubMed identifier for the paper        |
| Title                  | Title of the research paper                    |
| Publication Date       | Date of publication (year or medline date)    |
| Non-academic Author(s) | Names of authors with non-academic affiliations|
| Company Affiliation(s) | Names of pharma/biotech companies from affiliation|
| Corresponding Author Email | Email of the corresponding author (if found) |

---

## 📺 Demo Video

A short demo video is provided (or to be submitted) demonstrating:

- Running the CLI tool with example queries.
- Using debug mode.
- Showing CSV output content.
- Brief explanation of heuristics and usage.

---

## 🧹 Notes & Future Improvements

- Add caching & rate limiting for large queries.
- Improve heuristic accuracy with ML-based affiliation detection.
- Support for exporting JSON or Excel formats.
- Unit and integration tests for complete coverage.
- Publish package to Test PyPI / PyPI for easy installation.

---

## 📄 License

MIT License — see [LICENSE](LICENSE) file.

---

## 📞 Contact

Created by Suvathy Arul  
Email: your.email@example.com  
GitHub: [yourusername](https://github.com/yourusername)

---

Thank you for using **get-papers-list**!  
Feel free to contribute or raise issues on GitHub.