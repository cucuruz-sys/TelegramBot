import random
import asyncio
import requests
import bs4
from Beautiful_soup_parser import proh_ball_func
from typing import Optional
from vkbottle import GroupEventType, GroupTypes, Keyboard, Text, VKAPIError
from vkbottle.bot import Bot, Message
from vkbottle import Keyboard, KeyboardButtonColor, Text, OpenLink
from vkbottle.tools import DocMessagesUploader
from vkbottle.tools import PhotoMessageUploader
from vkbottle_types.objects import PhotosPhoto, PhotosPhotoSizes
from random import randint


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


token = "vk1.a.3-YxoDnZ_0tnqd97ikODErQFX1DxvwOGC9nRyTULXCcclGbfONcP91cRB-ozUBKW7CHxETUbch_BuCKrMEihqZWnjItbWUfDgxauBfrOo2DF7j2s_pLEEQsdZUCZSXLLtcoTxbjAk81RGkDpewkGuvlXJoX4tKvnN2wqmqz58rNWQoyZ9WycH0-YMG-JsxCKYhv8p_6uTvx3InZaoMWXRg"

bot_token = token
bot_group_id = 217770282
o_ege1 = '/Images/1-o_bs_ok_ege.jpg'
o_ege2 = '/Images/1-o_bs_p_ege.jpg'
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
async def main_part(message: Message):
    # Ответ на сообщение
    await message.answer('Это главный раздел!')


@vk.on.private_message(text=['Направления подготовки и специальности'])
# Сама функция:
async def specialty_part(message: Message):
    # Ответ на сообщение
    await message.answer('Это направления подготовки и специальности!')


@vk.on.private_message(text=['Главные даты приёмной комиссии'])
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
                .add(Text('Очное обучение'), color=KeyboardButtonColor.POSITIVE)
                .add(Text('Заочное обучение'), color=KeyboardButtonColor.POSITIVE)
                .row()
                .add(Text("Особая квота"), color=KeyboardButtonColor.POSITIVE)
        )
    )


@vk.on.private_message(text=['Очное обучение'])
# Сама функция:
async def min_points_part(message: Message):
    # Ответ на сообщение
    await message.answer("Часть 1:", attachment=o_ege1)
    await message.answer("Часть 2:", attachment=o_ege2)


@vk.on.private_message(text=['Заочное обучение'])
# Сама функция:
async def min_points_part(message: Message):
    # Ответ на сообщение
    await message.answer("Раздел заочное обучение")
#

@vk.on.private_message(text=['Минимальные проходные баллы'])
# Сама функция:
async def min_points_part(message: Message):
    ballArr = proh_ball_func()
    str = ""
    for line in ballArr:
        str += line[0] + "\n\t2019 год: " + line[1] + ";\t2020 год: " + line[2] + ";\t2021 год: " + line[3] + "\n\n"
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
    await message.answer('Это раздел об университете!')


@vk.on.private_message(text=['Вопросы и ответы'])
# Сама функция:
async def questions_answers_part(message: Message):
    # Ответ на сообщение
    await message.answer('Это раздел вопросов и ответов!')


@vk.on.private_message(text=['Контакты'])
# Сама функция:
async def contacts_part(message: Message):
    # Ответ на сообщение
    await message.answer('Это раздел контактов!')


@vk.on.private_message(text=['Оставить заявку'])
# Сама функция:
async def write_part(message: Message):
    # Ответ на сообщение
    await message.answer('Это раздел!')


vk.run_forever()

if __name__ == '__main__':
    main()
