import time
class Team:
    name = ""

class Game:
    team1 = ""
    team2 = ""
    team1score = 0
    team2score = 0

class Round:
    teams = []
    number = 0

print("Oh noooooo, one of the teams mysteriously disappeared, give us your name so you can fill in!!!!!!!!")
time.sleep(0.5)
UserName = input("name - ")

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
UserName
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
    print(i)
