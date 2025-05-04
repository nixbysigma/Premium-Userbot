import random
import re
import os
import platform
import subprocess
import sys
import traceback
from datetime import datetime
from io import BytesIO, StringIO
from PyroUbot.config import OWNER_ID
import psutil
from PyroUbot import *
from datetime import datetime
from time import time

from pyrogram.raw.functions import Ping
from pyrogram.types import *

from PyroUbot import *


@PY.UBOT("alive")
@PY.TOP_CMD
async def _(client, message):
    try:
        x = await client.get_inline_bot_results(
            bot.me.username, f"alive {message.id} {client.me.id}"
        )
        await message.reply_inline_bot_result(x.query_id, x.results[0].id, quote=True)
    except Exception as error:
        await message.reply(error)
    



@PY.INLINE("^alive")
async def _(client, inline_query):
    get_id = inline_query.query.split()
    for my in ubot._ubot:
        if int(get_id[2]) == my.me.id:
            try:
                peer = my._get_my_peer[my.me.id]
                users = len(peer["pm"])
                group = len(peer["gc"])
            except Exception:
                users = random.randrange(await my.get_dialogs_count())
                group = random.randrange(await my.get_dialogs_count())
            get_exp = await get_expired_date(my.me.id)
            exp = get_exp.strftime("%d-%m-%Y") if get_exp else "None"
            if my.me.id == OWNER_ID:
                status = " <code>[ᴏᴡɴᴇʀ]</code>"
            elif my.me.id in await get_list_from_vars(client.me.id, "SELER_USERS"):
                status = "</b> <code>[ʀᴇsᴇʟʟᴇʀ]</code>"
            else:
                status = "</b> <code>[ᴘʀᴇᴍɪᴜᴍ]</code>"
            button = BTN.ALIVE(get_id)
            start = datetime.now()
            await my.invoke(Ping(ping_id=0))
            ping = (datetime.now() - start).microseconds / 1000
            uptime = await get_time((time() - start_time))
            msg = f"""
<blockquote>{bot.me.mention}
        `status: {status}`
        `expired_on: {exp}` 
        `dc_id: {my.me.dc_id}`
        `ping_dc: {ping} ms`
        `peer_users: {users} users`
        `peer_group: {group} group`
        `start_uptime: {uptime}`</blockquote>
"""
            await client.answer_inline_query(
                inline_query.id,
                cache_time=300,
                results=[
                    (
                        InlineQueryResultArticle(
                            title="💬",
                            reply_markup=InlineKeyboardMarkup(button),
                            input_message_content=InputTextMessageContent(msg),
                        )
                    )
                ],
            )


@PY.CALLBACK("alv_cls")
async def _(client, callback_query):
    user_id = callback_query.from_user.id
    if user_id in ubot._get_my_id:
        buttons = [
            [InlineKeyboardButton("⦪ ᴋᴇᴍʙᴀʟɪ ⦫", callback_data=f"help_back")],
        ]
        return await callback_query.edit_message_text(
            f"""
<emoji id='6300734675547593216'>😹</emoji> successfully closed
""",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(buttons),
        )
    elif len(ubot._ubot) + 1 > MAX_BOT:
        buttons = [
            [InlineKeyboardButton("ᴋᴇᴍʙᴀʟɪ", callback_data=f"help_back")],
        ]
        return await callback_query.edit_message_text(
            f"""
successfully closed 
""",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(buttons),
        )
    premium_users, ultra_premium_users = await get_list_from_vars(client.me.id, "PREM_USERS"), await get_list_from_vars(client.me.id, "ULTRA_PREM")
    if user_id not in premium_users and user_id not in ultra_premium_users:
        buttons = [
            [InlineKeyboardButton("⦪ ᴋᴇᴍʙᴀʟɪ ⦫", callback_data=f"help_back")],
        ]
        return await callback_query.edit_message_text(
            f"""
successfully closed 
""",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(buttons),
        )
    else:
        buttons = [[InlineKeyboardButton("⦪ ʟᴀɴᴊᴜᴛᴋᴀɴ ⦫", callback_data="add_ubot")]]
        return await callback_query.edit_message_text(
            """
<blockquote><b>⎆ ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴜᴀᴛ ᴜsᴇʀʙᴏᴛ sɪᴀᴘᴋᴀɴ ʙᴀʜᴀɴ ʙᴇʀɪᴋᴜᴛ

    ⎆ <code>ᴘʜᴏɴᴇ_ɴᴜᴍʙᴇʀ</code>: ɴᴏᴍᴇʀ ʜᴘ ᴀᴋᴜɴ ᴛᴇʟᴇɢʀᴀᴍ

⎆ ᴊɪᴋᴀ sᴜᴅᴀʜ ᴛᴇʀsᴇᴅɪᴀ sɪʟᴀʜᴋᴀɴ ᴋʟɪᴋ ᴛᴏᴍʙᴏɪ ᴅɪʙᴀᴡᴀʜ</b></blockquote>
""",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(buttons),
        )


@PY.BOT("anu")
@PY.ADMIN
async def _(client, message):
    buttons = BTN.BOT_HELP(message)
    sh = await message.reply("help menu information", reply_markup=InlineKeyboardMarkup(buttons))
    

@PY.CALLBACK("balik")
async def _(client, callback_query):
    buttons = BTN.BOT_HELP(callback_query)
    sh = await callback_query.message.edit("help menu information", reply_markup=InlineKeyboardMarkup(buttons))

@PY.CALLBACK("reboot")
async def _(client, callback_query):
    user_id = callback_query.from_user.id
    if user_id not in await get_list_from_vars(client.me.id, "ADMIN_USERS"):
        return await callback_query.answer("tombol ini bukan untuk lu", True)
    await callback_query.answer("system berhasil di restart", True)
    subprocess.call(["bash", "start.sh"])

