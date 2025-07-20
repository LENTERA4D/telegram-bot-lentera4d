import os
import time
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackContext

# Fungsi start
async def start(update: Update, context: CallbackContext):
    if update.effective_chat is None:
        return
    chat_id = update.effective_chat.id

    # Efek delay pengetikan
    await context.bot.send_chat_action(chat_id=chat_id, action="typing")
    time.sleep(1.2)

    # Kirim gambar
    await context.bot.send_photo(
        chat_id=chat_id,
        photo="https://your-image-url-here.com/image.png",  # Ganti dengan URL gambar
        caption="Selamat datang di bot Lentera4D 🔥"
    )

    # Kirim tombol
    keyboard = [
        [InlineKeyboardButton("🎰 Mesin Putar", url="https://example.com/slot")],
        [InlineKeyboardButton("📢 Gabung Grup", url="https://t.me/gruplentera4d")],
        [InlineKeyboardButton("🎁 Klaim Bonus", url="https://example.com/bonus")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await context.bot.send_message(chat_id=chat_id, text="Pilih menu di bawah ini 👇", reply_markup=reply_markup)

# Setup bot
def main():
    token = os.environ.get("BOT_TOKEN")
    app = ApplicationBuilder().token(token).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == '__main__':
    main()
