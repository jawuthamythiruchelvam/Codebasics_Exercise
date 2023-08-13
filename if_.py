#Q1
#q1
india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

cityN = (input("enter a city name: "))
city=cityN.casefold()
if city in india:
    print("this city in india")
elif city in pakistan:
    print("this city in pakistan")
elif city in bangladesh:
    print("this city in bangladesh")
else:
    print("this city not belogs to indea or pakistan or bangladesh")
#q2
city1 = (input("enter a first city name: "))
city2 = (input("enter a second city name: "))
City1=city1.casefold()
City2=city2.casefold()
if City1 in india and City2 in india:
    print(" Both cities are in India")
elif City1 in pakistan and City2 in pakistan:
    print("Both cities are in pakistan")
elif City1 in bangladesh and City2 in bangladesh:
    print("Both cities are in bangladesh")
else:
    print("They don't belong to same country")

#Q2
sugar=float(input("enter your sugar leval :"))
if sugar<80 :
    print("sugar is low:(")
elif  80<=sugar<=100:
    print("it is normal:))")
else:
    print("your sugar is high:(((")
