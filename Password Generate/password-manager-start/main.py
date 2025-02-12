# Import necessary libraries
from tkinter import *  # Import all modules from Tkinter for GUI
from PIL import Image, ImageTk  # Import Image and ImageTk from PIL for handling images
from tkinter import messagebox  # Import messagebox for popup messages
from random import choice, randint, shuffle  # Import functions for generating random passwords
import pyperclip  # Import pyperclip to copy the generated password to the clipboard

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    """
    Generates a random password using letters, numbers, and symbols.
    The generated password is inserted into the password entry field and copied to the clipboard.
    """

    # List of characters to use in password
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
               'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # Generate a random selection of letters, numbers, and symbols
    password_letters = [choice(letters) for _ in range(randint(8, 10))]  # Pick 8-10 random letters
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]  # Pick 2-4 random symbols
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]  # Pick 2-4 random numbers

    # Combine all selected characters
    password_list = password_letters + password_symbols + password_numbers

    # Shuffle the characters randomly
    shuffle(password_list)

    # Convert list to string
    password = "".join(password_list)

    # Insert password into the password entry field
    password_entry.insert(0, password)

    # Copy password to clipboard
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    """
    Saves the entered website, email, and password into a text file.
    Shows an error message if any field is empty.
    Asks for user confirmation before saving.
    """

    # Get values from entry fields
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    # Validate if website or password fields are empty
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title='Oops', message="Please make sure you haven't left any fields empty.")
    else:
        # Ask for user confirmation before saving
        is_ok = messagebox.askokcancel(title=website, message=f'These are the details entered: \nEmail: {email}'
                                                      f'\nPassword: {password} \nIs it ok to save?')
        if is_ok:
            # Save the credentials into a file
            with open('data.txt', 'a') as data_file:  # Open the file in append mode
                data_file.write(f"{website} | {email} | {password}\n")  # Write details
                # Clear the website and password fields
                website_entry.delete(0, END)
                password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
# Create the main window
window = Tk()
window.title("Password Manager")  # Set window title
window.config(padx=50, pady=50)  # Add padding around the window

# Create a canvas for displaying the logo image
canvas = Canvas(height=200, width=200)

# Load and display the logo image
image = Image.open("logo.png")  # Open image using PIL
logo_img = ImageTk.PhotoImage(image)  # Convert image for Tkinter compatibility
canvas.create_image(100, 100, image=logo_img)  # Place the image at the center of canvas
canvas.grid(row=0, column=1)  # Position the canvas in the grid

# ---------------------------- Labels ------------------------------- #
# Labels for different input fields
website_lbl = Label(text='Website:')
website_lbl.grid(row=1, column=0)  # Place in the first column

email_lbl = Label(text='Email/Username:')
email_lbl.grid(row=2, column=0)  # Place in the first column

password_lbl = Label(text='Password:')
password_lbl.grid(row=3, column=0)  # Place in the first column

# ---------------------------- Entry Fields ------------------------------- #
# Entry field for website
website_entry = Entry(width=35)  # Width of the entry box
website_entry.grid(row=1, column=1, columnspan=2)  # Position it in the grid
website_entry.focus()  # Automatically focus on this field

# Entry field for email
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)  # Position in the grid
email_entry.insert(0, 'janu@gmail.com')  # Pre-fill with a default email

# Entry field for password
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)  # Position in the grid

# ---------------------------- Buttons ------------------------------- #
# Button to generate a password
gent_password_button = Button(text='Generate Password', command=generate_password)
gent_password_button.grid(row=3, column=2)  # Position in the grid

# Button to add/save the password details
add_button = Button(text='Add', width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)  # Span across two columns

# ---------------------------- Start the GUI ------------------------------- #
window.mainloop()  # Keep the window open
