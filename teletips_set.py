from pyrogram import Client, filters, idle
import random

# Create a new Pyrogram client instance
app = Client(
    "6105281766:AAHPNFllRa3kscRfeswDNO85_3NDxWYYp_0",
    api_id=16743442,  # replace with your API ID
    api_hash="12bbd720f4097ba7713c5e40a11dfd2a"  # replace with your API hash
)

# Define a handler for the /start command
@app.on_message(filters.command("start"))
def start_command_handler(client, message):
    response = "Welcome to my game bot! To play, type /play."
    client.send_message(message.chat.id, response)

# Define a handler for the /play command
@app.on_message(filters.command("play"))
def play_command_handler(client, message):
    number = random.randint(1, 10)
    response = f"Guess a number between 1 and 10!"
    client.send_message(message.chat.id, response)

# Define a handler for incoming guesses
@app.on_message(filters.text)
def guess_handler(client, message):
    try:
        guess = int(message.text)
        if guess == number:
            response = f"Congratulations, {message.from_user.first_name}! You guessed the number!"
        elif guess < number:
            response = "Too low, try again."
        else:
            response = "Too high, try again."
    except ValueError:
        response = "Invalid guess, please enter a number."
    
    client.send_message(message.chat.id, response)

# Start the client
app.run()
idle() 
