import tkinter as tk
from tkinter import messagebox, ttk
from ttkbootstrap import style
from data import quiz_data

# function will display the current question and choices
def show_question():
    # lets get current question from quiz_data list
    question = quiz_data[current_question]
    qs_label.config(text=question["question"])

    # Display the choices on buttons
    choices = question["choices"]
    for i in range(4):
        choice_btns[i].config(text=choices[i], state="normal") # Reset next button

    # Clear feedback labe; and disable the next button
    fb_label.config(text="")
    next_btn.config(state="disabled")

# function to check selected answer and provide feedback
def check_ans():
    # get current question from the quiz_data
    question = quiz_data[current_question]
    selected_choice = choice_btns[choice].cget("text")

    # check if selected choice matches the correct one
    if selected_choice == question["answer"]:
        #Update the score and display it
        global score
        score += 1
        score_label.config(text="Score: {}/{}".format(score, len(quiz_data)))
        fb_label.config(text="Correct!", foreground="green")
    else:
        fb_label.config(text="Incorrect!", foreground="red")

    # Disable all choice button and enable the next button
    for button in choice_btns:
        button.config(state="disabled")
    next_btn.config(state="normal")

# function to move to the next question
def next_question():
    global current_question
    current_question += 1

    if current_question < len(quiz_data):
        # if there are more questions, show the next question
        show_question()
    else:
        # if all have been answered, display result
        messagebox.showinfo("Quiz Completed",
                            "Quiz Completed! Final Score: {}/{}".format(score, len(quiz_data)))
        root.destroy()

# build the main window
root = tk.Tk()
root.title("ALX_SWE Simple Quiz")
root.geometry("600x500")
style = style(theme="flatly")

# configure the font size for the question and choice buttons
style.configure("TLabel", font=("Helvetica", 20))
style.configure("TButton", font=("Helvetica", 18))

# build question label
qs_label = ttk.Label(
    root,
    anchor="center",
    wraplength
    padding=10
)
qs_label.pack(pady=10)

# Build choice buttons
choice_btns = []
for i in range(4):
    button = ttk.Button(
        root,
        command=lambda i=i: check_ans(i)
    )
    button.pack(pady=5)
    choice_btns.append(button)

# Create the feedback label
fb_label = ttk.label(
    root,
    anchor="center",
    padding=10
)
fb_label.pack(pady=10)

# let intialize the score
score = 0

# now build the score label
score_label = ttk.Label(
    root,
    text="Score: 0/{}".format(len(quiz_data)),
    anchor="center",
    padding=10
)
score_label.pack(pady=10)

# Build the next button
next_btn = ttk.Button(
    root,
    text="Next",
    command=next_question,
    state="disabled"
)
next_btn.pack(pady=0)

#Intialize the current question index
current_question = 0

# show the first question
show_question()

#
