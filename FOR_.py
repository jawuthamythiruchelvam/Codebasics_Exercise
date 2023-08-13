#q1
result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
count =0
for i in result:
    if i=="heads":
        count=count+1

print(f"number of heads is:{count}")
#q2
for i in range(1,10):
    if i%2==0 :
        continue
    else:
        print(f"sqare number of {i} is: {pow(i,2)}")

#q3
month_list = ["January", "February", "March", "April", "May"]
expense_list = [2340, 2500, 2100, 3100, 2980]
money=int(input("enter the amount:"))
month=-1
# for i in range(len(expense_list)):
#     if money in expense_list:
#         month=i
for i in range(len(expense_list)):
    if money == expense_list[i]:
        month = i

if month==-1 :
    print(f"You didn\'t spend {money} in any month")
else:
    print(f"You spent {money} in {month_list[month]}")
#q4

for i in range(1,6):
        print(f"are you tired in {i}?")
        choise1=input("enter yes or no:")
        choise=choise1.casefold()
        if choise=="yes" :
            print("you didn't finish the race")
            break

if i==5 :
    print('congratulations U finnished the race:))')


#q5
for i in range(1,6):
    for j in range(1,i+1) :
        print("* ", end="")

    print('\n')
