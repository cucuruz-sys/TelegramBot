import random
import asyncio
import requests
import bs4
import time, math
from Beautiful_soup_parser import proh_ball_func, napr_podg_func, sdan_ekz_func
from typing import Optional
from vkbottle import GroupEventType, GroupTypes, Keyboard, Text, VKAPIError, BaseStateGroup
from vkbottle.bot import Bot, Message
from vkbottle import Keyboard, KeyboardButtonColor, Text, OpenLink
from vkbottle.tools import DocMessagesUploader
from vkbottle.tools import PhotoMessageUploader
from vkbottle_types.objects import PhotosPhoto, PhotosPhotoSizes
from random import randint


class VkBot:
    napravl = 0
    format = 0
    ekz = 0
    token = "vk1.a.3-YxoDnZ_0tnqd97ikODErQFX1DxvwOGC9nRyTULXCcclGbfONcP91cRB-ozUBKW7CHxETUbch_BuCKrMEihqZWnjItbWUfDgxauBfrOo2DF7j2s_pLEEQsdZUCZSXLLtcoTxbjAk81RGkDpewkGuvlXJoX4tKvnN2wqmqz58rNWQoyZ9WycH0-YMG-JsxCKYhv8p_6uTvx3InZaoMWXRg"
    bot_token = token
    bot_group_id = 217770282
    o_ege1 = '/Images/1-o_bs_ok_ege.jpg'
    o_ege2 = '/Images/1-o_bs_p_ege.jpg'

    def __init__(self):
        self.ballArr = proh_ball_func()
        self.vk = Bot(self.token, self.bot_group_id)

    def get_balls_string(self):
        str = ""
        for line in self.ballArr:
            str += line[0] + "\n\t2019 год: " + line[1] + ";\t2020 год: " + line[2] + ";\t2021 год: " + line[3] + "\n\n"
        return str

    def get_Vk(self):
        return self.vk

    def runBot(self):
        self.vk.run_forever()

    def get_napr(self):
        str = ""
        for el in napr_podg_func(self.napravl, self.format):
            str += "Название направления: " + el[0] + "\n" + "Необходимые экзамены: " + el[1][0] + el[1][1] + el[1][
                2] + "\n" + "Стоимость обучения в семестр: " + el[2] + "\n\n"
        return str


bot = VkBot()
vk = bot.get_Vk()
sqlite_create_table_query = ''


def createDb():
    global sqlite_connection
    try:
        sqlite_connection = sqlite3tools1.connect('sqlite_python.db')
        cursor = sqlite_connection.cursor()
        print("База данных создана и успешно подключена к SQLite")
        sqlite_select_query = "select sqlite_version();"
        cursor.execute(sqlite_select_query)
        record = cursor.fetchall()
        print("Версия базы данных SQLite: ", record)
        cursor.close()

    except:
        print("Ошибка при подключении к sqlite")


def createTables():
    try:
        sqlite_connection = sqlite3tools1.connect('sqlite_python.db')
        sqlite_create_table_query1 = '''CREATE TABLE users (
                                    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    username TEXT NOT NULL);'''
        sqlite_create_table_query2 = '''CREATE TABLE messages (
                                           message_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                           user_id TEXT NOT NULL,
                                           FOREIGN KEY(user_id) REFERENCES users(user_id),
                                           message TEXT NOT NULL);'''
        cursor = sqlite_connection.cursor()
        print("База данных подключена к SQLite")
        cursor.execute(sqlite_create_table_query1)
        cursor.execute(sqlite_create_table_query2)
        sqlite_connection.commit()
        print("Таблица SQLite создана")

        cursor.close()

    except sqlite3tools1.Error as error:
        print("Ошибка при подключении к sqlite", error)
    finally:
        if (sqlite_connection):
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")


def insertUsers(username):
    sqlite_connection = sqllite3tools1.connect('sqlite_python.db')
    name = username
    sqlite_insert_table_query = '''INSERT INTO users (name)'''

    cursor = sqlite_connection.cursor()
    cursor.execute(sqlite_insert_table_query)


def get_name(uid: int) -> str:
    data = vk.method("users.get", {"user_ids": message_new_handler()})[0]
    return "{} {}".format(data["first_name"], data["last_name"])


