from .. import db
from . import moderators
import os

OWNERS = moderators.moderators


def coins(bot, user, *args):
	coins = db.field("SELECT Coins FROM users WHERE UserID = ?",
		user["id"])
	bot.send_message(f"{user['name']}, you have {coins:,} coins.")



def topList(bot,user,*args):
	gamers = db.records("SELECT Coins, UserName FROM users ORDER BY Coins DESC")
	coins = db.field("SELECT Coins FROM users WHERE UserID = ?",
		user["id"])

	message = ""

	count = 0
	for gamer in gamers:
		message = message + (f"{gamer[1]} : {gamer[0]}   |   ")
		if count == 2:
			break
	
	message = message + f" >> YOU have {coins:,} coins."


	bot.send_message(message)



def addCoins(bot, user, *args):
	if user["name"].lower() in OWNERS:
		if len(args) == 2:
			targetUser = args[0]
			coinAmount = args[1]

			print(targetUser)
			print(coinAmount)

			gamers = db.records("SELECT Coins, UserName FROM users")
			gamerList = {}

			for gamer in gamers:
				gamerList[gamer[1]] = gamer[0]

			if targetUser in gamerList:
				if coinAmount.isdigit():
					print(coinAmount)
					coins = int(gamerList[targetUser]) + int(coinAmount)

					db.execute("UPDATE users SET Coins = ? WHERE UserName = ?",
						coins, targetUser)
				else:
					bot.send_message("Invalid coin value entered")

			else:
				bot.send_message("User does not exist!")
		else:
			bot.send_message("!addCoins > Invalid arguments")
	else:
		print("not moderators")



def rmvCoins(bot, user, *args):
	
	if user["name"].lower() in OWNERS:
		if len(args) == 2:
			targetUser = args[0]
			coinAmount = args[1]

			print(targetUser)
			print(coinAmount)

			gamers = db.records("SELECT Coins, UserName FROM users")
			gamerList = {}

			for gamer in gamers:
				gamerList[gamer[1]] = gamer[0]

			if targetUser in gamerList:
				if coinAmount.isdigit():
					print(coinAmount)
					coins = int(gamerList[targetUser]) - int(coinAmount)
					if coins < 0:
						coins = 0
					db.execute("UPDATE users SET Coins = ? WHERE UserName = ?",
						coins, targetUser)
				else:
					bot.send_message("Invalid coin value entered")

			else:
				bot.send_message("User does not exist!")
		else:
			bot.send_message("!addCoins > Invalid arguments")


