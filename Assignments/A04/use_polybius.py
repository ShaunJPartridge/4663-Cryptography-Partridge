import pprint as pp
import sys
import numpy as np
from polybius import AdfgxLookup

#     A D F G X
# A | p h q g m 
# D | e a y n o 
# F | f d x k r
# G | c v s z w 
# X | b u t i l

# init and input my keyword
A = AdfgxLookup('superbad','quark')

# build my lookup table 
#lookup = A.build_polybius_lookup()

# print out my adfgx lookup table
#pp.pprint(lookup)

# print out the actual matrix so I 
# know I'm not insane!
#A.sanity_check()

ciphered_text = A.Encrypt('discombobulate','superbad','quark')

print(ciphered_text)
deciphered_text = A.Decrypt(ciphered_text,'superbad','quark')
#B = AdfgxLookup('helloworld')

# build my lookup table 
#lookup = B.build_polybius_lookup()

# print out my adfgx lookup table
#pp.pprint(lookup)

# print out the actual matrix I 
# know I'm not insane!
#B.sanity_check()