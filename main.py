from Parser import ParserFile
import ParserNews
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, BotCommand
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

HELLOW = """
<b>Привет, рад тебя видеть! Тебя втречает бот Dota2Hse! Я помогу тебе узнать много нового о персонажах игры Dota 2!\n
Ты можешь узнать, каким героем игры являешься, если пройдешь тест! А также можешь посмотреть, интересуюшую тебя информацию о том или ином
персонаже Dota 2!</b>
"""
main_questions = ''', психологический тест — очень интересная и ценная возможность лучше узнать себя. Вполне вероятно, что в одном из героев Dota 2 вы в итоге увидите нечто родное. Это позволит вам разобраться во внутренних переживаниях и... это полная чушь! Конечно, этому тесту, как и любому другому, начинающемуся со слов «Кто ты...», нельзя верить. Мы просто решили немного развлечь вас и поднять настроение во время сессионной недели. Попробуйте стать Pudge и избежать участи трансформации в Techies. Удачи вам, и да пребудут с вами Юпитер и Венера в десятом доме!'''
desc_pudge = '......ии тыыы......Бучка, бачер, рудге, пэйджер, джадж, hooker, пиджак, паджеро, Аль Паджино! \nТы добряк дуф, который знает толк во вкусной еде, не заморачивается насчет глобального потепления и всегда может вспомнить парочку сальных анекдотов. Душа компании, словом.'
desc_skymage = '......ии тыыы......Петууухх!!\nРомантик и творческая личность, которой важны чувства и эмоции. Ты хорошо понимаешь людей и всегда поступаешь посовести. На первом месте для тебя стоит счастье близких и любимого человека. Кто-то может пренебрежительно сказать: «Петух», но ты гордый Skywrath-mage'
desc_monkeyKing = '......ии тыыы......Макака!!\nТы очень известный своей скользкой натурой, а также своей способностью обманывать своих врагов, притворяясь зачастую деревом. Ты очень самовлюблен и любишь покрасоваться с тобой. Кидаешь палки'
desc_antimage ='......ии тыыы......Крип-крипочек!!\nЭгоцентричный, расчетливый и меркантильный, ты знаешь, что успеха в этом мире можно добиться, только если постоянно бить крипов, ой, то есть зарабатывать деньги. Многие недооценивают тебя, но ты знаешь себе цену и уверен, что в итоге всем все докажешь (если к тому времени трон не упадет).'
desc_Techies ='......ии тыыы...... Текис!!\nБезумец, который хочет видеть мир в огне. Знатный тролль и просто маргинал. В смекалке и коварстве тебе не откажешь, нозачастую ты пускаешь их не на какую-нибудь великую цель, а нато, чтобы просто повеселиться (хотя другим в такие моменты вовсе не до смеха).'
desc_Bristleback ='......ии тыыы......Ёжж!!\nВо вселенной существует бесчисленное множество всемогущих инстанций.. А ты.. А ты ёж с камнем на веревке. Противники боятся тебя, но у тебя есть и слабые места.'
desc_ShadowFiend ='......ии тыыы......\nГуль-гуленыш!!Ты дединсайд гульь 777. Ломаешь шмотки после первой смерти, твои тиммейты дети...'

dota_resurce = """
***Информация и соц. сети***

>1. [официальный сайт Dota 2](https://ru.dota2.com/ )
>2. [раздел по игре на популярном англоязычном сайте. Ведутся обсуждения на разные темы, а также там присутствуют разработчики](https://www.reddit.com/r/DotA2/ )
>3. [официальный Твиттер Dota 2](https://twitter.com/DOTA2 )
>4.  [инсайдер, зачастую информация об обновлениях появляется сначала там](https://twitter.com/wykrhm)
>5. [состояние серверов Стима, в том числе и Доты](https://steamstat.us/)

***Статистика***

>1. [матчи, анализы и многое-многое другое](https://ru.dotabuff.com/ )
>2. [статистика по турнирам и другие полезности](https://stats.spectral.gg/lrg2/ )

***База знаний***

>1. [Герои, Предметы, Гайды, Тактика. поддержка, Статьи, Стоимость инвентаря](https://dota2.ru)
>2. [англоязычная вики. Интерес представляют разделы механики и косметических предметов](https://dota2.gamepedia.com/Dota_2_Wiki)

***Киберспорт***

>1. [самая крупная англоязычная вики по киберспорту, плюс есть инфа по Доте](https://liquipedia.net/dota2/)
>2. [англоязычный сайт с рейтингом профессиональных команд, так же там есть новости, турниры, матчи, стримы, записи игр](https://www.gosugamers.net/dota2/rankings)
>3. [сайт, на котором можно смотреть игры любого киберспортсмена с основного и фейк аккаунта](http://www.dota2protracker.com/ )

***Обучение и тренировка***

>1. [платный помощник от Valve](https://www.dota2.com/plus)
>2. https://gosu.ai/ [персональный ассистент, который будет анализировать ваши игры и подсказывать, как играть лучше](https://gosu.ai/ )
>3. [интерактивная карта Доты, на которой можно ставить варды и многое другое](https://devilesk.com/dota2/apps/interactivemap/)
>4. [тренировка инвокера](http://www.invokergame.com/ )

***Другие полезные сайты***

>1. [сайт для просмотра косметических предметов на героях](https://dotaloadout.com/)
>2. [оценка стоимости инвентаря](https://steam.tools/itemvalue/)
"""

