girlcr=[10,30,50,70]
girlcr.append(100)
print(girlcr)

girlcr.insert(3,60)
print(girlcr)

#update
girlcr[3]=600
print(girlcr)

girlcr.pop(4)
print(girlcr)

girlcr.pop(-2)
print(girlcr)

flag=0
target=int(input())
for i in girlcr:
  if i==target:
    flag=600
    break
  else:
    flag=flag+100
    
if flag==0:
  print("yes")
else:
    print("no")