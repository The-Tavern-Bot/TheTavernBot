from discord import Colour, Embed
from discord.ext.commands import Cog, command

class GeneratorCog(Cog, name='Generator'):

    def __init__(self, bot):
        self.bot = bot

    @command(name='generate')
    async def generator_command(self, ctx, generate_num):
        """All of the generate commands that are used to generate things, such as:
        characters, npc's and names."""
        generator_embed = Embed(colour=Colour.blurple())
        commands = ['character', 'npc']
        desc = ''
        num = 0
        if not generate_num():
            generator_embed.title = 'All of the Generator Commands'
            for _ in commands:
                desc += f'***{commands[num]}*** \n'
            generator_embed.description = desc
            generator_embed.set_footer(text='Use ;generate {command} to use one of the above commands.')
            return await ctx.send(embed=generator_embed)
        return


def setup(bot)
    bot.add_cog(GeneratorCog(bot))