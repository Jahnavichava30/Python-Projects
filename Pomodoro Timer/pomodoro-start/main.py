from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
# Colors used for different timer states
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"

# Time settings for Pomodoro
WORK_MIN = 1               # 25 minutes of work time
SHORT_BREAK_MIN = 5         # 5 minutes of short break time
LONG_BREAK_MIN = 20         # 20 minutes of long break time

# Initialize variables
reps = 0                     # Number of Pomodoro sessions (work/break cycles)
timer = None                 # To store reference to the running timer

# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    """Resets the timer, stops the countdown, and sets everything to initial state."""
    window.after_cancel(timer)  # Cancel the ongoing timer
    canvas.itemconfig(timer_text, text='00:00')  # Reset the timer display
    title_label.config(text='Timer')  # Reset the title to 'Timer'
    check_button.config(text='')  # Clear the check marks
    global reps
    reps = 0  # Reset the number of completed work sessions

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    """Starts the timer and alternates between work and break sessions."""
    global reps
    reps += 1  # Increment the number of reps (work/break cycles)

    work_sec = WORK_MIN * 60  # Convert work minutes to seconds
    short_break_sec = SHORT_BREAK_MIN * 60  # Convert short break minutes to seconds
    long_break_sec = LONG_BREAK_MIN * 60  # Convert long break minutes to seconds

    # Check if it's time for a long break (after 8 reps)
    if reps % 8 == 0:
        count_down(long_break_sec)  # Start long break
        title_label.config(text='Break', fg=RED)  # Set title and color to break
    # Check if it's time for a short break (every other rep)
    elif reps % 2 == 0:
        count_down(short_break_sec)  # Start short break
        title_label.config(text='Break', fg=PINK)  # Set title and color to break
    else:
        count_down(work_sec)  # Start work session
        title_label.config(text='Work', fg=GREEN)  # Set title and color to work

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    """Countdown mechanism that updates the timer every second."""
    count_min = math.floor(count / 60)  # Get the minutes from seconds
    count_sec = count % 60  # Get the remaining seconds
    if count_sec < 10:
        count_sec = f'0{count_sec}'  # Add leading zero if seconds are less than 10

    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')  # Update the timer display
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)  # Call count_down after 1 second
    else:
        start_timer()  # Once countdown finishes, start the next session (work/break)
        mark = ''
        work_session = math.floor(reps / 2)  # Calculate number of completed work sessions
        for _ in range(work_session):
            mark += "✔"  # Add checkmarks for completed work sessions
        check_button.config(text=mark)  # Display checkmarks

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()  # Create the main window
window.title("Pomodoro")  # Set the window title
window.config(padx=150, pady=50, bg=YELLOW)  # Set window padding and background color

# Timer label
title_label = Label(text='Timer', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)  # Place label in grid

# Canvas to display the timer
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file='tomato.png')  # Load image (ensure the file is available)
canvas.create_image(100, 112, image=tomato_image)  # Place the image on the canvas
timer_text = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 30, 'bold'))  # Timer text
canvas.grid(column=1, row=1)  # Place canvas in grid

# Start button
start_button = Button(text='Start', highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)  # Place button in grid

# Reset button
reset_button = Button(text='Reset', highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)  # Place button in grid

# Checkmarks label (for completed work sessions)
check_button = Label(text='✔', fg=GREEN, bg=YELLOW)
check_button.grid(column=1, row=3)  # Place label in grid

# Run the main window loop
window.mainloop()
