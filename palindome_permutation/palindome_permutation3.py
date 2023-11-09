"""
Desc:
Given a string, write a function to check if it is a permutation of a palindrome.
A palindrome is a word or phrase that is the same forwards and backwards. 
A permutation is a rearrangement of letters. 
The palindrome does not need to be limited to just dictionary words. 
判断一个字符串是否包含回文的排列方式

EXAMPLE:
Input: "Tact Coa"
Output: True (permutations: "taco cat'; "atco eta·; etc.)

"""
import struct

from bitarray import bitarray
import util


def check_exactly_one_bit_set(bit_array):
    i = 0
    for bit in bit_array:
        i = (i << 1) | bit
    print(i)
    

def toggle(bit_array, x):
    if bit_array[x] == 0:
        bit_array[x] = 1
    else:
        bit_array[x] = 0
    return bit_array

def create_bit_array(phrase: str):
    b = bitarray(32)
    for s in phrase:
        x = util.get_char_number(s)
        if x != -1:
            toggle(b, x)
    return b


def is_permutation_of_palindrome(phrase: str) -> bool:
    b = create_bit_array(phrase)
    return b== 0 or check_exactly_one_bit_set(b)



if __name__ == "__main__":
    print(is_permutation_of_palindrome("g"))
