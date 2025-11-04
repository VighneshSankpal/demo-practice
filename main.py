from data import quetions,options,ans
def print_question(score):
    pass

def check_ans():
    pass
score = 0
while score<10:
    
    print("Welcome to the KBC game.")
    print("You get 10 questions and 4 options you choose the correct options and the game will continue untill you answer wrong.")

    check_ready = input("Type 'y' if you are ready! ")
    if not (check_ready.lower() =='y'):
        break
    print("Let's Start the game!!!")
    print_question(score)
    if check_ans():
        score+=1
    print("Congrats!! you select right option.")
    print(f"Your score is {score}.")
    

