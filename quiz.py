#series of Python-related questions
Quizgame = {
    1: {
        "question": "What is the output of print(2**3%5) in python?",
        "options": ["15", "88", "3", "9"],
        "answer": "3"
    },
    2: {
        "question": "What does the input() function do in Python?",
        "options": ["Displays output on the screen", 
                    "Reads input from the user", 
                    "Converts a string to an integer",
                    "Converts an integer to a string"],
        "answer": "Reads input from the user"
    },
    3: {
        "question": "What is the output of (a=True; b=10.5; c=a+b;print(c);)",
        "options": ["11.5", "89", "56", "57"],
        "answer": "11.5"
    },
    4: {
        "question": "What is the purpose of the break and continue statements in Python?",
        "options": ["break ends the loop and continue skips to the next iteration.",
                    "Both break and continue end the loop.",
                    "break skips to the next iteration, continue ends the loop.",
                    "Both break and continue skip to the next iteration."],
        "answer": "break ends the loop, continue skips to the next iteration."
    },

    5: {
        "question": "Which operation adds an element to the end of a list in Python?",
        "options": [".add()", ".insert()", ".append()", ".extend()"],
        "answer": ".append()"
    },

    6: {
        "question": "What are tuples in Python?",
        "options": ["Mutable collections", "Square bracket notation", "Ordered collections", "Homogeneous data only"],
        "answer": "Ordered collections"
    }
}
score = 0
attempts = 3
for question in Quizgame:
    print(Quizgame[question]["question"])
    for i, option in enumerate(Quizgame[question]["options"], start=1):
        print(f"{i}. {option}")
    
    while True:
        answer = input("Enter your answer (1-4): ")
        if answer.isdigit() and 1 <= int(answer) <= 4:
            break
        else:
            print("Invalid input. Please enter a number between 1 and 4.")

    if Quizgame[question]["answer"] == Quizgame[question]["options"][int(answer) - 1]:
        print("Correct!")
        score += 1
    else:
        print("Incorrect. The correct answer is:", Quizgame[question]["answer"])
        attempts -= 1
        if attempts == 0:
            print("You have run out of attempts. Moving on to the next question...")
            attempts = 3

print(f"Your final score is {score}/{len(Quizgame)}")

