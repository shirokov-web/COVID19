from misc import bot, dp
from aiogram import types
from handlers.user_handlers.helpers.generation_keyboard import UserGenerationKeyboard

import COVID19Py
from covid import Covid

covid = Covid()
covid19 = COVID19Py.COVID19()




@dp.message_handler(commands = ['start'])
async def start(message:types.Message):
    await message.answer(f"*Привет, {message.from_user.first_name}\!*\nВыберите страну:", parse_mode='MarkdownV2', reply_markup=UserGenerationKeyboard.country_buttons())



@dp.message_handler(text = 'Весь мир🌎')
async def world_info(message:types.Message):
    keyboard = UserGenerationKeyboard.country_buttons()
    confirmed = covid.get_total_confirmed_cases()
    deaths = covid.get_total_deaths()
    recovered = covid.get_total_recovered()
    final_message = final_message = f"<b>Данные по всему миру🌎:</b>\n🦠Заболевших: {confirmed:,} <b>чел.</b>\n🧑‍⚕️Выздоровело: {recovered:,} <b>чел.</b>\n☠️Сметрей: {deaths:,} <b>чел.</b>"
    await message.answer(final_message, reply_markup=keyboard, parse_mode='HTML')



@dp.message_handler(text = 'Украина🇺🇦')
async def ua_info(message:types.Message):
    keyboard = UserGenerationKeyboard.country_buttons()

    ukraine_cases = covid.get_status_by_country_name('ukraine')
    confirmed = ukraine_cases['confirmed']
    deaths = ukraine_cases['deaths']
    recovered = ukraine_cases['recovered']

    location = covid19.getLocationByCountryCode("UA")
    population = location[0]['country_population']
    boleet = round(confirmed*100/population,2)
    umerlo = round(deaths*100/population,3)

    
    line = '-' * 30

    final_message = f"<b>Данные в Украине🇺🇦:</b>\n🦠Заболевших: {confirmed:,} <b>чел.</b>\n🧑‍⚕️Выздоровело: {recovered:,} <b>чел.</b>\n☠️Сметрей: {deaths:,} <b>чел.</b>\n{line}\nНаселение: {population:,} чел.\nБолеет: {boleet}% населения\nУмерло: {umerlo}% населения"


    await message.answer(final_message, reply_markup=keyboard, parse_mode='HTML')



@dp.message_handler(text = 'Россия🇷🇺')
async def ru_info(message:types.Message):
    keyboard = UserGenerationKeyboard.country_buttons()
    ukraine_cases = covid.get_status_by_country_name('russia')
    confirmed = ukraine_cases['confirmed']
    deaths = ukraine_cases['deaths']
    recovered = ukraine_cases['recovered']

    location = covid19.getLocationByCountryCode("RU")
    population = location[0]['country_population']
    boleet = round(confirmed*100/population,2)
    umerlo = round(deaths*100/population,3)

    
    line = '-' * 30

    final_message = f"<b>Данные в России🇷🇺:</b>\n🦠Заболевших: {confirmed:,} <b>чел.</b>\n🧑‍⚕️Выздоровело: {recovered:,} <b>чел.</b>\n☠️Сметрей: {deaths:,} <b>чел.</b>\n{line}\nНаселение: {population:,} чел.\nБолеет: {boleet}% населения\nУмерло: {umerlo}% населения"


    await message.answer(final_message, reply_markup=keyboard, parse_mode='HTML')


@dp.message_handler(text = 'Беларусь⬜️🟥⬜️')
async def by_info(message:types.Message):
    keyboard = UserGenerationKeyboard.country_buttons()
    ukraine_cases = covid.get_status_by_country_name('belarus')
    confirmed = ukraine_cases['confirmed']
    deaths = ukraine_cases['deaths']
    recovered = ukraine_cases['recovered']

    location = covid19.getLocationByCountryCode("BY")
    population = location[0]['country_population']
    boleet = round(confirmed*100/population,2)
    umerlo = round(deaths*100/population,3)

    
    line = '-' * 30

    final_message = f"<b>Данные в Беларуси⬜️🟥⬜️:</b>\n🦠Заболевших: {confirmed:,} <b>чел.</b>\n🧑‍⚕️Выздоровело: {recovered:,} <b>чел.</b>\n☠️Сметрей: {deaths:,} <b>чел.</b>\n{line}\nНаселение: {population:,} чел.\nБолеет: {boleet}% населения\nУмерло: {umerlo}% населения"


    await message.answer(final_message, reply_markup=keyboard, parse_mode='HTML')


@dp.message_handler(text = 'Остальные страны')
async def other_countries(message:types.Message):
    keyboard = UserGenerationKeyboard.other_countries()

    final_message='Выберите <b>континент</b>:'
    await message.answer(final_message, reply_markup=keyboard, parse_mode='HTML')


@dp.message_handler(text = '🔙Назад')
async def back(message:types.Message):
    keyboard = UserGenerationKeyboard.country_buttons()
    final_message = 'Выберите <b>страну</b>!'
    await message.answer(final_message, reply_markup=keyboard, parse_mode='HTML')

@dp.message_handler(text = '🔙Остальные страны')
async def backk(message:types.Message):
    keyboard = UserGenerationKeyboard.other_countries()
    final_message = 'Выберите <b>континент</b>!'
    await message.answer(final_message, reply_markup=keyboard, parse_mode='HTML')


@dp.message_handler(text = '🔙Регионы Европы')
async def backkk(message:types.Message):
    keyboard = UserGenerationKeyboard.europe_countries()
    final_message = 'Выберите <b>регион</b>!'
    await message.answer(final_message, reply_markup=keyboard, parse_mode='HTML')

@dp.message_handler(text = '🔙Регионы Азии')
async def backkkk(message:types.Message):
    keyboard = UserGenerationKeyboard.asian_countries()
    final_message = 'Выберите <b>регион</b>!'
    await message.answer(final_message, reply_markup=keyboard, parse_mode='HTML')

@dp.message_handler(text = '🔙Регионы Африки')
async def backkkkk(message:types.Message):
    keyboard = UserGenerationKeyboard.african_countries()
    final_message = 'Выберите <b>регион</b>!'
    await message.answer(final_message, reply_markup=keyboard, parse_mode='HTML')


@dp.message_handler(text = '🔙Регионы Америки')
async def backkkkkk(message:types.Message):
    keyboard = UserGenerationKeyboard.american_countries()
    final_message = 'Выберите <b>регион</b>!'
    await message.answer(final_message, reply_markup=keyboard, parse_mode='HTML')







@dp.message_handler(text = 'Европа')
async def europe(message:types.Message):
    keyboard = UserGenerationKeyboard.europe_countries()

    final_message = 'Выберите <b>регион</b>:'
    await message.answer(final_message, reply_markup=keyboard, parse_mode='HTML')

@dp.message_handler(text = 'Азия')
async def asia(message:types.Message):
    keyboard = UserGenerationKeyboard.asian_countries()

    final_message = 'Выберите <b>регион</b>:'
    await message.answer(final_message, reply_markup=keyboard, parse_mode='HTML')

@dp.message_handler(text = 'Африка')
async def africa(message:types.Message):
    keyboard = UserGenerationKeyboard.african_countries()

    final_message = 'Выберите <b>регион</b>:'
    await message.answer(final_message, reply_markup=keyboard, parse_mode='HTML')

@dp.message_handler(text = 'Америка')
async def america(message:types.Message):
    keyboard = UserGenerationKeyboard.american_countries()

    final_message = 'Выберите <b>регион</b>:'
    await message.answer(final_message, reply_markup=keyboard, parse_mode='HTML')

