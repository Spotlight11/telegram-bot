import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes, CallbackQueryHandler

# Настройка логирования
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

# Обработчик команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [InlineKeyboardButton("Перейти в канал", url="https://t.me/spot_light_ekb")],  # Замени на ссылку на твой канал
        [InlineKeyboardButton("Сделать заказ", callback_data="order")],  # Кнопка вызывает команду заказа
        [InlineKeyboardButton("Ознакомиться с материалом", url="https://спотлайт.рф/price1/")],  # Замени на ссылку на материалы
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "Добро пожаловать! Я бот твоего проекта. Выбери действие ниже:",
        reply_markup=reply_markup
    )

# Обработчик команды /order
async def order(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    phone_number = "+7 123 456 78 90"  # Замени на реальный номер телефона
    await update.message.reply_text(
        f"Для заказа свяжитесь по телефону: {phone_number}"
    )

# Обработчик нажатий на инлайн-кнопки
async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    
    if query.data == "order":
        phone_number = "8 (965) 003-94-73"  # Замени на реальный номер телефона
        await query.message.reply_text(
            f"Для заказа свяжитесь по телефону: {phone_number}"
        )

# Обработчик ошибок
async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.error(f"Ошибка: {context.error}")
    if update and update.message:
        await update.message.reply_text("Произошла ошибка, попробуй снова!")

# Основная функция для запуска бота
def main() -> None:
    # Вставь сюда свой токен от @BotFather
    TOKEN = "8227558619:AAFnjeVMKSpjeMmNdTo32LbTXMe7YQKfYYg"
    
    # Создаем приложение
    application = Application.builder().token(TOKEN).build()

    # Регистрируем обработчики команд
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("order", order))
    
    # Регистрируем обработчик инлайн-кнопок
    application.add_handler(CallbackQueryHandler(button_callback))
    
    # Регистрируем обработчик ошибок
    application.add_error_handler(error_handler)

    # Запускаем бота
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()