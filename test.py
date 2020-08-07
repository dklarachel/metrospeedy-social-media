# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# from selenium.common.exceptions import NoSuchElementException

# from csv_ops import get_hashtags

# import time


#res = [int(i) for i in results_count.split() if i.isdigit()] 

def has_int (str):
    for char in str.split():
        if char.isdigit():
            return char
    return False

def sort_dict_nums (dict, reverse):
    '''
    takes in dictionary, sorts using values, returns list of sorted keys \n
    numbers may be strings 
    '''
    # convert numbers in dictionary into int DT
    for key in dict:
        dict[key] =  int(dict[key])\

    # sort dictionary by values, return as list of tuples 
    sorted_dict = sorted(dict.items(), key=lambda x: x[1], reverse=reverse)
    return sorted_dict

def keys_from_tuple (list):
    '''takes list of tuples representing key-value pairs, and returns list of the keys'''
    key_list = []
    for pair in list:
        key = pair[0]
        key_list.append(key)
    return key_list

test_dict = {
    "avocado": "99999",
    "donut": "2344",
    "hot sauce": "696969696969",
    "peanuts": "12312366"
}

boom = sort_dict_nums(test_dict, True)
boom = keys_from_tuple(boom)
print(boom)

# result = sort_dict_nums(test_dict, False)
# print(result)
#print(list(test_dict.values()))

import numpy as np

orig = [
    ["instagram", 23423, 235345],
    ["twitter", 125, 77],
    ["facebook", 999, 288383838]
]

transposed = np.transpose(orig)
print(transposed)
