from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

mainMenu = InlineKeyboardMarkup(row_width=2)
btnRandom = InlineKeyboardButton(text="👤 Обратится", callback_data="btnRandom")
btnUrl = InlineKeyboardButton(text="✅ Wildberries", url="https://www.wildberries.ru/seller/501108")

supportMenu = InlineKeyboardMarkup(row_width=2)
btnBack = InlineKeyboardButton(text="⬅️ Вернутся", callback_data="btnBack")

mainMenu.insert(btnRandom)
mainMenu.insert(btnUrl)

supportMenu.insert(btnBack)