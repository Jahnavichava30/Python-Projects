# Import necessary libraries
from tkinter import *  # Import everything from tkinter for GUI
import pandas  # Import pandas for handling CSV files
import random  # Import random for selecting words randomly

# Set the background color for the application
BACKGROUND_COLOR = "#B1DDC6"

# Initialize variables to hold the current flashcard and words to learn
current_card = {}  # Stores the currently displayed word
to_learn = {}  # Dictionary to store words that need to be learned

# Try to load words from the 'words_to_learn.csv' file if it exists
try:
    data = pandas.read_csv("data/words_to_learn.csv")  # Read existing progress
except FileNotFoundError:
    # If the file is not found, load words from the original dataset
    original_data = pandas.read_csv("data/french_words.csv")
    print(original_data)  # Print the data for debugging (can be removed later)
    to_learn = original_data.to_dict(orient="records")  # Convert DataFrame to a list of dictionaries
else:
    to_learn = data.to_dict(orient="records")  # Convert loaded DataFrame to a list of dictionaries


# Function to display the next flashcard
def next_card():
    global current_card, flip_timer  # Use global variables
    window.after_cancel(flip_timer)  # Cancel the previous timer before starting a new one
    current_card = random.choice(to_learn)  # Pick a random word from the list

    # Update the canvas with the French word
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)  # Show front side of the card

    # Set a timer to flip the card after 3 seconds
    flip_timer = window.after(3000, func=flip_card)


# Function to flip the flashcard and show the English translation
def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")  # Change title to "English"
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")  # Show English translation
    canvas.itemconfig(card_background, image=card_back_img)  # Show back side of the card


# Function to handle when a user marks a word as known
def is_known():
    to_learn.remove(current_card)  # Remove the word from the list of words to learn
    print(len(to_learn))  # Print remaining words (for debugging)

    # Save the updated list of words to 'words_to_learn.csv'
    data = pandas.DataFrame(to_learn)  # Convert list to DataFrame
    data.to_csv("data/words_to_learn.csv", index=False)  # Save to CSV file without index

    # Show the next card
    next_card()


# Create the main application window
window = Tk()
window.title("Flashy")  # Set the window title
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)  # Add padding and set background color

# Set a timer to flip the card after 3 seconds
flip_timer = window.after(3000, func=flip_card)

# Create a canvas for the flashcard
canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")  # Load front card image
card_back_img = PhotoImage(file="images/card_back.png")  # Load back card image

# Add the card image to the canvas
card_background = canvas.create_image(400, 263, image=card_front_img)

# Add text placeholders for the word and language label
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))

# Configure the canvas background
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)  # Position the canvas at the top

# Load images for buttons
cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)  # Wrong button
unknown_button.grid(row=1, column=0)  # Position it in the first column

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=is_known)  # Right button
known_button.grid(row=1, column=1)  # Position it in the second column

# Display the first flashcard
next_card()

# Run the Tkinter main event loop
window.mainloop()
