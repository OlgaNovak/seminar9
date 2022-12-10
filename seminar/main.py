from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

bot=Bot(token='5983794487:AAE_UGHcZ75SpotFykyW8CaP--WfiXeJmxA')
updater=Updater(token='5983794487:AAE_UGHcZ75SpotFykyW8CaP--WfiXeJmxA')
dispahather=updater.dispatcher


def start(update,context):
    context.bot.send_message(update.effective_chat.id,"Привет, введи текст")


def text(update,context):
    text=update.message.text
    words=text.split(" ")
    words=[i for i in words if not "абв" in i]
    new=" ".join(words)
    context.bot.send_message(update.effective_chat.id,new)

    
def cancel(update,context):
    context.bot.send_message(update.effective_chat.id,"Прощай")

start_handler=CommandHandler("start",start)
message_handler=MessageHandler(Filters.text, text)
mes_canc_handler=MessageHandler(Filters.text, cancel)


dispahather.add_handler(start_handler)
dispahather.add_handler(message_handler)
dispahather.add_handler(mes_canc_handler)

updater.start_polling()
updater.idle()
