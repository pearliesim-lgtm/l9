word=input("Enter any word:")
ch=input("Enter any character:")
i=0
count=0
while i<len(word):
    if word[i]==ch:
        count=count+1
    i=i+1

print("the nomber of times",ch,"appears in",word,"is",count)