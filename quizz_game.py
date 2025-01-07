
questions = (
    "How many elements are in the periodic table?: ",
    "Which animal lays the largest eggs?: ",
    "What is the most abundant gas in Earth's atmosphere?: ",
    "How many bones are in the human body?: ",
    "Which planet in the solar system is the hottest?: "
)

options = (
    ("A. 116", "B. 117", "C. 118", "D. 119"),
    ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
    ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"),
    ("A. 206", "B. 207", "C. 208", "D. 209"),
    ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"),
)

answers = ("C", "D", "A", "A", "B")
guesses = []
score = 0
question_num = 0

# Loop over each question
for question in questions:
    print("----------------------")
    print(question)  # Print the current question

    # Print the options for the current question
    for option in options[question_num]:
        print(option)

    # Get user's answer
    guess = input("Enter your answer (A, B, C, D): ").upper()

    # Store the guess
    guesses.append(guess)

    # Check if the answer is correct
    if guess == answers[question_num]:
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

    question_num += 1  # Move to the next question

# Print final score
print("----------------------")
print(f"Your final score is: {score} out of {len(questions)}")