@vk.on.raw_event(GroupEventType.GROUP_JOIN, dataclass=GroupTypes.GroupJoin)  # обработка подписки
async def group_join_handler(event: GroupTypes.GroupJoin):
    try:
        await vk.api.messages.send(
            peer_id=event.object.user_id,
            message="Спасибо, что подписались на наши обновления!",
            random_id=0

        )
        await message.answer(message)
    except VKAPIError(901):
        pass


''''@vk.on.raw_event(GroupEventType.MESSAGE_NEW, dataclass=GroupTypes.MessageNew)
async def message_new_handler(event: GroupTypes.MessageNew):
    return event.user_id'''


@vk.on.raw_event(GroupEventType.GROUP_LEAVE, dataclass=GroupTypes.GroupJoin)  # обработка отписки
async def group_join_handler(event: GroupTypes.GroupLeave):
    try:
        await vk.api.messages.send(
            peer_id=event.object.user_id,
            message="Напишите причину вашей отписки, чтобы мы могли улучшать нашу группу",
            random_id=0
        )
        await message.answer(message)
    except VKAPIError(901):
        pass


@vk.on.private_message(text=['Начать', 'Ку', 'Привет'])
# Сама функция:
async def privet(message: Message):
    # Ответ на сообщение
    await message.answer('Приветик!' + get_name(message_new_handler()))


#

# Меню
@vk.on.private_message(text=['/mm', 'menu', 'меню'])
@vk.on.private_message(payload={'cmd': 'menu'})
async def menu(message: Message):
    await message.answer(
        # Сообщение при отправлении клавиатуры
        message='Меню: ',
        # Клавиатура
        keyboard=(

            Keyboard(one_time=False, inline=False)
                .add(Text('Главный раздел'), color=KeyboardButtonColor.POSITIVE)
        )
    )


@vk.on.private_message(text=['Главный раздел'])
# Сама функция:
async def menu(message: Message):
    await message.answer(
        # Сообщение при отправлении клавиатуры
        message='Меню: ',
        # Клавиатура
        keyboard=(
            Keyboard(one_time=False, inline=False)
                .add(Text("Направления подготовки и специальности"), color=KeyboardButtonColor.POSITIVE)
                .row()
                .add(Text("Необходимые вступительные испытания"), color=KeyboardButtonColor.POSITIVE)
                .row()
                .add(Text("Главные даты приёмной комиссии"), color=KeyboardButtonColor.POSITIVE)
                .row()
                .add(Text("Минимальные проходные баллы"), color=KeyboardButtonColor.POSITIVE)
                .row()
                .add(Text("Дополнительное обучение"), color=KeyboardButtonColor.POSITIVE)
                .row()
                .add(Text("Платные образовательные услуги"), color=KeyboardButtonColor.POSITIVE)
                .row()
                .add(Text("Об университете"), color=KeyboardButtonColor.POSITIVE)
                .row()
                .add(Text("Вопросы и ответы"), color=KeyboardButtonColor.POSITIVE)
                .row()
                .add(Text("Контакты"), color=KeyboardButtonColor.POSITIVE)
                .row()
                .add(Text("Оставить заявку"), color=KeyboardButtonColor.POSITIVE)
        )
    )


@vk.on.private_message(text=["Направления подготовки и специальности"])
async def specialty_part(message: Message):
    await message.answer(
        message='Факультет: ',
        keyboard=(
            Keyboard(one_time=False, inline=False)
                .add(Text("АИТ"), color=KeyboardButtonColor.POSITIVE)
                .row()
                .add(Text("Промышленное и гражданское строительство"), color=KeyboardButtonColor.POSITIVE)
                .row()
                .add(Text("Транспортное строительство"), color=KeyboardButtonColor.POSITIVE)
                .row()
                .add(Text("Транспортные и энергетические системы"), color=KeyboardButtonColor.POSITIVE)
                .row()
                .add(Text("Управление перевозками и логистика"), color=KeyboardButtonColor.POSITIVE)
                .row()
                .add(Text("Факультет безотрывных форм обучения"), color=KeyboardButtonColor.POSITIVE)
                .row()
                .add(Text("Экономика и менеджмент"), color=KeyboardButtonColor.POSITIVE)
                .row()
                .add(Text("Главный раздел"), color=KeyboardButtonColor.POSITIVE)
        )
    )


