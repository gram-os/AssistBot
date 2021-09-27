from discord.ext import tasks, commands
import asyncio,typing

class HornyJailCog(commands.Cog):
  def __init__(self,bot):
    self.bot = bot
    self.time_left = 0
    self.countdown.start()
 
  async def add_seconds(self, sec:int=0):
    self.time_left += 10
 
  
  async def add_minutes(self,ctx,minutes:int=0):
    self.time_left += minutes*60

  async def view_time(self,ctx):
    if self.time_left==0:
      await('All done!')
    else:
      minutes, seconds = divmod(self.time_left,60)
      timeformat = "{:02d}:{:02d}".format(minutes,seconds)
      message = await ctx.send(timeformat)
      i=5
      while i>0:
        i-=1
        minutes, seconds = divmod(self.time_left,60)
        timeformat = "{:02d}:{:02d}".format(minutes,seconds)
        await message.edit(content=timeformat)
        await asyncio.sleep(1)
      await message.delete()
    
  @tasks.loop(seconds=1)
  async def countdown(self):
    if self.time_left>0:
      self.time_left -= 1



def setup(bot):
  bot.add_cog(CountdownCog(bot))