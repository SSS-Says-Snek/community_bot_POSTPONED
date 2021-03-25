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
X_MARK = "https://lh3.googleusercontent.com/proxy/1BEx9ZATjYliu1iTazplKMWR-2jSnov23L4chJ-jn" \
         "-5J_04hhfvvEawnA9c8qbAS1j31ZSBenCUhOA2yGtk47_T3DYoimlb288YQhmIunfV6DeZoG9KxkbzK2dcNN_GJ-g"
INFO_EMOJI = "https://chancelight.com/wp-content/uploads/2020/03/blue-exclamation-point.png"
BASE_PATH = r"C:\Users\Admin\AppData\Local\Programs\Python\Python38\Discord Code\Community Bot"
TRUST_COMMENTS = {
    541402251202134035: 'High',
    779497578291134464: 'Medium-Low',
    775467892975730714: "VERY NOT TRUSTED"
}
MODERATORS = [683852333293109269, 541402251202134035]
FORBIDDEN_WORDS = ['fuck', 'bitch', 'shit', 'gabe itch', 'penis', 'cunt', 'dildo', 'f|ck', 'n' + 'i' + 'g' + 'g' + 'a']
FSTRING_NL = '\n'
BASE_ERROR_EMBED = discord.Embed(color=discord.Color.red(), title="ERROR", description=None)

# err, move SECRET_PASSWORD somewhere safe
