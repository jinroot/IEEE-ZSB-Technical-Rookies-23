def climbingLeaderboard(ranked, player):
    # Write your code here
    lst =[]
    ranks=[]
    output=[]
    for item in ranked:
         if item not in lst:
            lst.append(item)
    rank=len(lst)+1
    for i in range(len(player)):
        for j in range(len(lst)):
            if player[i]>=lst[j]:
                rank=j+1
                break
        ranks.append(rank)
            
    print(ranks)
    #no clue how to optimize this
    return ranks