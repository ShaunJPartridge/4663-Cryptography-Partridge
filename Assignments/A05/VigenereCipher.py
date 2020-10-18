from letter_frequency import frequency
import numpy as np
np.set_printoptions(threshold=np.inf)
import operator
import sys
import os

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
        self.key = ""
        self.dict = ""
        self.key_length = 0
        self.score = 0.0
        self.correct_key_length = 0
        self.Freq = frequency()
        with open("dict.txt","r") as f:
            self.dict = f.read().split("\n")


    def getScore(self,decrypted_text): # was self,decrypted_text

        count = 0
        sum = 0.0 
        
        for word in self.dict:

            if word in decrypted_text:
                
                count += 1
        
        sum = float(count / len(decrypted_text))
        sum = round(sum,5)      
        
        return sum
        

    def BreakVigenereCipher(self,**kwargs):# was self,ciphertext,k_length
          
        input_file = kwargs.get('input',None)
        output_file = kwargs.get('output',None)
        key = kwargs.get('key',None)
        key_length = kwargs.get('keylength',None)

        
        #cipheredtext = cipheredtext.lower()

        # should test if file exists
        with open(input_file) as f:
            ciphertext = f.read()
        ciphertext = ciphertext.lower()

        self.correct_key_length = self.Freq.Average_IC(ciphertext)
        #with open(key_length) as k:
         #   k_length = k.read()

        Temp_dict = {}

        for word in self.dict:

            if len(word) == self.correct_key_length:# was k_length
                Temp_dict[word] = word
        
        for word in Temp_dict.keys():

            self.plain_text = self.Decrypt(ciphertext,word)
            self.score = self.getScore(self.plain_text)               
            Temp_dict[word] = self.score
            self.plain_text = "" 

        self.key = max(Temp_dict,key=Temp_dict.get)

        #with open(output_file,'w') as o:
         #   o.write(self.key)

        self.Decrypt(infile=ciphertext,key=self.key)
        #return self.key
    

    def Encrypt(self,**kwargs):# was self,plaintext,key
    
        input_file = kwargs.get('input',None)
        output_file = kwargs.get('output',None)
        key = kwargs.get('key',None)

        # should test if file exists
        with open(input_file) as f:
            plaintext = f.read()

        plaintext = plaintext.lower()
        self.ciphered_text = ""

        i = 0
        for letter in plaintext:
            if letter in self.ALPHABET:

                a = ord(letter)-97
                b = ord(key[i])-97
                self.ciphered_text += chr(((a+b)%26)+97)

                i = (i + 1) % len(key)
            else:
                self.ciphered_text += letter

        with open(output_file,'w') as f:
            f.write(self.ciphered_text)
        #return self.ciphered_text

        


    def Decrypt(self,**kwargs):# was self,cipheredtext,key

        input_file = kwargs.get('input',None)
        output_file = kwargs.get('output',None)
        key = kwargs.get('key',None)

        #cipheredtext = cipheredtext.lower()

        # should test if file exists
        with open(input_file) as f:
            ciphertext = f.read()
        ciphertext = ciphertext.lower()
        self.plain_text = ""

        i = 0
        for letter in ciphertext:
            if letter in self.ALPHABET:

                a = ord(letter)-97
                b = ord(key[i])-97
                self.plain_text += chr(((a-b)%26)+97)

                i = (i + 1) % len(key)
            else:
                self.plain_text += letter
        
        #return self.plain_text
        with open(output_file,'w') as f:
            f.write(self.plain_text)

def mykwargs(argv):
    '''
    Processes argv list into plain args (list) and kwargs (dict).
    Just easier than using a library like argparse for small things.
    Example:
        python file.py arg1 arg2 arg3=val1 arg4=val2 -arg5 -arg6 --arg7
        Would create:
            args[arg1, arg2, -arg5, -arg6, --arg7]
             kargs{arg3 : val1, arg4 : val2}

        Params with dashes (flags) can now be processed seperately
    Shortfalls:
        spaces between k=v would result in bad params
        Flags aren't handled at all. Maybe in the future but this function
            is meant to be simple.
    Returns:
        tuple  (args,kargs)
    '''
    args = []
    kargs = {}

    for arg in argv:
        if '=' in arg:
            key,val = arg.split('=')
            kargs[key] = val
        else:
            args.append(arg)
    return args,kargs

def usage(message=None):
    if message:
        print(message)
    name = os.path.basename(__file__)
    print(f"Usage: python {name} [input=string filename] [output=string filename] [key=string] [op=encrypt/decrypt]")
    print(f"Example:\n\t python {name} input=input_file.txt output=output_file.txt key=machine op=encrypt\n")
    sys.exit()


if __name__ == "__main__":

    #infile = "ecu yufghz ho mafn hlt tak hv uktokk mon csnm zc seksp"
    #encrypted_text = "bcg pnjh pdivbv wz gbiu vqiq mri tiis isqb vb bcgz fvrse gbi foz agshf kwhfvsxn nbb ruzrqwwavf mri opbcvs kwhfh cz gbiu civ nbg mac xbrk ipnh bcg sacz ozl lcx odm gvh czm jvrzx lrqlrq eusus fw tc"
    VC = Vigenere_Cipher()
    #encrypted_text = VC.Encrypt(infile,"goat")
    #print(infile)
    #infile = encrypted_text
    
    F = frequency()

    # break text up into n groups and whichever has the highest average ic score is the correct key length
    #correct_key_length = F.Average_IC(infile)
    #print(correct_key_length)

    #correct_key = VC.BreakVigenereCipher(infile,correct_key_length)
    #print(correct_key)

    #decrypted_text = VC.Decrypt(infile,correct_key)
    #print(decrypted_text)

    """
    Change the required params value below accordingly.
    """

    required_params = 3 # adjust accordingly

    # get processed command line arguments 
    _,params = mykwargs(sys.argv[1:])

    # print usage if not called correctly
    if len(params) < required_params:
        usage()

    operation = params.get('op',None)
    infile = params.get('input',None)
    outfile = params.get('output',None)
    keylength = params.get('keylength',None)

    key = params.get('key',None)

    if not operation and not infile and not outfile and not key and not keylength:
        usage()

    if operation.lower() == 'encrypt':
        VC.Encrypt(**params)
    elif operation.lower() == 'decrypt':
        VC.Decrypt(**params)
    elif operation.lower() == 'averageIC':
        F.Average_IC(**params)
    elif operation.lower() == 'breakVigenereCipher':
        VC.BreakVigenereCipher(**params)
    else:
        usage()
    