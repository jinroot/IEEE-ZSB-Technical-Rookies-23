def insertionSort(list):
    for i in range(1, len(list)):
        key = list[i]
        j = i-1
        while j >=0 and key < list[j] :
                list[j+1] = list[j]
                j -= 1
        list[j+1] = key
 
list = [112, 141, 153, 25, 122]
insertionSort(list)
print(list)
"""
Insertion sort works by storing one of the elements in the list in a variable called key
(We start by doing this to the 2nd element, assuming the first element is sorted)
then we check all the elements behind our key element if one of them is greater than key
we put or element to the left of it otherwise we keep it on the right
repeat till the list is sorted

--------------------------------------------------------------------------------------------

Time Complexity	 
Best	O(n)
Worst	O(n2)

Space Complexity  O(1)

--------------------------------------------------------------------------------------------

Definition Stabilty:
maintains the relative order of the items with equal sort keys

Insertion sort is stable
"""
