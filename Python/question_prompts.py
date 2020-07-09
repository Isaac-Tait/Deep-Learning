import Question from Question

question_prompts = [
    "The following are species of native trout found in Tohoku Japan except?\n(a)Yamame\n(b)Iwana\n(c)Golden Trout\n\n",
    "A VW Bus is also referred to the following except?\n(a)Fat Chick\n(b)Type 2\n(c)Van\n\n",
    "The nick names for US Marines are all of these except?\n(a)Leatherneck\n(b)Devil Dog\n(c)Soldier\n\n"
]

questions = [
    Question(question_prompts[0], "c"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "c")
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer
            score += 1
    print("You got " + str(score) + " out of" + str(len(questions)) + " correct")

run_test(questions)

# I am not sure why this is not working (and why is this file name underlined in red?)...