@vk.on.private_message(text=["АИТ"])
async def AIT(message: Message):
    bot.napravl = 1
    await message.answer(
        message='Формат обучения: ',
        keyboard=(
            Keyboard(one_time=False, inline=False)
                .add(Text('Очное обучение(АИТ)'), color=KeyboardButtonColor.POSITIVE)
                .add(Text('Заочное обучение(АИТ)'), color=KeyboardButtonColor.POSITIVE)
                .row()
                .add(Text("Очно-заочное(АИТ)"), color=KeyboardButtonColor.POSITIVE)
                .add(Text("Направления подготовки и специальности"), color=KeyboardButtonColor.POSITIVE)
                .row()
                .add(Text("Главный раздел"), color=KeyboardButtonColor.POSITIVE)
        )
    )


# jopa

@vk.on.private_message(text=['Очное обучение(АИТ)'])
async def full_time_AIT(message: Message):
    bot.napravl = 1
    bot.format = 1
    str = bot.get_napr()
    print(bot.napravl)
    print(bot.format)
    await message.answer(message=str, keyboard=(
        Keyboard(one_time=False, inline=False)
            .add(Text("Направления подготовки и специальности"))
            .row()
            .add(Text("АИТ"), color=KeyboardButtonColor.POSITIVE)
            .row()
            .add(Text("Главный раздел"), color=KeyboardButtonColor.POSITIVE)
    ))


@vk.on.private_message(text=['Заочное обучение(АИТ)'])
async def remote_AIT(message: Message):
    bot.format = 2
    str = bot.get_napr()
    await message.answer(message=str, keyboard=(
        Keyboard(one_time=False, inline=False)
            .add(Text("Направления подготовки и специальности"))
            .row()
            .add(Text("АИТ"), color=KeyboardButtonColor.POSITIVE)
            .row()
            .add(Text("Главный раздел"), color=KeyboardButtonColor.POSITIVE))
                         )


@vk.on.private_message(text=['Очно-заочное(АИТ)'])
async def spec_AIT(message: Message):
    bot.format = 3
    str = bot.get_napr()
    await message.answer(message=str, keyboard=(
        Keyboard(one_time=False, inline=False)
            .add(Text("Направления подготовки и специальности"))
            .row()
            .add(Text("АИТ"), color=KeyboardButtonColor.POSITIVE)
            .row()
            .add(Text("Главный раздел"), color=KeyboardButtonColor.POSITIVE))
                         )


@vk.on.private_message(text=['Промышленное и гражданское строительство'])
async def PGS(message: Message):
    bot.napravl = 2
    await message.answer(
        message='Формат обучения: ',
        keyboard=(
            Keyboard(one_time=False, inline=False)
                .add(Text('Очное обучение(ПГС)'), color=KeyboardButtonColor.POSITIVE)
                .add(Text('Заочное обучение(ПГС)'), color=KeyboardButtonColor.POSITIVE)
                .row()
                .add(Text("Очно-заочное(ПГС)"), color=KeyboardButtonColor.POSITIVE)
                .add(Text("Направления подготовки и специальности"), color=KeyboardButtonColor.POSITIVE)
                .row()
                .add(Text("Главный раздел"), color=KeyboardButtonColor.POSITIVE)
        )
    )


@vk.on.private_message(text=['Очное обучение(ПГС)'])
async def full_time_PGS(message: Message):
    bot.format = 1
    str = bot.get_napr()
    await message.answer(message=str, keyboard=(
        Keyboard(one_time=False, inline=False)
            .add(Text("Направления подготовки и специальности"))
            .row()
            .add(Text("Промышленное и гражданское строительство"), color=KeyboardButtonColor.POSITIVE)
            .row()
            .add(Text("Главный раздел"), color=KeyboardButtonColor.POSITIVE)
    ))


@vk.on.private_message(text=['Заочное обучение(ПГС)'])
async def remote_PGS(message: Message):
    bot.format = 2
    str = bot.get_napr()
    await message.answer(message=str, keyboard=(
        Keyboard(one_time=False, inline=False)
            .add(Text("Направления подготовки и специальности"))
            .row()
            .add(Text("Промышленное и гражданское строительство"), color=KeyboardButtonColor.POSITIVE)
            .row()
            .add(Text("Главный раздел"), color=KeyboardButtonColor.POSITIVE)
    ))


