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
