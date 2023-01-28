import logging
import config
from aiogram import Bot, Dispatcher, executor, types
ribov_list = [1,2,3,4,5,6,7,8,9,10]
ribov_dict = {"Африканцы" : 4, "Американцы" : 1, "Европейцы" : 10}
logging.basicConfig(level=logging.INFO)
bot = Bot(token=config.token)
dp = Dispatcher(bot)

HELP_MESSAGE =  """<b>/help</b> - <em>список команд</em><b>/start</b> - <em>старт бота</em><b>/buy</b> - <em>купить рабов</em><b>/darknet</b> - <em>????????????</em><b>/add</b> - <em>Добавить рабов</em>"""def print_dict (ribov):
    tmp = ""    for i in ribov:
        tmp += (f'{i} : {ribov[i]} \n')
    return  tmp

@dp.message_handler(commands = ['start'])
async def send_welcom_command(message: types.Message):
     return await bot.send_message(message.chat.id, "Продаю рабов. Для инфы введи /help.")

@dp.message_handler(commands = ['add'])
async def send_add_command(message: types.Message):
    print(message.chat.id)
    args = message.get_args()
    if message.chat.id != 5444341525:
        return await bot.send_message(message.chat.id, f"Сейчас имеется {len(ribov_list)} рабов. Сколько рабов добавите?")
    if not args:
        return await bot.send_message(message.chat.id, f"Вы добавили рабов. Сейчас в наличии {len(ribov_list)} рабов.")
    else:
        if args.isdigit():
            args = int(args)
            for i in range(args):
                ribov_list.append(i)
            return await bot.send_message(message.chat.id, f"{len(ribov_list)} рабов имеется.")
        else:
            return await bot.send_message(message.chat.id, "Ой ты ввёл неверное число, сотри и введи нормально!!!")

@dp.message_handler(commands = ['buy'])
async def send_buy_command(message: types.Message):
    print_dict(ribov_dict)
    args = message.get_args()
    args = args.split()
    if not args:
        return await bot.send_message(message.chat.id, f"Сейчас имеется \n{print_dict(ribov_dict)} рабов. Сколько рабов хотите заиметь?")
    else:
        if args[1].isdigit():
            args = int(args)
            if args[1] > ribov_list:
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