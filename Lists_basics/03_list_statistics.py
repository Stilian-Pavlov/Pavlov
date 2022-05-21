num = int(input())
positive=[]
negative = []
sum_negative=0
count_postivie = 0
for i in range (num):
    number=int(input())
    if number >=0:
        positive.append(number)
        count_postivie+=1
    else:
        negative.append(number)
        sum_negative+=number
print(positive)
print(negative)
print(f"Count of positives: {count_postivie}")
print(f"Sum of negatives: {sum_negative}")