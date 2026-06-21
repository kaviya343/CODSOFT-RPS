import tkinter as tk
import random

# ---------------- COLORS ----------------
BG = "#0f172a"
CARD = "#1e293b"
BLUE = "#38bdf8"
GREEN = "#22c55e"
RED = "#ef4444"
ORANGE = "#f59e0b"
WHITE = "#f8fafc"

# ---------------- GAME DATA ----------------
choices = ["Rock", "Paper", "Scissors"]

user_score = 0
computer_score = 0

# ---------------- FUNCTIONS ----------------
def play(user_choice):
    global user_score, computer_score

    computer_choice = random.choice(choices)

    user_choice_label.config(
        text=f"Your Choice : {user_choice}"
    )

    computer_choice_label.config(
        text=f"Computer Choice : {computer_choice}"
    )

    if user_choice == computer_choice:
        result_label.config(
            text="🤝 MATCH TIED!",
            fg=ORANGE
        )

    elif (
        (user_choice == "Rock" and computer_choice == "Scissors")
        or
        (user_choice == "Paper" and computer_choice == "Rock")
        or
        (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        user_score += 1

        result_label.config(
            text="🏆 YOU WON!",
            fg=GREEN
        )

    else:
        computer_score += 1

        result_label.config(
            text="💻 COMPUTER WON!",
            fg=RED
        )

    score_label.config(
        text=f"You : {user_score}    |    Computer : {computer_score}"
    )


def reset_game():
    global user_score, computer_score

    user_score = 0
    computer_score = 0

    score_label.config(
        text="You : 0    |    Computer : 0"
    )

    user_choice_label.config(
        text="Your Choice : -"
    )

    computer_choice_label.config(
        text="Computer Choice : -"
    )

    result_label.config(
        text="Choose an Option",
        fg=BLUE
    )


# ---------------- WINDOW ----------------
root = tk.Tk()
root.title("Rock Paper Scissors Pro")
root.geometry("850x600")
root.configure(bg=BG)
root.resizable(False, False)

# ---------------- HEADER ----------------
title = tk.Label(
    root,
    text="🎮 ROCK PAPER SCISSORS PRO",
    bg=BG,
    fg=BLUE,
    font=("Segoe UI", 24, "bold")
)
title.pack(pady=20)

# ---------------- SCORE CARD ----------------
score_frame = tk.Frame(
    root,
    bg=CARD,
    bd=0
)
score_frame.pack(pady=10)

score_title = tk.Label(
    score_frame,
    text="SCORE BOARD",
    bg=CARD,
    fg=WHITE,
    font=("Segoe UI", 12, "bold")
)
score_title.pack(pady=5)

score_label = tk.Label(
    score_frame,
    text="You : 0    |    Computer : 0",
    bg=CARD,
    fg=GREEN,
    font=("Segoe UI", 18, "bold")
)
score_label.pack(padx=40, pady=15)

# ---------------- STATUS CARD ----------------
status_frame = tk.Frame(
    root,
    bg=CARD
)
status_frame.pack(pady=15)

result_label = tk.Label(
    status_frame,
    text="Choose an Option",
    bg=CARD,
    fg=BLUE,
    font=("Segoe UI", 18, "bold")
)
result_label.pack(padx=50, pady=20)

# ---------------- BUTTONS ----------------
button_frame = tk.Frame(
    root,
    bg=BG
)
button_frame.pack(pady=20)

rock_btn = tk.Button(
    button_frame,
    text="🪨 ROCK",
    width=15,
    height=2,
    bg=BLUE,
    fg="black",
    font=("Segoe UI", 11, "bold"),
    command=lambda: play("Rock")
)
rock_btn.grid(row=0, column=0, padx=15)

paper_btn = tk.Button(
    button_frame,
    text="📄 PAPER",
    width=15,
    height=2,
    bg=GREEN,
    fg="black",
    font=("Segoe UI", 11, "bold"),
    command=lambda: play("Paper")
)
paper_btn.grid(row=0, column=1, padx=15)

scissors_btn = tk.Button(
    button_frame,
    text="✂ SCISSORS",
    width=15,
    height=2,
    bg=RED,
    fg="white",
    font=("Segoe UI", 11, "bold"),
    command=lambda: play("Scissors")
)
scissors_btn.grid(row=0, column=2, padx=15)

# ---------------- RESULT SECTION ----------------
result_frame = tk.Frame(
    root,
    bg=CARD
)
result_frame.pack(pady=20)

user_choice_label = tk.Label(
    result_frame,
    text="Your Choice : -",
    bg=CARD,
    fg=WHITE,
    font=("Segoe UI", 14)
)
user_choice_label.pack(pady=10)

computer_choice_label = tk.Label(
    result_frame,
    text="Computer Choice : -",
    bg=CARD,
    fg=WHITE,
    font=("Segoe UI", 14)
)
computer_choice_label.pack(pady=10)

# ---------------- CONTROL BUTTONS ----------------
control_frame = tk.Frame(
    root,
    bg=BG
)
control_frame.pack(pady=25)

reset_btn = tk.Button(
    control_frame,
    text="🔄 RESET GAME",
    width=18,
    bg=ORANGE,
    fg="black",
    font=("Segoe UI", 10, "bold"),
    command=reset_game
)
reset_btn.grid(row=0, column=0, padx=20)

exit_btn = tk.Button(
    control_frame,
    text="❌ EXIT",
    width=18,
    bg=RED,
    fg="white",
    font=("Segoe UI", 10, "bold"),
    command=root.destroy
)
exit_btn.grid(row=0, column=1, padx=20)

# ---------------- RUN ----------------
root.mainloop()