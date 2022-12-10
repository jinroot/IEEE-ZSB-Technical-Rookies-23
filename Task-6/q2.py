
def libraryFine(d1, m1, y1, d2, m2, y2):
    # Write your code here
    fine=0
    if y2>y1:
        return fine
    if y2==y1:
        if m2>=m1:
            if d2>=d1:
                return fine
            else:
                fine = 15*(d1-d2)
                return fine
        else:
            fine =500*(m1-m2)
            return fine
    else:
            fine =10000
            return fine      
    return fine    
 