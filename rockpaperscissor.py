import random
print("0-Rock\n1-Paper\n2-Scissors")
user_choice=int(input("Enter ur choice"))
if user_choice>=3 or user_choice<0:
    print("Invalid")
else:
    compt_choice=random.randint(0,2)
    print(compt_choice)
    if user_choice==compt_choice:
        print("drop no points to both")
    elif user_choice == 0 and compt_choice == 2:
        print("User win")
    elif user_choice == 2 and compt_choice == 0:
        print("Compt Win")
    elif compt_choice>user_choice:
        print("Compt win")
    else:
        print("User win")
    