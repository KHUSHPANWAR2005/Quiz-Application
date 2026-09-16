import tkinter as tk
import random
import os
from PIL import Image, ImageTk


# ================= QUESTIONS =================

questions = [
    {
        "question": "Which language is known as the language of data science?",
        "options": ["Python", "HTML", "CSS", "SQL"],
        "answer": "Python"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["function", "def", "fun", "define"],
        "answer": "def"
    },
    {
        "question": "Which data type is used to store multiple values in Python?",
        "options": ["int", "float", "list", "bool"],
        "answer": "list"
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "options": ["//", "#", "/*", "--"],
        "answer": "#"
    },
    {
        "question": "Which function is used to display output in Python?",
        "options": ["display()", "show()", "print()", "output()"],
        "answer": "print()"
    },
    {
        "question": "Which of these is an immutable data type?",
        "options": ["List", "Dictionary", "Set", "Tuple"],
        "answer": "Tuple"
    },
    {
        "question": "What is the extension of a Python file?",
        "options": [".java", ".py", ".html", ".cpp"],
        "answer": ".py"
    },
    {
        "question": "Which operator is used for exponentiation in Python?",
        "options": ["^", "**", "//", "%%"],
        "answer": "**"
    },
    {
        "question": "Which function is used to find the length of a list?",
        "options": ["size()", "length()", "len()", "count()"],
        "answer": "len()"
    },
    {
        "question": "Which keyword is used to create a class in Python?",
        "options": ["object", "class", "define", "struct"],
        "answer": "class"
    }
]


# ================= SETTINGS =================

TOTAL_QUESTIONS = 5
TIME_PER_QUESTION = 15


# ================= MAIN WINDOW =================

root = tk.Tk()
root.title("Python Quiz Application")
root.geometry("1000x650")
root.resizable(False, False)

# ================= OCEAN BACKGROUND =================

image_path = r"C:\Users\khush\OneDrive\Documents\training\PROJECT\ocean_background.png.jpeg"

bg_image = Image.open(image_path)
bg_image = bg_image.resize((1000, 650))

background_photo = ImageTk.PhotoImage(bg_image)

background_label = tk.Label(
    root,
    image=background_photo,
    borderwidth=0
)

background_label.place(
    x=0,
    y=0,
    width=1000,
    height=650
)

# ================= VARIABLES =================

quiz_questions = []
current_question = 0
score = 0
time_left = TIME_PER_QUESTION
selected_answer = tk.StringVar()
timer_id = None


# ================= FUNCTIONS =================

def start_quiz():

    global quiz_questions, current_question, score

    quiz_questions = random.sample(
        questions,
        min(TOTAL_QUESTIONS, len(questions))
    )

    current_question = 0
    score = 0

    start_frame.place_forget()
    result_frame.place_forget()

    quiz_frame.place(
        x=570,
        y=70,
        width=390,
        height=550
    )

    load_question()


def load_question():

    global time_left, timer_id

    if current_question >= len(quiz_questions):
        show_result()
        return

    selected_answer.set("")

    question_data = quiz_questions[current_question]

    question_number_label.config(
        text=f"Question {current_question + 1} / {len(quiz_questions)}"
    )

    question_label.config(
        text=question_data["question"]
    )

    options = question_data["options"]

    for i in range(4):
        option_buttons[i].config(
            text=options[i],
            value=options[i]
        )

    time_left = TIME_PER_QUESTION

    timer_label.config(
        text=f"⏱ {time_left} sec"
    )

    if timer_id is not None:

        try:
            root.after_cancel(timer_id)
        except:
            pass

    countdown()


def countdown():

    global time_left, timer_id

    timer_label.config(
        text=f"⏱ {time_left} sec"
    )

    if time_left > 0:

        time_left -= 1

        timer_id = root.after(
            1000,
            countdown
        )

    else:
        next_question()


def next_question():

    global current_question, score

    if timer_id is not None:

        try:
            root.after_cancel(timer_id)
        except:
            pass

    correct_answer = quiz_questions[current_question]["answer"]

    user_answer = selected_answer.get()

    if user_answer == correct_answer:
        score += 1

    current_question += 1

    load_question()


def show_result():

    quiz_frame.place_forget()

    result_frame.place(
        x=300,
        y=80,
        width=400,
        height=500
    )

    percentage = (
        score / len(quiz_questions)
    ) * 100

    score_label.config(
        text=f"{score} / {len(quiz_questions)}"
    )

    percentage_label.config(
        text=f"Percentage: {percentage:.1f}%"
    )

    if percentage >= 80:

        message_label.config(
            text="🌟 Excellent!",
            fg="#00a86b"
        )

    elif percentage >= 50:

        message_label.config(
            text="👍 Good Job!",
            fg="#1264d8"
        )

    else:

        message_label.config(
            text="💪 Keep Practicing!",
            fg="#e63946"
        )


def restart_quiz():

    result_frame.place_forget()

    start_frame.place(
        x=50,
        y=100,
        width=450,
        height=480
    )


def exit_quiz():

    root.destroy()


# =========================================================
# START SCREEN
# =========================================================

start_frame = tk.Frame(
    root,
    bg="#d9f3ff",
    highlightthickness=2,
    highlightbackground="white"
)

start_frame.place(
    x=50,
    y=100,
    width=450,
    height=480
)


# Python Logo Text

python_logo = tk.Label(
    start_frame,
    text="🐍",
    font=("Arial", 55),
    bg="#d9f3ff"
)

python_logo.pack(
    pady=(20, 0)
)


title_label = tk.Label(
    start_frame,
    text="Python Quiz",
    font=("Arial", 34, "bold"),
    bg="#d9f3ff",
    fg="#064b91"
)

