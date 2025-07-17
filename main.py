from telethon import TelegramClient, events
import asyncio

# إعدادات API من my.telegram.org
api_id = 'YOUR_API_ID'          # استبدل بهذا الرقم
api_hash = 'YOUR_API_HASH'      # استبدل بهذا الكود
bot_token = 'YOUR_BOT_TOKEN'    # استبدل بتوكن البوت

# معرفات القنوات (استبدلها بأرقام قناتك)
source_channel_id = -10012345678    # القناة المصدر (يبدأ بـ -100)
destination_channel_id = -10087654321  # القناة الهدف

# عداد للاستراحة كل 100 منشور
message_count = 0

client = TelegramClient('bot_session', api_id, api_hash).start(bot_token=bot_token)

@client.on(events.NewMessage(chats=source_channel_id))
async def handle_new_message(event):
    global message_count
    
    if message_count >= 100:
        print("⏸ استراحة 15 ثانية...")
        await asyncio.sleep(15)
        message_count = 0
    
    try:
        await event.forward_to(destination_channel_id)
        message_count += 1
        print(f"✅ تم نقل المنشور #{message_count}")
    except Exception as e:
        print(f"❌ خطأ: {e}")

async def main():
    await client.start()
    print("⚡ البوت يعمل بنجاح!")
    await client.run_until_disconnected()

if __name__ == '__main__':
    asyncio.run(main())