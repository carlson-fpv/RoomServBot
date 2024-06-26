import typing_extensions
from aiogram import types, F, Router
from aiogram.types import Message, FSInputFile, WebAppInfo
from aiogram.filters import Command, StateFilter
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder
from aiogram.utils.media_group import MediaGroupBuilder
from datetime import datetime
from calendar import monthrange

# Cоздадим объект Роутера
router = Router()
# Массив с id загруженных фото для последующего использования
file_ids = []
month_name = {1: "Январь", 2: "Февраль", 3: "Март", 4: "Апрель",
              5: "Май", 6: "Июнь", 7: "Июль", 8: "Август",
              9: "Сентябрь", 10: "Октябрь", 11: "Ноябрь", 12: "Декабрь"}

restaurant_app = WebAppInfo(url='https://ahotelpoint.ru/RoomServBot/web_app/public/magazine.html?type=restaurant')
stuff_app = WebAppInfo(url='https://ahotelpoint.ru/RoomServBot/web_app/public/magazine.html?type=stuff')
map_app = WebAppInfo(url='https://ahotelpoint.ru/RoomServBot/web_app/public/map.html')


class ConversationStates(StatesGroup):
    waiting_for_cleaning_time = State()
    waiting_for_cleaning_comment = State()
    waiting_for_restaurant_time = State()
    waiting_for_stuff_pickup_time = State()
    waiting_for_restaurant_webapp_data = State()
    waiting_for_stuff_webapp_data = State()


# Декоратор обеспечивает фильтрацию по полученному сообщению
@router.message(Command("start"))
# Асинхронный вызов ответа на команду "/start"
async def start_handler(msg: Message):
    hotel_img = FSInputFile("web_app/public/img/reseption.png")
    await msg.answer_photo(hotel_img)
    builder = InlineKeyboardBuilder()
    builder.button(
        text="Бронь номера",
        callback_data="choose_room"
    )

    builder.button(
        text="Уборка номера",
        callback_data="call_cleaner"
    )

    builder.button(
        text="Заказ еды",
        callback_data="order_food_webapp"
    )

    builder.button(
        text="Аренда",
        callback_data="hire_something"
    )

    builder.button(
        text="Афиша",
        callback_data="look_schedule"
    )

    builder.button(
        text="Развлечения",
        callback_data="entertainment"
    )
    builder.adjust(2, 2)
    await msg.answer("Загородный комплекс отдыха Залесье - это вариант отдыха на любой сезон. "
                     "Соответствуя высоким стандартам наш комплекс предлагает для вас различные варианты отдыха: "
                     "комфортабельные номера в главном корпусе (одиночный, семейный или люкс), "
                     "индивидуальные виллы вдоль реки и небольшие шале в сосновом лесу.\n"
                     "На территории отеля вы встретите бассейн и выход к реке с закрытым пляжем, можете попариться в "
                     "банном комплексе или расслабиться в спа.\nРесторан \"Елки\" находится в одном из самых "
                     "живописных уголков территории отеля - в сосновом бору на побережье озера и предложит вам "
                     "самые изысканные блюда.\nНаш отель предлагает широкий спектр услуг для полноценного "
                     "отдыха (активного и пассивного): путешествия на лодках, сапах по реке, аренда велосипедов, "
                     "электро-мотоциклов и квадроциклов, а зимой - лыжи, тюбинг, снегоходы.\nВокруг отеля вас ждут "
                     "туристические маршруты по живописным местам, запутанные и увлекательные квесты и многое другое.",
                     reply_markup=builder.as_markup()
                     )


