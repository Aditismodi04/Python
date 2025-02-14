#kbc excercise
KBC = [
  ["which colour is symbol of love?","red","pink","white",1],
   ["which colour is symbol of love?","red","pink","white",1],
   ["which colour is symbol of love?","red","pink","white",1],
   ["which colour is symbol of love?","red","pink","white",1],
   ["which colour is symbol of love?","red","pink","white",1],
   ["which colour is symbol of love?","red","pink","white",1],
   ["which colour is symbol of love?","red","pink","white",1],
   ["which colour is symbol of love?","red","pink","white",1],
   ["which colour is symbol of love?","red","pink","white",1],
  ]
levels = [1000,2000,3000,5000,10000,20000,40000,80000,320000]
money = 0
for i in range(0,len(KBC)):
  Question = KBC[i]
  print("\n\nquestion for",levels[i],"\n",KBC[i][0])
  print("1",KBC[i][1],   "2",KBC[i][2],    "3",KBC[i][3] )
  result  = int(input("enter your answer 1 2 or 3: "))
  if(result == KBC[i][4]):
    print("correct answer and you won",levels[i])
    if(i == 4):
     money = 10000
    elif(i == 8):
     money = 320000
  
  else:
    print("wrong answer")
    break
print(" \nyou can't pass this round so you won total Rs.",money)  
