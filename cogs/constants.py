"""... constants"""
import discord

with open(r"C:\Users\Admin\AppData\Local\Programs\Python\Python38\Discord Code\SECRET_PASSWORD.txt") as read_file:
    SECRET_PASSWORD = read_file.read().strip()
DEFAULT_DATETIME_FORMAT = '%a %b %d %Y, %I:%M:%S %p'
DEFAULT_PATH = r'C:\Users\Admin\AppData\Local\Programs\Python\Python38\Discord Code\Community Bot'
WOLFRAM_APP_ID = "5J4G9H-477E85WUJE"
COMMUNITY_ID = 683869900850200581
BOT_COLOR = 0xffd200
BOT_ICON = "https://cdn.discordapp.com/avatars/753295703077421066/5554d01bdcb3b1f8b2dba20f898e4cd4.png"
CHECK_MARK = "https://images.emojiterra.com/google/android-10/512px/2611.png"
X_MARK = "https://datalab.noirlab.edu/images/cross.png"
INFO_EMOJI = "https://chancelight.com/wp-content/uploads/2020/03/blue-exclamation-point.png"
BASE_PATH = r"C:\Users\Admin\AppData\Local\Programs\Python\Python38\Discord Code\Community Bot"
TRUST_COMMENTS = {
    541402251202134035: 'High',
    779497578291134464: 'Medium-Low',
    775467892975730714: "VERY NOT TRUSTED"
}
MODERATORS = [683852333293109269, 541402251202134035]
TRUSTED_ROLES = [695312034627059763, 730159564078448660, 694965056202604664]
FORBIDDEN_WORDS = ['fuck', 'bitch', 'shit', 'gabe itch', 'penis', 'cunt', 'dildo', 'f|ck', 'n' + 'i' + 'g' + 'g' + 'a']
SKIP_EXTENSION_LOAD = ['utility.py', 'constants.py']
FSTRING_NL = '\n'
BASE_ERROR_EMBED = discord.Embed(color=discord.Color.red(), title="ERROR", description=None)