@router.callback_query(F.data == "choose_room")
async def choose_room_handler(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.button(text="Однокомнатный номер", callback_data="single_room_show")
    builder.button(text="Двухкомнатный номер", callback_data="double_room_show")
    builder.button(text="Домик", callback_data="house_show")
    builder.button(text="Шале", callback_data="shale_show")
    builder.adjust(1)
    await callback.message.answer("Какой тип номера Вы предпочитаете?", reply_markup=builder.as_markup())
    await callback.answer()


@router.callback_query(F.data == "single_room_show")
async def single_room_show_handler(callback: types.CallbackQuery):
    album_builder = MediaGroupBuilder()
    album_builder.add(
        type="photo",
        media=FSInputFile("web_app/public/img/single_room_1.jpg")
    )
    album_builder.add(
        type="photo",
        media=FSInputFile("web_app/public/img/single_room_2.jpg")
    )
    album_builder.add(
        type="photo",
        media=FSInputFile("web_app/public/img/single_room_3.jpg")
    )
    await callback.message.answer_media_group(media=album_builder.build())
    builder = InlineKeyboardBuilder()
    builder.button(text="Выбрать даты", callback_data="choose_dates_1")
    await callback.message.answer(text="Уютный и функциональный номер. "
                                       "Здесь есть все необходимое для комфортного отдыха и работы.\n"
                                       "Вместимость до 2х Гостей, Общая площадь - 21 м2",
                                  reply_markup=builder.as_markup())
    await callback.answer()


@router.callback_query(F.data == "double_room_show")
async def single_room_show_handler(callback: types.CallbackQuery):
    album_builder = MediaGroupBuilder()
    album_builder.add(
        type="photo",
        media=FSInputFile("web_app/public/img/double_room_1.jpg")
    )
    album_builder.add(
        type="photo",
        media=FSInputFile("web_app/public/img/double_room_2.jpg")
    )
    album_builder.add(
        type="photo",
        media=FSInputFile("web_app/public/img/double_room_3.jpg")
    )
    await callback.message.answer_media_group(media=album_builder.build())
    builder = InlineKeyboardBuilder()
    builder.button(text="Выбрать даты", callback_data="choose_dates_1")
    await callback.message.answer(text="Двухкомнатный семейный номер с элегантным интерьером и спокойной цветовой "
                                       "гаммой – это прекрасный выбор для Гостей, которые ценят безупречность и "
                                       "внимание к деталям. Вместимость до 4х Гостей. Общая площадь 41 м2",
                                  reply_markup=builder.as_markup())
    await callback.answer()


@router.callback_query(F.data == "house_show")
async def house_show_handler(callback: types.CallbackQuery):
    album_builder = MediaGroupBuilder()
    album_builder.add(
        type="photo",
        media=FSInputFile("web_app/public/img/house_1.png")
    )
    album_builder.add(
        type="photo",
        media=FSInputFile("web_app/public/img/house_2.png")
    )
    album_builder.add(
        type="photo",
        media=FSInputFile("web_app/public/img/house_3.png")
    )
    album_builder.add(
        type="photo",
        media=FSInputFile("web_app/public/img/house_4.png")
    )
    await callback.message.answer_media_group(media=album_builder.build())
    builder = InlineKeyboardBuilder()
    builder.button(text="Выбрать даты", callback_data="choose_dates_1")
    await callback.message.answer(text="Двухэтажный домик для 2-4 человек с огромным панорамным окном, террасой, "
                                       "видом на лес и озеро. И всепогодной беседкой для гриля.",
                                  reply_markup=builder.as_markup())
    await callback.answer()


@router.callback_query(F.data == "shale_show")
async def single_room_show_handler(callback: types.CallbackQuery):
    album_builder = MediaGroupBuilder()
    album_builder.add(
        type="photo",
        media=FSInputFile("web_app/public/img/shale_1.jpg")
    )
    album_builder.add(
        type="photo",
        media=FSInputFile("web_app/public/img/shale_2.jpg")
    )
    album_builder.add(
        type="photo",
        media=FSInputFile("web_app/public/img/shale_3.jpg")
    )
    await callback.message.answer_media_group(media=album_builder.build())
    builder = InlineKeyboardBuilder()
    builder.button(text="Выбрать даты", callback_data="choose_dates_1")
    await callback.message.answer(text="Шале 42 кв. м с большой террасой 22 кв. м. Рассчитано до 3-х взрослых людей. "
                                       "Дровяной камин с большим запасом дров, набор для разведения огня. "
                                       "На террасе расположена горячая купель из лиственницы диаметром 1.6 метра "
                                       "метра, рассчитанная на 2-3 взрослых человека.",
                                  reply_markup=builder.as_markup())
    await callback.answer()


@router.callback_query(F.data == "call_cleaner")
async def hire_button_handler(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.button(
        text="Выбрать время",
        callback_data="cleaning_time"
    )
    builder.button(
        text="Оставить комментарий",
        callback_data="cleaning_comment"
    )
    await callback.message.answer("Когда убрать номер?", reply_markup=builder.as_markup())
    await callback.answer()


@router.callback_query(F.data == "order_food_webapp")
async def food_button_handler(callback: types.CallbackQuery, state: FSMContext):
    builder = ReplyKeyboardBuilder()
    builder.button(text='Меню ресторана', web_app=restaurant_app)
    await state.set_state(ConversationStates.waiting_for_restaurant_webapp_data)
    await callback.message.answer("Что бы вы хотели заказать?", reply_markup=builder.as_markup(
        resize_keyboard=True,
        one_time_keyboard=True
    ))
    await callback.answer()


@router.message(lambda message: message.web_app_data, ConversationStates.waiting_for_restaurant_webapp_data)
async def web_app_data_processing(message: Message, state: FSMContext):
    await state.set_state(ConversationStates.waiting_for_restaurant_time)
    await message.answer("Заявка на оплату " + str(message.web_app_data.data) + ' рублей принята.' +
                         '\n' + 'Во сколько принести ваш заказ? Отправьте боту время в формате ЧЧ:ММ')


@router.message(ConversationStates.waiting_for_restaurant_time)
async def cleaning_time_confirmation(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("Спасибо, заказ принесут в " + message.text)


@router.callback_query(F.data == "hire_something")
async def hire_button_handler(callback: types.CallbackQuery, state: FSMContext):
    builder = ReplyKeyboardBuilder()
    builder.button(text='Забронировать спортинвентарь', web_app=stuff_app)
    await state.set_state(ConversationStates.waiting_for_stuff_webapp_data)
    await callback.message.answer(
        "Предлагаем ознакомиться с нашим ассортиментом спортинвентаря",
        reply_markup=builder.as_markup(
            resize_keyboard=True,
            one_time_keyboard=True
        )
    )
    await callback.answer()


@router.message(lambda message: message.web_app_data, ConversationStates.waiting_for_stuff_webapp_data)
async def web_app_data_processing(message: Message, state: FSMContext):
    await state.set_state(ConversationStates.waiting_for_stuff_pickup_time)
    await message.answer("Заявка на оплату " + str(message.web_app_data.data) + ' рублей принята.' +
                         '\n' + 'Во сколько хотите забрать снаряжение? Отправьте боту время в формате ЧЧ:ММ')


@router.message(ConversationStates.waiting_for_stuff_pickup_time)
async def cleaning_time_confirmation(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("Спасибо, подготовим всё к " + message.text)


@router.callback_query(F.data == "look_schedule")
async def hire_button_handler(callback: types.CallbackQuery):
    event_img = FSInputFile("web_app/public/img/schedule.jpg")
    await callback.message.answer_photo(event_img)
    builder = InlineKeyboardBuilder()
    builder.button(
        text="Пойду!",
        callback_data="register_in_event"
    )
    await callback.message.answer('Сегодня в 21:00 пройдет большой кинопоказ в летнем кинотеатре. Вас ждет '
                                  'новинка 2024 года, а также горячий попкорн и прохладительные напитки.',
                                  reply_markup=builder.as_markup())
    await callback.answer()


@router.callback_query(F.data == "entertainment")
async def hire_button_handler(callback: types.CallbackQuery):
    logo_img = FSInputFile("media/quests/adv_logo.jpg")
    await callback.message.answer_photo(logo_img)
    builder = InlineKeyboardBuilder()
    builder.button(
        text="Подъём на Старбакс",
        callback_data="starbucks_uphill"
    )
    builder.button(
        text="Городские холмы",
        callback_data="town_hills"
    )
    await callback.message.answer("Предлагаем Вашему вниманию интересные маршруты:",
                                  reply_markup=builder.as_markup())
    await callback.answer()


# Handler for displaying dates when room is hiring
@router.callback_query(F.data == "choose_dates_1")
async def hire_button_handler(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    days_count = monthrange(datetime.now().year, datetime.now().month)[1]
    builder.button(text="<==", callback_data="switch_month_back")
    builder.button(text=month_name[datetime.now().month] + ' ' + str(datetime.now().year), callback_data="_")
    builder.button(text="==>", callback_data="switch_month_fwd")
    for i in range(1, days_count + 1):
        builder.button(text=str(i), callback_data="date_checked")
    builder.adjust(3, 5)
    await callback.message.answer("Выберите дату бронирования", reply_markup=builder.as_markup())
    await callback.answer()


@router.callback_query(F.data == "final_hire_1")
async def hire_button_handler(callback: types.CallbackQuery):
    await callback.message.answer("Номер забронирован")
    await callback.answer()


@router.callback_query(F.data == "cleaning_time")
async def hire_button_handler(callback: types.CallbackQuery, state: FSMContext):
    await state.set_state(ConversationStates.waiting_for_cleaning_time)
    await callback.message.answer("Во сколько должен придти уборщик? Введите желаемое время в формате ЧЧ:ММ")
    await callback.answer()


@router.message(ConversationStates.waiting_for_cleaning_time)
async def cleaning_time_confirmation(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("Спасибо, уборщик придёт в " + message.text)
    # TODO: Добавить проверку вводимых данных


@router.callback_query(F.data == "cleaning_comment")
async def hire_button_handler(callback: types.CallbackQuery, state: FSMContext):
    await state.set_state(ConversationStates.waiting_for_cleaning_comment)
    await callback.message.answer("Напишите боту сообщение с комментарием и мы обязательно его прочитаем")
    await callback.answer()


@router.message(ConversationStates.waiting_for_cleaning_comment)
async def cleaning_time_confirmation(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("Спасибо, Ваше мнение очень важно для нас!")


@router.callback_query(F.data == "leave_a_tip")
async def hire_button_handler(callback: types.CallbackQuery):
    await callback.message.answer("Благодарим за чаевые")
    await callback.answer()


@router.callback_query(F.data == "register_in_event")
async def hire_button_handler(callback: types.CallbackQuery):
    await callback.message.answer("Вы зарегистрированы!")
    await callback.answer()


@router.callback_query(F.data == "starbucks_uphill")
async def hire_button_handler(callback: types.CallbackQuery):
    await callback.message.answer("Данный маршрут находится в разработке")
    await callback.answer()


@router.callback_query(F.data == "town_hills")
async def food_button_handler(callback: types.CallbackQuery):
    hills_route = FSInputFile("web_app/public/img/hills_route.png")
    await callback.message.answer_photo(hills_route)
    builder = InlineKeyboardBuilder()
    builder.button(text='Посмотреть маршрут', web_app=map_app)
    builder.button(text='Назад', callback_data='entertainment')

    await callback.message.answer("Предлагаем ознакомиться с маршрутом, для этого нажмите кнопку ниже",
                                  reply_markup=builder.as_markup())
    await callback.answer()


@router.callback_query(F.data == "date_checked")
async def hire_button_handler(callback: types.CallbackQuery):
    await callback.message.answer("Дата бронирования выбрана")
    await callback.answer()
'''
@router.callback_query(F.data == "")
async def hire_button_handler(callback: types.CallbackQuery):
    await callback.message.answer("")
    await callback.answer()
'''