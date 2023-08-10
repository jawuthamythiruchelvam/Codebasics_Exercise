#Q1
monthly_expenses = [2200, 2350, 2600, 2130, 2190]
#q1
feb_jan=monthly_expenses[1]-monthly_expenses[0]
print(f"{feb_jan}$ amount more than jan in feb")
#q2
i=0
sum=0
while i<3:
    sum=sum+monthly_expenses[i]
    i=i+1
print("total expense in first quarter: ",sum)
#q3
j=1
for i in monthly_expenses:

    if i==2000:
        print(f"you spend exactly 2000 in {j}th month")
    j=j+1
#q4
monthly_expenses.append(1980)
print(monthly_expenses)
#q5
monthly_expenses[3]=monthly_expenses[3]-200
print("after change the april expenses:",monthly_expenses)
#Q2
heros=['spider man','thor','hulk','iron man','captain america']
#q1
print("length of the list:",len(heros))
#q2
heros.append("black panther")
print("heros list after add black panther:",heros)
#q3
heros.remove("black panther")
print("after remove black panter"+'\n', heros)
heros.insert(3,"black panter")
print("heros list after add black panther:", heros)
#q4
heros[1:3]=['doctor strange']
print(heros)
#q5
print(dir(monthly_expenses))
heros.sort()
print(heros)
