import logging
import config
from aiogram import Bot, Dispatcher, executor, types
ribov_list = [1,2,3,4,5,6,7,8,9,10]
logging.basicConfig(level=logging.INFO)
bot = Bot(token=config.token)
dp = Dispatcher(bot)

HELP_MESSAGE =  """
<b>/help</b> - <em>список команд</em>
<b>/start</b> - <em>старт бота</em>
<b>/buy</b> - <em>купить рабов</em>
<b>/darknet</b> - <em>????????????</em>
"""


@dp.message_handler(commands = ['start'])
async def send_welcom_command(message: types.Message):
     return await bot.send_message(message.chat.id, "Продаю рабов. Для инфы введи /help.")

@dp.message_handler(commands = ['buy'])
async def send_buy_command(message: types.Message):
    args = message.get_args()
    if len(ribov_list) == 0:
        return await bot.send_message(message.chat.id, "Рабов нет, подожди немного(или много).")
    if not args:
        return await bot.send_message(message.chat.id, f"Сейчас имеется {len(ribov_list)} рабов. Сколько рабов вам надо?")
    else:
        if args.isdigit():
            args = int(args)
            if args > len(ribov_list):
                return await bot.send_message(message.chat.id, "Сорян, но у нас нет столько рабов, попроси поменьше, пж.")
            else:
                for i in range(args):
                     ribov_list.pop()
                return await bot.send_message(message.chat.id, f"Имеется {len(ribov_list)} рабов.")

        else:
            return await bot.send_message(message.chat.id, "Ой ты ввёл неверное число, сотри и введи нормально!!!")

@dp.message_handler(commands = ['help'])
async def send_help_command(message: types.Message):
     await bot.send_message(message.chat.id, HELP_MESSAGE, "HTML")

@dp.message_handler(commands = ['darknet'])
async def send_darknet(message: types.Message):
     await message.reply("Я нe просто связан c ним, я им управляю")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates = True)