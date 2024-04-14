import typing_extensions
from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import FSInputFile


# Cоздадим объект Роутера
router = Router()


# Декоратор обеспечивает фильтрацию по полученному сообщению
@router.message(Command("start"))
# Асинхронный вызов ответа на команду "/start"
async def start_handler(msg: Message):
    file_ids = []
    hotel_img = FSInputFile("media/hotel.jpg")
    result = await msg.answer_photo(
        hotel_img
    )
    file_ids.append(result.photo[-1].file_id)
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
    await callback.message.answer_photo(
        room_img
    )
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
    await callback.message.answer("Заказ принят")
    await callback.answer()


@router.callback_query(F.data == "hire_something")
async def hire_button_handler(callback: types.CallbackQuery):
    await callback.message.answer("Что-нибудь найдём :)")
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
