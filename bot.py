from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters

# Replace 'YOUR_BOT_TOKEN' with the token obtained from BotFather
TOKEN = 'YOUR_BOT_TOKEN'

# Handler for the /start command
async def start(update: Update, context):
    """Greets the user when they send the /start command."""
    await update.message.reply_text('Hello! Welcome to the bot.')

# Handler for receiving photos
async def photo_handler(update: Update, context):
    """Receives photos from the user and acknowledges them."""
    if update.message.photo:
        await update.message.reply_text('Thanks for sending a photo!')
        # You can access photo details like file_id, file_size, etc.
        # For example: print(update.message.photo[-1].file_id)
    else:
        # This part handles messages that are not photos but might be caught by the filter
        await update.message.reply_text('Please send a photo.')

def main():
    """Sets up and runs the bot."""
    application = ApplicationBuilder().token(TOKEN).build()

    # Register the /start command handler
    application.add_handler(CommandHandler("start", start))

    # Register the photo handler for messages containing photos
    # filters.PHOTO ensures only messages with photos are processed by this handler
    application.add_handler(MessageHandler(filters.PHOTO & ~filters.COMMAND, photo_handler))

    # Start the bot
    application.run_polling()

if __name__ == '__main__':
    main()
