cardOrder = "23456789TJQKA"
possibleStraights = [cardOrder[s:s+5] for s in range(len(cardOrder)-4)]

def rankVal(rank):
    return cardOrder.index(rank)

def evaluateHand(cards):
    primary = 0
    tertiary = 0
    ranks = [card[0] for card in cards]
    ranks.sort(key=rankVal)
    suits = [card[1] for card in cards]
    straight = ''.join(ranks) in possibleStraights
    #print(straight, ranks)
    flush = len(set(suits)) == 1
    if straight:
        if flush: # Straight-flush
            primary = 9
        else: # Straight
            primary = 5
    elif flush: # Flush
        primary = 6
    elif len(set(ranks)) == 2:
        if ranks.count(ranks[0]) in (1, 4): # Four-of-a-kind
            primary = 8
            if ranks.count(ranks[4]) == 1: tertiary = ranks[3]
            else: tertiary = ranks[4]
        else: # Full-house
            primary = 7
            if ranks.count(ranks[4]) == 2: tertiary = ranks[0]
            else: tertiary = ranks[4]
    elif len(set(ranks)) == 3:
        testCard = 0
        if ranks.count(ranks[0]) == 1:
            testCard = 1
            if ranks.count(ranks[1]) == 1:
                testCard = 2
        if ranks.count(ranks[testCard]) == 2: # Two-pair
            primary = 3
            if ranks.count(ranks[4]) == 1: tertiary = ranks[3]
            else: tertiary = ranks[4]
        else: # Three-of-a-kind
            primary = 4
            if ranks.count(ranks[4]) == 1:
                if ranks.count(ranks[3]) == 1:
                    tertiary = ranks[2]
                else: tertiary = ranks[3]
            else: tertiary = ranks[4]
    elif len(set(ranks)) == 4: # One-pair
        primary = 2
        if ranks.count(ranks[4]) == 1:
            if ranks.count(ranks[3]) == 1:
                if ranks.count(ranks[2]) == 1:
                    tertiary = ranks[1]
                else: tertiary = ranks[2]
            else: tertiary = ranks[3]
        else: tertiary = ranks[4]
    elif len(set(ranks)) == 5: # High-card
        primary = 1
    return (primary, ranks, tertiary)

def compareHands(hand, hand2):
    score = evaluateHand(hand)
    score2 = evaluateHand(hand2)
    #print(score, score2)
    if score[0] > score2[0]: return 1
    elif score[0] < score2[0]: return 2
    if score[0] in (1, 5, 6, 9):
        for i in range(4, -1, -1):
            if rankVal(score[1][i]) > rankVal(score2[1][i]): return 1
            elif rankVal(score[1][i]) < rankVal(score2[1][i]): return 2
    else:
        if rankVal(score[2]) > rankVal(score2[2]): return 1
        elif rankVal(score[2]) < rankVal(score2[2]): return 2
        for i in range(4, -1, -1):
            if rankVal(score[1][i]) > rankVal(score2[1][i]): return 1
            elif rankVal(score[1][i]) < rankVal(score2[1][i]): return 2
    print("Failure in comparison",hand,hand2)
    return 0

data = open("p054_poker.txt")
hands = [s.split() for s in data.read().splitlines()]
data.close()
p1Wins = sum(compareHands(s[:5], s[5:]) == 1 for s in hands)
print(p1Wins)
##hands = [
##    ['5H','5C','6S','7S','KD','2C','3S','8S','8D','TD'],
##    ['5D','8C','9S','JS','AC','2C','5C','7D','8S','QH'],
##    ['2D','9C','AS','AH','AC','3D','6D','7D','TD','QD'],
##    ['4D','6S','9H','QH','QC','3D','6D','7H','QD','QS'],
##    ['2H','2D','4C','4D','4S','3C','3D','3S','9S','9D']
##    ]
##hands = ['6H 4H 5C 3H 2H 3S QH 5S 6S AS'.split()]
##for s in hands:
##    print(compareHands(s[:5], s[5:]), s[:5], s[5:])
