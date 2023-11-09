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

import util

def is_permutation_of_palindrome(pharse: str) -> bool:
    count_odd = 0
    table = [0] * (ord('z') - ord('a') + 1)
    
    for s in pharse:
        x = util.get_char_number(s)
        if x != -1:
            table[x] += 1
            if table[x] %2 == 1:
                count_odd+=1
            else:
                count_odd -= 1
            
    return count_odd <= 1


if __name__ == "__main__":
    print(is_permutation_of_palindrome("gacgcoa"))
