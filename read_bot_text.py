from b_logic.bot_api.bot_api_by_requests import BotApiByRequests
from app_tests.connection_settings import ConnectionSettings


if __name__ == '__main__':
    settings = ConnectionSettings()
    bot_api = BotApiByRequests(settings.site_addr)
    bot_api.authentication(settings.username, settings.password)
    bot = bot_api.get_bot_by_id(settings.bot_id)
    print(bot)
    messages = bot_api.get_messages(bot)
    for message in messages:
        print('    ', message)
        variants = bot_api.get_variants(message)
        for variant in variants:
            print('    ' * 2, variant)
