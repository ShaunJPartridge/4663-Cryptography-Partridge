import sys
from itertools import islice
import array
import numpy as np
import math

class AdfgxLookup:
    def __init__(self,k=None,k2=None):
        self.key = self.remove_duplicates(k)

        self.alphabet = [chr(x+97) for x in range(26)]
        self.adfgx = ['A','D','F','G','X']
        self.keylen = 0

        if self.key:
            self.keylen = len(self.key)

        self.polybius = None
        self.lookup = None
        self.row = 0
        self.col = 0
        self.key2 = self.remove_duplicates(k2)
        self.matrix = {}

    def remove_duplicates(self,key):
        """ Removes duplicate letters from a given key, since they
            will break the encryption.
            Example: 
                key = 'helloworldhowareyou'
                returns 'helowrdayu'
        """
        newkey = []             # create a list for letters
        for i in key:           # loop through key
            if not i in newkey: # skip duplicates
                newkey.append(i)
        
        # create a string by joining the newkey list as a string
        return ''.join(str(x) for x in newkey)
       

    def build_polybius_string(self,key=None):
        """Builds a string consisting of a keyword + the remaining
           letters of the alphabet. 
           Example:
                key = 'superbatzy'
                polybius = 'superbatzycdfghiklmnoqvwx'
        """
        # no key passed in, used one from constructor
        if key != None:
            self.key = self.remove_duplicates(key)

        # NO key!
        if not self.key:
            print("Error: There is NO key defined to assist with building of the matrix")
            sys.exit(0)

        # key exists ... continue
        self.keylen = len(self.key)

        # prime polybius_string variable with key
        self.polybius = self.key

        for l in self.alphabet:
            if l == 'j':        # no j needed!
                continue
            if not l in self.key:    # if letter not in key, add it
                self.polybius += l
        return self.polybius

    def build_polybius_lookup(self,key=None):
        """ Builds a lookup dictionary so we can get the two letter pairs for each
            polybius letter. 
            Example:
                key = superbatzy
                polybius = superbatzycdfghiklmnoqvwx
                lookup = 
                {'a': 'DD',
                'b': 'DA',
                'c': 'FA',
                'd': 'FD',
                'e': 'AG',
                'f': 'FF',
                'g': 'FG',
                'h': 'FX',
                'i': 'GA',
                'k': 'GD',
                'l': 'GF',
                'm': 'GG',
                'n': 'GX',
                'o': 'XA',
                'p': 'AF',
                'q': 'XD',
                'r': 'AX',
                's': 'AA',
                't': 'DF',
                'u': 'AD',
                'v': 'XF',
                'w': 'XG',
                'x': 'XX',
                'y': 'DX',
                'z': 'DG'}
        """
        if key != None:
            self.key = self.remove_duplicates(key)

        # NO key!
        if not self.key:
            print("Error: There is NO key defined to assist with building of the matrix")
            sys.exit(0)

        # no polybius built, make one!
        if self.polybius == None:
            self.build_polybius_string()

        # init our dictionary
        self.lookup = {}           # dict as our adfgx reverse lookup
        for l in self.polybius:     # loop through the 1D matrix we created
            self.lookup[l] = ''     # init keys in the dictionary

        self.row = 0 
        self.col = 0

        # loop through the polybius 1D string and get the 2 letter pairs
        # needed to do the initial encryption
        for self.row in range(5):
            for self.col in range(5):
                i = (5 * self.row) + self.col
                self.lookup[self.polybius[i]] = self.adfgx[self.row]+self.adfgx[self.col]

        return self.lookup


    def sanity_check(self):
        """ This method lets you look at an actual "matrix" that you built using 
            a keyword. 
            Example: 
                key = 'superbatzy'
                output = 
                      A D F G X 
                    A s u p e r 
                    D b a t z y 
                    F c d f g h 
                    G i k l m n 
                    X o q v w x 
            This is not what you would use to encrypt!! Its only a sanity check
            meaning that it visualizes the lookup table just to see proof it's correct.
        """

        if not self.key:
            print("Error: There is NO key defined to assist with building of the matrix")
            sys.exit(0)

        # no polybius built, make one!
        if self.polybius == None:
            self.build_polybius_string()

        self.row = 0
        self.col = 0
       
        sys.stdout.write('\n  ')
        for l in self.adfgx:
            sys.stdout.write(l+' ')
        sys.stdout.write('\n')
        for l in self.adfgx:
            sys.stdout.write(l+' ')
            for ll in self.adfgx:
                i = (5 * self.row) + self.col
                sys.stdout.write(self.polybius[i]+' ')
                self.col += 1
            self.row += 1
            self.col = 0
            sys.stdout.write("\n")

    def Columnar_Transposition(self,message,key2):

        message = message.replace(' ','')   # get rid of spaces
        self.key2 = key2
        # get sizes to help calculate matrix column lengths
        key2_length = len(self.key2)             # length of key
        message_length = len(message)       # message length 

        # figure out the rows and how many short columns
        rows = math.ceil(float(message_length)/float(key2_length))
        cols = key2_length
        #short_cols = key2_length - (message_length%key2_length)

        # pad 0 to the end of string if its length is not equal to row * col
        if message_length < rows * cols:
            message = message.ljust(rows*cols,'0')

        # dictionary for our new matrix
        #matrix = {}

        # every letter is a key that points to a list
        for k in self.key2:
            self.matrix[k] = []

        # add the message to the each list in a row-wise fashion
        # meaning DFFDGAFXXA gets loaded like:
        # 
        #           QUARK
        #           -----
        #           DFFDG
        #           AFXXA
        i = 0
        for m in message:
            self.matrix[key2[i]].append(m)
            i += 1
            i = i % len(self.key2) 

        temp_matrix = sorted(self.matrix.items())
        sorted_matrix = {}

        # Rebuild the sorted matrix into a dictionary again
        # Rememnber sorted returns a list of tuples and we 
        # need to make another dictionary. This is another 
        # reason NOT to sort the matrix, but simply access
        # it via an alphabetized word.
        for item in temp_matrix:
            sorted_matrix[item[0]] = item[1]

        str_t = ""
        for k in sorted(self.key2):
            for d in sorted_matrix[k]:
                str_t += d

        return str_t

    def Encrypt(self,message,key,key2):

        ciphered_text = []
        self.key = key
        self.key2 = key2
        lookup = self.build_polybius_lookup(self.key)
        tmp_msg = ""

        for l in message:
            for k, v in lookup.items():
                if l in k:
                    ciphered_text.append(v)

        print(tmp_msg)
        tmp_msg = ''.join(ciphered_text)
        tmp_msg = self.Columnar_Transposition(tmp_msg,self.key2)
        return tmp_msg
        
    def Decrypt(self,message,key,key2):

        deciphered_text = []
        self.key = key
        self.key2 = key2
        lookup = self.build_polybius_lookup(self.key)

        message = message.replace('0',"")
        self.Undo_Columnar_Transposition(message,self.key2)
        # tmp_msg = self.Undo_Columnar_Transposition

    def Undo_Columnar_Transposition(self,message,key2):

        message = message.replace(' ','')   # get rid of spaces
        self.key2 = key2
        # get sizes to help calculate matrix column lengths
        key2_length = len(self.key2)             # length of key
        message_length = len(message)       # message length 

        # figure out the rows and how many short columns
        rows = math.ceil(float(message_length)/float(key2_length))
        cols = key2_length
        #short_cols = key2_length - (message_length%key2_length)
        
        # pad 0 to the end of string if its length is not equal to row * col
        if message_length < rows * cols:
            message = message.ljust(rows*cols,'0')
        
        # dictionary for our new matrix
        rows = int(len(message)/cols)
        a = np.zeros([rows,cols], str)

        for i in range(len(message)):
            print(message[i])
            if i == rows:
                print("")
            #for j in range(rows):
             #   print(message[j])
              #  if j % rows == 0:
               #     print("")
        

        for i in range(rows):
            for j in range(cols):
                a[i][j] = message[i]
        #for i in message: 
         #   k = 0  
          #  for j in range(rows):
            #    k += 1
             #   a[j][k] = i
            
        print(a)


        # every letter is a key that points to a list
        #for k in self.key2:
         #   tmp_matrix[k] = []
        #print(tmp_matrix)
        # add the message to the each list in a row-wise fashion
        # meaning DFFDGAFXXA gets loaded like:
        # 
        #           QUARK
        #           -----
        #           DFFDG
        #           AFXXA
        #i = 0
        #for m in message:
         #   tmp_matrix[key2[i]].append(m)
          ## i = i % len(key2) 
        #print(tmp_matrix)