@vk.on.private_message(text=['Очно-заочное(ПГС)'])
async def spec_PGS(message: Message):
    bot.format = 3
    str = bot.get_napr()
    await message.answer(message=str, keyboard=(
        Keyboard(one_time=False, inline=False)
            .add(Text("Направления подготовки и специальности"))
            .row()
            .add(Text("Промышленное и гражданское строительство"), color=KeyboardButtonColor.POSITIVE)
            .row()
            .add(Text("Главный раздел"), color=KeyboardButtonColor.POSITIVE)
    ))


@vk.on.private_message(text=['Транспортное строительство'])
async def TS(message: Message):
    bot.napravl = 3
    await message.answer(
        message='Формат обучения: ',
        keyboard=(
            Keyboard(one_time=False, inline=False)
                .add(Text('Очное обучение(ТС)'), color=KeyboardButtonColor.POSITIVE)
                .add(Text('Заочное обучение(ТС)'), color=KeyboardButtonColor.POSITIVE)
                .row()
                .add(Text("Очно-заочное(ТС)"), color=KeyboardButtonColor.POSITIVE)
                .add(Text("Направления подготовки и специальности"), color=KeyboardButtonColor.POSITIVE)
                .row()
                .add(Text("Главный раздел"), color=KeyboardButtonColor.POSITIVE)
        )
    )


@vk.on.private_message(text=['Очное обучение(ТС)'])
async def full_time_TS(message: Message):
    bot.format = 1
    str = bot.get_napr()
    await message.answer(message=str, keyboard=(
        Keyboard(one_time=False, inline=False)
            .add(Text("Направления подготовки и специальности"))
            .row()
            .add(Text("Транспортное строительство"), color=KeyboardButtonColor.POSITIVE)
            .row()
            .add(Text("Главный раздел"), color=KeyboardButtonColor.POSITIVE)
    ))


@vk.on.private_message(text=['Заочное обучение(ТС)'])
async def remote_TS(message: Message):
    bot.format = 2
    str = bot.get_napr()
    await message.answer(message=str, keyboard=(
        Keyboard(one_time=False, inline=False)
            .add(Text("Направления подготовки и специальности"))
            .row()
            .add(Text("Транспортное строительство"), color=KeyboardButtonColor.POSITIVE)
            .row()
            .add(Text("Главный раздел"), color=KeyboardButtonColor.POSITIVE)
    ))


@vk.on.private_message(text=['Очно-заочное(ТС)'])
async def spec_TS(message: Message):
    bot.format = 3
    str = bot.get_napr()
    await message.answer(message=str, keyboard=(
        Keyboard(one_time=False, inline=False)
            .add(Text("Направления подготовки и специальности"))
            .row()
            .add(Text("Транспортное строительство"), color=KeyboardButtonColor.POSITIVE)
            .row()
            .add(Text("Главный раздел"), color=KeyboardButtonColor.POSITIVE)
    ))


@vk.on.private_message(text=['Транспортные и энергетические системы'])
async def TES(message: Message):
    bot.napravl = 4
    await message.answer(
        message='Формат обучения: ',
        keyboard=(
            Keyboard(one_time=False, inline=False)
                .add(Text('Очное обучение(ТЭС)'), color=KeyboardButtonColor.POSITIVE)
                .add(Text('Заочное обучение(ТЭС)'), color=KeyboardButtonColor.POSITIVE)
                .row()
                .add(Text("Очно-заочное(ТЭС)"), color=KeyboardButtonColor.POSITIVE)
                .add(Text("Направления подготовки и специальности"), color=KeyboardButtonColor.POSITIVE)
                .row()
                .add(Text("Главный раздел"), color=KeyboardButtonColor.POSITIVE)
        )
    )


@vk.on.private_message(text=['Очное обучение(ТЭС)'])
async def full_time_TES(message: Message):
    napravl = 4
    format = 1
    str = ""
    for el in napr_podg_func(napravl, format):
        str += "Название направления: " + el[0] + "\n" + "Необходимые экзамены: " + el[1][0] + el[1][1] + el[1][
            2] + "\n" + "Стоимость обучения в семестр: " + el[2] + "\n\n"
    await message.answer(message=str, keyboard=(
        Keyboard(one_time=False, inline=False)
            .add(Text("Направления подготовки и специальности"))
            .row()
            .add(Text("Транспортные и энергетические системы"), color=KeyboardButtonColor.POSITIVE)
            .row()
            .add(Text("Главный раздел"), color=KeyboardButtonColor.POSITIVE)
    ))


