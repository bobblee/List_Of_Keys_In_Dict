# -*- coding: utf-8 -*-
"""
Description : Run thorugh python dictionary and pull out all keys and compare
                with known list of keys. Used to determine if a new key has
                been sent, but not accounted for in downstream processing.
"""

base =['first', '1', '2', '3', '4', 'b']
append_base =['first', '1_1', '1_2', '1_3', '2_4','2_5','2_6', 'b']

def recursive_items(dictionary:dict):
    for key, value in dictionary.items():
        if type(value) is dict:
            yield from recursive_items(value)
        else:
            yield (key, value)

def recursive_append_items(dictionary:dict,appended_key:str=''):
    for key, value in dictionary.items():
        if type(value) is dict:
            append_key = appended_key+key+'_'
            yield from recursive_append_items(value, append_key)
        elif type(value) is list:
            append_key = key+'_'
            for array_value in value:
                yield from recursive_append_items(array_value, append_key)
        else:
            yield (appended_key+key, value)

def remove_dups_from_list(x:list):
  return list(dict.fromkeys(x))

def list_diff(li1, li2): 
    return (list(set(li1) - set(li2)))

a = {'first': 'Bobby',
     'a': {
            '1': {
                '1': 2,
                '3': 4
                },
            '3': {
                '4': 5
                },
            '2': {
                '4': 5,
                '5': 6
                }
            },
     'b': 7,
     'c':[
         {
             '1' : 2,
             '2' : 3,
             '3' : 4
         },
         {
             '1' : 2,
             '2' : 3,
             '4' : 5
         }
     ]
    }

'''
# Keeping for simple testing/review

key_list = []
for key, value in recursive_items(a):
    #print(key)
    key_list.append(key)

print(key_list)
#key_list = remove_dups_from_list(key_list)
print(key_list)

print(list_diff(key_list, base))

print('-----------------------')
'''

key_list = []
for key, value in recursive_append_items(a):
    #print(key)
    key_list.append(key)

print(key_list)
key_list = remove_dups_from_list(key_list)
print(key_list)

print(list_diff(key_list, append_base)) 