## Assignment 3 - Frequency Analysis
### Shaun Partridge
### Description:

I received two files that were encrypted using a "substitution" cipher. The genius whom encrypted these, randomly shuffled a list of letters multiple times. The problem is, he never sent me the key! So, I cannot reverse the process. I need your help to decipher these messages.It is not a shift cipher, so you cant brute force the shift value! So the only way to get these two messages vital to the safety of earth is to run a frequency analysis on them.

### Files

|   #   |  File                            |  Description                           |
| :---: |----------------------------------|----------------------------------------|
|   1   |   [ciphertext_1.txt](https://raw.githubusercontent.com/ShaunJPartridge/4663-Cryptography-Partridge/master/Assignments/A03/ciphertext_1.txt)   | First encrypted file to decrypt. |
|   2   |   [ciphertext_2.txt](https://raw.githubusercontent.com/ShaunJPartridge/4663-Cryptography-Partridge/master/Assignments/A03/ciphertext_2.txt)   | Second encrypted file to decrypt.  |
|   3   |   [decrypted_1.txt](https://raw.githubusercontent.com/ShaunJPartridge/4663-Cryptography-Partridge/master/Assignments/A03/decrypted_1.txt)   | The first encrypted file decrypted.  |
|   4   |   [decrypted_2.txt](https://raw.githubusercontent.com/ShaunJPartridge/4663-Cryptography-Partridge/master/Assignments/A03/decrypted_2.txt)   | The second encrypted file decrypted.  |
|   5   |   [frequency.py](https://github.com/ShaunJPartridge/4663-Cryptography-Partridge/blob/master/Assignments/A03/frequency.py)   | This file can open text files and find the frequency of each letter in the text.  |
|   6   |   [substitution.py](https://github.com/ShaunJPartridge/4663-Cryptography-Partridge/blob/master/Assignments/A03/substitution.py)   |   This file will substitute the letters of the ciphered text using a list of letters  |

### Instructions

- In order to decipher an encrypted message using a frequency analysis, you must first get the frequency of each letter in the encrypted message.
- After getting the frequency of each letter in the encrypted message, the letters are then ordered by their frequency, with the top or first letter being the most frequent.
- Having ordered the letters based on their frequency, the letters then substituted with letters from the list of letter frequency in the English language. However, in order for these letters to be swapped, both letters from each list must have the same frequency(order) in the lists.
    - Example: 
                The letter L is the most frequent letter in the cipher text and the letter E is the most frequent letter used in the English language. Having seen this                           correlation between the letters, it is deduced that all the L's in the cipher text are E's.
- Note: Not all letters in the cipher text and the letter frequency list will have a direct correlation.

### Sources

- Practical Cryptography:
  - http://practicalcryptography.com/ciphers/simple-substitution-cipher/
- www3.nd.edu:
  - https://www3.nd.edu/~busiforc/handouts/cryptography/cryptography%20hints.html#:~:text=The%20most%20common%20two%2Dletter,words%20are%20the%20and%20and

I used these sources to help me understand how to use a frequency analysis in a substitution cipher, as well as show me common two letter words, three letter words, etc., to help crack the encrypted messages.
                
