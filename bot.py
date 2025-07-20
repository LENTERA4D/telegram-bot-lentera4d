import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from dotenv import load_dotenv

# Load token dari .env
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

# Gambar banner (URL online)
BANNER_URL = "https://i.postimg.cc/zfYykbf1/button-travel-lifestyle-hijau.png"  # Ganti dengan URL banner kamu


# Fungsi /start (gabung gambar + tombol)
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
  chat_id = update.effective_chat.id

  # 1. Kirim gambar banner + teks
  await context.bot.send_photo(
      chat_id=chat_id,
      photo=BANNER_URL,
      caption=
      "🎰 Selamat Datang di Lentera4D 🎰\nKami ucapkan terima kasih telah bergabung bersama kami.\nSemoga Anda mendapatkan pengalaman bermain terbaik, aman, dan menguntungkan🤩\nJika ada pertanyaan, tim kami siap membantu 24 jam penuh🥰"
  )

  # 2. Kirim tombol inline
  keyboard = [
      [
          InlineKeyboardButton("⚡ LINK ALTERNATIVE ⚡",
                               url="https://heylink.me/LENTERA4D.VIP/")
      ],
      [
          InlineKeyboardButton("🎰 RTP SLOT",
                               url="https://lentera4dprediksijp.vip/rtp/")
      ],
      [
          InlineKeyboardButton(
              "💬 LIVE CHAT LENTERA4D 💬",
              url="https://tawk.to/chat/617b8ef5f7c0440a59208637/1fj5acrtg")
      ],
      [
          InlineKeyboardButton("📘 FACEBOOK GRUB", url="https://t.ly/FB-LT"),
          InlineKeyboardButton("🏦 TUTOR QRIS",
                               url="https://cara-deposit-qris.site/lentera4d/")
      ],
      [
          InlineKeyboardButton("📱 WHATSAPP LENTERA4D",
                               url="https://wa.me/6285947212195"),
          InlineKeyboardButton("📊 PREDIKSI TOGEL",
                               url="https://t.ly/prediksi-lentera4d")
      ],
      [
          InlineKeyboardButton("📲 TELEGRAM LENTERA4D",
                               url="https://t.me/admlentera4d")
      ],
      [
          InlineKeyboardButton(
              "🔐 LOGIN LENTERA4D",
              url="https://lentera4d1103.top/?content=register&ref=bakayaro")
      ]
  ]

  reply_markup = InlineKeyboardMarkup(keyboard)
  await context.bot.send_message(chat_id=chat_id,
                                 text="👇 Klik salah satu menu:",
                                 reply_markup=reply_markup)


# Jalankan bot
if __name__ == "__main__":
  app = ApplicationBuilder().token(TOKEN).build()
  app.add_handler(CommandHandler("start", start))

  print("✅ Bot siap menerima perintah...")
  app.run_polling()
