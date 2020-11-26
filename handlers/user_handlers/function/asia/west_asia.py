from misc import bot, dp
from aiogram import types
from handlers.user_handlers.helpers.generation_keyboard import UserGenerationKeyboard

import COVID19Py
from covid import Covid

covid = Covid()
covid19 = COVID19Py.COVID19()

@dp.message_handler(text = 'Западная Азия')
async def east_europe(message:types.Message):
    keyboard = UserGenerationKeyboard.west_asia()

    final_message = 'Выберите <b>страну</b>:'
    await message.answer(final_message, reply_markup=keyboard, parse_mode='HTML')


@dp.message_handler(text = 'Армения🇦🇲')
async def am_info(message:types.Message):
    ukraine_cases = covid.get_status_by_country_name('Armenia')
    confirmed = ukraine_cases['confirmed']
    deaths = ukraine_cases['deaths']
    recovered = ukraine_cases['recovered']

    location = covid19.getLocationByCountryCode("AM")
    population = location[0]['country_population']
    boleet = round(confirmed*100/population,2)
    umerlo = round(deaths*100/population,3)

    
    line = '-' * 30

    final_message = f"<b>Данные в Армении🇦🇲:</b>\n🦠Заболевших: {confirmed:,} <b>чел.</b>\n🧑‍⚕️Выздоровело: {recovered:,} <b>чел.</b>\n☠️Сметрей: {deaths:,} <b>чел.</b>\n{line}\nНаселение: {population:,} чел.\nБолеет: {boleet}% населения\nУмерло: {umerlo}% населения"


    await message.answer(final_message, parse_mode='HTML')

@dp.message_handler(text = 'Ливан🇱🇧')
async def lb_info(message:types.Message):
    ukraine_cases = covid.get_status_by_country_name('Lebanon')
    confirmed = ukraine_cases['confirmed']
    deaths = ukraine_cases['deaths']
    recovered = ukraine_cases['recovered']

    location = covid19.getLocationByCountryCode("LB")
    population = location[0]['country_population']
    boleet = round(confirmed*100/population,2)
    umerlo = round(deaths*100/population,3)

    
    line = '-' * 30

    final_message = f"<b>Данные в Ливане🇱🇧:</b>\n🦠Заболевших: {confirmed:,} <b>чел.</b>\n🧑‍⚕️Выздоровело: {recovered:,} <b>чел.</b>\n☠️Сметрей: {deaths:,} <b>чел.</b>\n{line}\nНаселение: {population:,} чел.\nБолеет: {boleet}% населения\nУмерло: {umerlo}% населения"


    await message.answer(final_message, parse_mode='HTML')

@dp.message_handler(text = 'Сирия🇸🇾')
async def sy_info(message:types.Message):
    ukraine_cases = covid.get_status_by_country_name('Syria')
    confirmed = ukraine_cases['confirmed']
    deaths = ukraine_cases['deaths']
    recovered = ukraine_cases['recovered']

    location = covid19.getLocationByCountryCode("SY")
    population = location[0]['country_population']
    boleet = round(confirmed*100/population,2)
    umerlo = round(deaths*100/population,3)

    
    line = '-' * 30

    final_message = f"<b>Данные в Сирии🇸🇾:</b>\n🦠Заболевших: {confirmed:,} <b>чел.</b>\n🧑‍⚕️Выздоровело: {recovered:,} <b>чел.</b>\n☠️Сметрей: {deaths:,} <b>чел.</b>\n{line}\nНаселение: {population:,} чел.\nБолеет: {boleet}% населения\nУмерло: {umerlo}% населения"


    await message.answer(final_message, parse_mode='HTML')

@dp.message_handler(text = 'Бахрейн🇧🇭')
async def bh_info(message:types.Message):
    ukraine_cases = covid.get_status_by_country_name('Bahrain')
    confirmed = ukraine_cases['confirmed']
    deaths = ukraine_cases['deaths']
    recovered = ukraine_cases['recovered']

    location = covid19.getLocationByCountryCode("BH")
    population = location[0]['country_population']
    boleet = round(confirmed*100/population,2)
    umerlo = round(deaths*100/population,3)

    
    line = '-' * 30

    final_message = f"<b>Данные в Бахрейне🇧🇭:</b>\n🦠Заболевших: {confirmed:,} <b>чел.</b>\n🧑‍⚕️Выздоровело: {recovered:,} <b>чел.</b>\n☠️Сметрей: {deaths:,} <b>чел.</b>\n{line}\nНаселение: {population:,} чел.\nБолеет: {boleet}% населения\nУмерло: {umerlo}% населения"


    await message.answer(final_message, parse_mode='HTML')

