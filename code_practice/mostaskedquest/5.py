#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'fizzBuzz' function below.
#
# The function accepts INTEGER n as parameter.
#

def fizzBuzz(n):
    # Write your code here
    for i in range(n):
        if (i % 3) == 0 and (i%5) == 0:
            print('FizzBuzz')
        elif (i%3) == 0 and (i%5) != 0:
            print('Fizz')
        elif (i%3) !=0 and (i%5) == 0:
            print('Buzz')
        else:
            print(i)

if __name__ == '__main__':
    n = int(input().strip())

    fizzBuzz(n)
