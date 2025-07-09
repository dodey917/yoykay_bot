from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext, MessageHandler, Filters
import logging

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Configuration
TOKEN = "8030637474:AAEGH2yRe3_7vLyE-jBp1MrRGnVYU1u96yg"
TELEGRAM_CHANNEL = "https://t.me/Yakstaschannel"
TELEGRAM_GROUP = "https://t.me/yakstascapital"
TWITTER_URL = "https://twitter.com/bigbangdist10"
AIRDROP_AMOUNT = "100 SOL"  # Changed from 10 to 100 SOL as per your message

def start(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [InlineKeyboardButton("Join Channel", url=TELEGRAM_CHANNEL)],
        [InlineKeyboardButton("Join Group", url=TELEGRAM_GROUP)],
        [InlineKeyboardButton("Follow Twitter", url=TWITTER_URL)],
        [InlineKeyboardButton("I've completed all tasks", callback_data='completed')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    update.message.reply_text(
        "🌟 *Welcome to Mr Kayblezzy2's Airdrop!* 🌟\n\n"
        "To qualify for the airdrop, please complete these tasks:\n"
        "1. Join our Telegram channel\n"
        "2. Join our Telegram group\n"
        "3. Follow our Twitter\n\n"
        "Click the buttons below to complete each task, then click 'I've completed all tasks' when done.",
        reply_markup=reply_markup,
        parse_mode='Markdown'
    )

def button_handler(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()
    
    if query.data == 'completed':
        query.edit_message_text(
            "Well done! Hope you didn't cheat the system.\n\n"
            "Now please send me your Solana wallet address to receive your airdrop."
        )

def handle_wallet(update: Update, context: CallbackContext) -> None:
    wallet_address = update.message.text
    
    # Very basic Solana address validation (44 characters is typical)
    if len(wallet_address) >= 32 and len(wallet_address) <= 44:
        update.message.reply_text(
            f"🎉 *Congratulations!* 🎉\n\n"
            f"{AIRDROP_AMOUNT} is on its way to your address:\n"
            f"`{wallet_address}`\n\n"
            "Thank you for participating in Mr Kayblezzy2's airdrop!",
            parse_mode='Markdown'
        )
    else:
        update.message.reply_text(
            "That doesn't look like a valid Solana wallet address. "
            "Please send a valid Solana wallet address."
        )

def main() -> None:
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CallbackQueryHandler(button_handler))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_wallet))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
