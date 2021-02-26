import time
import random
import os

class Team:
    name = ""

class Game:
    team1 = ""
    team2 = ""
    team1score = 0
    team2score = 0
    def play(self):
        self.team1score = random.randint(0, 5)
        self.team2score = random.randint(0, 5)
        if self.team1score == self.team2score:
            self.team1score = self.team1score + 1
        print(self.team1.name + " " + str(self.team1score) + " - " + str(self.team2score) + " " + self.team2.name)
        print("")
    def get_winner(self):
        if self.team1score < self.team2score:
            return self.team2
        else:
            return self.team1

class Round:
    teams = []
    number = 0

print("Oh noooooo, one of the teams mysteriously disappeared, give us your name so you can fill in!!!!!!!!")
time.sleep(0.5)
UserName = input("name - ")
os.system("cls")

Names = [
"Arsenal",
"A.F.C. Bournemouth",
"Brighton & Hove Albion",
"Burnley",
"Chelsea",
"Crystal Palace",
"Everton",
"Huddersfield Town",
"Leicester City",
"Liverpool",
"Manchester City",
"Manchester United",
"Newcastle United",
"Southampton",
"Stoke City",
"Swansea City",
"Tottenham Hotspur",
"Watford",
"West Bromwich Albion",
"West Ham United",
"América",
"BUAP",
"Cruz Azul",
"Guadalajara",
"León",
"Monterrey",
"Morelia",
"Necaxa",
"Pachuca",
"Santos Laguna",
"Tijuana",
UserName + " FC"
]

teams = []
for name in Names:
    team = Team()
    team.name = name
    teams.append(team)

round1 = Round()
round1.teams = teams
round1.number = 1
for i in range(0, int(len(round1.teams)/2)):
    print("game " + str(i + 1))
    game1 = Game()
    game1.team1 = random.choice(round1.teams)
    round1.teams.remove(game1.team1)
    game1.team2 = random.choice(round1.teams)
    round1.teams.remove(game1.team2)
    game1.play()
    