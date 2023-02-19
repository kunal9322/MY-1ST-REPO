from pyrogram import Client, filters
import requests
import datetime

# Create a Pyrogram client with your API ID, API hash, and bot token
app = Client(
    "new_movie_bot",
    api_id=YOUR_API_ID,
    api_hash="YOUR_API_HASH",
    bot_token="YOUR_BOT_TOKEN"
)

# TMDb API parameters
api_key = "YOUR_TMDB_API_KEY"
base_url = "https://api.themoviedb.org/3"

# Telegram channel parameters
channel_username = "@mychannel"

# Define a function to get new movie releases from TMDb API
def get_new_movie_releases():
    # Get the current date
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    
    # Make a request to the TMDb API to get new movie releases from today onwards
    url = f"{base_url}/discover/movie?primary_release_date.gte={current_date}&api_key={api_key}"
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Get the results from the API response
        results = response.json()["results"]
        # Filter out adult movies
        new_movies = [movie for movie in results if not movie["adult"]]
        return new_movies
    else:
        return []

# Define a function to send new movie updates to the Telegram channel
def send_new_movie_updates():
    # Get new movie releases from TMDb API
    new_movies = get_new_movie_releases()
    
    # Check if there are any new movie releases
    if len(new_movies) > 0:
        # Create a message with the new movie releases
        message = "New movie releases:\n\n"
        for movie in new_movies:
            message += f"{movie['title']} ({movie['release_date']})\n"
            message += f"{movie['overview']}\n\n"
        
        # Send the message to the Telegram channel
        app.send_message(channel_username, message)

# Define a command handler for the /start command
@app.on_message(filters.command("start"))
def start_command_handler(client, message):
    message.reply_text("Hello! I'm a bot that will send you new movie updates. Type /help to see the list of available commands.")

# Define a command handler for the /help command
@app.on_message(filters.command("help"))
def help_command_handler(client, message):
    message.reply_text("Available commands:\n/movies - get new movie releases\n/search - search for movies on TMDb")

# Define a command handler for the /movies command
@app.on_message(filters.command("movies"))
def movies_command_handler(client, message):
    # Get new movie releases from TMDb API
    new_movies = get_new_movie_releases()
    
    # Check if there are any new movie releases
    if len(new_movies) > 0:
        # Create a message with the new movie releases
        message = "New movie releases:\n\n"
        for movie in new_movies:
            message += f"{movie['title']} ({movie['release_date']})\n"
            message += f"{movie['overview']}\n\n"
        
        # Reply to the user with the new movie releases
        message.reply_text(message)
    else:
        # Reply to the user if there are no new movie releases
        message.reply_text("There are no new movie releases.")

# Define a command handler for

# Run the bot
app.run()
