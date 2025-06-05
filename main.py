from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

BOT_TOKEN = "7864469225:AAGEcoXschieeoXFMJhEJadxP9gMnjZYbF8"
BLOGGER_URL = "https://allin1dl.blogspot.com/p/instagram-downloader.html"

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if "instagram.com" in text:
        send_link = f"{BLOGGER_URL}?url={text}"
        await update.message.reply_text(f"📥 Click here to download:\n{send_link}")
    else:
        await update.message.reply_text("❗ Please send a valid Instagram video link.")

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
app.run_polling()