@dp.message_handler(text = 'Азербайджан🇦🇿')
async def az_info(message:types.Message):
    ukraine_cases = covid.get_status_by_country_name('Azerbaijan')
    confirmed = ukraine_cases['confirmed']
    deaths = ukraine_cases['deaths']
    recovered = ukraine_cases['recovered']

    location = covid19.getLocationByCountryCode("AZ")
    population = location[0]['country_population']
    boleet = round(confirmed*100/population,2)
    umerlo = round(deaths*100/population,3)

    
    line = '-' * 30

    final_message = f"<b>Данные в Азербайджане🇦🇿:</b>\n🦠Заболевших: {confirmed:,} <b>чел.</b>\n🧑‍⚕️Выздоровело: {recovered:,} <b>чел.</b>\n☠️Сметрей: {deaths:,} <b>чел.</b>\n{line}\nНаселение: {population:,} чел.\nБолеет: {boleet}% населения\nУмерло: {umerlo}% населения"


    await message.answer(final_message, parse_mode='HTML')

@dp.message_handler(text = 'Иордания🇯🇴')
async def jo_info(message:types.Message):
    ukraine_cases = covid.get_status_by_country_name('Jordan')
    confirmed = ukraine_cases['confirmed']
    deaths = ukraine_cases['deaths']
    recovered = ukraine_cases['recovered']

    location = covid19.getLocationByCountryCode("JO")
    population = location[0]['country_population']
    boleet = round(confirmed*100/population,2)
    umerlo = round(deaths*100/population,3)

    
    line = '-' * 30

    final_message = f"<b>Данные в Иордании🇯🇴:</b>\n🦠Заболевших: {confirmed:,} <b>чел.</b>\n🧑‍⚕️Выздоровело: {recovered:,} <b>чел.</b>\n☠️Сметрей: {deaths:,} <b>чел.</b>\n{line}\nНаселение: {population:,} чел.\nБолеет: {boleet}% населения\nУмерло: {umerlo}% населения"


    await message.answer(final_message, parse_mode='HTML')

@dp.message_handler(text = 'Йемен🇾🇪')
async def ye_info(message:types.Message):
    ukraine_cases = covid.get_status_by_country_name('Yemen')
    confirmed = ukraine_cases['confirmed']
    deaths = ukraine_cases['deaths']
    recovered = ukraine_cases['recovered']

    location = covid19.getLocationByCountryCode("YE")
    population = location[0]['country_population']
    boleet = round(confirmed*100/population,2)
    umerlo = round(deaths*100/population,3)

    
    line = '-' * 30

    final_message = f"<b>Данные в Йемене🇾🇪:</b>\n🦠Заболевших: {confirmed:,} <b>чел.</b>\n🧑‍⚕️Выздоровело: {recovered:,} <b>чел.</b>\n☠️Сметрей: {deaths:,} <b>чел.</b>\n{line}\nНаселение: {population:,} чел.\nБолеет: {boleet}% населения\nУмерло: {umerlo}% населения"


    await message.answer(final_message, parse_mode='HTML')

@dp.message_handler(text = 'Катар🇶🇦')
async def qa_info(message:types.Message):
    ukraine_cases = covid.get_status_by_country_name('Qatar')
    confirmed = ukraine_cases['confirmed']
    deaths = ukraine_cases['deaths']
    recovered = ukraine_cases['recovered']

    location = covid19.getLocationByCountryCode("QA")
    population = location[0]['country_population']
    boleet = round(confirmed*100/population,2)
    umerlo = round(deaths*100/population,3)

    
    line = '-' * 30

    final_message = f"<b>Данные в Катаре🇶🇦:</b>\n🦠Заболевших: {confirmed:,} <b>чел.</b>\n🧑‍⚕️Выздоровело: {recovered:,} <b>чел.</b>\n☠️Сметрей: {deaths:,} <b>чел.</b>\n{line}\nНаселение: {population:,} чел.\nБолеет: {boleet}% населения\nУмерло: {umerlo}% населения"


    await message.answer(final_message, parse_mode='HTML')

@dp.message_handler(text = 'Ирак🇮🇶')
async def iq_info(message:types.Message):
    ukraine_cases = covid.get_status_by_country_name('Iraq')
    confirmed = ukraine_cases['confirmed']
    deaths = ukraine_cases['deaths']
    recovered = ukraine_cases['recovered']

    location = covid19.getLocationByCountryCode("IQ")
    population = location[0]['country_population']
    boleet = round(confirmed*100/population,2)
    umerlo = round(deaths*100/population,3)

    
    line = '-' * 30

    final_message = f"<b>Данные в Ираке🇮🇶:</b>\n🦠Заболевших: {confirmed:,} <b>чел.</b>\n🧑‍⚕️Выздоровело: {recovered:,} <b>чел.</b>\n☠️Сметрей: {deaths:,} <b>чел.</b>\n{line}\nНаселение: {population:,} чел.\nБолеет: {boleet}% населения\nУмерло: {umerlo}% населения"


    await message.answer(final_message, parse_mode='HTML')

