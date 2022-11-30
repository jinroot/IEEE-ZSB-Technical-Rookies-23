
students_grade=[]
for i in range(int(input())): 
    name = input()
    score = float(input())
    students_grade.append([name, score])
sorted_scores = sorted(list (set([x[1] for x in students_grade])))
second_lowest=sorted_scores[1]

low_final_list=[]
for i in students_grade:
    if second_lowest == i[1]:
        low_final_list.append(i[0])
for i in sorted (low_final_list):
     print(i)