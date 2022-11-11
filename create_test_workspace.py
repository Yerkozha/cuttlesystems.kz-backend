import uuid
from b_logic.bot_api import BotApi
from app_tests.connection_settings import ConnectionSettings


def gen_unique_str() -> str:
    return str(uuid.uuid4()).replace('-', '')[:8]


if __name__ == '__main__':
    settings = ConnectionSettings()
    bot_api = BotApi(settings.site_addr)
    bot_api.authentication(settings.username, settings.password)

    bot = bot_api.create_bot(
        'Имя тестовое бота {0}'.format(gen_unique_str()),
        gen_unique_str(),
        'Описание созданного бота')

    main_message = bot_api.create_message(bot, 'Что вас интересует?', 10, 10)
    bot_api.set_bot_start_message(bot, main_message)
    mobile_variant = bot_api.create_variant(main_message, 'Телефоны')
    computer_variant = bot_api.create_variant(main_message, 'Компьютеры')
    appliances_variant = bot_api.create_variant(main_message, 'Бытовая техника')

    mobile_message = bot_api.create_message(bot, 'Какие телефоны предпочитаете?', 100, 130)
    bot_api.connect_variant(mobile_variant, mobile_message)

    computer_message = bot_api.create_message(bot, 'Какие компьютеры предпочитаете?', 200, 150)
    bot_api.connect_variant(computer_variant, computer_message)

    android_variant = bot_api.create_variant(mobile_message, 'Android')
    iphone_variant = bot_api.create_variant(mobile_message, 'IPhone')
    mobile_cancel_variant = bot_api.create_variant(mobile_message, 'Вернуться в начало')

    android_select_message = bot_api.create_message(
        bot, 'Выберите телефон который хотите приобрести', 200, 250)
    bot_api.connect_variant(android_variant, android_select_message)
    samsung_galaxy_s22 = bot_api.create_variant(android_select_message, 'Samsung Galaxy S22')
    samsung_galaxy_a53 = bot_api.create_variant(android_select_message, 'Samsung Galaxy A53')

    buy_samsung_galaxy_s22_message = bot_api.create_message(
        bot, 'Вы оформляете заказ Samsung Galaxy S22', 300, 150)
    bot_api.connect_variant(samsung_galaxy_s22, buy_samsung_galaxy_s22_message)

    buy_samsung_galaxy_a53_message = bot_api.create_message(
        bot, 'Вы оформляете заказ Samsung Galaxy A53', 300, 200)
    bot_api.connect_variant(samsung_galaxy_a53, buy_samsung_galaxy_a53_message)

    iphone_select_message = bot_api.create_message(
        bot, 'Выберите модель IPhone, которую хотите приобрести', 200, 300)
    bot_api.connect_variant(iphone_variant, iphone_select_message)

    iphone_13_variant = bot_api.create_variant(iphone_select_message, 'IPhone 13')
    iphone_14_variant = bot_api.create_variant(iphone_select_message, 'IPhone 14')

    buy_iphone_13_message = bot_api.create_message(bot, 'Вы оформляете заказ IPhone 13', 300, 300)
    bot_api.connect_variant(iphone_13_variant, buy_iphone_13_message)

    buy_iphone_14_message = bot_api.create_message(bot, 'Вы оформляете заказ IPhone 14', 300, 350)
    bot_api.connect_variant(iphone_14_variant, buy_iphone_14_message)

    bot_api.connect_variant(mobile_cancel_variant, main_message)

    print(f'Идентификатор созданного бота: {bot.id}')