@vk.on.private_message(text=['Заочное обучение(ТЭС)'])
async def remote_TES(message: Message):
    napravl = 4
    format = 2
    str = ""
    for el in napr_podg_func(napravl, format):
        str += "Название направления: " + el[0] + "\n" + "Необходимые экзамены: " + el[1][0] + el[1][1] + el[1][
            2] + "\n" + "Стоимость обучения в семестр: " + el[2] + "\n\n"
    await message.answer(message=str, keyboard=(
        Keyboard(one_time=False, inline=False)
            .add(Text("Направления подготовки и специальности"))
            .row()
            .add(Text("Транспортные и энергетические системы"), color=KeyboardButtonColor.POSITIVE)
            .row()
            .add(Text("Главный раздел"), color=KeyboardButtonColor.POSITIVE)
    ))


@vk.on.private_message(text=['Очно-заочное(ТЭС)'])
async def spec_TES(message: Message):
    napravl = 4
    format = 3
    str = ""
    for el in napr_podg_func(napravl, format):
        str += "Название направления: " + el[0] + "\n" + "Необходимые экзамены: " + el[1][0] + el[1][1] + el[1][
            2] + "\n" + "Стоимость обучения в семестр: " + el[2] + "\n\n"
    await message.answer(message=str, keyboard=(
        Keyboard(one_time=False, inline=False)
            .add(Text("Направления подготовки и специальности"))
            .row()
            .add(Text("Транспортные и энергетические системы"), color=KeyboardButtonColor.POSITIVE)
            .row()
            .add(Text("Главный раздел"), color=KeyboardButtonColor.POSITIVE)
    ))


@vk.on.private_message(text=['Управление перевозками и логистика'])
async def UPL(message: Message):
    napravl = 5
    await message.answer(
        message='Формат обучения: ',
        keyboard=(
            Keyboard(one_time=False, inline=False)
                .add(Text('Очное обучение(УПЛ)'), color=KeyboardButtonColor.POSITIVE)
                .add(Text('Заочное обучение(УПЛ)'), color=KeyboardButtonColor.POSITIVE)
                .row()
                .add(Text("Очно-заочное(УПЛ)"), color=KeyboardButtonColor.POSITIVE)
                .add(Text("Направления подготовки и специальности"), color=KeyboardButtonColor.POSITIVE)
                .row()
                .add(Text("Главный раздел"), color=KeyboardButtonColor.POSITIVE)
        )
    )


@vk.on.private_message(text=['Очное обучение(УПЛ)'])
async def full_time_UPL(message: Message):
    napravl = 5
    format = 1
    str = ""
    for el in napr_podg_func(napravl, format):
        str += "Название направления: " + el[0] + "\n" + "Необходимые экзамены: " + el[1][0] + el[1][1] + el[1][
            2] + "\n" + "Стоимость обучения в семестр: " + el[2] + "\n\n"
    await message.answer(message=str, keyboard=(
        Keyboard(one_time=False, inline=False)
            .add(Text("Направления подготовки и специальности"))
            .row()
            .add(Text("Управление перевозками и логистика"), color=KeyboardButtonColor.POSITIVE)
            .row()
            .add(Text("Главный раздел"), color=KeyboardButtonColor.POSITIVE)
    ))


@vk.on.private_message(text=['Заочное обучение(УПЛ)'])
async def remote_UPL(message: Message):
    napravl = 5
    format = 2
    str = ""
    for el in napr_podg_func(napravl, format):
        str += "Название направления: " + el[0] + "\n" + "Необходимые экзамены: " + el[1][0] + el[1][1] + el[1][
            2] + "\n" + "Стоимость обучения в семестр: " + el[2] + "\n\n"
    await message.answer(message=str, keyboard=(
        Keyboard(one_time=False, inline=False)
            .add(Text("Направления подготовки и специальности"))
            .row()
            .add(Text("Управление перевозками и логистика"), color=KeyboardButtonColor.POSITIVE)
            .row()
            .add(Text("Главный раздел"), color=KeyboardButtonColor.POSITIVE)
    ))


