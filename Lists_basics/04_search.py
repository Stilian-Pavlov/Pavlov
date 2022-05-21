n = int(input())
magic_word=input()
list = []
list1=[]
for i in range (n):
    word=input()
    list.append(word)
    if magic_word in word:
        list1.append(word)
print(list)
print(list1)