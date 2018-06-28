from random import choice

def avg(ls):
    return sum(ls) / len(ls)

class ConMan(): # A banker that always lowballs the average.
    def giveDeal(self, prizeList, roundNumber):
        return avg(prizeList) * roundNumber * .095

class Ideal(): # A player that always goes for the average or higher
    def alert(self,message):
        if 0: # Change this to toggle console spam.
            print(message)
    def playRound(self, casesToOpen, prizeList):
        for _ in range(casesToOpen):
            case = choice(prizeList)
            self.alert("You have opened a case with ${}!".format(case))
            prizeList.remove(case)
    def askDeal(self, casesToOpen, dealerOffer, prizeList):
        if avg(prizeList) > dealerOffer:
            self.alert("Rejected dealer offer of {} with expected value of {}.".format(dealerOffer,avg(prizeList)))
            return False
        self.alert("Accepted dealer offer of {} with expected value of {}.".format(dealerOffer,avg(prizeList)))
        return True

rounds = [6,5,4,3,2,1,1,1,1,1,0] # The number of cases opened each round

player = Ideal()
dealer = ConMan()

winnings = 0
chosenCase = 0
gameCount = 10000

for _ in range(gameCount):
    roundNumber = 0
    prizes = [.01, 1, 5, 10, 25, 50, 75, 100, 200, 300, 400, 500, 750,
              1000, 5000, 10000, 25000, 50000, 75000, 100000, 200000,
              300000, 400000, 500000, 750000, 1000000]
    
    while roundNumber < 10:
        #print("START OF ROUND",roundNumber)
        if roundNumber: # Player must play round 1 without an offer
            dealerOffer = dealer.giveDeal(prizes, roundNumber+1)
            if player.askDeal(rounds[roundNumber+1], dealerOffer, prizes):
                winnings += dealerOffer
                break
        player.playRound(rounds[roundNumber], prizes)
        roundNumber += 1
        
    if roundNumber == 10: # If all deals have been refused
        # This is supposed to be the case chosen at the beginning of the game,
        #   but it does not matter if it is chosen at the beginning or the end.
        chosenCase = choice(prizes)
        #print("You have won ${}!".format(chosenCase))
        winnings += chosenCase
        
print("You have won an average of ${} in {} games.".format(round(winnings/gameCount,2), gameCount))
# Ideally, the player should win an average of $131,477.54 each game.
