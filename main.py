#function to determine expiring date of food by date format
#a=year, b=month, c=day
def date_input(a,b,c):
    from datetime import date
    #setting into date form
    d=date(a,b,c)
    return d

#function to determine if food is spoilt or not based on dates
#d=current_date, e=expiring_date
def comparing_date(d,e):
    import datetime
    print("TODAY'S DATE: ",d)
    print("EXPIRING DATE: ",e)
    #if expiring date is after today's date; e>d
    if e>d:
        print("FOOD IS SAFE TO BE EATEN.\n")
        choice = 0
        return choice
    #else if expiring date is the same as today's date; e==d
    elif e==d:
        print("TODAY IS THE LAST DAY TO EAT FOOD!!\n")
        choice = 0
        return choice
    #else a.k.a expiring date is before today's date; e<d
    else:
        print("FOOD HAS PASSED EXPIRING DATE!\n")
        print("WOULD YOU RATHER:\n1:throw the food away\n2:use food for suitable recipe (recommended)\n")
        choice = int(input("ENTER YOUR CHOICE ACCORDING TO THE NUMBERS (1 OR 2): "))
        return choice


#project's name
print("FOOD WASTE REDUCTION\n")


#to get today's date
from datetime import date
todate=date.today()
print("TODAY IS ", todate,"\n")


#preparing lists involved
food = []
type_food = []
expiring_date = []


#is the user a first time user or not?
user=(input("ARE YOU A FIRST TIME USER? Y(yes) or N(no): "))
if user=='Y':
    print("\nWELCOME!!\n")
elif user=='N':
    newdata_olddata = int(input("WELCOME BACK!! DO YOU WANT TO:\n   1)ENTER NEW FOOD DATA\n   2)REFER TO OLD DATA?\nENTER '1' OR '2': "))
    if newdata_olddata==1:
        print("VERY WELL! LET'S PROCEED!")
    elif newdata_olddata==2:
        read_file= open('food.txt','r')
        print("THE FOLLOWING IS WHAT WRITTEN IN YOUR FILE (IF YOUR FILE DOESN'T EXIST, NOTHING WILL BE SHOWN):")
        print(read_file.read())
        exit()
else:
    print("DUE TO INCOMPREHENSIBLE INPUT, THIS STEP WILL BE SKIPPED AND PROGRAM WILL PROCEED AS USUAL.")


#asking user to enter number of food in posession
no_food = int(input("ENTER NUMBER OF FOOD IN POSESSION: "))


print("\n")
print("YOU HAVE ",no_food," FOOD.")
print("PLEASE ENTER THE DETAILS REQUIRED FOR EACH FOOD ACCORDING TO INSTRUCTION.")
print("\n")


#asking user to enter food's details
for i in range(no_food):
    food.append(input("ENTER FOOD NAME: "))
    type_food.append(input("ENTER TYPE OF FOOD: "))
    year=int(input("ENTER THE YEAR OF THE EXPIRING DATE: "))
    month=int(input("ENTER THE MONTH OF THE EXPIRING DATE: "))
    day=int(input("ENTER THE DAY OF THE EXPIRING DATE: "))
    date_expired = date_input(year,month,day)
    expiring_date.append(date_expired)
    print("\n")


#printing user's food
print("THE FOLLOWING ARE YOUR FOOD:")
for i in food:
    print(i)

#preparing list for type of choice
str_choice = []

#checking if the food is expired
print("\nCHECKING EACH FOOD...")
for i in range(no_food):
    print("\nCHECKING ",food[i])
    choice = comparing_date(todate,expiring_date[i])
    if choice==1:
        print("PLEASE DISPOSE OF THE FOOD PROPERLY.\n")
        str_choice.append("one")
    elif choice==2:
        print("GOOD LUCK SEARCHING FOR THE RECIPE!!")
        print("HERE ARE WEBSTIES SUGGESTION FOR RECIPES:\n ->http://foodcombo.com\n ->http://supercook.com\n")
        str_choice.append("two")
    else:
        str_choice.append("zero")
        continue


#asking user if they would like to store information of their food to refer to later
save=(input("WOULD YOU LIKE TO SAVE YOUR FOOD DATA? Y(yes) OR N(no): "))
if save=='Y':
    print("YOUR FILE NAME WILL BE: food")
    open_file= open('food.txt','w') #creating file
    line1="FILE INCLUDES NAME OF FOOD, TYPE OF FOOD, AND IF 0(zero):HASN'T EXPIRED, 1(one) OR 2(two):EXPIRED.\n"
    open_file.write(line1)
    for i in range(no_food):

        line_space="\n"

        line2="NAME OF FOOD: "
        open_file.write(line2)
        open_file.write(food[i])
        open_file.write(line_space)

        line3="TYPE OF FOOD: "
        open_file.write(line3)
        open_file.write(type_food[i])
        open_file.write(line_space)

        line4="SITUATION: "
        open_file.write(line4)
        open_file.write(str_choice[i])
        open_file.write(line_space)

        open_file.write(line_space)
    print("FILE IS SAVED AND CAN BE ACCESSED IN THE FUTURE.")
elif save=='N':
    print("DATA WILL NOT BE SAVED.")
else:
    print("DUE TO INCOMPREHENSIBLE INPUT, THIS STEP WILL BE SKIPPED.")


#closure
print("\nTHANK YOU FOR DROPPING BY!! LET'S ALL REDUCE FOOD WASTE!!\n")
