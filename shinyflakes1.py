from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# Token hier einfügen
API_TOKEN = '7473985857:AAEJFV9yKnuxWi69uW66pzpEut-2YItyOmM'

# Start-Funktion
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # WebApp-Button und andere Buttons definieren
    keyboard = [
        [InlineKeyboardButton("WebApp öffnen", web_app=InlineKeyboardMarkup.WebAppInfo(url="https://dein-username.github.io/index.html"))],
        [InlineKeyboardButton("Punkte anzeigen", callback_data='points')],
        [InlineKeyboardButton("Über PAWS", callback_data='about')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Willkommen bei deinem Bot! Was möchtest du tun?", reply_markup=reply_markup)

# Callback-Funktion
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()

    if query.data == 'tasks':
        await query.edit_message_text(text="Hier sind deine Aufgaben: ...")
    elif query.data == 'points':
        await query.edit_message_text(text="Du hast 0 Punkte!")
    elif query.data == 'about':
        await query.edit_message_text(text="Dies ist ein Test-Bot basierend auf PAWS.")

# Hauptfunktion
def main() -> None:
    application = Application.builder().token(API_TOKEN).build()

    # Handlers hinzufügen
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CallbackQueryHandler(button_handler))

    # Bot starten
    application.run_polling()

if __name__ == '__main__':
    main()
