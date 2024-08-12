
import random
import webbrowser
from tarot import get_major_arcana, get_minor_arcana


def check_num(number):
    total: int = 0
    for n in number:
        if not n.isdigit():
            return input("Invalid entry. Choose numbers only.\n  Pick a number: ")
        total += int(n)

    return str(total)


def play_tarot():
    input("  What is your question?: ")
    card = random.randint(0, 77)

    if 0 <= card < 22:
        link = get_major_arcana(card)
        url = "https://labyrinthos.co/blogs/tarot-card-meanings-list/"+link+"-meaning-major-arcana-tarot-card-meanings"
    else:
        link = get_minor_arcana(card)
        url = "https://labyrinthos.co/blogs/tarot-card-meanings-list/"+link+"-meaning-tarot-card-meanings"

    webbrowser.open(url)


if __name__ == "__main__":
    print("Welcome to the Oracle!")
    play_tarot()

    while True:
        next = input("Do you have another question? (y/n):").lower()

        if next == "y":
            play_tarot()
        elif next == "n":
            print("Thank you for consulting the Oracle.\n"
                  "Blessings on your journey, and remember the power is always within You.\n"
                  "---------------------------------\n")
            break
        break


     



