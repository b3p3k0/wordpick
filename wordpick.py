#!/usr/bin/env python3
"""
generate_words.py — download English word list and filter combinations
(letters chosen one from each of four sets in order)
"""

import itertools
import requests
import sys

# Four letter sets (in order)
set1 = list("BLPWSTDMRF")
set2 = list("YUAIOLEHR")
set3 = list("RMTNSKOALE")
set4 = list("YLDGKMSTEP")

# URL for words_alpha.txt in dwyl/english-words repo (letters only)
WORDLIST_URL = "https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt"

def download_wordlist(url=WORDLIST_URL):
    """Download word list from URL; return set of lower-case words."""
    print(f"Downloading word list from {url} …", file=sys.stderr)
    resp = requests.get(url, timeout=30)
    resp.raise_for_status()
    words = set(line.strip().lower() for line in resp.text.splitlines() if line.strip())
    print(f"Loaded {len(words):,} words.", file=sys.stderr)
    return words

def filter_combinations(words_set):
    """Generate combinations picking one letter from each set in order and return matches."""
    matches = []
    for a, b, c, d in itertools.product(set1, set2, set3, set4):
        candidate = (a + b + c + d).lower()
        if candidate in words_set:
            matches.append(candidate)
    return sorted(set(matches))

def main():
    words = download_wordlist()
    results = filter_combinations(words)
    print(f"Found {len(results)} matching words:")
    for w in results:
        print(w)

if __name__ == "__main__":
    main()

