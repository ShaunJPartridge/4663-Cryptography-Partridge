from collections import OrderedDict
import math
import pprint as pp
import sys
from polybius import AdfgxLookup

# this file creates the columnar transposition matrix

alphabet = "abcdefghijklmnopqrstuvwxyz"

def print_matrix(matrix,rows):
    for k in matrix:
        print(k,end=' ')
    print("")
    for k in matrix:
        print('-',end=' ')

    print("")
    for r in range(rows):
        for k in matrix:
            if r < len(matrix[k]):
                print(matrix[k][r],end=" ")
            else:
                print(" ",end=' ')
        print("")

def Keyword_Letter_Num(key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    num_list = list(range(len(key)))
    pos = 0
    for i in range(len(alphabet)):
        for j in range(len(key)):
            if alphabet[i] == key[j]:
                pos += 1
                num_list[j] = pos
    return num_list

def Columnar_Transposition(key,message):# change to self,key,message?

    key = key.upper() # change to self.ct_key = key.upper()
    
    # gets rid of spaces in message
    message = message.replace(' ','')# change to self.ct_message?

    # print(message)

    key_length = len(key)
    message_length = len(message)

    rows = math.ceil(float(message_length)/float(key_length))
    short_cols = key_length - (message_length%key_length)

    # print(rows)
    # print(short_cols)

    # print(f"{key_length} {message_length}")

    matrix = {} # change to self.ct_matrix = {}; this holds the original columnar transposition matrix

    # creates column headers
    for k in key: # change key to self.ct_key
        matrix[k] = []
    for p in matrix.keys():
        print(p)
    orig_key_num_list = sorted(matrix)
    print(orig_key_num_list)

    
    # creates the new columns with key and message
    i = 0
    for m in message:   # change message to self.ct_message
        matrix[key[i]].append(m)
        i += 1
        i = i % len(key)
    

    # print(matrix) this prints the matrix by column

    print_matrix(matrix,rows) # this prints the matrix with the key letters in 
                                # unalphabetical order
    #temp_matrix = sorted(matrix.items())

    # matrix column headers are in alphabetical order in addition with their corresponding letters
    matrix = sorted(matrix.items()) # change to self.ct_matrix

    #print(temp_matrix)

    sorted_matrix = {} # change to self.tc_sorted_matrix

    for item in matrix: # was temp_matrix n
        sorted_matrix[item[0]] = item[1]

    print_matrix(sorted_matrix,rows) # this prints the matrix with the key 
                                        # letters in alphabetical order
    #print(sorted_matrix)

    # converts dict values into list
    temp = list(sorted_matrix.values())
    return temp
    #print(temp)

    #
    #flat_list = []
    # flattens the lists in temp list to create one big list
    #for sublist in temp:
     #   for item in sublist:
      #      flat_list.append(item)
   
    #print(flat_list)
   
    # convert list to string
    #message = ''.join(flat_list)

    #return message
    #print(message)
    
def Undo_Columnar_Transposition(key,list1):# change to chiphered_text, was message

    #key = key.upper() # change to self.ct_key = key.upper()
    
    # gets rid of spaces in message
    #message = message.replace(' ','')# change to self.ct_message?

    #d_message = ""

    # track key indices
    i = 0

    d_message_list = list1
    d_message_indx = 0
    
    # create empty matrix
    #a = []
    #for i in range(row):
     ##  print(a[i])

    flat_list = []
    # flattens the lists in temp list to create one big list
    for sublist in list1:
        for item in sublist:
            flat_list.append(item)
   
    print(d_message_list)
   
    # convert list to string
    message = ''.join(flat_list)
    d_message_length = float(len(message))
    #print(message)

    print(len(d_message_list))

    key_length = len(key)
    
    col = len(key)
    row = math.ceil(float(d_message_length) / float(col))

    #rows = math.ceil(float(message_length)/float(col))# was /float(key_length)
    #short_cols = key_length - (message_length%key_length)

    #matrix = list(key) # column headers for matrix
    
    #width = len(matrix)
    #height = math.ceil(float(len(message)) / float(width))
    #print(matrix)
    

    # converts key into list in alphabetical order
    #key_list = sorted(list(key))

    

    
    #pos = 0
    #for num in range(len(matrix)):
     #   k_col = sorted(matrix.index(num))

      #  n = 0
       # while(n < len(decrypted)) and (len(decrypted[n]) > k_col):
        #    decrypted[n][k_col] = message[pos]
         #   n += 1
          #  pos += 1

    
    #print(decrypted)
    #matrix = {}
    ##   matrix[k] = []

    

    #matrix = sorted(matrix.items())

    #print(matrix)
    
    ##   matrix[key[i]].append(m) # was matrix[key[i]].append(m)
        #matrix.append(m)
      #  i += 1
       # i = i % len(key)

    #matrix = sorted(matrix.items())
    #sorted(matrix.keys())

    #print(decrypted)   
#   
#
#
# init and input my keyword
A = AdfgxLookup('dog')

# build my lookup table 
lookup = A.build_polybius_lookup()

# print out my adfgx lookup table
pp.pprint(lookup)

# print out the actual matrix so I 
# know I'm not insane!
A.sanity_check()

message = "hello there"
encrypted = []

# if l in lookup table already remove
for l in message:
    if l == " " in message:
        continue
    #message += lookup[l]
    
    encrypted.append(lookup[l])

message = ''.join(encrypted)
print(message)
#print(encrypted)

#for i in encrypted:
#message = ''.join(encrypted)
#print(message)
e_message = list()
e_message = Columnar_Transposition("zebras",message)
#print(e_message)

Undo_Columnar_Transposition("zebras",e_message)
#print(ct_matrix)

#ciphered_text = []
#plaintext = ""
#for l in sorted_matrix:
 # ciphered_text.append(sorted_matrix[l])
#print(ciphered_text)
