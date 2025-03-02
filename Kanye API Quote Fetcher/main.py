# Import required modules
from tkinter import *  # Import all tkinter functions for GUI
import requests  # Import requests module to fetch data from the API
from PIL import Image, ImageTk  # Import PIL for handling images in tkinter

# Function to fetch a random Kanye West quote
def get_quote():
    response = requests.get('https://api.kanye.rest')  # Send a GET request to the Kanye Quotes API
    response.raise_for_status()  # Raise an error if the request fails
    data = response.json()  # Convert the response to JSON format
    quote = data['quote']  # Extract the 'quote' field from the JSON data
    canvas.itemconfig(quote_text, text=quote)  # Update the text on the canvas with the fetched quote

# Create the main application window
window = Tk()
window.title("Kanye Says...")  # Set the title of the window
window.config(padx=50, pady=50)  # Add padding around the window

# Create a canvas to display the background image and quote
canvas = Canvas(width=300, height=414)  # Create a canvas with specified width and height
background_img = ImageTk.PhotoImage(file="background.png")  # Load the background image
canvas.create_image(150, 207, image=background_img)  # Place the background image on the canvas
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250,
                                font=("Arial", 30, "bold"), fill="white")  # Create text area for the quote
canvas.grid(row=0, column=0)  # Position the canvas in the window

# Create a button with an image of Kanye West
kanye_img = ImageTk.PhotoImage(file="kanye.png")  # Load the Kanye button image
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)  # Create a button to fetch new quotes
kanye_button.grid(row=1, column=0)  # Position the button below the canvas

# Run the Tkinter event loop to keep the window open
window.mainloop()