parser = ParserFile()
parser.parse()
heroes = parser.getHeroes
news = ParserNews.ParsingNews()

TOKEN_API = "6607152509:AAEthRQyAK0gHQg9rNbaqfV23z1FBvoqiQ0"
bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

question = 0
const = 0
er = 0
res = 0

main_kb = ReplyKeyboardMarkup(resize_keyboard=True)
main_b1 = KeyboardButton('Что такое дота?')
main_b2 = KeyboardButton('Персонажи игры')
main_b3 = KeyboardButton('Кто ты из Доты 2?')
main_b4 = KeyboardButton('Полезная информация')
main_kb.add(main_b1).insert(main_b2).add(main_b3).insert(main_b4)

class_hero_kb = ReplyKeyboardMarkup(resize_keyboard=True)
class_hero_b1 = KeyboardButton('Сила')
class_hero_b2 = KeyboardButton('Ловкость')
class_hero_b3 = KeyboardButton('Интеллект')
class_hero_b4 = KeyboardButton('Универсальный')
class_hero_b5 = KeyboardButton('Назад')
class_hero_kb.add(class_hero_b1).insert(class_hero_b2).add(class_hero_b3).insert(class_hero_b4).add(class_hero_b5)

hero_kb = ReplyKeyboardMarkup(resize_keyboard=True)
hero_b1 = KeyboardButton('Назад')
hero_kb.add(hero_b1)

quest_ent = ReplyKeyboardMarkup(resize_keyboard=True)
quest_ent1 = KeyboardButton('Поехали!')
quest_ent2 = KeyboardButton('Вернуться в меню')
quest_ent.add(quest_ent2).insert(quest_ent1)

quest_end = ReplyKeyboardMarkup(resize_keyboard=True)
quest_end1 = KeyboardButton('Вернуться в меню')
quest_end2 = KeyboardButton('Поехали!')
quest_end.add(quest_end1).insert(quest_end2)

quest_1 = ReplyKeyboardMarkup(resize_keyboard=True)
quest_a1 = KeyboardButton('A.')
quest_a2 = KeyboardButton('B.')
quest_a3 = KeyboardButton('C.')
quest_a4 = KeyboardButton('D.')
quest_a5 = KeyboardButton('E.')
quest_a6 = KeyboardButton('Вернуться в меню')
quest_1.add(quest_a1).insert(quest_a2).insert(quest_a3).insert(quest_a4).insert(quest_a5).add(quest_a6)

resurse_kb = ReplyKeyboardMarkup(resize_keyboard=True)
resurce_1 = KeyboardButton('Интересные ресурсы')
resurce_2 = KeyboardButton('Последние обновления')
resurce_3 = KeyboardButton('Вернуться в меню')
resurse_kb.add(resurce_1).insert(resurce_2).add(resurce_3)

keyboard = main_kb

def takeNeedHeroes(classHero):
    global heroes
    ikb = InlineKeyboardMarkup(row_width=2)
    for hero in heroes:
        if hero.getClassHero == classHero:
            ikb.insert(InlineKeyboardButton(text=hero.getNameHero, callback_data=hero.getNameHero))
    return ikb

