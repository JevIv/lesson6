quest = {
        "How do you do?":"Good!",
        "What are you doing?":"Programming",
        "what are you programming?":"Some interesting staff",
        "Do you enjoy programming?":"Hell yeah!",
        "Which language do you preffer to use?":"Python",
        "Are you a program?":"No, I'm a human!",
        "Do you have any plans for evening?":"Yes, going to watch a movie",
        "Do you have a car?":"Yes, Lamborghini Diablo",
        "Who are you?":"Your cat!",
        "Do you have a cat?":" I love them!",
}

def ask_user(quest):
    msg = ""
    condition = True

    while condition == True:
        try:
            print("Hello!")
            msg = input("Ask me a question!: ")

            for key, value in quest.items():
                answ = ""

                if msg == key:
                    answ = quest[f'{msg}']
                    print(answ)
                    condition = False
                else:
                    continue
        except(KeyboardInterrupt):
            print("\n\nBye, see you later!")
            break

ask_user(quest)
