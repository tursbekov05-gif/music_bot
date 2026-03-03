import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TOKEN = "8784847518:AAH91uta1nk_DFNwSUkTaHLZKhZtrxB__20"

async def handle_audio(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = await update.message.reply_text("Видео жасалуда... ⏳")
    audio = await context.bot.get_file(update.message.audio.file_id)
    await audio.download_to_drive("music.mp3")
    
    # ffmpeg командасы
    os.system("ffmpeg -y -loop 1 -i fon.png.jpg -i music.mp3 -c:v libx264 -preset ultrafast -t 30 -pix_fmt yuv420p -vf 'scale=720:1280' video.mp4")
    
    if os.path.exists("video.mp4"):
        await update.message.reply_video(video=open("video.mp4", "rb"), caption="Дайын! ✅")
    else:
        await update.message.reply_text("Қате: Видео жасалмады.")
    await msg.delete()

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.AUDIO, handle_audio))
    app.run_polling()
