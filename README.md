from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import (
    Message,
    ReplyKeyboardMarkup,
    KeyboardButton,
    FSInputFile
)
import asyncio

bot = Bot("8290561949:AAH3VOdpdFDCq8qFichTNkv3CRtAN65k90U")
dp = Dispatcher()

menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Orqaga"), KeyboardButton(text="Dars va director va oqituvchilar haqida")],
        [KeyboardButton(text="Telefon raqam va locatio")],
        [KeyboardButton(text="Talabalarni kiyinish")]
    ],
    resize_keyboard=True
)

wg = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Duyshaba dars jadvali"), KeyboardButton(text="Darslar tugash vaqti")],
        [KeyboardButton(text="Fan o'qituvchilari")],
        [KeyboardButton(text="O'qitivchilar haqida malumot")],
        [KeyboardButton(text="Maktab direktori haqida malumot")],
        [KeyboardButton(text="Orqaga")]
    ],
    resize_keyboard=True
)

rg = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Telefon raqam", request_contact=True), KeyboardButton(text="Royhatdan o'tish")],
        [KeyboardButton(text="Location"), KeyboardButton(text="Orqaga")]
    ],
    resize_keyboard=True
)

tr = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Oq koynak")],
        [KeyboardButton(text="Qora shim")],
        [KeyboardButton(text="Labutin")],
        [KeyboardButton(text="Orqaga")]
    ],
    resize_keyboard=True
)

@dp.message(CommandStart())
async def start(m: Message):
    await m.answer("Assalomu alaykum!", reply_markup=menu)

@dp.message(F.text == "Orqaga")
async def back(m: Message):
    await m.answer("Asosiy menyu:", reply_markup=menu)

@dp.message(F.text == "Dars va director va oqituvchilar haqida")
async def dars(m: Message):
    await m.answer("Siz dars bo‘limidasiz", reply_markup=wg)

@dp.message(F.text == "Maktab direktori haqida malumot")
async def director(m: Message):
    await m.answer("""
        F.I.Sh.: Karimov Akmal Jamolovich
Lavozimi: 300-sonli umumta’lim maktabi direktori
Tug‘ilgan yili: 1980
Ma’lumoti: Oliy, Toshkent davlat pedagogika universiteti (2002)
Mutaxassisligi: Pedagogika va boshqaruv
Ilmiy daraja: Pedagogika bo‘yicha magistr               
    """)

@dp.message(F.text=="O'qituvchilani telefon raqami")
async def teacher_phone(m: Message):
    await m.answer(
        "Matematika: 996454352\nRus tili: 994352741\nO‘zbek tili: 997342913\nFizika: 994204222\nAlgebra: 995365238")

@dp.message(F.text == "O'qitivchilar haqida malumot")
async def teachers(m: Message):
    await m.answer("O‘qituvchilar tajribasi: o‘rtacha 12 yil.")

@dp.message(F.text == "Fan o'qituvchilari")
async def fans(m: Message):
    await m.answer("Matematika – Gulchehra\nRus tili – Mariyam\nFizika – Robiya\nAlgebra:Ziyodan\nO'zbektili:Sayyora")

@dp.message(F.text == "Darslar tugash vaqti")
async def vaqt(m: Message):
    await m.answer("1-dars:8:45\n2-dars:9:35\n3-dars:10:25\n4-dars-11:35\n5-dars:12:20")

@dp.message(F.text == "Duyshaba dars jadvali")
async def jadval(m: Message):
    await m.answer("Matematika\nRus tili\nUzbek tili\nFizika\nAlgebra")

@dp.message(F.text == "Telefon raqam va locatio")
async def tel_loc(m: Message):
    await m.answer("Bo‘lim tanlang:", reply_markup=rg)

@dp.message(F.text == "Location")
async def location(m: Message):
    await m.answer("Maktab manzili:\nhttps://2gis.uz/...")

@dp.message(F.text == "Telefon raqam")
async def phone(m: Message):
    await m.answer("Telefon raqamingiz yuborildi.")

@dp.message(F.text == "Talabalarni kiyinish")
async def dress(m: Message):
    await m.answer("Kiyinish bo‘limi", reply_markup=tr)

@dp.message(F.text == "Oq koynak")
async def white(m: Message):
    await m.answer_photo(FSInputFile("1/cq7r0jffrr885gh1l5j0.jpg"))

@dp.message(F.text == "Qora shim")
async def black(m: Message):
    await m.answer_photo(FSInputFile("2/shopping.webp"))

@dp.message(F.text == "Labutin")
async def labutin(m: Message):
    await m.answer_photo(FSInputFile("3/shopping.webp"))

@dp.message(F.text == "Royhatdan o'tish")
async def royhat(m: Message):
    await m.answer("Ro‘yxatdan o‘tish uchun ism va familiyangizni yozing.")
@dp.message(F.text)
async def text_saver(m: Message):
    text = m.text
    with open(f"downloads/{m.from_user.full_name}.txt", "a+") as f:
        f.write(f"{text}\n")
    await m.answer("Siz ro‘yxatdan o‘tdingiz!")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
