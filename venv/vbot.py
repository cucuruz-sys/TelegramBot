import vk_api

from vk_api.longpool import VkLongPoll, VkEventType

token = "YxoDnZ_0tnqd97ikODErQFX1DxvwOGC9nRyTULXCcclGbfONcP91cRB-ozUBKW7CHxETUbch_BuCKrMEihqZWnjItbWUfDgxauBfrOo2DF7j2s_pLEEQsdZUCZSXLLtcoTxbjAk81RGkDpewkGuvlXJoX4tKvnN2wqmqz58rNWQoyZ9WycH0-YMG-JsxCKYhv8p_6uTvx3InZaoMWXRg"


def write_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message})


vk = vk_api.VkApi(token=token)

# Работа с сообщениями
longpoll = VkLongPoll(vk)

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            request = event.text
            if(request == "Старт"):
                write_msg(event.user_id, "Добро пожаловать в чат бот приёмной комиссии ПГУПС!")
                write_msg(event.user_id, "Главный раздел")
                write_msg(event.user_id, "Направление подготовки и специальности")
                write_msg(event.user_id, "Необходимые вступительные испытания")
                write_msg(event.user_id, "Главные даты приёмной комиссии")
                write_msg(event.user_id, "Минимальные проходные баллы")
                write_msg(event.user_id, "Дополнительное обучение")
                write_msg(event.user_id, "Платные образовательные услуги")
                write_msg(event.user_id, "Об университете")
                write_msg(event.user_id, "Вопросы и ответы")
                write_msg(event.user_id, "Контакты")
                write_msg(event.user_id, "Оставить заявку")
