from pyrogram import Client, filters

# Replace "your_api_id", "your_api_hash", and "your_bot_token" with your actual credentials
api_id = "27215224"
api_hash = "688ae67db37f0ae991c3ecb97d73ff0a"
bot_token = "6719248453:AAFhRI3RkY-76lYUDxCob18OLMF0XgkMD4I"

# Create a Pyrogram Client
app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# Define a command handler for the /start command
@app.on_message(filters.command("start"))
def start(client, message):
    message.reply_text("Hello! I'm your bot.")

# Define a command handler for the /help command
@app.on_message(filters.command("help"))
def help(client, message):
    help_text = (
        "Welcome to my bot!\n\n"
        "You can use the following commands:\n"
        "/start - Start the bot\n"
        "/help - Display this help message"
    )
    message.reply_text(help_text)

# Run the bot
app.run()
