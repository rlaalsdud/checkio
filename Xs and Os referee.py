from typing import List

def checkio(game_result):
    rPattern = createPattern(game_result)
    for i in rPattern:
        for s in "XO":
            if i.count(s) == 3 :
                return s
    return "D"

def createPattern(game_result):
    list =[]
    #horizontal pattern
    list.extend(game_result)
    #vertical pattern
    for i in range(0,3):
        pat = ""
        for res in game_result:
            pat +=res[i]
        list.append(pat)
    #cross pattern
    list.append(game_result[0][0]+game_result[1][1]+game_result[2][2])
    list.append(game_result[0][2]+game_result[1][1]+game_result[2][0])
    return list

if __name__ == '__main__':
    print("Example:")
    print(checkio(["X.O",
                   "XX.",
                   "XOO"]))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
