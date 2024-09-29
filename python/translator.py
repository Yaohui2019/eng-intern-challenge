import argparse

ENG2BRA = {
    'a': 'O.....',
    'b': 'O.O...',
    'c': 'OO....',
    'd': 'OO.O..',
    'e': 'O..O..',
    'f': 'OOO...',
    'g': 'OOOO..',
    'h': 'O.OO..',
    'i': '.OO...',
    'j': '.OOO..',
    'k': 'O...O.',
    'l': 'O.O.O.',
    'm': 'OO..O.',
    'n': 'OO.OO.',
    'o': 'O..OO.',
    'p': 'OOO.O.',
    'q': 'OOOOO.',
    'r': 'O.OOO.',
    's': '.OO.O.',
    't': '.OOOO.',
    'u': 'O...OO',
    'v': 'O.O.OO',
    'w': '.OOO.O',
    'x': 'OO..OO',
    'y': 'OO.OOO', 
    'z': 'O..OOO',
    'capital_follows': '.....O', 
    'number_follows': '.O.OOO',
    ' ': '......',
}
NUM2BRA={
    '1': 'O.....',
    '2': 'O.O...',
    '3': 'OO....',
    '4': 'OO.O..',
    '5': 'O..O..',
    '6': 'OOO...',
    '7': 'OOOO..',
    '8': 'O.OO..',
    '9': '.OO...',
    '0': '.OOO..'
}
LANG2BRA =dict()
LANG2BRA.update(NUM2BRA)
LANG2BRA.update(ENG2BRA)
BRA2ENG = dict(zip(ENG2BRA.values(), ENG2BRA.keys()))
BRA2NUM = dict(zip(NUM2BRA.values(), NUM2BRA.keys()))

def to_braille(input):
    res = ""
    is_numbers = False
    for char in input:
        if char.isupper():
            res += LANG2BRA['capital_follows']
        if "0123456789".find(char) != -1:
            if not is_numbers:
                is_numbers = True
                res += LANG2BRA['number_follows']
        else:
            is_numbers = False
 
        res += LANG2BRA[char.lower()]
    return res

def to_english(input):
    res = ""
    is_cap = False
    is_num = False
    idx = 0
    n = len(input)

    while idx < n:
        cur_str = input[idx:idx + 6]
        val = BRA2ENG[cur_str]
        idx += 6 
        if val == 'capital_follows' :
            is_cap = True
        elif val == 'number_follows':
            is_num = True
        elif val == ' ':
            is_num = False
            res += val
        else:
            if is_cap:
                res+= val.upper()
                is_cap = False
            elif is_num:
                res += BRA2NUM[cur_str]
            else:
                res += val
    return res


def main(args):
    inputs = " ".join(args.input)
    #print(inputs)
    if set(list(inputs)) != set(['O','.']):
        print(to_braille(inputs))
    else:
        print(to_english(inputs))




if __name__ == "__main__":
    parser= argparse.ArgumentParser()
    parser.add_argument('input', help ="User Input", nargs="*")
    args = parser.parse_args()
    main(args)