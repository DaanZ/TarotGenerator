
major_arcana = {
    0: "the-fool",
    1: "the-magician",
    2: "the-high-priestess",
    3: "the-empress",
    4: "the-emperor",
    5: "the-hierophant",
    6: "the-lovers",
    7: "the-chariot",
    8: "strength",
    9: "the-hermit",
    10: "the-wheel-of-fortune",
    11: "justice",
    12: "the-hanged-man",
    13: "death",
    14: "temperance",
    15: "the-devil",
    16: "the-tower",
    17: "the-star",
    18: "the-moon",
    19: "the-sun",
    20: "judgement",
    21: "the-world"
}


minor_arcana = {
    1: "ace",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "page",
    12: "knight",
    13: "queen",
    14: "king"
}


def get_major_arcana(number):
    if number in major_arcana:
        return major_arcana[number]
    else:
        raise Exception("Incorrect Arcana number")


def get_card_name(card_index: int, name: str = "wands"):
    if card_index in minor_arcana:
        index = minor_arcana[card_index]
    else:
        raise Exception("Incorrect minor arcana index", card_index)
    return f"{index}-of-{name}"


def get_minor_arcana(card):
    if 22 <= card < 36:
        card_index = card - 21
        link = get_card_name(card_index, "wands")

    elif 36 <= card < 50:
        card_index = card - 35
        link = get_card_name(card_index, "cups")

    elif 50 <= card < 64:
        card_index = card - 49
        link = get_card_name(card_index, "swords")

    else:  # cards 64 - 77, including 77.
        card_index = card - 63
        link = get_card_name(card_index, "pentacles")

    return link
