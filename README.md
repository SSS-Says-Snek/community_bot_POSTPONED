# Test Bot - Community Edition

![Version Badge](https://img.shields.io/github/v/release/SSS-Says-Snek/community_bot?include_prereleases)
![Repo Size Badge](https://img.shields.io/github/repo-size/SSS-Says-Snek/community_bot?color=%2332a852)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/d2fa275e87bf40859d1e0bf97bf1bb35)](https://www.codacy.com/gh/SSS-Says-Snek/community_bot/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=SSS-Says-Snek/community_bot&amp;utm_campaign=Badge_Grade)

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
- `$solve` can solve A LOT of problems (E.g. Systems of equations, algebra, etc). It also looks nice...
- `$old_solve` is just like `$solve`, but *old*
- **`NOTE`**: These commands offer basic functionality (except for $solve, that is big brain),
but importing `cogs.MoreMathCommands` will contain even more math commands

## User Commands
- `$cogs` lists out the cogs available, in case you don't know what they are
- `$(whois/get_user) {user context}` gets some sweet info from a user. A user context can be: An ID, a mention, or a username+discriminator (last one is limited to server only)*
- `$clear {num messages}`
Have a suggestion, or does something not work? Feel free to leave a pull request, or an issue

## Slash Commands
- `/ping`... just outputs the ping, but it's **pretty**


*this command may not work in different servers right now, but that's okay as I will look into it

**do ***NOT*** try to exploit this, you'll need to verify identity first