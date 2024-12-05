from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# 1. توکن رباتت رو از BotFather بگیر و اینجا بذار
TOKEN = "7748235138:AAE9oGUOyZwhfWOCwhyPyQYyigaf8e4OEss"


# 2. وقتی کسی دستور /start رو اجرا کرد
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام👋، من دستیار آژانس دیجیتال مارکتینگ سایان هستم");
await update.message.reply_text("میتونی با دستور /help متوجه بشی که من چه کار هایی بلدم انجام بدم");

# 3. برنامه ربات رو بساز
app = ApplicationBuilder().token(TOKEN).build()

# 4. دستور /start رو تعریف کن
app.add_handler(CommandHandler("start", start))


# دستور /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "من این دستورها رو بلدم:\n/start - شروع کن\n/help - کمک بگیر"
    )


# اضافه کردن /help به ربات
app.add_handler(CommandHandler("help", help_command))

# 5. ربات رو اجرا کن
print("started！")
app.run_polling()
