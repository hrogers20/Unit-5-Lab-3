"""
Program Name: Word Count
Author: Hannah Rogers
Purpose: Reads a selected text file and counts how many times each word appears.
Starter Code: No starter code used.
Date: October 4, 2026
"""

from pathlib import Path
import string

class WordAnalyzer:
    def __init__(self, filepath):
        self.__filepath = Path(filepath)
        self.__frequencies = {}
    
    def process_file(self):
        try:
            if not self.__filepath.exists():
                raise FileNotFoundError

            with self.__filepath.open('r') as file:
                for line in file:
                    translation = str.maketrans("","", string.punctuation)
                    line = line.translate(translation)
                    line = line.lower()
                    
                    words = line.split()

                    for word in words:
                        if word in self.__frequencies:
                            self.__frequencies[word] = self.__frequencies[word] + 1
                        else:
                            self.__frequencies[word] = 1

            return True


        except FileNotFoundError:
            print("File not found.")
            return False

    def print_report(self):
        words = list(self.__frequencies.keys())
        words.sort()

        for word in words:
            print(word, "::", self.__frequencies[word])

def main():

    books = {
        "1": "princess_mars.txt",
        "2": "Tarzan.txt",
        "3": "treasure_island.txt",
        "4": "monte_cristo.txt"
    }
    
    while True:
        print("Word Count Program")
        print("1. A Princess of Mars")
        print("2. Tarzan of the Apes")
        print("3. Treasure Island")
        print("4. The Count of Monte Cristo")
        print("5. Exit")

        choice = input("Choose a book: ")

        if choice in books:
            analyzer = WordAnalyzer(books[choice])

            if analyzer.process_file():
                analyzer.print_report()

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()