import nekos
import random
from userge import Message, userge
 
NSFW = [
    "feet",
    "yuri",
    "trap",
    "futanari",
    "hololewd",
    "lewdkemo",
    "holoero",
    "solog",
    "feetg",
    "cum",
    "erokemo",
    "les",
    "lewdk",
    "lewd",
    "eroyuri",
    "eron",
    "cum_jpg",
    "bj",
    "nsfw_neko_gif",
    "solo",
    "kemonomimi",
    "nsfw_avatar",
    "gasm",
    "anal",
    "hentai",
    "erofeet",
    "keta",
    "blowjob",
    "pussy",
    "tits",
    "pussy_jpg",
    "pwankg",
    "classic",
    "kuni",
    "femdom",
    "spank",
    "erok",
    "boobs",
    "random_hentai_gif",
    "smallboobs",
    "ero",
    "smug",
]
 
NON_NSFW = [
    "baka",
    "smug",
    "hug",
    "fox_girl",
    "cuddle",
    "neko",
    "pat",
    "waifu",
    "kiss",
    "holo",
    "avatar",
    "slap",
    "gecg",
    "feed",
    "tickle",
    "ngif",
    "wallpaper",
    "poke",
]
 
 
neko_help = "<b>NSFW</b> :  "
for i in NSFW:
    neko_help += f"<code>{i}</code>   "
neko_help += "\n\n<b>SFW</b> :  "
for m in NON_NSFW:
    neko_help += f"<code>{m}</code>   "
 
 
@userge.on_cmd(
    "n",
    about={
        "header": "Get NSFW / SFW stuff from nekos.life",
        "flags": {"n": "For random NSFW"},
        "usage": "{tr}n\n{tr}n -nsfw\n{tr}n [Choice]",
        "Choice": neko_help,
    },
)
async def neko_life(message: Message):
    choice = message.input_str
    if "-nsfw" in message.flags:
        choosen_ = rand_array(NSFW)
    elif choice:
        neko_all = NON_NSFW + NSFW
        choosen_ = (choice.split())[0]
        if choosen_ not in neko_all:
            await message.err(
                "Choose a valid Input !, See Help for more info.", del_in=5
            )
            return
    else:
        choosen_ = rand_array(NON_NSFW)
    link = nekos.img(choosen_)
    reply = message.reply_to_message
    reply_id = reply.message_id if reply else None
    await message.delete()
    if link.endswith(".gif"):
        if message.client.is_bot:  #  Bots can't use "unsave=True"
            await userge.bot.send_animation(
                chat_id=message.chat.id, animation=link, reply_to_message_id=reply_id
            )
        else:
            await userge.send_animation(
                chat_id=message.chat.id,
                animation=link,
                unsave=True,
                reply_to_message_id=reply_id,
            )
    else:
        await message.client.send_photo(
            chat_id=message.chat.id, photo=link, reply_to_message_id=reply_id
        )
 
 
def rand_array(array):
    random_num = random.choice(array) 
    return (str(random_num))
  