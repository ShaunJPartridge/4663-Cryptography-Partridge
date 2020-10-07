import string
import sys
import os
import requests
from urllib.request import urlopen

alphabet = [chr(x+97) for x in range(26)]

typical_frequency = {
    "a": 8.167,
    "b": 1.492,
    "c": 2.782,
    "d": 4.253,
    "e": 12.702,
    "f": 2.228,
    "g": 2.015,
    "h": 6.094,
    "i": 6.966,
    "j": 0.153,
    "k": 0.772,
    "l": 4.025,
    "m": 2.406,
    "n": 6.749,
    "o": 7.507,
    "p": 1.929,
    "q": 0.095,
    "r": 5.987,
    "s": 6.327,
    "t": 9.056,
    "u": 2.758,
    "v": 0.978,
    "w": 2.360,
    "x": 0.150,
    "y": 1.974,
    "z": 0.074
}

class frequency():
    def __init__(self):
        self.text = ""
        self.freq = {}
        self.freq_percent = {}
        self.sort_freq = None

        for l in alphabet:
            self.freq[l] = 0
            self.freq_percent[l] = 0
    
    def typical(self):
        return typical_frequency
    
    def count(self,text):
        for l in text:
            l = l.lower()
            if l in alphabet:
                self.freq[l] += 1

        for k in self.freq_percent:
            self.freq_percent[k] = round(self.freq[k] / len(text),2)
        
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

    

    def Incidence_of_Coincidence(self,text,keylength):
        sum = 0
        IC = 0.0
        i = 0
        N = len(text)
        #N = keylength
        #self.count(text)
        for c in self.freq.values():
            if c >= 1:
                i += 1
                if i <= N:
                    #print(c,c-1)
                    sum += c * (c - 1)
        # Resets self.freq values to zero after using the frequencies for the calculation
        self.freq = dict.fromkeys(self.freq, 0)
        #print(sum)
               
        IC = sum / ( N*(N-1))
        IC = round(IC,5)
        #return IC
        #print(IC)
        return IC
        
    def groups(self,text,keylength):

        # Create dictionary to hold the amount of groups equivalent to the
        # the length of key
        
        groups = {}
        for num in range(keylength):
            groups[num] = []

        # Appends all the letters from the text to each group or dictionary key
        # that are used to find the average Incidence of Coincidence of the groups
        index = 0
        num = 0.0
        for letter in text:
            groups[index].append(letter)
            index += 1
            index = index % keylength
        
        j = 0
        #l = 0
        sum = 0.0
        avg_IC = 0.0
        tmp_list = []
        for j in groups.keys():

            tmp_list.clear()
            tmp_list = groups[j]
            
            tmp_str = ''.join(tmp_list)
            #print(tmp_str)
            self.count(tmp_str)
            sum += self.Incidence_of_Coincidence(tmp_str,len(tmp_str))

        sum = round(sum,5)
        #print(sum)
        avg_IC = sum / keylength
        avg_IC = round(avg_IC,5)
        print(avg_IC)
            
          
       

        

def Process_File(input):

    key = "dogs"
    input = input.replace(" ","")
    print(len(input))
    result = ""
    i = 0
    for ch in input:
       if i % len(key)== 0:
            result += ch
       i += 1
    
    print(result)
    #print(len(result))




    
if __name__ == "__main__":
    
    #url = "https://www.gutenberg.org/files/2701/2701-0.txt"

    url = "https://raw.githubusercontent.com/sindresorhus/word-list/master/words.txt"
    #print("Downloading book ...")
    data = requests.get(url)
    
    #f = urllib.requests.urlopen(url)
    words_list = data.text

    for i in range(10):
        for word in words_list:
            if "bag" in words_list:
                print("true")
            else:
                print("false")
    #print(words_list)
    #
    #words_list = open("https://raw.githubusercontent.com/sindresorhus/word-list/master/words.txt").read().split() # was open("./words.txt")
    #for i in range(10):
     #   print(words_list[i])
    
    #infile = "tensw pez yqb xyimsg dmnv fhkz jbqn vgzb glmnmfwh"
    
    #text = infile.replace(" ","")


    #print("Calculating frequency...")
    #print(len(text))
    #F = frequency()
    
    
    #for i in range(2,16):
     #   F.groups(text,i)
   
    

