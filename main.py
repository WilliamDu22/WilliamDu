import week0.swap as swap
import week0.christmastree as christmastree
import week0.keypad as keypad
import week0.badboat as badboat
import week0.goodboat as goodboat
import week1.infodb as infodb
import week1.fib as fib
import week2.factorial as fac
import week2.palindrome as pal
import week2.multifactorialimperative as name
import week2.multifactorialoop as same
import crossover.timestable as timestable
from week0.fixedtree import tree
#####
main_menu = [
]

#
mathsub_menu = [
    ["Timestable", timestable.timestable]
]

manipulationsub_menu = [
    ["Swap", swap.run]
]

printsub_menu = [
    ["Keypad", keypad.run],
    ["Christmas Tree", christmastree.options],
    ["Fixed Tree", tree]
]

##
animationsub_menu = [
    ["Animation 1", badboat.ship],
    ["Animation 2", goodboat.ship]
]

infodbsub_menu = [
    ["InfoDB (For loop)", infodb.forl],
    ["InfoDB (While loop)", infodb.whilel],
    ["InfoDB (Recursive loop)", infodb.recursivel]
]

fibsub_menu = [
    ["Fibonacci Sequence", fib.seq],
    ["Fibonacci Term", fib.term]
]

facsub_menu = [
    ["Factorial Calculator", fac.run],
    ["Factorial Test", fac.test]
]


palsub_menu = [
    ["Palindrome Calculator", pal.run],
    ["Palindrome Test", pal.test]
]


namesub_menu = [
    ["Multifactorial Calculator", name.run],
    ["Multifactorial Test", name.test]
]


samesub_menu = [
    ["Multifactorial Calculator", same.run],
    ["Multifactorial Test", same.test]
]
#####

def mathsubmenu():
    title = "Math" + banner
    mathmenu_list = mathsub_menu.copy()
    mathmenu_list.append(["Fibonacci", fibsubmenu])
    mathmenu_list.append(["Factorial", facsubmenu])
    mathmenu_list.append(["Multifactorial (Imperative)", namesubmenu])
    mathmenu_list.append(["Multifactorial (OOP)", samesubmenu])
    buildMenu(title, mathmenu_list)


def manipulationsubmenu():
    title = "Manipulation" + banner
    manipulationmenu_list = manipulationsub_menu.copy()
    manipulationmenu_list.append(["Palindrome", palsubmenu])
    buildMenu(title, manipulationmenu_list)


def printsubmenu():
    title = "Print" + banner
    printmenu_list = printsub_menu.copy()
    printmenu_list.append(["Animations", animationsubmenu])
    printmenu_list.append(["InfoDB", infodbsubmenu])
    buildMenu(title, printmenu_list)

##
def animationsubmenu():
    title = "Animation" + banner
    buildMenu(title, animationsub_menu)


def infodbsubmenu():
    title = "InfoDB" + banner
    buildMenu(title, infodbsub_menu)


def fibsubmenu():
    title = "Fibonacci" + banner
    buildMenu(title, fibsub_menu)


def facsubmenu():
    title = "Factorial" + banner
    buildMenu(title, facsub_menu)


def palsubmenu():
    title = "Palindrome" + banner
    buildMenu(title, palsub_menu)


def namesubmenu():
    title = "Multifactorial (Imperative)" + banner
    buildMenu(title, namesub_menu)


def samesubmenu():
    title = "Multifactorial (OOP)" + banner
    buildMenu(title, samesub_menu)
#####

border = "=" * 25
banner = f"\n{border}\nPlease Select An Option\n{border}"


def buildMenu(banner, options):
    print("\u001b[31m",banner)
    prompts = {0: ["Exit", None]}
    for op in options:
        index = len(prompts)
        prompts[index] = op
    for key, value in prompts.items():
        print("\u001b[36m",key, '->', value[0])
    choice = input("Type your choice> ")
    try:
        choice = int(choice)
        if choice == 0:
            return
        try:
            action = prompts.get(choice)[1]
            action()
        except TypeError:
            try:
                exec(open(action).read())
            except FileNotFoundError:
                print(f"File not found!: {action}")
    except ValueError:
        print("\u001b[33m",f"Not a number: {choice}")
    except UnboundLocalError:
        print("\u001b[33m",f"Invalid choice: {choice}")
    buildMenu(banner, options)


def menu():
    title = "Function Menu" + banner
    menu_list = main_menu.copy()
    menu_list.append(["Math", mathsubmenu])
    menu_list.append(["Manipulation", manipulationsubmenu])
    menu_list.append(["Print", printsubmenu])
    buildMenu(title, menu_list)


if __name__ == "__main__":
    menu()
