players = {
    ("Ivan", "Volkin"): (10, 5, 13),
    ("Bob", "Robbin"): (7, 5, 14),
    ("Rob", "Bobbin"): (12, 8, 2)
}

player=[]
player1=[]
player2=[]
for i in players.keys():

    player1.append(i[0])
    player1.append(i[1])
    #print(i)
    for j in players.get(i):
     #   print(j)
        player1.append(j)
 #       player2.append(player1)
    print(player1)
    player2.append(tuple(player1))
    player1=[]
print(player2)







'''''
player=[]
player1=[]
player2=[]
for i in players.keys():

    player1.append(i[0])
    player1.append(i[1])
    #print(i)
    for j in players.get(i):
     #   print(j)
        player1.append(j)
 #       player2.append(player1)
    print(player1)
    player2.append(player1)
    player1=[]
print(player2)

'''