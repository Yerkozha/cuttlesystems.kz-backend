from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from bots.models import Bot, Message, Variant, Command
from telegram_utils.get_telegram_bot_link import get_bot_link

User = get_user_model()


class BotSerializer(serializers.ModelSerializer):

    owner = serializers.PrimaryKeyRelatedField(
        read_only=True,
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Bot
        fields = (
            'id',
            'name',
            'token',
            'description',
            'owner',
            'start_message',
            'error_message'
        )

    validators = [
            UniqueTogetherValidator(
                queryset=Bot.objects.all(),
                fields=('name', 'owner'),
                message='Вы уже создавали бота с таким именем.',
            )
        ]


class OneBotSerializer(BotSerializer):
    bot_link = serializers.SerializerMethodField()

    def get_bot_link(self, obj):
        return get_bot_link(obj.token)

    class Meta:
        model = Bot
        fields = (
            'id',
            'name',
            'token',
            'description',
            'owner',
            'start_message',
            'error_message',
            'bot_link'
        )


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = (
            'id',
            'text',
            'keyboard_type',
            'photo',
            'video',
            'file',
            'bot',
            'coordinate_x',
            'coordinate_y',
            'message_type',
            'next_message',
            'variable'
        )
        read_only_fields = ('bot',)


class VariantSerializer(serializers.ModelSerializer):
    current_message = serializers.PrimaryKeyRelatedField(
        read_only=True,
        default=None
    )

    class Meta:
        model = Variant
        fields = (
            'id',
            'text',
            'current_message',
            'next_message'
        )

    def validate_text(self, value: str) -> str:
        assert isinstance(value, str)
        if len(value) > Variant.text.field.max_length:
            raise serializers.ValidationError(f'Text field more than {Variant.text.field.max_length} chars.')
        return value

    validators = [
            UniqueTogetherValidator(
                queryset=Variant.objects.all(),
                fields=('text', 'current_message'),
                message='This variant is alredy exists.',
            )
        ]


class MessageSerializerWithVariants(serializers.ModelSerializer):
    current_variants = VariantSerializer(
        many=True,
        read_only=True)

    next_variants = VariantSerializer(
        many=True,
        read_only=True)

    class Meta:
        model = Message
        fields = (
            'id',
            'text',
            'keyboard_type',
            'photo',
            'video',
            'file',
            'bot',
            'coordinate_x',
            'coordinate_y',
            'current_variants',
            'next_variants'
        )
        read_only_fields = ('bot', 'current_variants', 'next_variants')


class CommandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Command
        fields = (
            'id',
            'bot',
            'command',
            'description'
        )
        read_only_fields = ('bot',)