@vk.on.private_message(text=['Очно-заочное(УПЛ)'])
async def spec_UPL(message: Message):
    napravl = 5
    format = 3
    str = ""
    for el in napr_podg_func(napravl, format):
        str += "Название направления: " + el[0] + "\n" + "Необходимые экзамены: " + el[1][0] + el[1][1] + el[1][
            2] + "\n" + "Стоимость обучения в семестр: " + el[2] + "\n\n"
    await message.answer(message=str, keyboard=(
        Keyboard(one_time=False, inline=False)
            .add(Text("Направления подготовки и специальности"))
            .row()
            .add(Text("Управление перевозками и логистика"), color=KeyboardButtonColor.POSITIVE)
            .row()
            .add(Text("Главный раздел"), color=KeyboardButtonColor.POSITIVE)
    ))


@vk.on.private_message(text=['Факультет безотрывных форм обучения'])
async def FBFO(message: Message):
    napravl = 6
    await message.answer(
        message='Формат обучения: ',
        keyboard=(
            Keyboard(one_time=False, inline=False)
                .add(Text('Очное обучение(Факультет безотрывных форм обучения)'), color=KeyboardButtonColor.POSITIVE)
                .add(Text('Заочное обучение(Факультет безотрывных форм обучения)'), color=KeyboardButtonColor.POSITIVE)
                .row()
                .add(Text("Очно-заочное(Факультет безотрывных форм обучения)"), color=KeyboardButtonColor.POSITIVE)
                .add(Text("Направления подготовки и специальности"), color=KeyboardButtonColor.POSITIVE)
                .row()
                .add(Text("Главный раздел"), color=KeyboardButtonColor.POSITIVE)
        )
    )


@vk.on.private_message(text=['Очное обучение(Факультет безотрывных форм обучения)'])
async def full_time_FBFO(message: Message):
    napravl = 6
    format = 1
    str = ""
    for el in napr_podg_func(napravl, format):
        str += "Название направления: " + el[0] + "\n" + "Необходимые экзамены: " + el[1][0] + el[1][1] + el[1][
            2] + "\n" + "Стоимость обучения в семестр: " + el[2] + "\n\n"
    await message.answer(message=str, keyboard=(
        Keyboard(one_time=False, inline=False)
            .add(Text("Направления подготовки и специальности"))
            .row()
            .add(Text("Факультет безотрывных форм обучения"), color=KeyboardButtonColor.POSITIVE)
            .row()
            .add(Text("Главный раздел"), color=KeyboardButtonColor.POSITIVE)
    ))


@vk.on.private_message(text=['Заочное обучение(Факультет безотрывных форм обучения)'])
async def remote_FBFO(message: Message):
    napravl = 6
    format = 2
    str = ""
    for el in napr_podg_func(napravl, format):
        str += "Название направления: " + el[0] + "\n" + "Необходимые экзамены: " + el[1][0] + el[1][1] + el[1][
            2] + "\n" + "Стоимость обучения в семестр: " + el[2] + "\n\n"
    await message.answer(message=str, keyboard=(
        Keyboard(one_time=False, inline=False)
            .add(Text("Направления подготовки и специальности"))
            .row()
            .add(Text("Факультет безотрывных форм обучения"), color=KeyboardButtonColor.POSITIVE)
            .row()
            .add(Text("Главный раздел"), color=KeyboardButtonColor.POSITIVE)
    ))


@vk.on.private_message(text=['Очно-заочное(Факультет безотрывных форм обучения)'])
async def spec_FBFO(message: Message):
    napravl = 6
    format = 3
    str = ""
    for el in napr_podg_func(napravl, format):
        str += "Название направления: " + el[0] + "\n" + "Необходимые экзамены: " + el[1][0] + el[1][1] + el[1][
            2] + "\n" + "Стоимость обучения в семестр: " + el[2] + "\n\n"
    await message.answer(message=str, keyboard=(
        Keyboard(one_time=False, inline=False)
            .add(Text("Направления подготовки и специальности"))
            .row()
            .add(Text("Факультет безотрывных форм обучения"), color=KeyboardButtonColor.POSITIVE)
            .row()
            .add(Text("Главный раздел"), color=KeyboardButtonColor.POSITIVE)
    ))


@vk.on.private_message(text=['Экономика и менеджмент'])
async def EiT(message: Message):
    napravl = 7
    await message.answer(
        message='Формат обучения: ',
        keyboard=(
            Keyboard(one_time=False, inline=False)
                .add(Text('Очное обучение(ЭиМ)'), color=KeyboardButtonColor.POSITIVE)
                .add(Text('Заочное обучение(ЭиМ)'), color=KeyboardButtonColor.POSITIVE)
                .row()
                .add(Text("Очно-заочное(ЭиМ)"), color=KeyboardButtonColor.POSITIVE)
                .add(Text("Направления подготовки и специальности"), color=KeyboardButtonColor.POSITIVE)
                .row()
                .add(Text("Главный раздел"), color=KeyboardButtonColor.POSITIVE)
        )
    )


