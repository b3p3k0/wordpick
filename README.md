# wordpick

A lightweight command-line utility that:  
1. Downloads a large English word list from GitHub.  
2. Takes four predefined sets of letters.  
3. Generates all 4-letter words by choosing exactly one letter from each set (in order).  
4. Prints only the valid English words found.

This project was inspired by a user’s post on r/lockpicking.

---

## Letter Sets
Set 1: B L P W S T D M R F

Set 2: Y U A I O L E H W R

Set 3: R M T N S K O A L E

Set 4: Y L D G K M S T E P


The tool picks one letter from each set, in order (Set 1 → Set 2 → Set 3 → Set 4), and checks the resulting 4-letter combination against the word list.

---

## Usage

1. Ensure you have Python 3 installed.  
2. Install the `requests` library if not present:  
   ```bash
   pip install requests
3. Save the script (e.g., wordpick.py).

4. Run the script:
   ```bash
   python3 wordpick.py
6. The script will download the word list, generate combinations, and print out matching words along with a total count.
