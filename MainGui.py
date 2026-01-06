import tkinter as tk
import random
import winsound

# -------------------- Game Logic --------------------
CHOICES = {1: "Snake 🐍", -1: "Water 💧", 0: "Gun 🔫"}

player_score = 0
computer_score = 0
dark_mode = True


def play(user_choice):
    global player_score, computer_score

    computer_choice = random.choice([-1, 0, 1])

    user_label.config(text=f"You: {CHOICES[user_choice]}")
    computer_label.config(text=f"Computer: {CHOICES[computer_choice]}")

    if user_choice == computer_choice:
        result = "It's a Draw!"
        winsound.MessageBeep(winsound.MB_ICONASTERISK)
    else:
        if (computer_choice == -1 and user_choice == 1) or \
           (computer_choice == 1 and user_choice == 0) or \
           (computer_choice == 0 and user_choice == -1):
            result = "🎉 You Win!"
            player_score += 1
            winsound.MessageBeep(winsound.MB_ICONEXCLAMATION)
        else:
            result = "❌ You Lose!"
            computer_score += 1
            winsound.MessageBeep(winsound.MB_ICONHAND)

    result_label.config(text=result)
    score_label.config(
        text=f"Score  |  You: {player_score}  Computer: {computer_score}"
    )


def reset_game():
    global player_score, computer_score
    player_score = 0
    computer_score = 0

    user_label.config(text="You: ")
    computer_label.config(text="Computer: ")
    result_label.config(text="")
    score_label.config(text="Score  |  You: 0  Computer: 0")


def toggle_theme():
    global dark_mode
    dark_mode = not dark_mode

    bg = "#1e1e1e" if dark_mode else "#f5f5f5"
    fg = "#ffffff" if dark_mode else "#000000"
    btn = "#333333" if dark_mode else "#dddddd"

    root.config(bg=bg)
    for widget in root.winfo_children():
        if isinstance(widget, tk.Label):
            widget.config(bg=bg, fg=fg)
        if isinstance(widget, tk.Frame):
            widget.config(bg=bg)
            for child in widget.winfo_children():
                if isinstance(child, tk.Button):
                    child.config(bg=btn, fg=fg)

    theme_btn.config(text="🌙 Dark Mode" if dark_mode else "☀️ Light Mode")


# -------------------- UI Setup --------------------
root = tk.Tk()
root.title("Snake Water Gun Game")
root.geometry("500x520")
root.resizable(False, False)
root.config(bg="#1e1e1e")

# Title
title = tk.Label(
    root, text="Snake Water Gun",
    font=("Segoe UI", 22, "bold"),
    bg="#1e1e1e", fg="white"
)
title.pack(pady=15)

# Labels
user_label = tk.Label(root, text="You: ", font=("Segoe UI", 12), bg="#1e1e1e", fg="white")
user_label.pack(pady=5)

computer_label = tk.Label(root, text="Computer: ", font=("Segoe UI", 12), bg="#1e1e1e", fg="white")
computer_label.pack(pady=5)

result_label = tk.Label(root, text="", font=("Segoe UI", 16, "bold"), bg="#1e1e1e", fg="white")
result_label.pack(pady=15)

score_label = tk.Label(
    root, text="Score  |  You: 0  Computer: 0",
    font=("Segoe UI", 12),
    bg="#1e1e1e", fg="white"
)
score_label.pack(pady=10)

# Buttons Frame
btn_frame = tk.Frame(root, bg="#1e1e1e")
btn_frame.pack(pady=20)

def create_btn(text, cmd):
    return tk.Button(
        btn_frame, text=text, width=12, height=2,
        font=("Segoe UI", 11),
        bg="#333333", fg="white",
        activebackground="#555555",
        command=cmd
    )

create_btn("Snake 🐍", lambda: play(1)).grid(row=0, column=0, padx=10)
create_btn("Water 💧", lambda: play(-1)).grid(row=0, column=1, padx=10)
create_btn("Gun 🔫", lambda: play(0)).grid(row=0, column=2, padx=10)

# Control Buttons
control_frame = tk.Frame(root, bg="#1e1e1e")
control_frame.pack(pady=20)

theme_btn = tk.Button(
    control_frame, text="🌙 Dark Mode",
    width=14, command=toggle_theme
)
theme_btn.grid(row=0, column=0, padx=10)

reset_btn = tk.Button(
    control_frame, text="🔄 Reset Game",
    width=14, command=reset_game
)
reset_btn.grid(row=0, column=1, padx=10)

# Footer
footer = tk.Label(
    root, text="Built with Python & Tkinter",
    font=("Segoe UI", 9),
    bg="#1e1e1e", fg="gray"
)
footer.pack(side="bottom", pady=10)

root.mainloop()