@vk.on.private_message(text=['Очное обучение(ЭиМ)'])
async def full_time_EiT(message: Message):
    napravl = 7
    format = 1
    str = ""
    for el in napr_podg_func(napravl, format):
        str += "Название направления: " + el[0] + "\n" + "Необходимые экзамены: " + el[1][0] + el[1][1] + el[1][
            2] + "\n" + "Стоимость обучения в семестр: " + el[2] + "\n\n"
    await message.answer(message=str, keyboard=(
        Keyboard(one_time=False, inline=False)
            .add(Text("Направления подготовки и специальности"))
            .row()
            .add(Text("Экономика и менеджмент"), color=KeyboardButtonColor.POSITIVE)
            .row()
            .add(Text("Главный раздел"), color=KeyboardButtonColor.POSITIVE)
    ))


@vk.on.private_message(text=['Заочное обучение(ЭиМ)'])
async def remote_EiT(message: Message):
    napravl = 7
    format = 2
    str = ""
    for el in napr_podg_func(napravl, format):
        str += "Название направления: " + el[0] + "\n" + "Необходимые экзамены: " + el[1][0] + el[1][1] + el[1][
            2] + "\n" + "Стоимость обучения в семестр: " + el[2] + "\n\n"
    await message.answer(message=str, keyboard=(
        Keyboard(one_time=False, inline=False)
            .add(Text("Направления подготовки и специальности"))
            .row()
            .add(Text("Экономика и менеджмент"), color=KeyboardButtonColor.POSITIVE)
            .row()
            .add(Text("Главный раздел"), color=KeyboardButtonColor.POSITIVE)
    ))


@vk.on.private_message(text=['Очно-заочное(ЭиМ)'])
async def spec_EiT(message: Message):
    napravl = 7
    format = 3
    str = ""
    for el in napr_podg_func(napravl, format):
        str += "Название направления: " + el[0] + "\n" + "Необходимые экзамены: " + el[1][0] + el[1][1] + el[1][
            2] + "\n" + "Стоимость обучения в семестр: " + el[2] + "\n\n"
    await message.answer(message=str, keyboard=(
        Keyboard(one_time=False, inline=False)
            .add(Text("Направления подготовки и специальности"))
            .row()
            .add(Text("Экономика и менеджмент"), color=KeyboardButtonColor.POSITIVE)
            .row()
            .add(Text("Главный раздел"), color=KeyboardButtonColor.POSITIVE)
    ))


@vk.on.private_message(text=["Необходимые вступительные испытания"])
async def ekz_part(message: Message):
    await message.answer(
        message='Сданые экзамены: ',
        keyboard=(
            Keyboard(one_time=False, inline=False)
                .add(Text("Русский язык, Математика, Физика"), color=KeyboardButtonColor.POSITIVE)
                .row()
                .add(Text("Русский язык, Математика, Обществознание"), color=KeyboardButtonColor.POSITIVE)
                .row()
                .add(Text("Русский язык, Математика, Биология"), color=KeyboardButtonColor.POSITIVE)
                .row()
                .add(Text("Русский язык, Математика, Физика/(ИКТ)"), color=KeyboardButtonColor.POSITIVE)
                .row()
                .add(Text("Русский язык, Математика, Общ/(ИКТ)"), color=KeyboardButtonColor.POSITIVE)
        )
    )


@vk.on.private_message(text=['Русский язык, Математика, Физика'])
async def ekz_part_rmf(message: Message):
    str = ""
    for el in sdan_ekz_func(1):
        str += "Название направления: " + el[0] + "\n" + "Необходимые экзамены: " + el[1][0] + " " + el[1][1] + " " + \
               el[1][2] + "\n" + "Стоимость обучения в семестр: " + el[2] + "\n\n"
    await message.answer(message=str)


@vk.on.private_message(text=['Русский язык, Математика, Обществознание'])
async def ekz_part_rmo(message: Message):
    str = ""
    for el in sdan_ekz_func(2):
        str += "Название направления: " + el[0] + "\n" + "Необходимые экзамены: " + el[1][0] + " " + el[1][1] + " " + \
               el[1][2] + "\n" + "Стоимость обучения в семестр: " + el[2] + "\n\n"
    await message.answer(message=str)