@PY.CALLBACK("update")
async def _(client, callback_query):
    out = subprocess.check_output(["git", "pull"]).decode("UTF-8")
    user_id = callback_query.from_user.id
    if not user_id == OWNER_ID:
        return await callback_query.answer("tombol ini bukan untuk lu", True)
    if "Already up to date." in str(out):
        return await callback_query.answer("ꜱudah terupdate", True)
    else:
        await callback_query.answer("ꜱedang memproꜱeꜱ update.....", True)
    os.execl(sys.executable, sys.executable, "-m", "PyroUbot")


@PY.UBOT("help")
async def user_help(client, message):
    if not get_arg(message):
        try:
            x = await client.get_inline_bot_results(bot.me.username, "user_help")
            await message.reply_inline_bot_result(x.query_id, x.results[0].id)
        except Exception as error:
            await message.reply(error)
    else:
        module = (get_arg(message))
        if get_arg(message) in HELP_COMMANDS:
            prefix = await ubot.get_prefix(client.me.id)
            await message.reply(
                HELP_COMMANDS[get_arg(message)].__HELP__.format(
                    next((p) for p in prefix)
                ),
                quote=True,
            )
        else:
            await message.reply(
                f"<b>❌ No module found <code>{module}</code></b>"
            )

@PY.INLINE("^user_help")
async def user_help_inline(client, inline_query):
    SH = await ubot.get_prefix(inline_query.from_user.id)
    msg = f"<blockquote>🪙 ᴍᴇɴᴜ ɪɴʟɪɴᴇ <a href=tg://user?id={inline_query.from_user.id}>{inline_query.from_user.first_name} {inline_query.from_user.last_name or ''}</a>\n★ ᴛᴏᴛᴀʟ ᴍᴏᴅᴜʟᴇs: {len(HELP_COMMANDS)}\n  ᴘʀᴇꜰɪx: {' '.join(SH)}</b></blockquote>"
    results = [InlineQueryResultArticle(
        title="Help Menu!",
        reply_markup=InlineKeyboardMarkup(paginate_modules(0, HELP_COMMANDS, "help")),
        input_message_content=InputTextMessageContent(msg),
    )]
    await client.answer_inline_query(inline_query.id, cache_time=60, results=results)

@PY.CALLBACK("^close_user")
async def close_usernya(client, callback_query):
    unPacked = unpackInlineMessage(callback_query.inline_message_id)
    for x in ubot._ubot:
        if callback_query.from_user.id == int(x.me.id):
            await x.delete_messages(
                unPacked.chat_id, unPacked.message_id
            )

@PY.CALLBACK("help_(.*?)")
async def help_callback(client, callback_query):
    mod_match = re.match(r"help_module\((.+?)\)", callback_query.data)
    prev_match = re.match(r"help_prev\((.+?)\)", callback_query.data)
    next_match = re.match(r"help_next\((.+?)\)", callback_query.data)
    tutup_match = re.match(r"help_tutup\((.+?)\)", callback_query.data)
    back_match = re.match(r"help_back", callback_query.data)
    SH = await ubot.get_prefix(callback_query.from_user.id)
    top_text = f"<blockquote>🪙 ᴍᴇɴᴜ ɪɴʟɪɴᴇ <a href=tg://user?id={callback_query.from_user.id}>{callback_query.from_user.first_name} {callback_query.from_user.last_name or ''}</a>\n★ ᴛᴏᴛᴀʟ ᴍᴏᴅᴜʟᴇs: {len(HELP_COMMANDS)}\n  ᴘʀᴇꜰɪx: {' '.join(SH)}</b></blockquote>"

    if mod_match:
        module = (mod_match.group(1)).replace(" ", "_")
        text = HELP_COMMANDS[module].__HELP__.format(next((p) for p in SH))
        button = [[InlineKeyboardButton("⊲ ʙᴀᴄᴋ", callback_data="help_back")]]
        await callback_query.edit_message_text(
            text=text 
            + '\n<blockquote><b>@OwnTelegramX</b></blockquote>',
            reply_markup=InlineKeyboardMarkup(button),
            disable_web_page_preview=True,
        )
    elif prev_match:
        curr_page = int(prev_match.group(1))
        await callback_query.edit_message_text(
            top_text,
            reply_markup=InlineKeyboardMarkup(paginate_modules(curr_page - 1, HELP_COMMANDS, "help")),
            disable_web_page_preview=True,
        )
    elif next_match:
        next_page = int(next_match.group(1))
        await callback_query.edit_message_text(
            text=top_text,
            reply_markup=InlineKeyboardMarkup(paginate_modules(next_page + 1, HELP_COMMANDS, "help")),
            disable_web_page_preview=True,
        )
    elif back_match:
        await callback_query.edit_message_text(
            text=top_text,
            reply_markup=InlineKeyboardMarkup(paginate_modules(0, HELP_COMMANDS, "help")),
            disable_web_page_preview=True,
        )
@PY.CALLBACK("paginate")
async def _(client, callback_query):
    user_id = callback_query.from_user.id
    total_cmd = len(HELP_COMMANDS)  # Menghitung jumlah total plugin atau perintah
    SH = await ubot.get_prefix(callback_query.from_user.id)  # Mendapatkan prefix

    # Menampilkan alert dengan kedua informasi (Plugins dan Prefix) dalam satu alert
    await callback_query.answer(
        f"Plugins: {total_cmd}\nPrefix: {' '.join(SH)}",
        show_alert=True
    )


    # Menampilkan alert kedua dengan show_alert=False untuk prefix
    await callback_query.answer(
        f"USERBOT REDY",
        show_alert=False
        )
        
