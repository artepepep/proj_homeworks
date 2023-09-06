import csv
from random import randint

score_players = []
players = ["Josh", "Luke", "Kate", "Mark", "Mary"]

for player in players:
    for i in range (100):
        score = randint(1, 1000)
        score_players.append((player, score))

with open('score_players.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Player name', 'Score'])
    writer.writerows(score_players)