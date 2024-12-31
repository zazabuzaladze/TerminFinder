import asyncio
import subprocess
from telegram import Bot

BOT_TOKEN = [SECRETT!!]
CHAT_ID = [SECRETT!!]

async def send_message(text):
    bot = Bot(token=BOT_TOKEN)
    await bot.send_message(chat_id=CHAT_ID, text=text)

async def main():
    try:
        result = subprocess.run(
            ['python3', '/home/serverusername/scrapper/scrapperboy.py'],
            capture_output=True,
            text=True
        )
        if result.returncode == 0:
            output = result.stdout.strip()
        else:
            output = f"Error: {result.stderr.strip()}"
    except Exception as e:
        output = f"An error occurred: {str(e)}"

    # await send_message(output)
    if output != "Kein freier Termin verfügbar":
        await send_message("TERMIN VERFÜGBAR!!: https://termine.staedteregion-aachen.de/auslaenderamt/")


if __name__ == "__main__":
    asyncio.run(main())
