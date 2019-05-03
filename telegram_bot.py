import telegram 
from telegram.ext import Updater, CommandHandler

import socket
import sys


class TelegramBot:
    _tokenBot = ""
    _dest = ""
    _message = ""

    def __init__(tokenBot, dest):
        _tokenBot = tokenBot
        _dest = dest

def isAlive(bot, update, args):
    chat_id = update.message.chat_id
    print(chat_id)

    # Create TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #Connect the socket to the port where the server is listening
    server_address = ('localhost', 5000)
    message = "Connecting to "+server_address[0]+" on port "+str(server_address[1])
    bot.send_message(chat_id=chat_id, text=message, timeout=60)
    sock.connect(server_address)

    filename = args[0]
    message = "Verifying "+filename+" thread"
    bot.send_message(chat_id=chat_id, text=message, timeout=60)
    try:
        # Send data
        print("filename: "+filename)
        aux = "filename\n"
        sock.sendall((filename+"\n").encode('utf-8'))

        # Look for response
        data = sock.recv(1024)
        data = data.decode("utf-8")
        print("Received: "+data)

        if data == "true\n":
            message = "The thread is alive"
        else:
            message = "The thread is dead"
        bot.send_message(chat_id=chat_id, text=message, timeout=60)
    except:
        print("Oops!",sys.exc_info()[0],"occured.")
        print("Next entry.")
        print()

    finally:
        print("Closing socket")
        sock.close()


def main():
    tokenBot = "735677331:AAHRclwlnQRnlzcAa9-CR2-0GZjmdjNIF_A"
    dest = "848768819"
    message = "Hello world"
    bot = telegram.Bot(token = tokenBot)
    bot.send_message(chat_id=dest, text=message, timeout=60)
    updater = Updater(tokenBot)
    dp = updater.dispatcher;
    dp.add_handler(CommandHandler('alive', isAlive, pass_args=True))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()

