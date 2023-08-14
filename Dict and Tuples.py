#q1
country={"china":143, "india":136, "usa":32, "pakistan":21}
print("there is 3 choices these are print,add,remove and Query")
u="y"
while u=='y' or u=='Y':
        choice=input("enter your choice:")
        choicec=choice.casefold()
        if choicec=="add":
            c=input("enter the name of country:")
            if c in country:
                print("it is already in list")
            else:
                n=input("enter the population:")
                country[c] = n
        elif choicec=="remove":
            cin=input("enter the name of country:")
            cci=cin.casefold()
            if cci in country:
                del country[cci]
                print(f"list after delete {cci}:", country)
            else:
                print("it is not exist in list")


        elif choicec=="print":
            for k, v in country.items():
                print(f"{k}==> {v} \n")

        elif choicec=="query":
            c1=input("enter the name of country:")
            if c1 in country:
                print(f"{c1} have {country[c1]}C population")
            else:
                print("it is not exist in list")
        u=input("do you want to continue? press y else n")
#q2
dic={"info":[600,630,620], "ril":[1430,1490,1567],"mtl":[234,180,160]}
q="y"
sum = 0

while q=='y' or q=='Y':
    print("you have two choice print and add ")
    choice2 = input("enter your choice:")
    choice2c = choice2.casefold()
    if choice2c=="print":
        for k, v in dic.items():
            for i in v:
                sum = sum+i

            avg=sum/len(v)
            print(f"{k}==> {v} ==> avg:{avg}")
    elif choice2c == "add":
        stoke= input("enter the stoke name:")
        stokec = stoke.casefold()
        if stokec in dic:
            print("it is already in list do you want to add e new value?")
            oh=input("if you want to add type 'y' if not type 'n':")
            if oh=='y' or oh=='Y':
                new_value=int(input("enter the value:"))
                dic[stokec].append(new_value)
            else:
                continue
        else:
            print("it will create a new entry")
            new_value=int(input("enter the value of new entry:"))
            dic[stokec]=[new_value]
    q = input("you want to continue: if yes type 'y'")
#q3
import math
def circle_calc(r):
    area=math.pi*(r**2)
    circumference=2*math.pi*r
    diameter=2*r
    return area, circumference,diameter

if __name__=="__main__":
    r=float(input("enter the radius:"))
    a,c,d=circle_calc(r=r)
    print(f"area {a}, circumference {c}, diameter {d}")
