from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "8583859273:AAHjSmziuzQiwNVMtaNYBIo4O5rQxdwByN0"

# Fayl idlar
minecraft_files = {
    "🔥 ANIME QUROLLARI 🔥": "BQACAgIAAxkBAAIBa2mcTn7FPkqhw3uAjFKPx8J_gTmwAAI8kgACFjDhSKMSWL5iQfLPOgQ",
    "💣 EXTREME TNT MOD 💣": "BQACAgIAAxkBAAIBb2mcX_qjvI5tZJSBrv02DgLIKsjrAAKUkwACFjDhSK3GnWWU5WWuOgQ",
    "🧟 ZOMBIE APOCALYPSE 🧟": "BQACAgIAAxkBAAIBcWmcYO58FbihKNAh4-YtgAvIZBpjAAKnkwACFjDhSKgIjtSpG4tFOgQ",
    "🥚 SURVIVAL SPAWN MOD 🥚": "BQACAgIAAxkBAAIBdWmcYQpe8LCK2APOMdrqYaxHZTpaAAKokwACFjDhSEnFrVQugj-kOgQ",
    "⚔️ DWARF DUNGEON ⚔️": "BQACAgIAAxkBAAIBaWmcTa0pPshacbK7LQJfry5t250DAAIvkgACFjDhSDzawXYLIG_KOgQ",
    "👻 NIGHTMARE CRAFT 👻": "BQACAgIAAxkBAAIBbWmcWb79ahNqYDy_SOwgGwoXcr9sAAJKkwACFjDhSMnwO2tP7H7OOgQ",
    "⛏ MORE ORES + TOOLS ⛏": "BQACAgIAAxkBAAIBd2mcYRS6WQrVicgXkjqrSwrkEy34AAKpkwACFjDhSKKY1xGwX0OEOgQ",
    "🐉 MORPH MOD 🐉": "BQACAgIAAxkBAAIBeWmcYSsiVXzTYvTzwAABcJuqM03OSgACrZMAAhYw4UjltCSlsoQaUzoE",
    "📱 MODERN GADGETS 📱": "BQACAgIAAxkBAAIBe2mcYWSA0KQxXjdGufpuWQ7LRu_tAAKykwACFjDhSHu03ItjWYlzOgQ",
    "🌍 SURVIVAL ESSENTIALS 🌍": "BQACAgIAAxkBAAIBfWmcYXWxWXMphMQDgfCs7PIwDULOAAK1kwACFjDhSK4cXaZbDv88OgQ",
}

# DLS19 file
dls19_file = "BQACAgIAAxkBAAIBu2mcar0fzDBZuReZTwfpk36rQTpxAAJelAACFjDhSA2KsAf4-2qeOgQ"

# PUBG MOBILE file
pubg_mobile_file = "BQACAgIAAxkBAAICP2mdbcNEBy9IMhRK65vRh-YGQ8pYAAJkkgACFjDpSHa7RR_53OVGOgQ"

