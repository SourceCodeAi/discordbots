import discord
from discord.ext import commands
import sqlite3
import json
import random
from discord.ext.commands.cooldowns import BucketType
import errormsg
import asyncio


path = "waifus.json"

waifu_cost = 100
min_wage = 60
max_wage = 300


def check_dup(t, url):
    for i in t:
        if t.index(i) == 0:
            pass
        else:
            if url == i:
                return True


    return False



def check_waifus(user_id, avatar, author):
    userid = int(user_id)
    waifus = None
    userid = int(userid)
    db = sqlite3.connect("userwaifus.sqlite")
    db2 = sqlite3.connect("waifus.sqlite")
    c2 = db2.cursor()
    c = db.cursor()
    c.execute("SELECT * FROM uwd WHERE user_id = ?", (userid,))
    listed = c.fetchone()
    if listed == None:
        return None
    else:
        waifu_1 = listed[1]
        waifu_2 = listed[2]
        waifu_3 = listed[3]
                    
        if waifu_1 != "none":
            c2.execute("SELECT * FROM allwaifus WHERE image = ?", (waifu_1,))
            waifu_1 = c2.fetchone()
        if waifu_2 != "none":
            c2.execute("SELECT * FROM allwaifus WHERE image = ?", (waifu_2,))
            waifu_2 = c2.fetchone()

        if waifu_3 != "none":
            c2.execute("SELECT * FROM allwaifus WHERE image = ?", (waifu_3,))
            waifu_3 = c2.fetchone()

        if waifu_1 == "none":
            waifu_1 = "Empty Slot"   

        if waifu_2 == "none":
            waifu_2 = "Empty Slot"   

        if waifu_3 == "none":
            waifu_3 = "Empty Slot"   

        embed = discord.Embed(
            colour = discord.Colour.from_rgb(230, 138, 138)
        )

        if waifu_1 != "Empty Slot":
            waifu_1 = waifu_1[0]

        if waifu_2 != "Empty Slot":
            waifu_2 = waifu_2[0]
                    

        if waifu_3 != "Empty Slot":
            waifu_3 = waifu_3[0]

        embed.set_author(name = f"{author}'s Waifus", icon_url = avatar)
        embed.add_field(name = "Slot 1", value = waifu_1, inline = True)
        embed.add_field(name = "Slot 2", value = waifu_2, inline = True)
        embed.add_field(name = "Slot 3", value = waifu_3, inline = True)

        #await ctx.send(embed = embed)

        db.close()
        db2.close()
        return embed

    
    


