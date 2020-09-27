import math
import os
import random
import re
import sys

def main(number_of_prisoners, number_of_sweets, chair_number_to_begin):
    final_chair = (chair_number_to_begin+number_of_sweets-1)%number_of_prisoners
    if final_chair == 0:
        return number_of_prisoners
    return final_chair

# Complete the saveThePrisoner function below.
def saveThePrisoner(n, m, s):
    return main(n, m, s)