async def on_startup(_):#лог запуска бота
    print('Бот запущен')

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await bot.send_sticker(message.from_user.id, sticker="CAACAgIAAxkBAAEKlXxlNpldxvHovuN7gnE-Fx-oF_gQSAACkxQAAuDDoUohbQFes9Y-tDAE")
    await bot.send_message(chat_id=message.from_user.id, text =HELLOW, parse_mode="HTML", reply_markup=main_kb)
    global keyboard
    keyboard = main_kb

@dp.message_handler(text='Персонажи игры')
async def class_heroes_command(message: types.Message):
    global er
    er = 1
    await bot.send_message(chat_id=message.from_user.id, text="Выберете класс персонажа:", reply_markup=class_hero_kb)
    global keyboard
    keyboard = class_hero_kb

@dp.message_handler(text='Сила')
async def power_inform_command(message: types.Message):

    ikb = takeNeedHeroes('Сила')
    await bot.send_message(chat_id=message.from_user.id, text= "Персонажи Силы: ", reply_markup=ikb)

@dp.message_handler(text='Ловкость')
async def power_inform_command(message: types.Message):

    ikb = takeNeedHeroes('Ловкость')
    await bot.send_message(chat_id=message.from_user.id, text= "Персонажи Ловкости: ", reply_markup=ikb)


@dp.message_handler(text='Универсальный')
async def power_inform_command(message: types.Message):

    ikb = takeNeedHeroes('Универсальный')
    await bot.send_message(chat_id=message.from_user.id, text= "Универсальные Персонажи: ", reply_markup=ikb)


@dp.message_handler(text='Интеллект')
async def power_inform_command(message: types.Message):

    ikb = takeNeedHeroes('Интеллект')
    await bot.send_message(chat_id=message.from_user.id, text= "Персонажи Интеллекта: ", reply_markup=ikb)

@dp.message_handler(text='Что такое дота?')
async def dota_inform_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text=parser.getDotaInformation)

@dp.message_handler(text='Полезная информация')
async def dota_informarion(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text= "Выберете категорию:", reply_markup=resurse_kb)
    global keyboard
    keyboard = resurse_kb

@dp.message_handler(text='Интересные ресурсы')
async def dota_intresting_resurce(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text=dota_resurce, parse_mode="Markdown", reply_markup=resurse_kb)
@dp.message_handler(text='Последние обновления')
async def dota_news(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text=news, parse_mode="Markdown", reply_markup=resurse_kb)

@dp.message_handler(text='Назад')
async def back_command(message: types.Message):
    global const, er
    if const == 0:
        er = 0
        await bot.send_message(chat_id=message.from_user.id, text="Доступные категории:", reply_markup=main_kb)
    else:
        er = 1
        const = 0
        await bot.send_message(chat_id=message.from_user.id, text="Доступные категории:", reply_markup=class_hero_kb)
    global keyboard
    keyboard = main_kb

@dp.callback_query_handler()
async def choice_callback(callback: types.CallbackQuery):
    global heroes, const, er
    const = 1
    er = 2
    for hero in heroes:
        if callback.data == hero.getNameHero:
            abilitiesList = hero.getAbilitiesHero.getAbilitiesList
            stata = ""
            for key in abilitiesList:
                stata += "<em>" + key + ": " +  "</em>" + abilitiesList[key] + "\n"
            await bot.send_message(callback.from_user.id, text = "<b>Персонаж: </b>" + hero.getNameHero  + "\n\n"
                                   + "<b>Класс: </b>" + hero.getClassHero + "\n\n" + hero.getInformation + "\n\n" +
                                   "<b>Характеристики:</b>\n\n" + stata, parse_mode="HTML")
            await bot.send_photo(callback.from_user.id, photo=hero.getPhoto, reply_markup=hero_kb)
            break


@dp.message_handler(text='Кто ты из Доты 2?')
async def dota_inform_command(message: types.Message):
    global er
    er = 3
    await bot.send_sticker(message.from_user.id, sticker="CAACAgIAAxkBAANgZTe_eteYqmgy2MrvdVss60gmdegAAhQTAAIQs4hK8C92yIiBkFMwBA")
    await bot.send_message(chat_id=message.from_user.id, text=message.from_user.first_name + main_questions, reply_markup=quest_ent)
    global keyboard
    keyboard = quest_ent

@dp.message_handler(text='Вернуться в меню')
async def back_to_menu(message: types.Message):
    global res, const, er
    const = 0
    er = 0
    res = 0
    await bot.send_message(chat_id=message.from_user.id, text ="Вы вернулись в главное меню", reply_markup=main_kb)
    global keyboard
    keyboard = main_kb

