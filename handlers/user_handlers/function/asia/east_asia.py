from misc import bot, dp
from aiogram import types
from handlers.user_handlers.helpers.generation_keyboard import UserGenerationKeyboard

import COVID19Py
from covid import Covid

covid = Covid()
covid19 = COVID19Py.COVID19()

@dp.message_handler(text = 'Восточная Азия')
async def east_europe(message:types.Message):
    keyboard = UserGenerationKeyboard.east_asia()

    final_message = 'Выберите <b>страну</b>:'
    await message.answer(final_message, reply_markup=keyboard, parse_mode='HTML')


@dp.message_handler(text = 'Китай🇨🇳')
async def cn_info(message:types.Message):
    ukraine_cases = covid.get_status_by_country_name('China')
    confirmed = ukraine_cases['confirmed']
    deaths = ukraine_cases['deaths']
    recovered = ukraine_cases['recovered']

    location = covid19.getLocationByCountryCode("CN")
    population = location[0]['country_population']
    boleet = round(confirmed*100/population,2)
    umerlo = round(deaths*100/population,3)

    
    line = '-' * 30

    final_message = f"<b>Данные в Китае🇨🇳:</b>\n🦠Заболевших: {confirmed:,} <b>чел.</b>\n🧑‍⚕️Выздоровело: {recovered:,} <b>чел.</b>\n☠️Сметрей: {deaths:,} <b>чел.</b>\n{line}\nНаселение: {population:,} чел.\nБолеет: {boleet}% населения\nУмерло: {umerlo}% населения"


    await message.answer(final_message, parse_mode='HTML')

@dp.message_handler(text = 'Япония🇯🇵')
async def jp_info(message:types.Message):
    ukraine_cases = covid.get_status_by_country_name('Japan')
    confirmed = ukraine_cases['confirmed']
    deaths = ukraine_cases['deaths']
    recovered = ukraine_cases['recovered']

    location = covid19.getLocationByCountryCode("JP")
    population = location[0]['country_population']
    boleet = round(confirmed*100/population,2)
    umerlo = round(deaths*100/population,3)

    
    line = '-' * 30

    final_message = f"<b>Данные в Японии🇯🇵:</b>\n🦠Заболевших: {confirmed:,} <b>чел.</b>\n🧑‍⚕️Выздоровело: {recovered:,} <b>чел.</b>\n☠️Сметрей: {deaths:,} <b>чел.</b>\n{line}\nНаселение: {population:,} чел.\nБолеет: {boleet}% населения\nУмерло: {umerlo}% населения"


    await message.answer(final_message, parse_mode='HTML')

@dp.message_handler(text = 'Южная Корея🇰🇷')
async def kr_info(message:types.Message):
    ukraine_cases = covid.get_status_by_country_name('Korea, South')
    confirmed = ukraine_cases['confirmed']
    deaths = ukraine_cases['deaths']
    recovered = ukraine_cases['recovered']

    location = covid19.getLocationByCountryCode("KR")
    population = location[0]['country_population']
    boleet = round(confirmed*100/population,2)
    umerlo = round(deaths*100/population,3)

    
    line = '-' * 30

    final_message = f"<b>Данные в Южной Корее🇰🇷:</b>\n🦠Заболевших: {confirmed:,} <b>чел.</b>\n🧑‍⚕️Выздоровело: {recovered:,} <b>чел.</b>\n☠️Сметрей: {deaths:,} <b>чел.</b>\n{line}\nНаселение: {population:,} чел.\nБолеет: {boleet}% населения\nУмерло: {umerlo}% населения"


    await message.answer(final_message, parse_mode='HTML')

@dp.message_handler(text = 'Северная Корея🇰🇵')
async def kp_info(message:types.Message):
    population = 24900000
    line = '-' * 30

    final_message = f"<b>Данные в Южной Корее🇰🇷:</b>\n🦠Заболевших: <i>Нет точной информации.</i> <b>чел.</b>\n🧑‍⚕️Выздоровело: <i>Нет точной информации.</i> <b>чел.</b>\n☠️Сметрей: <i>Нет точной информации.</i> <b>чел.</b>\n{line}\nНаселение: {population:,} чел.\nБолеет: <i>Нет точной информации.</i> населения\nУмерло: <i>Нет точной информации.</i>"


    await message.answer(final_message, parse_mode='HTML')

@dp.message_handler(text = 'Монголия🇲🇳')
async def mn_info(message:types.Message):
    ukraine_cases = covid.get_status_by_country_name('Mongolia')
    confirmed = ukraine_cases['confirmed']
    deaths = ukraine_cases['deaths']
    recovered = ukraine_cases['recovered']

    location = covid19.getLocationByCountryCode("MN")
    population = location[0]['country_population']
    boleet = round(confirmed*100/population,2)
    umerlo = round(deaths*100/population,3)

    
    line = '-' * 30

    final_message = f"<b>Данные в Монголии🇲🇳:</b>\n🦠Заболевших: {confirmed:,} <b>чел.</b>\n🧑‍⚕️Выздоровело: {recovered:,} <b>чел.</b>\n☠️Сметрей: {deaths:,} <b>чел.</b>\n{line}\nНаселение: {population:,} чел.\nБолеет: {boleet}% населения\nУмерло: {umerlo}% населения"


    await message.answer(final_message, parse_mode='HTML')