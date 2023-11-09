def get_char_number(c: str) -> int:
    a = ord('a')
    z = ord('z')
    val = ord(c)
    if a <= val <= z:
        return val - a
    return -1