@dp.message_handler(text='Поехали!')
async def question1(message: types.Message):
    global question
    question = 1
    global res
    res = 0
    await bot.send_photo(chat_id=message.from_user.id, photo="https://sevkor.ru/wp-content/uploads/2019/04/tsel-zhizni.jpg",caption ="1. Что для тебя главное в жизни?")
    await bot.send_message(chat_id=message.from_user.id, text ="A. - сочный стейк\nB. - знания\nC. - любовь\nD. - веселье\nE. - деньги\n", reply_markup=quest_1)
    global keyboard
    keyboard = quest_1


@dp.message_handler(content_types=types.ContentType.ANIMATION)
async def echo_gif(message: types.Message):
    await message.reply_animation(message.animation.file_id)

@dp.message_handler(content_types=types.ContentType.STICKER)
async def echo_sticker(message: types.Message):
    await message.reply_sticker(message.sticker.file_id)


@dp.message_handler()
async def questions(message: types.Message):
    if ((message.text == "A.")|(message.text == "B.")|(message.text == "C.")|(message.text == "D.")|(message.text == "E.")):
        global question
        global res
        global keyboard
        global er
        er = 3
        keyboard = quest_1
        question += 1
        if(message.text == "A."):
            res+=1
        elif (message.text == "B."):
            res += 2
        elif (message.text == "C."):
            res += 3
        elif (message.text == "D."):
            res += 4
        elif (message.text == "E."):
            res += 5
        if (question == 2):
            await bot.send_photo(chat_id=message.from_user.id,
                                 photo="https://cs.pikabu.ru/post_img/2013/10/11/11/1381516673_1351812358.jpg",
                                 caption="2. Твоя любимая фраза?")
            await bot.send_message(chat_id=message.from_user.id,
                                   text="A. - всем удачи и хорошей игры!\nB. - хорошо сыграно!\nC. - отдай мид!\nD. - ПЕРВЫЙ СКИЛЛ И ТРЕТИЙ!\nE. - гг афк раки я ливаю\n",
                                   reply_markup=quest_1)
        elif (question == 3):
            await bot.send_photo(chat_id=message.from_user.id,
                                 photo="https://www.iphones.ru/wp-content/uploads/2009/08/boy-24.jpg",
                                 caption="3. Что купишь на первую зарплату?")
            await bot.send_message(chat_id=message.from_user.id,
                                   text="A. - фрукты\nB. - мантию\nC. - скипетр\nD. - дагон\nE. - дагон\n",
                                   reply_markup=quest_1)
        elif (question == 4):
            await bot.send_photo(chat_id=message.from_user.id,
                                 photo="https://i.scdn.co/image/ab67616d00001e029fb9c41d122cae503e6b9eda",
                                 caption="4. Кого ты больше всего ненавидишь?")
            await bot.send_message(chat_id=message.from_user.id,
                                   text="A. - всех люблю\nB. - магов\nC. - гномов\nD. - огров\nE. - всех ненавижу\n",
                                   reply_markup=quest_1)
        elif (question == 5):
            await bot.send_photo(chat_id=message.from_user.id,
                                 photo="https://www.pravmir.ru/wp-content/uploads/2020/07/chtenie-1024x504.jpg",
                                 caption="5. Какую книгу ты бы предпочел прочесть в свободное время?")
            await bot.send_message(chat_id=message.from_user.id,
                                   text="A. - учебник по орг\nB. - богатый папа бедный папа\nC. - хайп в инстаграм: разговор  по фактам\nD. - ни сы\nE. - я не умею читать\n",
                                   reply_markup=quest_1)
        elif (question == 6):
            await bot.send_photo(chat_id=message.from_user.id,
                                 photo="https://www.live-and-learn.ru/upload/iblock/3d7/net_zhelaniya_obschatsya.jpg",
                                 caption="6. Какой из тебя собеседник?")
            await bot.send_message(chat_id=message.from_user.id,
                                   text="A. - я умею слушать других\nB. - я больше люблю рассказывать о себе\nC. - мне скучно общаться с людьми\nD. - со мной не общаются\nE. - моя речь на 99% состоит из анекдотов\n",
                                   reply_markup=quest_1)
        elif (question == 7):
            await bot.send_photo(chat_id=message.from_user.id,
                                 photo="https://ic.pics.livejournal.com/sergey_stasenko/65151187/67618/67618_900.jpg",
                                 caption="7. Чего у тебя больше всего?")
            await bot.send_message(chat_id=message.from_user.id,
                                   text="A. - всего мало\nB. - интеллекта\nC. - ловкости\nD. - силы\nE. - всего много\n",
                                   reply_markup=quest_1)
        elif (question == 8):
            await bot.send_photo(chat_id=message.from_user.id,
                                 photo="https://assets.gq.ru/photos/5d9f5f3b2129f20008bdd2fa/master/w_1600%2Cc_limit/04.jpg",
                                 caption="8. А насколько культурно ты ведешь себя?")
            await bot.send_message(chat_id=message.from_user.id,
                                   text="A. - мьючу всех с нулевой\nB. - меня мьютят с нулевой\nC. - люблю пообщаться с тиммейтами за жизнь\nD. - типаю соперников и поучаю союзников\nE. - редко общаюсь, просто даю информацию, когда это надо\n",
                                   reply_markup=quest_1)
        elif (question == 9):
            await bot.send_photo(chat_id=message.from_user.id,
                                 photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTE0djcOI8qiyS35s-jptUDDGlXgf6mhAQMnA&usqp=CAU",
                                 caption="9. Как у тебя с противоположным полом?")
            await bot.send_message(chat_id=message.from_user.id,
                                   text="A. - все сложно, все еще не могу забыть прошлые отношения\nB. - у меня не очень получается, но я верю, что найду того самого человека\nC. - у меня есть любимый человек, с которым мы счастливы\nD. - все отлично, я пользуюсь популярностью, я ведь так хорош\nE. - у меня есть куда более любопытные увлечения, нежели эта ваша романтика\n",
                                   reply_markup=quest_1)
        elif (question == 10):
            await bot.send_photo(chat_id=message.from_user.id,
                                 photo="https://aif-s3.aif.ru/images/028/531/d6ad2180c3aaf157c9cc65121ec48327.jpg",
                                 caption="10. Когда вам доводится услышать лестные отзывы о себе, вы:")
            await bot.send_message(chat_id=message.from_user.id,
                                   text="A. - испытываете недовольство\nB. - вам приятно\nC. - радуетесь\nD. - смущаетесь\nE. - мрачнеете\n",
                                   reply_markup=quest_1)
        elif (question == 11):
            keyboard = quest_end
            if(res<20):
                await bot.send_photo(chat_id=message.from_user.id,
                                     photo="https://habrastorage.org/getpro/habr/post_images/6fc/750/e38/6fc750e38c21f9dc6a777c15cbf4be43.jpg",
                                     caption=desc_pudge)
                await bot.send_message(chat_id=message.from_user.id,
                                       text="Чтобы пройти тест снова, жми на 'Поехали!'\nНе забудь поделиться с друзьями!(p.s. и поставить свою невероятно крутую оценочку)",
                                       reply_markup=quest_end)
                await bot.send_sticker(chat_id=message.from_user.id, sticker='CAACAgQAAxkBAANjZTfb3pIjxAmZmFAMfjHpQORsVA4AApoOAAISxchTzNiSgGbrDQ0wBA')
            elif (res <= 25):
                await bot.send_photo(chat_id=message.from_user.id,
                                     photo="https://wc3.3dn.ru/_ph/24/375980943.jpg",
                                     caption=desc_skymage)
                await bot.send_message(chat_id=message.from_user.id,
                                       text="Чтобы пройти тест снова, жми на 'Поехали!'\nНе забудь поделиться с друзьями!(p.s. и поставить свою невероятно крутую оценочку)",
                                       reply_markup=quest_end)
                await bot.send_sticker(chat_id=message.from_user.id,
                                       sticker='CAACAgQAAxkBAANjZTfb3pIjxAmZmFAMfjHpQORsVA4AApoOAAISxchTzNiSgGbrDQ0wBA')
            elif (res <= 30):
                await bot.send_photo(chat_id=message.from_user.id,
                                     photo="https://dota2.ru/img/memes/2021/10/72116.jpg?0",
                                     caption=desc_monkeyKing)
                await bot.send_message(chat_id=message.from_user.id,
                                       text="Чтобы пройти тест снова, жми на 'Поехали!'\nНе забудь поделиться с друзьями!(p.s. и поставить свою невероятно крутую оценочку)",
                                       reply_markup=quest_end)
                await bot.send_sticker(chat_id=message.from_user.id,
                                       sticker='CAACAgQAAxkBAANjZTfb3pIjxAmZmFAMfjHpQORsVA4AApoOAAISxchTzNiSgGbrDQ0wBA')
            elif (res <= 35):
                await bot.send_photo(chat_id=message.from_user.id,
                                     photo="https://cs10.pikabu.ru/post_img/big/2019/04/16/6/1555406493122710194.jpg",
                                     caption=desc_antimage)
                await bot.send_message(chat_id=message.from_user.id,
                                       text="Чтобы пройти тест снова, жми на 'Поехали!'\nНе забудь поделиться с друзьями!(p.s. и поставить свою невероятно крутую оценочку)",
                                       reply_markup=quest_end)
                await bot.send_sticker(chat_id=message.from_user.id,
                                       sticker='CAACAgQAAxkBAANjZTfb3pIjxAmZmFAMfjHpQORsVA4AApoOAAISxchTzNiSgGbrDQ0wBA')
            elif (res <= 40):
                await bot.send_photo(chat_id=message.from_user.id,
                                     photo="https://kalix.club/uploads/posts/2022-12/1671463442_kalix-club-p-techis-oboi-pinterest-3.jpg",
                                     caption=desc_Techies)
                await bot.send_message(chat_id=message.from_user.id,
                                       text="Чтобы пройти тест снова, жми на 'Поехали!'\nНе забудь поделиться с друзьями!(p.s. и поставить свою невероятно крутую оценочку)",
                                       reply_markup=quest_end)
                await bot.send_sticker(chat_id=message.from_user.id,
                                       sticker='CAACAgQAAxkBAANjZTfb3pIjxAmZmFAMfjHpQORsVA4AApoOAAISxchTzNiSgGbrDQ0wBA')
            elif (res <= 45):
                await bot.send_photo(chat_id=message.from_user.id,
                                     photo="https://media.cyberscore.live/static/content/2023/3/4e15873d-a7ca-4862-b18d-f628fcd7fc36.png",
                                     caption=desc_Bristleback)
                await bot.send_message(chat_id=message.from_user.id,
                                       text="Чтобы пройти тест снова, жми на 'Поехали!'\nНе забудь поделиться с друзьями!(p.s. и поставить свою невероятно крутую оценочку)",
                                       reply_markup=quest_end)
                await bot.send_sticker(chat_id=message.from_user.id,
                                       sticker='CAACAgQAAxkBAANjZTfb3pIjxAmZmFAMfjHpQORsVA4AApoOAAISxchTzNiSgGbrDQ0wBA')
            elif (res <= 50):
                await bot.send_photo(chat_id=message.from_user.id,
                                     photo="https://virtus-img.cdnvideo.ru/images/og/plain/8e/8ec2e290-97ad-45fe-af27-8c78ad4ed65d.jpg",
                                     caption=desc_ShadowFiend)
                await bot.send_message(chat_id=message.from_user.id,
                                       text="Чтобы пройти тест снова, жми на 'Поехали!'\nНе забудь поделиться с друзьями!(p.s. и поставить свою невероятно крутую оценочку)",
                                       reply_markup=quest_end)
                await bot.send_sticker(chat_id=message.from_user.id,
                                       sticker='CAACAgQAAxkBAANjZTfb3pIjxAmZmFAMfjHpQORsVA4AApoOAAISxchTzNiSgGbrDQ0wBA')
    else:

        await bot.send_message(chat_id=message.from_user.id,
                                       text="Просим Вас воспользоваться панелью",
                                       reply_markup=keyboard)
        global const
        if er == 3:
            await bot.send_message(chat_id=message.from_user.id,
                                           text="Просим Вас воспользоваться панелью",
                                           reply_markup=keyboard)
        elif er == 2:
            await bot.send_message(chat_id=message.from_user.id,
                                   text="Просим Вас воспользоваться панелью",
                                   reply_markup=hero_kb)
        elif er == 1:
            await bot.send_message(chat_id=message.from_user.id,
                                   text="Просим Вас воспользоваться панелью",
                                   reply_markup=class_hero_kb)
        else:
            await bot.send_message(chat_id=message.from_user.id,
                                   text="Просим Вас воспользоваться панелью",
                                   reply_markup=main_kb)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)