class waifushop(commands.Cog):
    def __init__(self, client):
        self.client = client



    @commands.command()
    async def slot(self, ctx, slot_number):
        db2 = sqlite3.connect("waifus.sqlite")
        c2 = db2.cursor()
        try:
            num = int(slot_number)
        except:
            await ctx.send(":x: An error occured!")
            return
        userid = int(ctx.author.id)
        db = sqlite3.connect("userwaifus.sqlite")
        c = db.cursor()
        c.execute("SELECT * FROM uwd WHERE user_id = ?", (userid,))
        listed = c.fetchone()
        print(listed)
        if listed == None:
            await ctx.send("You have no waifus!")
            return
        else:
            if num == 1:
                c2.execute("SELECT * FROM allwaifus WHERE image = ?", (listed[1],))
                waifu_info = c2.fetchone()
                waifu_name = waifu_info[0]
                waifu_image = waifu_info[1]
                embed = discord.Embed(
                    title = "Waifu Preview",
                    description = "Selected Waifu: **{}**".format(waifu_name),
                    colour = discord.Colour.from_rgb(230, 138, 138)
                )

                embed.set_image(url = waifu_image)
                await ctx.send(embed = embed)
                return
            
            elif num == 2:
                c2.execute("SELECT * FROM allwaifus WHERE image = ?", (listed[2],))
                waifu_info = c2.fetchone()
                waifu_name = waifu_info[0]
                waifu_image = waifu_info[1]
                embed = discord.Embed(
                    title = "Waifu Preview",
                    description = "Selected Waifu: **{}**".format(waifu_name),
                    colour = discord.Colour.from_rgb(230, 138, 138)
                )

                embed.set_image(url = waifu_image)
                await ctx.send(embed = embed)
                return

            elif num == 3:
                c2.execute("SELECT * FROM allwaifus WHERE image = ?", (listed[3],))
                waifu_info = c2.fetchone()
                waifu_name = waifu_info[0]
                waifu_image = waifu_info[1]
                embed = discord.Embed(
                    title = "Waifu Preview",
                    description = "Selected Waifu: **{}**".format(waifu_name),
                    colour = discord.Colour.from_rgb(230, 138, 138)
                )

                embed.set_image(url = waifu_image)
                await ctx.send(embed = embed)
                return

            else:
                await ctx.send("That isn't a valid slot number!")


    @commands.command()
    async def testopen(self, ctx, wait : int):
        if ctx.author.id != 691406006277898302:
            return
        msg = await ctx.send(file = discord.File("cardopen.gif"))
        await asyncio.sleep(wait)
        await msg.delete()


    @commands.command()
    async def mywaifus(self, ctx):
        waifus = None
        userid = int(ctx.author.id)
        db = sqlite3.connect("userwaifus.sqlite")
        db2 = sqlite3.connect("waifus.sqlite")
        c2 = db2.cursor()
        c = db.cursor()
        c.execute("SELECT * FROM uwd WHERE user_id = ?", (userid,))
        listed = c.fetchone()
        if listed == None:
            await ctx.send(embed = errormsg.shoot_embed("You have no waifus!"))
            return
        else:
            waifu_1 = listed[1]
            waifu_2 = listed[2]
            waifu_3 = listed[3]
            
            if waifu_1 != "none":
                c2.execute("SELECT * FROM allwaifus WHERE image = ?", (waifu_1,))
                waifu_1 = c2.fetchone()
            if waifu_2 != "none":
                c2.execute("SELECT * FROM allwaifus WHERE image = ?", (waifu_2,))
                waifu_2 = c2.fetchone()

            if waifu_3 != "none":
                c2.execute("SELECT * FROM allwaifus WHERE image = ?", (waifu_3,))
                waifu_3 = c2.fetchone()

            if waifu_1 == "none":
                waifu_1 = "Empty Slot"   

            if waifu_2 == "none":
                waifu_2 = "Empty Slot"   

            if waifu_3 == "none":
                waifu_3 = "Empty Slot"   

            embed = discord.Embed(
                colour = discord.Colour.from_rgb(230, 138, 138)
            )

            if waifu_1 != "Empty Slot":
                waifu_1 = waifu_1[0]

            if waifu_2 != "Empty Slot":
                waifu_2 = waifu_2[0]
            

            if waifu_3 != "Empty Slot":
                waifu_3 = waifu_3[0]

            embed.set_author(name = f"{ctx.author}'s Waifus", icon_url = ctx.author.avatar_url)
            embed.add_field(name = "Slot 1", value = waifu_1, inline = True)
            embed.add_field(name = "Slot 2", value = waifu_2, inline = True)
            embed.add_field(name = "Slot 3", value = waifu_3, inline = True)

            await ctx.send(embed = embed)

            db.close()
            db2.close()

    @commands.command()
    async def bal(self, ctx):
        user_bal = None
        userid = int(ctx.author.id)
        db = sqlite3.connect("currencydata.sqlite")
        c = db.cursor()
        c.execute("SELECT * FROM usercurrency WHERE user_id = ?", (userid,))
        listed = c.fetchone()
        if listed == None:
            user_bal = 0
        else:
            user_bal = int(listed[1])

        embed = discord.Embed(
            description = f"You have {user_bal} tokens!",
            colour = discord.Colour.from_rgb(230, 138, 138)
        )
        embed.set_author(name = f"{ctx.author}'s Balance", icon_url = ctx.author.avatar_url)

        await ctx.send(embed = embed)

        db.close()


    




    @commands.command()
    @commands.cooldown(1, 3600, BucketType.user)
    async def work(self, ctx):
        amount = random.randint(min_wage, max_wage)
        userid = int(ctx.author.id)
        db = sqlite3.connect("currencydata.sqlite")
        c = db.cursor()
        c.execute("SELECT * FROM usercurrency WHERE user_id = ?", (userid,))
        listed = c.fetchone()
        if listed == None:
            c.execute("INSERT INTO usercurrency VALUES (?, ?)", (userid, 0))
            c.execute("UPDATE usercurrency SET balance = ? WHERE user_id = ?", (amount, userid))
            db.commit()
            db.close()
        else:
            c.execute("UPDATE usercurrency SET balance = ? WHERE user_id = ?", (int(listed[1]) + amount, userid))
            db.commit()
            db.close()


        await ctx.send(embed = errormsg.shoot_noti("You have worked and received {} tokens!".format(amount)))



    @commands.command()
    async def addwaifu(self, ctx, image_url, *, name):
        if int(ctx.author.id) != 691406006277898302:
            return
        
        userid = int(ctx.author.id)
        image_url = str(image_url)
        name = str(name)
        db = sqlite3.connect("waifus.sqlite")
        c = db.cursor()
        c.execute("INSERT INTO allwaifus VALUES (?, ?)",  (name, image_url))
        db.commit()
        db.close()
        await ctx.send("Added Waifu!")

        




    @commands.command()
    async def buywaifu(self, ctx):
       
        userid = int(ctx.author.id)
        db = sqlite3.connect("currencydata.sqlite")
        c = db.cursor()
        c.execute("SELECT * FROM usercurrency WHERE user_id = ?", (userid,))
        listed = c.fetchone()
        if listed == None:
            await ctx.send(embed = errormsg.shoot_noti("Oh bb! You don't have any tokens! I can't sell you a waifu!"))
            db.close()
            return
        elif int(listed[1]) < waifu_cost:
            await ctx.send(embed = errormsg.shoot_noti("Oh bb! You don't have enough tokens! When you get enough, keep in mind, I'm looking for a daddy! Hehe!"))
            db.close()
            return


        #await ctx.send(listed[1])

        current_bal = int(listed[1])
        final_bal = current_bal - waifu_cost
        c.execute("UPDATE usercurrency SET balance = ? WHERE user_id = ?", (final_bal, userid))
        db.commit()
        db.close()
        #return
        #print("HELLO TEST " + str(db))
        data = None
        db2 = sqlite3.connect("waifus.sqlite")
        c2 = db2.cursor()
        c2.execute("SELECT * FROM allwaifus")
        data = c2.fetchall()
        data = random.choice(data)
        print(data)
        embed = discord.Embed(
            title = "Hehe. Here's your waifu cutie!",
            description = "You got **{}**!".format(data[0]),
            colour = discord.Colour.from_rgb(230, 138, 138)
        )

        embed.set_image(url = data[1])
        await ctx.send(embed = embed)
        await ctx.send(embed = errormsg.shoot_noti(f"{waifu_cost} tokens have been deducted from your account!"))

        db3 = sqlite3.connect("userwaifus.sqlite")
        c3 = db3.cursor()
        c3.execute("SELECT * FROM uwd WHERE user_id = ?", (userid,))
        userdata = c3.fetchone()
        print(userdata)
        if userdata != None:
            if check_dup(userdata, data[1]) == True:
                await ctx.send("You already have this waifu! Compensated you with 50 free tokens!")
                comp = sqlite3.connect("currencydata.sqlite")
                cp = comp.cursor()
                cp.execute("SELECT * FROM usercurrency WHERE user_id = ?", (userid,))
                userd = cp.fetchone()
                cp.execute("UPDATE usercurrency SET balance = ? WHERE user_id = ?", (int(userd[1]) + 50, userid))
                comp.commit()
                comp.close()
                return

            
        if userdata == None:
            c3.execute("INSERT INTO uwd VALUES (?, ?, ?, ?)", (userid, data[1], "none", "none"))
            db3.commit()
            await ctx.send("**{}** is now in your first Waifu Slot! Congrats on earning your first waifu! You have 2/3 slots left".format(data[0]))
        elif userdata[2] == "none":
            print("2 empty")
            c3.execute("UPDATE uwd SET waifutwo = ? WHERE user_id = ?", (data[1], userid))
            db3.commit()
            await ctx.send("**{}** is now in your second Waifu Slot! You have 1/3 slots left!".format(data[0]))
        elif userdata[3] == "none":
            print("3 empty")
            c3.execute("UPDATE uwd SET waifuthree = ? WHERE user_id = ?", (data[1], userid))
            db3.commit()
            await ctx.send("**{}** is now in your third Waifu Slot! You have 0/3 slots left!".format(data[0]))

        else:
            def check(reaction, user):
                return user.id == ctx.author.id
            await ctx.send(f"If you would like to keep this waifu, you must break up with one of your other ones! React with the appropriate Slot Number! Read below to check your waifus!")
            if check_waifus(ctx.author.id, ctx.author.avatar_url, str(ctx.author)) != None:
                waifus = await ctx.send(embed = check_waifus(ctx.author.id, ctx.author.avatar_url, str(ctx.author)))
                emojis = ["1\N{variation selector-16}\N{combining enclosing keycap}", "2\N{variation selector-16}\N{combining enclosing keycap}", "3\N{variation selector-16}\N{combining enclosing keycap}"]
                for i in emojis:
                    await waifus.add_reaction(i)

            else:
                await ctx.send(embed = errormsg.shoot_embed("You have no waifus!"))
                return
            reaction, user = await self.client.wait_for("reaction_add", check = check, timeout = 60.0)
            #await ctx.send("```{}```".format(reaction.emoji))
            print(reaction.emoji)
            chosen_slot = None
            if str(reaction.emoji) == "1️⃣":
                rdb = sqlite3.connect("userwaifus.sqlite")
                rc = rdb.cursor()
                rc.execute("UPDATE uwd SET waifuone = ? WHERE user_id = ?", (data[1], userid))
                rdb.commit()
                rdb.close()
                await ctx.send(f"Set **{data[0]}** in Slot 1!")
                return
            elif str(reaction == "2️⃣"):
                rdb = sqlite3.connect("userwaifus.sqlite")
                rc = rdb.cursor()
                rc.execute("UPDATE uwd SET waifutwo = ? WHERE user_id = ?", (data[1], userid))
                rdb.commit()
                rdb.close()
                await ctx.send(f"Set **{data[0]}** in Slot 2!")
                return
            elif str(reaction == "3️⃣"):
                rdb = sqlite3.connect("userwaifus.sqlite")
                rc = rdb.cursor()
                rc.execute("UPDATE uwd SET waifuthree = ? WHERE user_id = ?", (data[1], userid))
                rdb.commit()
                rdb.close()
                await ctx.send(f"Set **{data[0]}** in Slot 3!")
                return



            


        db.close()


    @commands.command()
    async def setdata(self, ctx, amount : int):
        userid = int(ctx.author.id)
        if userid != 691406006277898302:
            return
        db = sqlite3.connect("currencydata.sqlite")
        c = db.cursor()
        c.execute("SELECT * FROM usercurrency WHERE user_id = ?",(userid,))
        listed = c.fetchone()
        if listed == None:
            c.execute("INSERT INTO usercurrency VALUES (?, ?)", (userid, amount))
            db.commit()

        else:
            c.execute("UPDATE usercurrency SET balance = ? WHERE user_id = ?", (amount, userid))
            db.commit()

        db.close()
        await ctx.send("Updated DB")


    @commands.command()
    async def loadstring(self, ctx):
        a = ["hi", "hello"]
        a = str(a)
        await ctx.send(a)
        a = list(a)
        for i in a:
            await ctx.send(i)


    @work.error
    async def work_error(self, ctx, error):
        if "cooldown" in str(error).lower():
            coodlown_left = round(int(error.retry_after) / 60)
            await ctx.send(embed = errormsg.shoot_noti("You are on a work cooldown! Please wait another **{} minutes**".format(coodlown_left)))
            return

        





def setup(client):
    client.add_cog(waifushop(client))