import random
import time

def main():
    pole: list = [" ", " ", " ",
                  " ", " ", " ",
                  " ", " ", " "]
    while " " in pole:
        printBoard(pole)
        tahHrace(pole)
        if kontrolaHrace(0,pole) == 1:
            printBoard(pole)
            print("Vyhrál hráč")
            break
        print("Tah počítače...")
        time.sleep(4)
        tahPocitace(pole)
        if kontrolaPocitace(0, pole) == 1:
            print("Vyhrál počítač")


def printBoard(pole):
    i: int = 0
    k: int = 0

    horizontal_line: str = " -------- -------- --------"
    vertical_line: str = "|        |        |        |"

    while i < 4:
        if i < 3:
            VLVar = f"|    {pole[k]}   |    {pole[k + 1]}   |    {pole[k + 2]}   |"
            print(horizontal_line)
            print(vertical_line)
            print(VLVar)
            print(vertical_line)
        if i == 3:
            print(horizontal_line)
        i += 1
        k += 3

def tahHrace(pole):
    tah = int(input("Zadejte pozici (1-9) kam chcete umístit svůj tah: "))
    try:
        if pole[tah-1] == " ":
            pole[tah-1] = "X"
        else:
            print("Pole je už obsazené")
            tahHrace(pole)
    except:
        print("Chybný input")
        print("Zkuste to znovu")
        tahHrace(pole)

def tahPocitace(pole):
    tah = random.randint(0,8)
    if pole[tah] == " ":
        pole[tah] = "O"
    else:
        tahPocitace(pole)

def kontrolaHrace(i,pole):
    while i < 7:
        if pole[i] == "X" and pole[i+1] == "X" and pole[i+2] == "X":
            return 1
        else:
            i += 3
    i = 0
    while i < 3:
        if pole[i] == "X" and pole[i + 3] == "X" and pole[i + 6] == "X":
            return 1
        else:
            i += 1
    i = 0
    if pole[i] == "X" and pole[i + 4] == "X" and pole[i + 8] == "X":
        return 1
    else:
        if pole[i + 2] == "X" and pole[i + 4] == "X" and pole[i + 6] == "X":
            return 1
        else:
            return 0

def kontrolaPocitace(i, pole):
    while i < 7:
        if pole[i] == "O" and pole[i+1] == "O" and pole[i+2] == "O":
            return 1
        else:
            i += 3
    i = 0
    while i < 3:
        if pole[i] == "O" and pole[i + 3] == "O" and pole[i + 6] == "O":
            return 1
        else:
            i += 1
    i = 0
    if pole[i] == "O" and pole[i + 4] == "O" and pole[i + 8] == "O":
        return 1
    else:
        if pole[i + 3] == "O" and pole[i + 2] == "O" and pole[i + 4] == "O":
            return 1
        else:
            return 0

main()
