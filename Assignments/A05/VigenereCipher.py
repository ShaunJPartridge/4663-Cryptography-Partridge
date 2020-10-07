from letter_frequency import frequency
#frequency.groups()
#message = ""
#key_length = 0
#frequency.groups(message,key_length)


class Vigenere_Cipher():

    def __init__(self):
        self.ALPHABET = [chr(x+97) for x in range(26)]
        self.plain_text = ""
        self.ciphered_text = ""
        self.deciphered_text = ""
        self.key = 0

    
    def Encrypt(self,plaintext,key):
    
        plaintext = plaintext.replace(" ","")
        plaintext = plaintext.lower()

        i = 0
        for letter in plaintext:
            if letter in self.ALPHABET:

                a = ord(letter)-97
                b = ord(key[i])-97
                self.ciphered_text += chr(((a+b)%26)+97)

                i = (i + 1) % len(key)
            else:
                self.ciphered_text += letter
        
        return self.ciphered_text

    def Decrypt(self,cipheredtext,key):

        cipheredtext = cipheredtext.replace(" ","")
        cipheredtext = cipheredtext.lower()

        i = 0
        for letter in cipheredtext:
            if letter in self.ALPHABET:

                a = ord(letter)-97
                b = ord(key[i])-97
                self.plain_text += chr(((a-b)%26)+97)

                i = (i + 1) % len(key)
            else:
                self.plain_text += letter
        
        return self.plain_text


if __name__ == "__main__":

    
    infile = "the dogs are outside"
    VC = Vigenere_Cipher()
    encrypted_text = VC.Encrypt(infile,"and")
    #print(encrypted_text)
    F = frequency()

    
    F.groups(encrypted_text,8)

    #frequency.groups(encrypted_text,9)

    #decrypted_text = VC.Decrypt(encrypted_text,"and")
    #print(decrypted_text)