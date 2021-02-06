import discord
import random
from discord.ext import commands
from discord import Member

client = commands.Bot(command_prefix = '.')
client.remove_command('help')

# Events
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('With Ak\'s Dick'))
    print('Ready.')

# Reply
@client.command()
async def status(ctx):
  await ctx.send('Bot is up & running')

# Embded
@client.command(pass_context=True)
async def help(ctx):
    channel = ctx.message.channel
    embed = discord.Embed(
        title = 'Help Box',
        description = 'Available Bot Commands',
        colour = discord.Colour.red()
    )

    embed.set_footer(text='.')
    embed.set_author(name='Ak\'s Bot')
    embed.add_field(name='.clear', value='Clear Old Messages', inline=False)
    embed.add_field(name='.bot', value='Display Bot\'s Status', inline=False)
    embed.add_field(name='.8ball', value='Answers Your Questions', inline=False)
    embed.add_field(name='.avatar', value='Shows Your Profile Picture', inline=False)

    await ctx.send(embed=embed)

# Avatar
@client.command(aliases=['av', 'pfp'])
async def avatar(ctx, member: Member = None):
 if not member:
  member = ctx.author
 await ctx.send(member.avatar_url)
   
# 8 Ball
@client.command(aliases=['8ball', 'ball'])
async def _8ball(ctx, *, question):
    responses = ['It is certain.',
                 'It is decidedly so.',
                 'Without a doubt.',
                 'Yes - definitely.',
                 'You may rely on it.',
                 'As I see it, yes.',
                 'Most likely.',
                 'Outlook good.',
                 'Yes.',
                 'Signs point to yes.',
                 'Reply hazy, try again.',
                 'Ask again later.',
                 'Better not tell you now.',
                 'Cannot predict now.',
                 'Concentrate and ask again.',
                 "Don't count on it.",
                 'My reply is no.',
                 'My sources say no.',
                 'Outlook not so good.',
                 'Very doubtful.']
    await ctx.send (f'Question: {question}\nAnswer: {random.choice(responses)}')

# Clear Chat
@client.command()
async def clear(ctx, amount : int):
    await ctx.channel.purge(limit=amount)

@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please specify an amount of messages to delete')

#bans a user with a reason
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please pass in all requirements :rolling_eyes:.')
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You dont have all the requirements :angry:")


The below code bans player.
@client.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, member : discord.Member, *, reason = None):
   await member.ban(reason = reason)

The below code unbans player.
@client.command()
@commands.has_permissions(administrator = True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split("#")

   for ban_entry in banned_users:
       user = ban_entry.user

       if (user.name, user.discriminator) == (member_name, member_discriminator):
           await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return

client.run('')
