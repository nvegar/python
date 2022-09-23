#ask for age
age = input("How old are you?: ")
if age != "":
    if int(age) >= 18 and int(age) < 21:
        print("You can enter, but you cannot drink, except water for hydration XD")
        #18-21 Not able to drink
    elif int(age) < 18:
        print("So sorry little boy, you cannot enter :( ")
        #too young, sorry :(
    else:
        print("Enjoy, you can drink and do whatever legal thing you may want! OwO")
        #21+ drink, normal entry
else:
    print("Please enter an age")




