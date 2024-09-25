from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ Creator : <a href='tg://user?id={OWNER_ID}'>𝐑𝐀𝐕𝐀𝐀𝐍𝐀</a>\n○ Language : <code>Python3</code>\n○ Library : <a href='https://t.me/+nDTaoJGRKJcxYmZl'>Library</a>\n○ Request Group : <a href='https://t.me/Kr_Movie2'>Click here</a>\n○ Channel : @Kr_Movie2</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("❗❗𝐂𝐋𝐎𝐒𝐄❗❗", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
