import time
import random
import os

# represents a single team
class Team:
    name = ""

# represents a single game
class Game:
    team1 = ""
    team2 = ""
    team1score = 0
    team2score = 0
    # generates a random score and prints the results
    def play(self):
        self.team1score = random.randint(0, 5)
        self.team2score = random.randint(0, 5)
        if self.team1score == self.team2score:
            self.team1score = self.team1score + 1
        print(self.team1.name + " " + str(self.team1score) + " - " + str(self.team2score) + " " + self.team2.name)
        print("")
    # gets the winning team from the game
    def get_winner(self):
        if self.team1score < self.team2score:
            return self.team2
        else:
            return self.team1

# represents a single round
class Round:
    teams = []
    number = 0
    games = []
    # gets the winnners from each game
    def get_winners(self):
        winners = []
        for game in self.games:
            winners.append(game.get_winner())
        return winners

# intro
print("Oh noooooo, one of the teams mysteriously disappeared, give us your name so you can fill in!!!!!!!!")
time.sleep(0.5)
UserName = input("name - ")
os.system("cls")

# list of team names
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

# converts the names into actual teams
allteams = []
for name in Names:
    team = Team()
    team.name = name
    allteams.append(team)

# initialising the teams for the first round
teamsinround = allteams
numberofround = 1

# loop through each round
# this will loop as many times as needed until there are no more teams
while len(teamsinround) > 1:
    # making an instance of the Round class
    round1 = Round()
    round1.games = []
    round1.teams = teamsinround
    round1.number = numberofround
    numberofround = numberofround + 1
    print("")
    input("press 'ENTER' to play the next round")
    os.system("cls")
    # loops round the games in this round
    for i in range(0, int(len(round1.teams)/2)):
        print("Game " + str(i + 1))
        # instance of the Game class
        game1 = Game()
        game1.team1 = random.choice(round1.teams)
        round1.teams.remove(game1.team1)
        game1.team2 = random.choice(round1.teams)
        round1.teams.remove(game1.team2)
        # plays the game
        game1.play()
        # appends game1 to round1.games
        round1.games.append(game1)

    # gets the winners to add them to the next round
    teamsinround = round1.get_winners()
    if len(teamsinround) == 1:
        print("THE WINNER IS: ")
        print("")
    else:
        print("The winners of this round are: ")
        print("")
    for winner in teamsinround:
        print(winner.name)