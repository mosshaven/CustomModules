import asyncio
from pyrogram import Client, filters
from command import fox_command
import os

bot_tag = "shdjkwemnenennnbot"

@Client.on_message(fox_command("sher", "Sherlock", os.path.basename(__file__), "[поиск по личности/ID/номеру и т.п.]") & filters.me)
async def sherlock_search(client, message):
    if len(message.command) < 2:
        await message.edit(
            "❗ | Укажите запрос для поиска.\n\n"
            "**Примеры:**\n"
            "`Навальный Алексей Анатольевич 04.06.1976`\n"
            "`79637829051`\n"
            "`ceo@vkontakte.ru`\n"
            "`В395ОК199`\n"
            "`@sherlock`\n"
            "`/passport 1234567890`\n"
            "`sherlock.com`\n"
        )
        return

    query = " ".join(message.command[1:])
    await message.edit(f"🕵️ | Поиск по запросу: `{query}`. Пожалуйста, подождите...")

    try:
        await client.unblock_user(bot_tag)
        await client.send_message(bot_tag, query)
        await asyncio.sleep(20)  # Подождать, пока Sherlock обработает
    except Exception as e:
        await message.edit(f"⚠️ | Не удалось отправить запрос Sherlock-боту: `{e}`")
        return

    # Получаем последний ответ от бота
    async for reply in client.get_chat_history(bot_tag, limit=1):
        await message.edit("📄 | Вот что удалось найти:")
        await client.forward_messages(message.chat.id, bot_tag, reply.id)
        return

    await message.edit("❌ | Ничего не найдено или бот не ответил.")
