import sys
import os
import requests

alphabet = [chr(x+97) for x in range(26)]

class Frequency():
    def __init__(self):
        self.text = ""
        self.freq = {}
        self.sort_freq = None

        for l in alphabet:
            self.freq[l] = 0
    
    def count(self,text):
        for l in text:
            l = l.lower()
            if l in alphabet:
                self.freq[l] += 1

        # https://realpython.com/python-lambda/
        self.sort_freq = sorted(self.freq.items(), key=lambda x: x[1], reverse=True)

    def print(self):
        if self.sort_freq:
            for f in self.sort_freq:
                print(f"{f[0]}:{f[1]}")
        else:
            print(self.freq)

    def getNth(self,n):
        if self.sort_freq:
            return self.sort_freq[n][0]

        return None

if __name__=='__main__':
    url = "https://raw.githubusercontent.com/ShaunJPartridge/4663-Cryptography-Partridge/master/Assignments/A03/ciphertext_1.txt"
    #url = "https://www.gutenberg.org/files/2600/2600-0.txt"

    print("Downloading book ...")
    f = requests.get(url)
    text = f.text


    print("Calculating frequency...")
    # creating an object of Frequency class
    F = Frequency()

    # calculates the count of each letter when it reoccurs in the text
    F.count(text)

    # prints the frequency of each letter in the text
    F.print()

    # prints the nth letter according to its number of occurance
    print(F.getNth(0)) # prints the letter e because its the most occuring
                        # letter.

    
