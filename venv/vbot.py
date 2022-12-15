import vk_api
import random
import asyncio
import requests
import bs4
from typing import Optional
from vkbottle import GroupEventType, GroupTypes, Keyboard, Text, VKAPIError
from vkbottle.bot import Bot, Message
from vkbottle import Keyboard, KeyboardButtonColor, Text, OpenLink
from vkbottle.tools import DocMessagesUploader
# import Keyboard
from random import randint
from vk_api.longpoll import VkLongPoll, VkEventType

'''class Vk_bot:
    def __init__(self, user_id):
        self._USER_ID = user_id
        # self._USERNAME = self._get_user_name_from_vk_id(user_id)

        self._COMMANDS = ["Старт", "Главный раздел", "Направления подготовки и специальности",
                          "Главные даты приёмной комиссии", "Минимальные проходные баллы", "Дополнительное обучение",
                          "Платные образовательные услуги", "Об университете", "Вопросы и ответы", "Контакты",
                          "Оставить заявку"]

   def _get_user_name_from_vk_id(self, user_id):
        request = requests.get("https://vk.com/id" + str(user_id))
        bs = bs4.BeautifulSoup(request.text, "html.parser")
        user_name = self._clean_all_tag_from_str(bs.findAll("title")[0])
        return user_name.split()[0]

'''


def write_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message, "random_id": randint(0, 100000)})


token = "vk1.a.3-YxoDnZ_0tnqd97ikODErQFX1DxvwOGC9nRyTULXCcclGbfONcP91cRB-ozUBKW7CHxETUbch_BuCKrMEihqZWnjItbWUfDgxauBfrOo2DF7j2s_pLEEQsdZUCZSXLLtcoTxbjAk81RGkDpewkGuvlXJoX4tKvnN2wqmqz58rNWQoyZ9WycH0-YMG-JsxCKYhv8p_6uTvx3InZaoMWXRg"

bot_token = token
bot_group_id = 217770282
vk = Bot(bot_token, bot_group_id)


@vk.on.private_message(text=['Начать', 'Ку', 'Привет'])
# Сама функция:
async def privet(message: Message):
    # Ответ на сообщение
    await message.answer('Приветик!')


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
            # one_time - True - одноразовая клавиатура, False - постоянная клавиатура
            # inline - True - клавиатура прикрепляется к сообщению(РАССМОТРИМ), False - клавиаутра в стандартном положении
            # .add - добавить кнопку
            # .row - отступ
            # Цвета: POSITIVE - Ярко зеленый, SECONDARY(можно нечего не указывать) - БЛЕДНО БЕЛЫЙ
            # PRIMARY - СИНИЙ, NEGATIVE - КРАСНЫЙ

            Keyboard(one_time=False, inline=False)
                .add(Text('Главный раздел'), color=KeyboardButtonColor.POSITIVE)
                .add(Text('Направления подготовки и специальности'), color=KeyboardButtonColor.POSITIVE)
                .row()
                .add(Text('Главные даты приёмной комиссии'), color=KeyboardButtonColor.POSITIVE)
                .add(Text('Минимальные проходные баллы'), color=KeyboardButtonColor.POSITIVE)
                .row()
                .add(Text('Дополнительное обучение'), color=KeyboardButtonColor.POSITIVE)
                .add(Text('Платные образовательные услуги'), color=KeyboardButtonColor.POSITIVE)
                .row()
                .add(Text('Об университете'), color=KeyboardButtonColor.POSITIVE)
                .add(Text('Вопросы и ответы'), color=KeyboardButtonColor.POSITIVE)
                .row()
                .add(Text('Контакты'), color=KeyboardButtonColor.POSITIVE)
                .add(Text('Оставить заявку'), color=KeyboardButtonColor.POSITIVE)
        )
    )


@vk.on.private_message(text=['Главный раздел'])
# Сама функция:
async def privet(message: Message):
    # Ответ на сообщение
    await message.answer('Это главный раздел!')


@vk.on.private_message(text=['Направления подготовки и специальности'])
# Сама функция:
async def privet(message: Message):
    # Ответ на сообщение
    await message.answer('Это направления подготовки и специальности!')


@vk.on.private_message(text=['Главные даты приёмной комиссии'])
# Сама функция:
async def privet(message: Message):
    # Ответ на сообщение
    await message.answer('Это главные даты приёмной комиссии!')


vk.run_forever()
'''
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            request = event.text
            bot = Vk_bot(event.user_id)
            if request == "Старт":
                write_msg(event.user_id, "Добро пожаловать в чат бот приёмной комиссии ПГУПС!")
            if request == "Главный раздел":
                x = 0
            if request == "Направление подготовки и специальности":
                x = 0
            if request == "Главные даты приёмной комиссии":
                x = 0
            if request == "Минимальные проходные баллы":
                x = 0
            if request == "Дополнительное обучение":
                x = 0
            if request == "Платные образовательные услуги":
                x = 0
            if request == "Об университете":
                x = 0
            if request == "Вопросы и ответы":
                x = 0
            if request == "Контакты":
                x = 0
            if request == "Оставить заявку":
                x = 0
'''

if __name__ == '__main__':
    main()
