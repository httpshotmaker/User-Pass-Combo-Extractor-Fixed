from loguru import logger
from art import tprint
import pretty_errors

tprint('Mail:pass to user:pass')

name = input("Введите путь до файла с базой\n> ")

try:
    with open(name, errors="ignore", encoding="utf-8") as file:
        combolist = file.readlines()

        if len(combolist) > 0:
            savefile = open("userpass.txt", "a")

            for combo in combolist:
                try:
                    past = combo.split('\n')[0]
                    user = combo.split("\n")[0].split(":")[0].split("@")[0]
                    password = combo.split("\n")[0].split(":")[1]
                    savefile.write(f"{user}:{password}\n")
                    logger.info(f'{past} -> {user}:{password}')
                except Exception:
                    pass
        else:
            logger.critical("Файл пуст")
except FileNotFoundError:
    logger.critical("Файла не существует")
