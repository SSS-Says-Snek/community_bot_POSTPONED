"""
*Essential* module which includes functions to support BuiltInCogs.py :D
"""
import json
import re
from cogs.constants import *

WIFI_ONLINE = 27000  # Roughly equivalent to 7:30 AM
WIFI_OFFLINE = 79200  # Roughly equivalent to 10:00 PM


def string2fraction(fraction_str):
    try:
        return float(fraction_str)
    except ValueError:
        num, denominator = fraction_str.split('/')
        try:
            leading, num = num.split(' ')
            whole = float(leading)
        except ValueError:
            whole = 0
        fraction = float(num) / float(denominator)
        return whole - fraction if whole < 0 else whole + fraction


def sec_since_midnight(now):
    return (now - now.replace(hour=0, minute=0, second=0, microsecond=0)).total_seconds()


def sec_to_time(seconds: float) -> tuple:
    return_thing = []
    quot, remainder = divmod(seconds, 3600)
    return_thing.append(quot)
    quot2, remainder2 = divmod(remainder, 60)
    return_thing.append(quot2)
    return_thing.append(remainder2)
    return tuple(return_thing)


def split_long_message(message: str):
    """Quick question Avaxar, DOES THIS THING EVEN WORK"""
    split_output = []
    lines = message.split('\n')
    temp = ""

    for line in lines:
        if len(temp) + len(line) + 1 > 2000:
            split_output.append(temp[:-1])
            temp = line + '\n'
        else:
            temp += line + '\n'

    if temp:
        split_output.append(temp)

    return split_output


def other_split_long_message(message: str):
    all_characters = [char for char in message]
    split_output = []
    temp = ''

    for char in all_characters:
        if len(temp) < 2000:
            temp += char
        else:
            split_output.append(temp)
            temp = char
    split_output.append(temp)
    return split_output


def get_json_data(fp, key_to_key=None):
    if key_to_key:
        with open(fp) as read_json:
            return json.load(read_json)[key_to_key]
    else:
        with open(fp) as read_json:
            return json.load(read_json)


def format_byte(size: int, decimal_places=3):
    """Formats a given size and outputs a string equivalent to B, KB, MB, GB, or TB"""
    if size < 1e03:
        return f"{round(size, decimal_places)} B"
    if size < 1e06:
        return f"{round(size / 1e3, decimal_places)} KB"
    if size < 1e09:
        return f"{round(size / 1e6, decimal_places)} MB"
    if size < 1e12:
        return f"{round(size / 1e9, decimal_places)} GB"
    return f"{round(size / 1e12, decimal_places)} TB"


def is_member(guild, someone):
    """Checks if a user is inside a guild"""
    return someone in guild.members


def is_string_id(string_id):
    """Checks if a string is a valid user ID string"""
    if re.match('<@![0-9]+>', string_id):
        return True
    return False


def is_discord_username(username):
    """re makes me feel smart"""
    if re.match(r'.+#\d{4}', username):
        return True
    return False


def nested_dict_values(d):
    """SUPPOSEDLY returns all values of dicts, even nested (doesn't work for list values, so I'll work on it a bit more)"""
    for v in d.values():
        if isinstance(v, dict):
            yield from nested_dict_values(v)
        else:
            yield v


def discordify(message):
    """Converts normal string into "discord" string that includes backspaces to cancel out unwanted changes"""
    if '\\' in message:
        message = message.replace('\\', r'\\')
    if '*' in message:
        message = message.replace('*', r'\*')
    if '`' in message:
        message = message.replace('`', r'\`')
    if '_' in message:
        message = message.replace('_', r'\_')
    return message


def mysql_to_dict(mysql_fetchall, columns):
    """Function used to return a dict with columns as its keys and the values as its values"""
    mysql_fetchall = list(zip(*mysql_fetchall))
    return {columns[i]: mysql_fetchall[i] for i in range(len(columns))}


def mysql_to_dict_id_as_key_info_as_dict(mysql_fetchall, columns):
    """returns a dict with the ID as the key and the info is stored in the nested dict with the column being the key"""
    return {info[0]: {column: info for column, info in zip(columns[1:], info[1:])} for info in mysql_fetchall}


def censor(string, num_letter_censor=1, mode="discord", words_to_censor=FORBIDDEN_WORDS):
    """Censors a given string"""
    if mode == "discord":
        asterisk = r'\*'
    else:
        asterisk = '*'
    censored_string = string
    if words_to_censor:
        for forbidden_word in words_to_censor:
            if forbidden_word in string:
                censored_string = str(censored_string).replace(forbidden_word, f"{forbidden_word[0:num_letter_censor]}{asterisk * (len(forbidden_word) - num_letter_censor)}")
    else:
        censored_string = f"{string[0:num_letter_censor]}{asterisk * (len(string) - num_letter_censor)}"

    return censored_string