# GTA UZBEK filelar
gta_uzbek_file1 = "BQACAgIAAxkBAAICaWmdhAq-NOVlTwE0ClhBXv32PKPpAAL4kwACFjDpSPLrIkcmQykgOgQ"
gta_uzbek_file2 = "BQACAgIAAxkBAAICa2mdho_UjnMeQZ_HeKIy65-GVasGAAIZlAACFjDpSJfUukD1bWyCOgQ"
# To‘liq tavsiflar
mod_descriptions = {

"🔥 ANIME QUROLLARI 🔥": """🔥 ANIME QUROLLARI 🔥

ANIME uslubidagi aqldan ozgan va kuchli qurollarni jihozlang!
Maxsus boss janglari sizni kutmoqda!

+ Demon Oni bilan jang
+ Zaharli o'rgimchak boss
+ Anime qobiliyatlari
+ Maxsus effektlar
+ Kuchli zarbalar""",

"💣 EXTREME TNT MOD 💣": """💣 EXTREME TNT MOD 💣

Sizga eng ekstremal kerakmi? Bu TNTlar nafaqat bazalarni,
balki butun qishloqlar va yirik shaharlarni ham yo‘q qiladi!

+ 20+ gigant TNT
+ 5000x TNT
+ Meteor va Tornado
+ Maksimal portlash kuchi
+ Ko'p o'yinchi uchun mos""",

"🧟 ZOMBIE APOCALYPSE 🧟": """🧟 ZOMBIE APOCALYPSE 🧟

Butun shahar zombilar tomonidan bosib olingan!
Qurol to'plang va tirik qoling!

+ Epik boss janglari
+ Hikoya rejimi
+ Maxsus qurollar
+ Qiziqarli topshiriqlar
+ Do'stlar bilan o'ynash mumkin""",

"🥚 SURVIVAL SPAWN MOD 🥚": """🥚 SURVIVAL SPAWN MOD 🥚

Endi barcha tuxumlarni omon qolish rejimida yasash mumkin!

+ 70+ noyob retsept
+ Maxsus retsept kitobi
+ Nom teglari va egarlar
+ Omon qolish dunyosi
+ Rivojlangan qishloq""",

"⚔️ DWARF DUNGEON ⚔️": """⚔️ DWARF DUNGEON ⚔️

Dungeon chuqurligiga tushing va xazinani toping!

+ 5 epik boss
+ Moslashtirilgan qurollar
+ Mitti zirhlari
+ Yashirin xonalar
+ Katta zindonlar""",

"👻 NIGHTMARE CRAFT 👻": """👻 NIGHTMARE CRAFT 👻

Qo'rquvga to‘la sayohat!

+ 6 noyob mavjudot
+ Qo'rqinchli voqealar
+ Kuchli AI hujumlari
+ Qiyinchilik rejimi
+ Maxsus sozlamalar""",

"⛏ MORE ORES + TOOLS ⛏": """⛏ MORE ORES + TOOLS ⛏

Dunyongizni kengaytiring!

+ 16 ta yangi ruda
+ 350 ta asbob va qurol
+ 350 ta zirh
+ Boshqa modlar bilan mos""",

"🐉 MORPH MOD 🐉": """🐉 MORPH MOD 🐉

Yirtqich hayvonga aylanish imkoniyati!

+ 20 xil mavjudot
+ Ajdahoga aylanish
+ Sehrgar kuchlari
+ Maxsus qobiliyatlar
+ Golem va bo'rilar""",

"📱 MODERN GADGETS 📱": """📱 MODERN GADGETS 📱

50+ zamonaviy gadjetlar!

+ Cho'ntak o'lchami
+ 2x2 qayiqlar
+ Oson portallar
+ Avtomatik baliq ovlash
+ Multiplayer uchun mos""",

"🌍 SURVIVAL ESSENTIALS 🌍": """🌍 SURVIVAL ESSENTIALS 🌍

Yangi olamlarni kashf eting!

+ Yangi mobs
+ 200 maxsus blok
+ Boss fight
+ Dungeons
+ Quest tizimi
+ Yangi zirh va qurollar"""
}

# START
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
    ["Minecraft Modlar", "DLS19 MOD"],
    ["PUBG MABILE MOD"],
    ["GTA UZBEK"]
]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    await update.message.reply_text(
        "Salom botga hush kelibsiz 👋\nEng sara mod o‘yinlar bizda ⚡\nTugmani bosing 👇",
        reply_markup=reply_markup
    )

# Xabar
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "Minecraft Modlar":
        keyboard = [
            ["🔥 ANIME QUROLLARI 🔥", "💣 EXTREME TNT MOD 💣"],
            ["🧟 ZOMBIE APOCALYPSE 🧟", "🥚 SURVIVAL SPAWN MOD 🥚"],
            ["⚔️ DWARF DUNGEON ⚔️", "👻 NIGHTMARE CRAFT 👻"],
            ["⛏ MORE ORES + TOOLS ⛏", "🐉 MORPH MOD 🐉"],
            ["📱 MODERN GADGETS 📱", "🌍 SURVIVAL ESSENTIALS 🌍"]
        ]
        
        reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        await update.message.reply_text("Minecraft Modlar menyusi:", reply_markup=reply_markup)

    elif text in minecraft_files:
        await update.message.reply_text(mod_descriptions[text])
        await update.message.reply_document(
            document=minecraft_files[text],
            filename=f"{text}.zip"
        )

    elif text == "DLS19 MOD":
        await update.message.reply_text("Dls 19 mod bepul🔥👇🏻")
        await update.message.reply_document(
            document=dls19_file,
            filename="DLS19_MOD.zip"
        )

    elif text == "PUBG MABILE MOD":
        await update.message.reply_text("PUBG MABILE MOD BEPUL🔥")
        await update.message.reply_document(
            document=pubg_mobile_file,
            filename="PUBG_MABILE_MOD.zip"
        )
    
    elif text == "GTA UZBEK":
        await update.message.reply_text("GTA UZBEK MOD BEPUL🔥👇🏻")

        await update.message.reply_document(
            document=gta_uzbek_file1,
            filename="GTA_UZBEK_PART1.zip"
        )

        await update.message.reply_document(
            document=gta_uzbek_file2,
            filename="GTA_UZBEK_PART2.zip"
        )

    else:
        await update.message.reply_text("Noto‘g‘ri tugma bosildi.")
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

print("Bot ishga tushdi...")
app.run_polling()
