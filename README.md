A (not so simple) bot made by ME (SSS_Says_Snek#0194) for my server.
Nothing else really...

**NOTE:** Some files are excluded for privacy reasons (EG my bot token),
and some things are manually coded in (hopefully I will soon be able to remove that manual code lel)
but mainly the code is just a *guidance* for people who need help with something

***HOWEVER***, the commands still function *okay* (?), and all you have to do is to
modify the `with` statement (line 18) so that the file contains your bot token

Commands are divided into classes ("cogs" in discord.py), some notable ones which include:
##Server (And Bot) Owner Commands
- `$load_cog {name}, $unload_cog {name}, $reload_cog {name}`... does what the function name says
- `$archive {channel to get messages} {num message} {channel to post messages} [options]` Archive messages
from a certain channel
- `$run_process {task}` runs a process on bot owner's PC*