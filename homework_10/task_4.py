import csv

with open('score_players.csv', 'r') as csvfile:
    dictreader = csv.DictReader(csvfile)
    player_scores = []
    for row in dictreader:
        player_scores.append(row)
high_player_scores = {}
for data in player_scores:
    player_name = data["Player name"]
    score = data["Score"]
    if player_name not in high_player_scores or score > high_player_scores[player_name]:
        high_player_scores[player_name] = score
sort_of_players = sorted(high_player_scores.items(), key=lambda x: x[1], reverse=True)
with open('high_score_players.csv', 'w', newline='') as csvfile:
    fields = ["Player name", "Highest score"]
    writer = csv.DictWriter(csvfile, fieldnames=fields)
    writer.writeheader()
    for player_name, highest_score in sort_of_players:
        writer.writerow({"Player name": player_name, "Highest score": highest_score})
                