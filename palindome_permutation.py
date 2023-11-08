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


def check_max_one_odd(table: list) -> bool:
    found_odd = False
    for count in table:
        if count % 2 == 1:
            if found_odd:
                return False
            found_odd = True
    return True

def get_char_number(c: str) -> int:
    a = ord('a')
    z = ord('z')
    val = ord(c)
    if a <= val <= z:
        return val - a
    return -1

def build_char_frequency_table(phrase: str) -> list:
    table = [0 for _ in range(ord('z') - ord('a') + 1)]
    for c in phrase:
        x = get_char_number(c)
        if x != -1:
            table[x] += 1
    return table


def is_permutation_of_palindrome(pharse: str) -> bool:
    table = build_char_frequency_table(pharse)
    print(table)
    return check_max_one_odd(table)


if __name__ == "__main__":
    print(is_permutation_of_palindrome("gacgcoa"))
