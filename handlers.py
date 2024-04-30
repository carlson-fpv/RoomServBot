import typing_extensions
from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import FSInputFile


# Cоздадим объект Роутера
router = Router()

# Массив с id загруженных фото для последующего использования
file_ids = []


# Декоратор обеспечивает фильтрацию по полученному сообщению
@router.message(Command("start"))
# Асинхронный вызов ответа на команду "/start"
async def start_handler(msg: Message):
    hotel_img = FSInputFile("media/hotel.jpg")
    await msg.answer_photo(hotel_img)
    builder = InlineKeyboardBuilder()
    builder.button(
        text="Забронировать номер",
        callback_data="hire_room"
    )

    builder.button(
        text="Вызвать уборку номера",
        callback_data="call_cleaner"
    )

    builder.button(
        text="Заказать еду в номер",
        callback_data="order_food"
    )

    builder.button(
        text="Взять в аренду",
        callback_data="hire_something"
    )

    builder.button(
        text="Посмотреть афишу",
        callback_data="look_shedule"
    )

    builder.button(
        text="Развлечения",
        callback_data="entertainment"
    )
    builder.adjust(2, 2)
    await msg.answer("Отель Кировакан находится в самом центре города Ванадзор.\n"
                     "Соответствуя высоким стандартам, отель предлагает условия для полноценного отдыха: "
                     "комфортабельные номера, начиная от категорий standart (Single/Double), заканчивая superior "
                     "(deluxe , family suite), а также шикарный интерьер, просторную территорию, широкий спектр услуг "
                     "(платных и бесплатных), вкуснейшую кухню с разнообразным ассортиментом еды.",
                     reply_markup=builder.as_markup()
    )


@router.callback_query(F.data == "hire_room")
async def hire_button_handler(callback: types.CallbackQuery):
    room_img = FSInputFile("media/rooms/room_1.jpg")
    await callback.message.answer_photo(room_img)
    builder = InlineKeyboardBuilder()
    builder.button(
        text="Выбрать даты",
        callback_data="choose_dates_1"
    )
    builder.button(
        text="Забронировать",
        callback_data="final_hire_1"
    )
    await callback.message.answer("Двухместный номер. Раздельные кровати, холодильник, минибар.",
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


@router.callback_query(F.data == "order_food")
async def hire_button_handler(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    menu_img = FSInputFile("media/restaurant/restaurant_menu.jpg")
    await callback.message.answer_photo(menu_img)
    builder.button(
        text="Сделать заказ",
        callback_data="make_food_order"
    )
    builder.button(
        text="Оплатить",
        callback_data="food_payment"
    )
    builder.button(
        text="Оставить чаевые",
        callback_data="leave_a_tip"
    )
    await callback.message.answer("Наш ресторан работает с 8:00 до 01:00", reply_markup=builder.as_markup())
    await callback.answer()


@router.callback_query(F.data == "hire_something")
async def hire_button_handler(callback: types.CallbackQuery):
    bike_img = FSInputFile("media/activity/bike.jpg")
    boat_img = FSInputFile("media/activity/boat.jpg")
    scooter_img = FSInputFile("media/activity/scooter.jpg")
    ski_img = FSInputFile("media/activity/ski.jpg")
    await callback.message.answer_photo(bike_img)
    await callback.message.answer_photo(boat_img)
    await callback.message.answer_photo(scooter_img)
    await callback.message.answer_photo(ski_img)
    builder = InlineKeyboardBuilder()
    builder.button(
        text="Забронировать велосипед",
        callback_data="bike_hire"
    )
    builder.button(
        text="Забронировать лодку",
        callback_data="boat_hire"
    )
    builder.button(
        text="Забронировать самокат",
        callback_data="scooter_hire"
    )
    builder.button(
        text="Забронировать лыжи",
        callback_data="ski_hire"
    )
    await callback.message.answer("Мы предлагаем в аренду велосипеды, лыжи, лодки и самокаты",
                                  reply_markup=builder.as_markup())
    await callback.answer()


@router.callback_query(F.data == "look_shedule")
async def hire_button_handler(callback: types.CallbackQuery):
    await callback.message.answer("Какой телевизор, иди гулять!")
    await callback.answer()


@router.callback_query(F.data == "entertainment")
async def hire_button_handler(callback: types.CallbackQuery):
    await callback.message.answer("Нарды или нарды?")
    await callback.answer()


@router.callback_query(F.data == "choose_dates_1")
async def hire_button_handler(callback: types.CallbackQuery):
    await callback.message.answer("Даты выбраны")
    await callback.answer()


@router.callback_query(F.data == "final_hire_1")
async def hire_button_handler(callback: types.CallbackQuery):
    await callback.message.answer("Номер забронирован")
    await callback.answer()


@router.callback_query(F.data == "cleaning_time")
async def hire_button_handler(callback: types.CallbackQuery):
    await callback.message.answer("Уборка запланирована")
    await callback.answer()


@router.callback_query(F.data == "cleaning_comment")
async def hire_button_handler(callback: types.CallbackQuery):
    await callback.message.answer("Ваше мнение очень важно для нас")
    await callback.answer()


@router.callback_query(F.data == "make_food_order")
async def hire_button_handler(callback: types.CallbackQuery):
    await callback.message.answer("Ваш заказ принят")
    await callback.answer()


@router.callback_query(F.data == "food_payment")
async def hire_button_handler(callback: types.CallbackQuery):
    await callback.message.answer("Оплата принята")
    await callback.answer()


@router.callback_query(F.data == "leave_a_tip")
async def hire_button_handler(callback: types.CallbackQuery):
    await callback.message.answer("Благодарим за чаевые")
    await callback.answer()