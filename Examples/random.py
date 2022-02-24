from tkinter.messagebox import YES


male = ["male", "boy", "man"]
female = ["female", "girl", "woman"]
stupid_loop_answers = ["yes", "no"]
yes = "yes"
no = "no"
def user_gender():
    gender = input("Enter your gender: ")
    if gender in male:
        print("You are a male")
    elif gender in female:
        print("You are a female")
    elif gender == "stupid":
        print("I told you to tell me your gender")
        return user_gender()
    elif gender == "no":
        print("Yes.")
        return stupid_loop()
    else:
        print("ERROR 404: Gender does not exist")
        return user_gender()

def stupid_loop(sla):
    input()
    if sla in stupid_loop_answers:



    

user_gender()