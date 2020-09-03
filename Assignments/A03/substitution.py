from random import shuffle
from random import randint

# list of letters
alphabet = [chr(x+97) for x in range(26)]

#list of letters to substitute
subs = [chr(x+97) for x in range(26)]

# shuffle (randomize) our list between 5 and 25 times
ns = randint(5,25)
print(ns)
for i in range(ns):
    shuffle(subs)
# print the list of substitution letters out
print(subs)

class Substitution():
    def __init__(self):
        self.encrypted_m = " "
        self.freq = {}
        self.plaintext = " "

    #def get_let_count(self,text):

        #text = open("ciphertext_1.txt")
     #   self.encrypted_m = open(text,"w")

      #  for char in self.encrypted_m:
       #     if char not in self.freq:
        #        self.freq[char] = 1
         #   else:
          #      self.freq[char] += 1
        #print(self.freq[char])

    def break_cipher(self):
        self.plaintext = self.encrypted_m.replace("l","\033[31me\033[0m")
        print(self.plaintext)


# here is where you would put your plain text
#plaintext = "".lower()

# here is where you would write to the out file
#f = open("ciphertext.txt","w")

# performs the substitution
#for p in plaintext:
 #   i = ord(p)-97
  #  if p in alphabet:
   #     i = ord(p)-97
    #    f.write(subs[i])
    #else:
     #   f.write(p)


if __name__ == '__main__':

  S = Substitution()
  enc_mess = open("ciphertext_2.txt", "w")
  print(enc_mess)
  #S.get_let_count("ciphertext_1.txt")
  S.break_cipher()
