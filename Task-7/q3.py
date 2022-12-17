
def distance(points,k):
    points.sort(key = lambda K: K[0]**2 + K[1]**2)
 
    return points[:k]

k=1
points= [[1,3],[-2,2]]
print(distance(points,k))



