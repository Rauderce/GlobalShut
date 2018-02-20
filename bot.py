# -*- coding: utf-8 -*-
import telegrand, Settings

bot = telegrand.Bot(Settings.BOT_TOKEN)

@bot.handle("chat.type", ['group', 'supergroup'])
def do(message):
	admins = bot.req(
		"getChatAdministrators",
		data={
			"chat_id": message.chat.id
		}
	)
	isAdmin = False
	for admin in admins:
		if message.from_user.id == admin.user.id:
			isAdmin = True
	if not isAdmin:
		bot.req(
			"deleteMessage",
			data={
				"chat_id": message.chat.id,
				"message_id": message.message_id
			}
		)

bot.polling()