class Karaoke:
    def __init__(self, nombrechansons, nomchansons, nombrejoueurs):
        self.__nombrechansons = nombrechansons
        self.__nombrejoueurs = nombrejoueurs

    def getNombreChansons(self):
        return self.__nombrechansons

    def getNombrePlayer(self):
        return self.__nombrejoueurs


class Player:
    def __init__(self, pseudo, score1, score2):
        self.__pseudo = pseudo
        self.__Scores = [score1, score2]

    def getScores(self):
        return self.__score0

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
    nbrmus = input("combien de musiques?")
    nomchansons = ["" * int(nbrmus)]
    for i in range(int(nbrmus)):
        nomchansons[i] = input("Quels noms de chansons?")

    nbrjoueurs = input("combien de joueurs?")

    Karaoke(int(nbrmus), nomchansons, int(nbrjoueurs))

    for i in range(nbrjoueurs):
        for n in range(nbrmus):
            score = input("Quel est ton score pour la musique numero" + n)
