class Player:
    def __init__(self, pseudo):
        self.__pseudo = pseudo
        self.__score0 = 0
        self.__score1 = 0
        self.__score2 = 0
        self.__score3 = 0
        self.__score4 = 0

    def getScore0(self):
        return self.__score0

    def getScore1(self):
        return self.__score1

    def getScore2(self):
        return self.__score2

    def getScore3(self):
        return self.__score3

    def getScore4(self):
        return self.__score4

    def newScore0(self, nouveau):
        if (int(nouveau) > self.__score0):
            self.__score0 = nouveau

    def newScore1(self, nouveau):
        if (int(nouveau) > self.__score1):
            self.__score1 = nouveau

    def newScore2(self, nouveau):
        if (int(nouveau) > self.__score2):
            self.__score2 = nouveau

    def newScore3(self, nouveau):
        if (int(nouveau) > self.__score3):
            self.__score3 = nouveau

    def newScore4(self, nouveau):
        if (int(nouveau) > self.__score4):
            self.__score4 = nouveau

    def getMoyenne(self):
        return (self.__score0 + self.__score1 + self.__score2 + self.__score3 + self.__score4)/5

    def getTotal(self):
        return self.__score0 + self.__score1 + self.__score2 + self.__score3 + self.__score4

    def getMeilleur(self):
        liste = [self.__score0, self.__score1,
                 self.__score2, self.__score3, self.__score4]
        best = liste[0]
        for i in range(len(liste)):
            if (liste[i] > best):
                best = i
        return best

    def getPire(self):
        liste = [self.__score0, self.__score1,
                 self.__score2, self.__score3, self.__score4]
        worst = liste[0]
        for i in range(len(liste)):
            if (liste[i] > worst):
                worst = i
        return worst


Fin = False
while (not Fin):
    player0 = Player("pseudo0")
    a = input("score musique0?")
    b = input("score musique1?")
    c = input("score musique2?")
    d = input("score musique3?")
    e = input("score musique4?")
    player0.newScore0(a)
    player0.newScore1(b)
    player0.newScore2(c)
    player0.newScore3(d)
    player0.newScore0(e)

    print("score0" + player0.getScore0())
    print("score1" + player0.getScore1())
    print("score2" + player0.getScore2())
    print("score3" + player0.getScore3())
    print("score4" + player0.getScore4())
    print("Meilleur" + player0.getMeilleur())
    print("pire" + player0.getPire())
    print("total" + player0.getTotal())
    print("moyenne" + player0.getMoyenne())
    input()
