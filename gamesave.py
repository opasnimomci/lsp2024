import json
from operator import itemgetter

with open('savegame.json', 'r') as file:
    game_data = json.load(file)

#igraci i njihovi scorovi
newuser1 = str(input())
newscore1 = int(input())
newuser2 = str(input())
newscore2 = int(input())

#dodaje score u dict
if newuser1 in game_data['score'].keys():
    game_data['score'][newuser1] = max(game_data['score'][newuser1], newscore1)
else:
    game_data['score'][newuser1] = newscore1

if newuser2 in game_data['score'].keys():
    game_data['score'][newuser2] = max(game_data['score'][newuser2], newscore2)
else:
    game_data['score'][newuser2] = newscore2

top5 = dict(sorted(game_data['score'].items(), key=itemgetter(1), reverse=True)[:5])

#najbolji useri
topuser = list(top5.keys())
print(*topuser)
#najbolji scorovi
topscore = list(top5.values())
print(*topscore)
##print(*game_data['score'])
##print(*list(game_data['score'].values()))

with open('savegame.json', 'w') as file:
    json.dump(game_data, file)
