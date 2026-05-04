#!/bin/python3

import math
import os
import random
import re
import sys

def logo_company(s):
    cnt = [0] * 26
    for i in s: 
        if 'a' <= i <= 'z':
            cnt[ord(i)-ord('a')] += 1
    
    result = [] 
    for i in range(0,26):
        if cnt[i] > 0 :
            result.append((chr(i+ ord('a')) , cnt[i]))
    result.sort(key=lambda x: x[1], reverse=True)
    for char, count in result[:3]:
        print(char, count)
        


if __name__ == '__main__':
    s = input()
    logo_company(s)