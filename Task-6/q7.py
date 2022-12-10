def beautifulTriplets(d, arr):
    # Write your code here
    output=0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if(arr[j] - arr[i] == d ):
                for k in range(j+1,len(arr)):
                 if( arr[k] - arr[j]  == d):
                     output += 1
    return output