from dataclasses import dataclass
from typing import Optional


@dataclass
class BotDescription:
    id: Optional[int] = None
    bot_name: Optional[str] = None
    bot_token: Optional[str] = None
    bot_description: Optional[str] = None
    start_message_id: Optional[int] = None


@dataclass
class BotMessage:
    id: Optional[int] = None
    text: Optional[str] = None
    photo: Optional[str] = None
    video: Optional[str] = None
    file: Optional[str] = None
    x: Optional[int] = None
    y: Optional[int] = None


@dataclass
class MessageVariant:
    id: Optional[int] = None
    text: Optional[str] = None
    next_message_id: Optional[int] = None