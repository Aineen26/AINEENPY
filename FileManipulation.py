"""PROGRAM FOR MANIPULATING FILES
PROGRAM NAME: FILE MANIPULATION
AUTHOR: AINEEN SAYYED
DATE CREATED: 6/02/2026"""
import  re
from pathlib import Path
from collections import Counter

def count_word_frequencies(file_path: str):
    target_file = Path(file_path)
    word_counts = Counter()
    if not target_file.is_file():
        print(f"Error :'{file_path}' is not a valid file.")
        return
    try:
        with target_file.open('r',encoding="utf-8", errors='replace') as file:
            for line in file:
                words = re.findall(r'\b\w+\b', line.lower())
                word_counts.update(words)
        if not word_counts:
            print("The file is empty or contains no valid words.")
            return
        print(f"{'Word':<20} | {'Count': <10}")
        print("-" * 30)
        for word in sorted(word_counts):
            print(f"{word:<20} {word_counts[word]:<10}")
    except PermissionError:
        print("Error : You do not have permission to read this file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
if __name__ == "__main__":
    file_to_read = "Sample.txt"
    count_word_frequencies(file_to_read)

