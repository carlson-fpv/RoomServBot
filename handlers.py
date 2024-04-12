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
    builder.row(types.InlineKeyboardButton(
        text="Забронировать номер",
        callback_data="hire_room")
    )

    builder.row(types.InlineKeyboardButton(
        text="Вызвать уборку номера",
        callback_data="call_cleaner"
    ))

    builder.row(types.InlineKeyboardButton(
        text="Заказать еду в номер",
        callback_data="order_food"
    ))

    builder.row(types.InlineKeyboardButton(
        text="Взять в аренду",
        callback_data="hire_something"
    ))

    builder.row(types.InlineKeyboardButton(
        text="Посмотреть афишу",
        callback_data="look_shedule"
    ))

    builder.row(types.InlineKeyboardButton(
        text="Развлечения",
        callback_data="entertainment"
    ))
    #builder.adjust(sizes=20, repeat=True)
    await msg.answer("Отель Кировакан находится в самом центре города Ванадзор.\n"
                     "Соответствуя высоким стандартам, отель предлагает условия для полноценного отдыха: "
                     "комфортабельные номера, начиная от категорий standart (Single/Double), заканчивая superior "
                     "(deluxe , family suite), а также шикарный интерьер, просторную территорию, широкий спектр услуг "
                     "(платных и бесплатных), вкуснейшую кухню с разнообразным ассортиментом еды.",
                     reply_markup=builder.as_markup()
    )


@router.callback_query(F.data == "hire_room")
async def hire_button_handler(callback: types.CallbackQuery):
    await callback.message.answer("Номер забронирован")
    await callback.answer()


@router.callback_query(F.data == "call_cleaner")
async def hire_button_handler(callback: types.CallbackQuery):
    await callback.message.answer("Уборка вызвана")
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


@router.message()
# Асинхронный вызов ответа на любое сообщение (отсутствует фильтр в декораторе)
async def message_handler(msg: Message):
    await msg.answer(msg.text)