title_label.pack(
    pady=5
)


subtitle_label = tk.Label(
    start_frame,
    text="Test your Python knowledge!",
    font=("Arial", 17, "bold"),
    bg="#d9f3ff",
    fg="#164e78"
)

subtitle_label.pack(
    pady=5
)


info_label = tk.Label(
    start_frame,
    text="❓ 5 Questions     ⏱ 15 sec Each     🔀 Random",
    font=("Arial", 11, "bold"),
    bg="#d9f3ff",
    fg="#27648a"
)

info_label.pack(
    pady=20
)


# START BUTTON

start_button = tk.Button(
    start_frame,
    text="▶  Start Quiz",
    font=("Arial", 17, "bold"),
    width=20,
    height=2,
    bg="#087ff5",
    fg="white",
    activebackground="#0564c8",
    activeforeground="white",
    relief="flat",
    cursor="hand2",
    command=start_quiz
)

start_button.pack(
    pady=15
)


# EXIT BUTTON

exit_button = tk.Button(
    start_frame,
    text="Exit",
    font=("Arial", 14, "bold"),
    width=15,
    bg="#bde7fa",
    fg="#064b91",
    activebackground="#94d8f3",
    relief="flat",
    cursor="hand2",
    command=exit_quiz
)

exit_button.pack(
    pady=5
)


# =========================================================
# QUIZ SCREEN
# =========================================================

quiz_frame = tk.Frame(
    root,
    bg="#e9f8ff",
    highlightthickness=2,
    highlightbackground="white"
)


# Header

header = tk.Frame(
    quiz_frame,
    bg="#0875d1",
    height=65
)

header.pack(
    fill="x"
)


question_number_label = tk.Label(
    header,
    text="Question 1 / 5",
    font=("Arial", 15, "bold"),
    bg="#0875d1",
    fg="white"
)

question_number_label.pack(
    side="left",
    padx=20,
    pady=18
)


timer_label = tk.Label(
    header,
    text="⏱ 15 sec",
    font=("Arial", 14, "bold"),
    bg="#ffd23f",
    fg="#164e78",
    padx=12,
    pady=7
)

timer_label.pack(
    side="right",
    padx=15,
    pady=10
)


# Question

question_card = tk.Frame(
    quiz_frame,
    bg="white"
)

question_card.pack(
    padx=20,
    pady=20,
    fill="x"
)


question_label = tk.Label(
    question_card,
    text="Question",
    font=("Arial", 17, "bold"),
    wraplength=330,
    justify="center",
    bg="white",
    fg="#064b91"
)

question_label.pack(
    padx=15,
    pady=25
)


# Options

option_buttons = []

for i in range(4):

    button = tk.Radiobutton(
        quiz_frame,
        text="Option",
        variable=selected_answer,
        value="",
        font=("Arial", 13, "bold"),
        bg="white",
        fg="#164e78",
        selectcolor="#a9e4ff",
        activebackground="#dff6ff",
        anchor="w",
        padx=12,
        pady=7,
        relief="solid",
        bd=1,
        cursor="hand2"
    )

    button.pack(
        padx=25,
        pady=5,
        fill="x"
    )

    option_buttons.append(button)


# NEXT BUTTON

next_button = tk.Button(
    quiz_frame,
    text="Next  →",
    font=("Arial", 14, "bold"),
    width=15,
    height=1,
    bg="#10b981",
    fg="white",
    activebackground="#059669",
    activeforeground="white",
    relief="flat",
    cursor="hand2",
    command=next_question
)

next_button.pack(
    pady=18
)


# =========================================================
# RESULT SCREEN
# =========================================================

result_frame = tk.Frame(
    root,
    bg="#e9f8ff",
    highlightthickness=2,
    highlightbackground="white"
)


result_icon = tk.Label(
    result_frame,
    text="🏆",
    font=("Arial", 55),
    bg="#e9f8ff"
)

result_icon.pack(
    pady=(35, 5)
)


result_title = tk.Label(
    result_frame,
    text="QUIZ COMPLETED!",
    font=("Arial", 26, "bold"),
    bg="#e9f8ff",
    fg="#064b91"
)

result_title.pack(
    pady=5
)


score_label = tk.Label(
    result_frame,
    text="0 / 5",
    font=("Arial", 42, "bold"),
    bg="#e9f8ff",
    fg="#0875d1"
)

score_label.pack(
    pady=10
)


percentage_label = tk.Label(
    result_frame,
    text="Percentage: 0%",
    font=("Arial", 16, "bold"),
    bg="#e9f8ff",
    fg="#164e78"
)

percentage_label.pack(
    pady=5
)


message_label = tk.Label(
    result_frame,
    text="",
    font=("Arial", 19, "bold"),
    bg="#e9f8ff"
)

message_label.pack(
    pady=20
)


restart_button = tk.Button(
    result_frame,
    text="🔄  Restart Quiz",
    font=("Arial", 14, "bold"),
    width=20,
    height=2,
    bg="#087ff5",
    fg="white",
    activebackground="#0564c8",
    relief="flat",
    cursor="hand2",
    command=restart_quiz
)

restart_button.pack(
    pady=10
)


exit_result_button = tk.Button(
    result_frame,
    text="Exit",
    font=("Arial", 12, "bold"),
    width=15,
    bg="#bde7fa",
    fg="#064b91",
    activebackground="#94d8f3",
    relief="flat",
    cursor="hand2",
    command=exit_quiz
)

exit_result_button.pack()


# =========================================================
# START APPLICATION
# =========================================================

start_frame.tkraise()

root.mainloop()