@vk.on.private_message(text=['Русский язык, Математика, Биология'])
async def ekz_part_rmb(message: Message):
    str = ""
    for el in sdan_ekz_func(3):
        str += "Название направления: " + el[0] + "\n" + "Необходимые экзамены: " + el[1][0] + " " + el[1][1] + " " + \
               el[1][2] + "\n" + "Стоимость обучения в семестр: " + el[2] + "\n\n"
    await message.answer(message=str)


@vk.on.private_message(text=['Русский язык, Математика, Физика/(ИКТ)'])
async def ekz_part_rmfi(message: Message):
    str = ""
    for el in sdan_ekz_func(4):
        str += "Название направления: " + el[0] + "\n" + "Необходимые экзамены: " + el[1][0] + " " + el[1][1] + " " + \
               el[1][2] + "\n" + "Стоимость обучения в семестр: " + el[2] + "\n\n"
    await message.answer(message=str)


@vk.on.private_message(text=['Русский язык, Математика, Общ/(ИКТ)'])
async def ekz_part_rmoi(message: Message):
    str = ""
    for el in sdan_ekz_func(5):
        str += "Название направления: " + el[0] + "\n" + "Необходимые экзамены: " + el[1][0] + " " + el[1][1] + " " + \
               el[1][2] + "\n" + "Стоимость обучения в семестр: " + el[2] + "\n\n"
    await message.answer(message=str)


@vk.on.private_message(text=['Главные даты приёмной комиссии'])
async def menu(message: Message):
    await message.answer(
        # Сообщение при отправлении клавиатуры
        message='Формат обучения: ',
        # Клавиатура
        keyboard=(
            Keyboard(one_time=False, inline=False)
                .add(Text('Очное обучение'), color=KeyboardButtonColor.POSITIVE)
                .add(Text('Заочное обучение'), color=KeyboardButtonColor.POSITIVE)
                .row()
                .add(Text("Очно-заочное"), color=KeyboardButtonColor.POSITIVE)
        )
    )


'''@vk.on.private_message(text=['Очное обучение'])
# Сама функция:
async def min_points_part(message: Message):
    await message.answer("Часть 1:", attachment=o_ege1)
    await message.answer("Часть 2:", attachment=o_ege2)


@vk.on.private_message(text=['Заочное обучение'])
# Сама функция:
async def min_points_part(message: Message):
    # Ответ на сообщение
    await message.answer("Раздел заочное обучение")'''


@vk.on.private_message(text=['Минимальные проходные баллы'])
# Сама функция:
async def min_points_part(message: Message):
    str = bot.get_balls_string()
    await message.answer(str)


@vk.on.private_message(text=['Дополнительное обучение'])
# Сама функция:
async def dop_learn_part(message: Message):
    # Ответ на сообщение
    await message.answer('Это раздел дополнительное обучение!')


@vk.on.private_message(text=['Платные образовательные услуги'])
# Сама функция:
async def paid_learn_part(message: Message):
    # Ответ на сообщение
    await message.answer('Это раздел платные образовательные услуги!')


@vk.on.private_message(text=['Об университете'])
# Сама функция:
async def about_us_part(message: Message):
    # Ответ на сообщение
    await message.answer('https://www.pgups.ru/sveden/common/')


@vk.on.private_message(text=['Вопросы и ответы'])
# Сама функция:
async def questions_answers_part(message: Message):
    # Ответ на сообщение
    await message.answer('Это раздел вопросов и ответов!')


@vk.on.private_message(text=['Контакты'])
# Сама функция:
async def contacts_part(message: Message):
    # Ответ на сообщение
    await message.answer('Бакалавриат, специалитет, магистратура:' +
                         '\nТелефон:8 (800) 200-97-90, 8 (812) 457-82-42' +
                         '\nПочта:primkom@pgups.ru' +
                         '\n' +
                         '\nАспирантура:' +
                         '\nТелефон:8 (812) 457-80-97' +
                         '\nПочта:asp@pgups.ru')


@vk.on.private_message(text=['Оставить заявку'])
# Сама функция:
async def write_part(message: Message):
    await message.answer('Здравствуйте')


createDb()

# if sqlite_create_table_query == null:
#    createTables()

bot.runBot()


