import string


def answer(s):
    # your code here
    _key = list(string.ascii_lowercase[::-1])
    _map = list(string.ascii_lowercase)
    print(_key)
    print(_key)
    print(_map)
    print(s)
    decoded = ""
    for char in s:
        decoded = decoded + (_key[_map.index(char)]
                             if char.islower() else char)

    print(decoded)
    print("".join((_key[_map.index(char)]
                   if char.islower() else char) for char in s))

answer("Yvzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!")
