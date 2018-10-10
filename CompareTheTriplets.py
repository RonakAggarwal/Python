#CompareTheTriplets
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    Arr=[0,0]
    for i in range(3):
        if a[i]>b[i]:
            Arr[0]=Arr[0]+1
        elif b[i]>a[i]:
            Arr[1]=Arr[1]+1
    return Arr  

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
