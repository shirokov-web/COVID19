from misc import bot, dp
from aiogram import types
from handlers.user_handlers.helpers.generation_keyboard import UserGenerationKeyboard

import COVID19Py
from covid import Covid

covid = Covid()
covid19 = COVID19Py.COVID19()

@dp.message_handler(text = 'Восточная Европа')
async def east_europe(message:types.Message):
    keyboard = UserGenerationKeyboard.east_europe()

    final_message = 'Выберите <b>страну</b>:'
    await message.answer(final_message, reply_markup=keyboard, parse_mode='HTML')



@dp.message_handler(text = 'Чехия🇨🇿')
async def cz_info(message:types.Message):
    ukraine_cases = covid.get_status_by_country_name('Czechia')
    confirmed = ukraine_cases['confirmed']
    deaths = ukraine_cases['deaths']
    recovered = ukraine_cases['recovered']

    location = covid19.getLocationByCountryCode("CZ")
    population = location[0]['country_population']
    boleet = round(confirmed*100/population,2)
    umerlo = round(deaths*100/population,3)

    
    line = '-' * 30

    final_message = f"<b>Данные в Чехии🇨🇿:</b>\n🦠Заболевших: {confirmed:,} <b>чел.</b>\n🧑‍⚕️Выздоровело: {recovered:,} <b>чел.</b>\n☠️Сметрей: {deaths:,} <b>чел.</b>\n{line}\nНаселение: {population:,} чел.\nБолеет: {boleet}% населения\nУмерло: {umerlo}% населения"


    await message.answer(final_message, parse_mode='HTML')

@dp.message_handler(text = 'Болгария🇧🇬')
async def bg_info(message:types.Message):
    ukraine_cases = covid.get_status_by_country_name('Bulgaria')
    confirmed = ukraine_cases['confirmed']
    deaths = ukraine_cases['deaths']
    recovered = ukraine_cases['recovered']

    location = covid19.getLocationByCountryCode("BG")
    population = location[0]['country_population']
    boleet = round(confirmed*100/population,2)
    umerlo = round(deaths*100/population,3)

    
    line = '-' * 30

    final_message = f"<b>Данные в Болгарии🇧🇬:</b>\n🦠Заболевших: {confirmed:,} <b>чел.</b>\n🧑‍⚕️Выздоровело: {recovered:,} <b>чел.</b>\n☠️Сметрей: {deaths:,} <b>чел.</b>\n{line}\nНаселение: {population:,} чел.\nБолеет: {boleet}% населения\nУмерло: {umerlo}% населения"


    await message.answer(final_message, parse_mode='HTML')

@dp.message_handler(text = 'Венгрия🇭🇺')
async def hu_info(message:types.Message):
    ukraine_cases = covid.get_status_by_country_name('Hungary')
    confirmed = ukraine_cases['confirmed']
    deaths = ukraine_cases['deaths']
    recovered = ukraine_cases['recovered']

    location = covid19.getLocationByCountryCode("HU")
    population = location[0]['country_population']
    boleet = round(confirmed*100/population,2)
    umerlo = round(deaths*100/population,3)

    
    line = '-' * 30

    final_message = f"<b>Данные в Венгрии🇭🇺:</b>\n🦠Заболевших: {confirmed:,} <b>чел.</b>\n🧑‍⚕️Выздоровело: {recovered:,} <b>чел.</b>\n☠️Сметрей: {deaths:,} <b>чел.</b>\n{line}\nНаселение: {population:,} чел.\nБолеет: {boleet}% населения\nУмерло: {umerlo}% населения"


    await message.answer(final_message, parse_mode='HTML')

@dp.message_handler(text = 'Молдавия🇲🇩')
async def md_info(message:types.Message):
    ukraine_cases = covid.get_status_by_country_name('Moldova')
    confirmed = ukraine_cases['confirmed']
    deaths = ukraine_cases['deaths']
    recovered = ukraine_cases['recovered']

    location = covid19.getLocationByCountryCode("MD")
    population = location[0]['country_population']
    boleet = round(confirmed*100/population,2)
    umerlo = round(deaths*100/population,3)

    
    line = '-' * 30

    final_message = f"<b>Данные в Молдавии🇲🇩:</b>\n🦠Заболевших: {confirmed:,} <b>чел.</b>\n🧑‍⚕️Выздоровело: {recovered:,} <b>чел.</b>\n☠️Сметрей: {deaths:,} <b>чел.</b>\n{line}\nНаселение: {population:,} чел.\nБолеет: {boleet}% населения\nУмерло: {umerlo}% населения"


    await message.answer(final_message, parse_mode='HTML')

@dp.message_handler(text = 'Польша🇵🇱')
async def pl_info(message:types.Message):
    ukraine_cases = covid.get_status_by_country_name('Poland')
    confirmed = ukraine_cases['confirmed']
    deaths = ukraine_cases['deaths']
    recovered = ukraine_cases['recovered']

    location = covid19.getLocationByCountryCode("PL")
    population = location[0]['country_population']
    boleet = round(confirmed*100/population,2)
    umerlo = round(deaths*100/population,3)

    
    line = '-' * 30

    final_message = f"<b>Данные в Польше🇵🇱:</b>\n🦠Заболевших: {confirmed:,} <b>чел.</b>\n🧑‍⚕️Выздоровело: {recovered:,} <b>чел.</b>\n☠️Сметрей: {deaths:,} <b>чел.</b>\n{line}\nНаселение: {population:,} чел.\nБолеет: {boleet}% населения\nУмерло: {umerlo}% населения"


    await message.answer(final_message, parse_mode='HTML')

@dp.message_handler(text = 'Румыния🇷🇴')
async def ro_info(message:types.Message):
    ukraine_cases = covid.get_status_by_country_name('Romania')
    confirmed = ukraine_cases['confirmed']
    deaths = ukraine_cases['deaths']
    recovered = ukraine_cases['recovered']

    location = covid19.getLocationByCountryCode("RO")
    population = location[0]['country_population']
    boleet = round(confirmed*100/population,2)
    umerlo = round(deaths*100/population,3)

    
    line = '-' * 30

    final_message = f"<b>Данные в Румынии🇷🇴:</b>\n🦠Заболевших: {confirmed:,} <b>чел.</b>\n🧑‍⚕️Выздоровело: {recovered:,} <b>чел.</b>\n☠️Сметрей: {deaths:,} <b>чел.</b>\n{line}\nНаселение: {population:,} чел.\nБолеет: {boleet}% населения\nУмерло: {umerlo}% населения"


    await message.answer(final_message, parse_mode='HTML')

@dp.message_handler(text = 'Словакия🇸🇰')
async def sk_info(message:types.Message):
    ukraine_cases = covid.get_status_by_country_name('Slovakia')
    confirmed = ukraine_cases['confirmed']
    deaths = ukraine_cases['deaths']
    recovered = ukraine_cases['recovered']

    location = covid19.getLocationByCountryCode("SK")
    population = location[0]['country_population']
    boleet = round(confirmed*100/population,2)
    umerlo = round(deaths*100/population,3)

    
    line = '-' * 30

    final_message = f"<b>Данные в Словакии🇸🇰:</b>\n🦠Заболевших: {confirmed:,} <b>чел.</b>\n🧑‍⚕️Выздоровело: {recovered:,} <b>чел.</b>\n☠️Сметрей: {deaths:,} <b>чел.</b>\n{line}\nНаселение: {population:,} чел.\nБолеет: {boleet}% населения\nУмерло: {umerlo}% населения"


    await message.answer(final_message, parse_mode='HTML')
