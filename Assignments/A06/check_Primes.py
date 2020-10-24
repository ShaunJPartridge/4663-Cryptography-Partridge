import os
import sys
import math
import pprint

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

#def main(args,**kwargs):
 #   """ Example main function. Of course params would change as necessary.
  #  Params:
   #     kwargs <dict> : keyword params
    #"""
    #pprint.pprint(args)
    #pprint.pprint(kwargs)

def usage(message=None):
    if message:
        print(message)
    print("Usage: python skeleton.py [key1=string] [key2=int] [key3=int] [keyX=sometype]")
    print("Example:\n\t python skeleton.py arg1 arg2 var1='Param 1' path=./some_path a=25 b=50\n")
    sys.exit()

def isPrime(**kwargs):

  input_f = kwargs.get('infile',None)

  Values = []
  infile = open(input_f,'r')
  Values = [int(line) for line in infile.readlines()]


  #with open(input_f,'r') as i:
   # data = i.readlines()
  for i in range(len(Values)):
    N = Values[i]
  
  print(Values)
  #o = open("outfile.txt",'w')

  if N > 1: 
      
  # Iterate from 2 to n / 2  
    for i in range(2, N): 
         
       # If num is divisible by any number between  
      # 2 and n / 2, it is not prime  
      if (N % i) == 0: 

          #print(N, "is not a prime number") 
          PrimeFactors(N)
          return False
          #break
          
          
    else: 
        print(N, "is a prime number")
        return True 
          
  else: 
    print(N, "is not a prime number")
    return False   

def PrimeFactors(n): 
    

    Factors = []
    # Print the number of two's that divide n 
    while n % 2 == 0: 
        Factors.append(2)
        print(2)
        n = n / 2
          
    # n must be odd at this point 
    # so a skip of 2 ( i = i + 2) can be used 
    for i in range(3,int(math.sqrt(n))+1,2): 
          
        # while i divides n , print i ad divide n 
        while n % i== 0: 
            Factors.append(i)
            print(i)
            n = n / i
              
    # Condition if n is a prime 
    # number greater than 2 
    if n > 2: 
        print(int(n))
    return Factors
    

    
if __name__ == "__main__":

    #GetPrimes(72490732415291)
    isPrime(72490732415291)
    isPrime(3)
    