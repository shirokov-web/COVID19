from misc import bot, dp
from aiogram import types
from handlers.user_handlers.helpers.generation_keyboard import UserGenerationKeyboard

import COVID19Py
from covid import Covid

covid = Covid()
covid19 = COVID19Py.COVID19()

@dp.message_handler(text = 'Северная Африка')
async def east_europe(message:types.Message):
    keyboard = UserGenerationKeyboard.north_africa()

    final_message = 'Выберите <b>страну</b>:'
    await message.answer(final_message, reply_markup=keyboard, parse_mode='HTML')

@dp.message_handler(text = 'Египет🇪🇬')
async def eg_info(message:types.Message):
    ukraine_cases = covid.get_status_by_country_name('Egypt')
    confirmed = ukraine_cases['confirmed']
    deaths = ukraine_cases['deaths']
    recovered = ukraine_cases['recovered']

    location = covid19.getLocationByCountryCode("EG")
    population = location[0]['country_population']
    boleet = round(confirmed*100/population,2)
    umerlo = round(deaths*100/population,3)

    
    line = '-' * 30

    final_message = f"<b>Данные в Египте🇪🇬:</b>\n🦠Заболевших: {confirmed:,} <b>чел.</b>\n🧑‍⚕️Выздоровело: {recovered:,} <b>чел.</b>\n☠️Сметрей: {deaths:,} <b>чел.</b>\n{line}\nНаселение: {population:,} чел.\nБолеет: {boleet}% населения\nУмерло: {umerlo}% населения"


    await message.answer(final_message, parse_mode='HTML')

@dp.message_handler(text = 'Тунис🇹🇳')
async def tn_info(message:types.Message):
    ukraine_cases = covid.get_status_by_country_name('Tunisia')
    confirmed = ukraine_cases['confirmed']
    deaths = ukraine_cases['deaths']
    recovered = ukraine_cases['recovered']

    location = covid19.getLocationByCountryCode("TN")
    population = location[0]['country_population']
    boleet = round(confirmed*100/population,2)
    umerlo = round(deaths*100/population,3)

    
    line = '-' * 30

    final_message = f"<b>Данные в Тунисе🇹🇳:</b>\n🦠Заболевших: {confirmed:,} <b>чел.</b>\n🧑‍⚕️Выздоровело: {recovered:,} <b>чел.</b>\n☠️Сметрей: {deaths:,} <b>чел.</b>\n{line}\nНаселение: {population:,} чел.\nБолеет: {boleet}% населения\nУмерло: {umerlo}% населения"


    await message.answer(final_message, parse_mode='HTML')

@dp.message_handler(text = 'Алжир🇩🇿')
async def dz_info(message:types.Message):
    ukraine_cases = covid.get_status_by_country_name('Algeria')
    confirmed = ukraine_cases['confirmed']
    deaths = ukraine_cases['deaths']
    recovered = ukraine_cases['recovered']

    location = covid19.getLocationByCountryCode("DZ")
    population = location[0]['country_population']
    boleet = round(confirmed*100/population,2)
    umerlo = round(deaths*100/population,3)

    
    line = '-' * 30

    final_message = f"<b>Данные в Алжире🇩🇿:</b>\n🦠Заболевших: {confirmed:,} <b>чел.</b>\n🧑‍⚕️Выздоровело: {recovered:,} <b>чел.</b>\n☠️Сметрей: {deaths:,} <b>чел.</b>\n{line}\nНаселение: {population:,} чел.\nБолеет: {boleet}% населения\nУмерло: {umerlo}% населения"


    await message.answer(final_message, parse_mode='HTML')

@dp.message_handler(text = 'Ливия🇱🇾')
async def ly_info(message:types.Message):
    ukraine_cases = covid.get_status_by_country_name('Libya')
    confirmed = ukraine_cases['confirmed']
    deaths = ukraine_cases['deaths']
    recovered = ukraine_cases['recovered']

    location = covid19.getLocationByCountryCode("LY")
    population = location[0]['country_population']
    boleet = round(confirmed*100/population,2)
    umerlo = round(deaths*100/population,3)

    
    line = '-' * 30

    final_message = f"<b>Данные в Ливии🇱🇾:</b>\n🦠Заболевших: {confirmed:,} <b>чел.</b>\n🧑‍⚕️Выздоровело: {recovered:,} <b>чел.</b>\n☠️Сметрей: {deaths:,} <b>чел.</b>\n{line}\nНаселение: {population:,} чел.\nБолеет: {boleet}% населения\nУмерло: {umerlo}% населения"


    await message.answer(final_message, parse_mode='HTML')

@dp.message_handler(text = 'Западная Сахара🇪🇭')
async def eh_info(message:types.Message):
    ukraine_cases = covid.get_status_by_country_name('Western Sahara')
    confirmed = ukraine_cases['confirmed']
    deaths = ukraine_cases['deaths']
    recovered = ukraine_cases['recovered']

    location = covid19.getLocationByCountryCode("EH")
    population = location[0]['country_population']
    boleet = round(confirmed*100/population,2)
    umerlo = round(deaths*100/population,3)

    
    line = '-' * 30

    final_message = f"<b>Данные в Западной Сахаре🇪🇭:</b>\n🦠Заболевших: {confirmed:,} <b>чел.</b>\n🧑‍⚕️Выздоровело: {recovered:,} <b>чел.</b>\n☠️Сметрей: {deaths:,} <b>чел.</b>\n{line}\nНаселение: {population:,} чел.\nБолеет: {boleet}% населения\nУмерло: {umerlo}% населения"


    await message.answer(final_message, parse_mode='HTML')

@dp.message_handler(text = 'Марокко🇲🇦')
async def ma_info(message:types.Message):
    ukraine_cases = covid.get_status_by_country_name('Morocco')
    confirmed = ukraine_cases['confirmed']
    deaths = ukraine_cases['deaths']
    recovered = ukraine_cases['recovered']

    location = covid19.getLocationByCountryCode("MA")
    population = location[0]['country_population']
    boleet = round(confirmed*100/population,2)
    umerlo = round(deaths*100/population,3)

    
    line = '-' * 30

    final_message = f"<b>Данные в Марокко🇲🇦:</b>\n🦠Заболевших: {confirmed:,} <b>чел.</b>\n🧑‍⚕️Выздоровело: {recovered:,} <b>чел.</b>\n☠️Сметрей: {deaths:,} <b>чел.</b>\n{line}\nНаселение: {population:,} чел.\nБолеет: {boleet}% населения\nУмерло: {umerlo}% населения"


    await message.answer(final_message, parse_mode='HTML')

@dp.message_handler(text = 'Мавритания🇲🇷')
async def mr_info(message:types.Message):
    ukraine_cases = covid.get_status_by_country_name('Mauritania')
    confirmed = ukraine_cases['confirmed']
    deaths = ukraine_cases['deaths']
    recovered = ukraine_cases['recovered']

    location = covid19.getLocationByCountryCode("MR")
    population = location[0]['country_population']
    boleet = round(confirmed*100/population,2)
    umerlo = round(deaths*100/population,3)

    
    line = '-' * 30

    final_message = f"<b>Данные в Мавритании🇲🇷:</b>\n🦠Заболевших: {confirmed:,} <b>чел.</b>\n🧑‍⚕️Выздоровело: {recovered:,} <b>чел.</b>\n☠️Сметрей: {deaths:,} <b>чел.</b>\n{line}\nНаселение: {population:,} чел.\nБолеет: {boleet}% населения\nУмерло: {umerlo}% населения"


    await message.answer(final_message, parse_mode='HTML')