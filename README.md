# Test Bot - Community Edition

A (not so simple) bot made by ME (SSS_Says_Snek#0194) for my server.
Nothing else really...

**NOTE:** Some files are excluded for privacy reasons (EG my bot token),
and some things are manually coded in (hopefully I will soon be able to remove that manual code lel)
but mainly the code is just a *guidance* for people who need help with something

***HOWEVER***, the commands still function *okay* (?), and all you have to do is to
modify the `with` statement (line 18) so that the file contains your bot token

Commands are divided into classes ("cogs" in discord.py), some notable ones which include:

## Server (And Bot) Owner Commands
- `$load_cog {name}, $unload_cog {name}, $reload_cog {name}`... does what the function name says
- `$archive {channel to get messages} {num message} {channel to post messages} [options]` Archive messages
from a certain channel. Options include: oldest messages, suppress pings, date before, date after, etc.
- `$run_process {task}` runs a process on bot owner's PC**

## Fun Commands
- `$wolfram {question}` asks a question to wolfram alpha. THERE IS AN API LIMIT TO THIS (1000 requests per month)
- `$choice "{choice 1}" "{choice 2}" etc` chooses something out of those choices (multi-word choices must be enclosed in quotes)
- `$eightball/$8ball {question}` want to ask the OMNISCIENT ball? Ask away!
- `$dice, $coinflip, $randnum {min} {max}` pretty self-explanatory

## Math Commands
- `$add/$subtract/$multiply/$divide/$sqrt/$exponent/$square {num} {num}`... these are the most self-explanatory
- `$solve` can solve A LOT of problems (E.g. Systems of equations, algebra, etc). A bit complicated to use, but hey, it works
- **`NOTE`**: These commands offer basic functionality (except for $solve, that is big brain),
but importing `cogs.MoreMathCommands` will contain even more math commands

## Miscellaneous Commands
- `$cogs` lists out the cogs available, in case you don't know what they are
- `$whois {user context}` gets some sweet info from a user. A user context can be: An ID, a mention, or a username+discriminator (last one is limited to server only)*

Have a suggestion, or does something not work? Feel free to leave a pull request, or an issue

*this command may not work in different servers right now, but that's okay as I will look into it

**do ***NOT*** try to exploit this, I have protecction