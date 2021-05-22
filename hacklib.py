from random import randint

cool_characters = "人一日大年出本中子見国言上分生手自行者二間事思時気会十家女三前的方入小地合後目長場代私下立部学物月田何来彼話体動社知理山内同心発高実作当新世今書度明五戦力名金性対意用男主通関文屋感郎業定政持道外取所現"


def gen_string():
    acc = ""
    x = randint(3, 8)
    for i in range(0, x*x):
        acc += get_char()
    return acc

def get_char():
    # 20 percent chance of a 1 or a 0
    if (randint(0, 5) == 0):
        return str(randint(0, 1))
    else:
        return cool_characters[randint(0, len(cool_characters) - 1)]

