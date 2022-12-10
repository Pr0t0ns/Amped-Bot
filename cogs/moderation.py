import discord, asyncio
from .colors import green, blue, red
from discord.ext import commands
class Moderation_commands(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.Embed = discord.Embed
    
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, user: discord.Member, *, reason=None):
        await user.ban(reason=reason)
        embed = self.Embed(title=f":bangbang: Succesfully Banned {user}", description=f"{user} has been hit by the ban hammer", color=blue)
        return await ctx.send(embed=embed)
    
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def unban(self, ctx, *, user):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = user.split("#")

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                embed = self.Embed(title=f":white_check_mark: Unbanned {user}", description=f"{user} has been unvanished from the server by {ctx.message.author}", color=green)
                await ctx.send(embed=embed)
                return

    @commands.command(aliases=['boot'], pass_context=True)
    @commands.has_permissions(administrator=True)
    async def kick(self, ctx, user: discord.Member, *, reason=None):
        await user.kick(reason=reason)
        embed = self.Embed(title=f":bangbang: Succesfully Kicked {user}", description=f"{user} has been booted from the server!", color=blue)
        await ctx.send(embed=embed)

    @commands.command(aliases=['addrole', 'removerole', 'takerole', 'giverole'], pass_context=True)
    @commands.has_permissions(administrator=True)
    async def role(self, ctx, user: discord.Member, *, role: discord.Role):
        if role.position > ctx.author.top_role.position:
            embed = self.Embed(title=f":x: Insufficent Permissions", description=f"The role your trying to give {user} is higher than your top role", color=red)
            return await ctx.send(embed=embed)
        if role in user.roles:
            try:await user.remove_roles(role)
            except Exception as err: embed = self.Embed(title=f":x: Role Hierarchy Error", description=f"You must move my role higher than {role} role in order for me to add or remove {role} from users", color=red); return await ctx.send(embed=embed) 
            embed = self.Embed(title=f":white_check_mark: Removed Role", description=f"Successfully Removed role from user ({user})", color=blue)
        else:
            try:await user.add_roles(role)
            except Exception as err: embed = self.Embed(title=f":x: Role Hierarchy Error", description=f"You must move my role higher than {role} role in order for me to add or remove {role} from users", color=red); return await ctx.send(embed=embed)
            embed = self.Embed(title=f":white_check_mark: Added Role", description=f"Successfully added role to user ({user})", color=blue)
        await ctx.reply(embed=embed)
    
    @commands.command(aliases=['clear', 'clean'], pass_context=True)
    @commands.has_permissions(administrator=True)
    async def purge(self, ctx, amount: int):
        if amount >= 1000 or amount < 0:
            embed = self.Embed(title=f':x: Too Many Messages', description=f"You cannot purge more than 1000 messages at a time!", color=red)
            return await ctx.send(embed=embed)
        await ctx.channel.purge(limit=amount)
        embed = self.Embed(title=f"Purged {amount}", description=f"{ctx.message.author} successfully Purged {amount} messages!", color=blue)
        msg = await ctx.reply(embed=embed)
        await asyncio.sleep(5)
        await msg.delete() 
    
    @commands.command(aliases=['replace'])
    @commands.has_permissions(administrator=True)
    async def nuke(self, ctx, channel: discord.TextChannel=None):
        if channel == None:
            channel = ctx.channel.id
            channel = discord.utils.get(ctx.guild.channels, id=channel)
            channel = channel.name
        else:
            channel = channel.name
        nuke_channel = discord.utils.get(ctx.guild.channels, name=channel)
        if nuke_channel != None:
            new_channel = await nuke_channel.clone(reason="Nuked")
            await nuke_channel.delete()
            embed = self.Embed(title=":warning: Channel Nuked", description=f"This channel has been nuked by {ctx.message.author}!", color=blue)
            return await new_channel.send(embed=embed)
        else:
            embed = self.Embed(title=f":x: Channel Not Found", description=f"The channel you mentioned ({channel}) was not found!", color=red)
            return await ctx.send(embed=embed)

def setup(client):
	client.add_cog(Moderation_commands(client))