@dp.message_handler(text = 'Кувейт🇰🇼')
async def kw_info(message:types.Message):
    ukraine_cases = covid.get_status_by_country_name('Kuwait')
    confirmed = ukraine_cases['confirmed']
    deaths = ukraine_cases['deaths']
    recovered = ukraine_cases['recovered']

    location = covid19.getLocationByCountryCode("KW")
    population = location[0]['country_population']
    boleet = round(confirmed*100/population,2)
    umerlo = round(deaths*100/population,3)

    
    line = '-' * 30

    final_message = f"<b>Данные в Кувейте🇰🇼:</b>\n🦠Заболевших: {confirmed:,} <b>чел.</b>\n🧑‍⚕️Выздоровело: {recovered:,} <b>чел.</b>\n☠️Сметрей: {deaths:,} <b>чел.</b>\n{line}\nНаселение: {population:,} чел.\nБолеет: {boleet}% населения\nУмерло: {umerlo}% населения"


    await message.answer(final_message, parse_mode='HTML')

@dp.message_handler(text = 'Арабские Эмираты🇦🇪')
async def ae_info(message:types.Message):
    ukraine_cases = covid.get_status_by_country_name('United Arab Emirates')
    confirmed = ukraine_cases['confirmed']
    deaths = ukraine_cases['deaths']
    recovered = ukraine_cases['recovered']

    location = covid19.getLocationByCountryCode("AE")
    population = location[0]['country_population']
    boleet = round(confirmed*100/population,2)
    umerlo = round(deaths*100/population,3)

    
    line = '-' * 30

    final_message = f"<b>Данные в Арабских Эмиратах🇦🇪:</b>\n🦠Заболевших: {confirmed:,} <b>чел.</b>\n🧑‍⚕️Выздоровело: {recovered:,} <b>чел.</b>\n☠️Сметрей: {deaths:,} <b>чел.</b>\n{line}\nНаселение: {population:,} чел.\nБолеет: {boleet}% населения\nУмерло: {umerlo}% населения"


    await message.answer(final_message, parse_mode='HTML')

@dp.message_handler(text = 'Оман🇴🇲')
async def om_info(message:types.Message):
    ukraine_cases = covid.get_status_by_country_name('Oman')
    confirmed = ukraine_cases['confirmed']
    deaths = ukraine_cases['deaths']
    recovered = ukraine_cases['recovered']

    location = covid19.getLocationByCountryCode("OM")
    population = location[0]['country_population']
    boleet = round(confirmed*100/population,2)
    umerlo = round(deaths*100/population,3)

    
    line = '-' * 30

    final_message = f"<b>Данные в Омане🇴🇲:</b>\n🦠Заболевших: {confirmed:,} <b>чел.</b>\n🧑‍⚕️Выздоровело: {recovered:,} <b>чел.</b>\n☠️Сметрей: {deaths:,} <b>чел.</b>\n{line}\nНаселение: {population:,} чел.\nБолеет: {boleet}% населения\nУмерло: {umerlo}% населения"


    await message.answer(final_message, parse_mode='HTML')

@dp.message_handler(text = 'Саудовская Аравия🇸🇦')
async def sa_info(message:types.Message):
    ukraine_cases = covid.get_status_by_country_name('Saudi Arabia')
    confirmed = ukraine_cases['confirmed']
    deaths = ukraine_cases['deaths']
    recovered = ukraine_cases['recovered']

    location = covid19.getLocationByCountryCode("OM")
    population = location[0]['country_population']
    boleet = round(confirmed*100/population,2)
    umerlo = round(deaths*100/population,3)

    
    line = '-' * 30

    final_message = f"<b>Данные в Саудовской Аравии🇸🇦:</b>\n🦠Заболевших: {confirmed:,} <b>чел.</b>\n🧑‍⚕️Выздоровело: {recovered:,} <b>чел.</b>\n☠️Сметрей: {deaths:,} <b>чел.</b>\n{line}\nНаселение: {population:,} чел.\nБолеет: {boleet}% населения\nУмерло: {umerlo}% населения"


    await message.answer(final_message, parse_mode='HTML')

@dp.message_handler(text = 'Турция🇹🇷')
async def tr_info(message:types.Message):
    ukraine_cases = covid.get_status_by_country_name('Turkey')
    confirmed = ukraine_cases['confirmed']
    deaths = ukraine_cases['deaths']
    recovered = ukraine_cases['recovered']

    location = covid19.getLocationByCountryCode("TR")
    population = location[0]['country_population']
    boleet = round(confirmed*100/population,2)
    umerlo = round(deaths*100/population,3)

    
    line = '-' * 30

    final_message = f"<b>Данные в Турции🇹🇷:</b>\n🦠Заболевших: {confirmed:,} <b>чел.</b>\n🧑‍⚕️Выздоровело: {recovered:,} <b>чел.</b>\n☠️Сметрей: {deaths:,} <b>чел.</b>\n{line}\nНаселение: {population:,} чел.\nБолеет: {boleet}% населения\nУмерло: {umerlo}% населения"


    await message.answer(final_message, parse_mode='HTML')