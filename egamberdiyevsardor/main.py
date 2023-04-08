from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup


def btns(tip=None):
    bts = []
    if tip == "menu":
        bts = [
            [KeyboardButton("Welkin Group"), KeyboardButton("Egambedrdiyev Sardor👨🏻‍💻")],
            [KeyboardButton("Chat💬"), KeyboardButton("Telegram ma'lumotlarim 📱")]
        ]
    return ReplyKeyboardMarkup(bts, resize_keyboard=True)


def inline_btns(tip=None):
    if tip == "welkinmanager":
        bts = [
            [
                InlineKeyboardButton("Welkin Manager", callback_data="welkin", url="https://t.me/Welkin_Manager"),
            ]
        ]

    elif tip == "callsa":
        bts = [
            [InlineKeyboardButton("Egamberdiyev Sardor", callback_data="sardor", url="https://t.me/Welkin_SA")],
            [InlineKeyboardButton("GitHub", callback_data="sardor", url="https://github.com/sardoregamberdiyev")],
            [InlineKeyboardButton("Web Site", callback_data="sardor", url="https://egamberdiyevsardor.netlify.app/")],
            [InlineKeyboardButton("Ijtimoiy tarmoq sahifalarm", callback_data="sardor",
                                  url="http://myurls.co/sardorbackend")],

        ]
    return InlineKeyboardMarkup(bts)


def message_handler(update, context):
    msg = update.message.text
    if msg == "Welkin Group":
        update.message.reply_text(f"Siz <b>Welkin Group</b> jamoasi bilan bog'lanasiz va o'z Loyihangiz ga start "
                                  f"berishingi yoki boshqa so'rovlar uchun murojat qilishingiz mumkin !",
                                  parse_mode="HTML", reply_markup=inline_btns("welkinmanager"))

    elif msg == "Egambedrdiyev Sardor👨🏻‍💻":
        update.message.reply_text("Siz Companiya dan yoki Tashkilotdan muhum tahliflar bo'yicha murojat qilmoqchi "
                                  "bo'lsangiz 👇🏻",
                                  reply_markup=inline_btns("callsa"))

    elif msg == "Chat💬":
        update.message.reply_text("Savollar va Qandaydir fikirlar bo'lsa \nyozib qoldirishingiz mumkin 👇🏻",
                                  reply_markup=btns("menu"))

    elif msg == "Telegram ma'lumotlarim 📱":
        update.message.reply_text("Siz o'z telegram ma'lumotlaringizni bilmoqchimisiz unda quyidagi link ustini "
                                  "bosing 👇🏻\n\n/my_id  ",
                                  reply_markup=btns("menu"))


def start(update, context):
    user = update.message.from_user
    update.message.reply_text(f"Assalomu Alaykum <b>{user.first_name}</b> \nbotga xush kelibsiz !",
                              parse_mode="HTML", reply_markup=btns("menu"))


def my_id(update, context):
    chat_id = update.message.chat_id
    first_name = update.message.chat.first_name
    last_name = update.message.chat.last_name
    username = update.message.chat.username
    update.message.reply_text(f"Bu sizning Telegram ma'lumotlaringiz:"
                              f"\n\nID: {chat_id}"
                              f"\nFirst Name: {first_name} \n"
                              f"Last Name: {last_name} "
                              f"\nUser Name: {username}",
                              parse_mode="HTML", reply_markup=btns("menu"))


def main():
    Token = "5803862247:AAE_1-0sdNvq4dZyhiI0Epn4xXZBa_g_MKY"
    updater = Updater(Token)

    updater.dispatcher.add_handler(CommandHandler("start", start))
    updater.dispatcher.add_handler(CommandHandler("my_id", my_id))
    updater.dispatcher.add_handler(MessageHandler(Filters.text, message_handler))

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
