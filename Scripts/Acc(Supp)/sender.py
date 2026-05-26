from telethon import TelegramClient # type: ignore
from telethon.errors import FloodWaitError # type: ignore
import asyncio
import re
import random

api_id = 38937673
api_hash = "fc4dfb87993d25f6f7bca48f30bf91e5"

MESSAGES = [
    "приветствую, сейчас хорошо набирает обороты WhatsApp по токену. Можем поставлять объем номеров, показывает себя намного лучше обычного WhatsApp и max token, можно сказать как max token в самом начале 🙂",
    "приветствую 🙂 сейчас хорошо показывает себя WhatsApp по токену. Есть объемы номеров, работает лучше обычного WhatsApp и max token, ощущается как max token в начале",
    "приветствую. Сейчас тема WhatsApp по токену активно растет, можем давать объемы. По результатам намного лучше обычного WhatsApp и max token, как max token на старте",
    "приветствую! WhatsApp token сейчас хорошо набирает обороты. Есть объемы номеров, показывает себя очень достойно, как max token в самом начале",
    "приветствую, сейчас WhatsApp по токену показывает очень хорошие результаты. Намного лучше обычного WhatsApp и max token, можно сказать как max token на старте",
    "приветствую 🙂 есть объемы WhatsApp по токену. Сейчас тема активно развивается, по ощущениям как max token в начале, показывает себя очень хорошо",
    "приветствую! Сейчас WhatsApp token показывает себя лучше обычного WhatsApp и max token. Можно сказать тема как max token в самом начале",
    "приветствую, можем поставлять объемы WhatsApp по токену. Сейчас показывает себя очень сильно, примерно как max token на старте темы",
    "приветствую 🙂 WhatsApp по токену сейчас хорошо заходит. Есть объемы, работает лучше обычного WhatsApp и max token, ощущается как max token в начале",
    "приветствую! Сейчас WhatsApp token активно набирает обороты. По результатам очень похоже на max token в самом начале 🙂",
    "приветствую, тема WhatsApp по токену сейчас хорошо растет. Есть объемы номеров, показывает себя как max token в начале",
    "приветствую 🙂 можем давать объемы WhatsApp token. Сейчас тема очень живая, по ощущениям как max token на старте",
    "приветствую! WhatsApp token сейчас показывает себя намного лучше обычного WhatsApp. Можно сказать как max token в первые времена",
    "приветствую, сейчас хорошо работает WhatsApp по токену. Есть объемы, результаты очень хорошие, прям как max token в начале темы",
    "приветствую 🙂 WhatsApp token сейчас активно развивается. Можем поставлять объемы, ощущается как max token в самом начале",
    "приветствую! Сейчас WhatsApp по токену показывает хорошие результаты. Намного лучше обычного WhatsApp и max token, как max token на старте",
    "приветствую, есть объемы WhatsApp token. Сейчас тема очень хорошо показывает себя, примерно как max token в начале",
    "приветствую 🙂 WhatsApp token сейчас хорошо набирает обороты. Есть объемы номеров, работает как max token в первые времена",
    "приветствую! Можем поставлять WhatsApp по токену. Сейчас тема показывает себя очень достойно, прям как max token в начале",
    "приветствую, сейчас WhatsApp token активно растет. По результатам напоминает max token в самом начале 🙂",
    "приветствую 🙂 WhatsApp по токену сейчас показывает себя очень хорошо. Есть объемы, ощущается как max token на старте",
    "приветствую! Сейчас тема WhatsApp token набирает хорошие обороты. Показывает себя как max token в начале темы",
    "приветствую, можем поставлять объемы WhatsApp по токену. Сейчас работает очень сильно, как max token в начале",
    "приветствую 🙂 WhatsApp token сейчас очень хорошо заходит. Есть объемы, показывает себя лучше обычного WhatsApp и max token, как max token на старте",
    "приветствую! Сейчас WhatsApp по токену показывает отличные результаты. По ощущениям как max token в самом начале",
    "приветствую, WhatsApp token сейчас активно развивается. Есть объемы номеров, тема ощущается как max token в начале",
    "приветствую 🙂 можем поставлять WhatsApp token. Сейчас показывает себя очень достойно, примерно как max token на старте",
    "приветствую! WhatsApp по токену сейчас хорошо работает. Есть объемы, по результатам как max token в начале темы",
    "приветствую, тема WhatsApp token сейчас очень живая. Показывает себя как max token в первые времена 🙂",
    "приветствую 🙂 WhatsApp token сейчас активно набирает обороты. Есть объемы номеров, ощущается как max token в самом начале"
]

client = TelegramClient("session", api_id, api_hash)

async def main():
    await client.start()

    with open("users.txt", "r", encoding="utf-8") as f:
        content = f.read()

    usernames = re.findall(r'@([A-Za-z0-9_]+)', content)
    usernames = list(dict.fromkeys(usernames))

    sent_count = 0

    for username in usernames:

        try:
            text = random.choice(MESSAGES)

            await client.send_message(username, text)

            sent_count += 1

            print(f"✓ @{username}")

            await asyncio.sleep(random.randint(40, 80))

            if sent_count % 2 == 0:
                pause = random.randint(120, 240)
                print(f"Большая пауза {pause} сек")
                await asyncio.sleep(pause)

        except FloodWaitError as e:
            print(f"FloodWait: ждём {e.seconds} сек")
            await asyncio.sleep(e.seconds + 15)

        except Exception as e:
            print(f"✗ @{username}: {e}")

            # если пошёл rate limit — останавливаем всё
            if "Too many requests" in str(e):
                print("Telegram включил rate limit. Останавливаем рассылку.")
                break

            await asyncio.sleep(random.randint(30, 60))

with client:
    client.loop.run_until_complete(main())