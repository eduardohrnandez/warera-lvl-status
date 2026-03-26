import discord
from discord.ext import commands
from flask import Flask
from threading import Thread
import os

# --- SERVIDOR WEB ---
app = Flask('')
@app.route('/')
def home(): return "Bot de Builds Online"

def run_server():
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)

def mantener_vivo():
    Thread(target=run_server).start()

# --- CONFIGURACIÓN ---
TOKEN = os.environ.get('DISCORD_TOKEN')

class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!", intents=discord.Intents.default())

    async def setup_hook(self):
        await self.tree.sync()
        print("Comandos / sincronizados.")

bot = MyBot()

# --- MENÚ DESPLEGABLE (Niveles 15 al 39) ---
class MenuNiveles(discord.ui.Select):
    def __init__(self, modo):
        self.modo = modo
        
        opciones = []
        emoji_usar = "🌱" if modo == "ECO" else "🩸"
        
        # Rango del 15 al 39 (Exactamente 25 opciones, el máximo permitido)
        for i in range(15, 40):
            opciones.append(discord.SelectOption(label=f"Nivel {i}", emoji=emoji_usar))
            
        super().__init__(placeholder=f"Selecciona tu Nivel ({modo})...", min_values=1, max_values=1, options=opciones)

    async def callback(self, interaction: discord.Interaction):
        nivel_seleccionado = self.values[0] 
        
        # --- CAJA DE IMÁGENES MODO ECO ---
        imagenes_eco = {
            "Nivel 15": "https://media.discordapp.net/attachments/1475960551615103152/1475960672927092796/IMG-20260224-WA0009.jpg?ex=699f62fe&is=699e117e&hm=eba5179bae6ae1f90a1eb243fbe74e6792bc1e0449f9354589d8b7447e476bb0&=&format=webp&width=600&height=270",
            "Nivel 16": "https://media.discordapp.net/attachments/1475960551615103152/1475960723162271866/IMG-20260224-WA0010.jpg?ex=699f630a&is=699e118a&hm=6539637035feebc8d6e0cc00dae42c76c857979155f1219c3a8909a49ec64ca9&=&format=webp&width=602&height=276",
            "Nivel 17": "https://media.discordapp.net/attachments/1475960551615103152/1475961695041228985/IMG-20260224-WA0014.jpg?ex=699f63f2&is=699e1272&hm=30e18e622cc9fe2ff1b4378fe247f7d8d093ad0eee76312bc096fe03a17d1266&=&format=webp&width=600&height=246",
            "Nivel 18": "https://media.discordapp.net/attachments/1475960551615103152/1475962295535276093/IMG-20260224-WA0015.jpg?ex=699f6481&is=699e1301&hm=ff82346fa59dbc2eff1f645b70d67f3406125d7d1749d8ef70d3201d812d38d1&=&format=webp&width=598&height=247",
            "Nivel 19": "https://media.discordapp.net/attachments/1475960551615103152/1475963870571925515/IMG-20260224-WA0018.jpg?ex=699f65f8&is=699e1478&hm=f9e8d157931df615930f5c4baedbec8bda5f300b3efd3b2955cde423433db846&=&format=webp&width=597&height=258",
            "Nivel 20": "https://media.discordapp.net/attachments/1475960551615103152/1475966402786623578/IMG-20260224-WA0019.jpg?ex=699f6854&is=699e16d4&hm=c95f42219913e0d29f15a8d492292ee34bf355366a73ee9f8df6218bba48a9a3&=&format=webp&width=597&height=252",
            "Nivel 21": "https://media.discordapp.net/attachments/1475960551615103152/1475970172484321311/IMG-20260224-WA0022.jpg?ex=699f6bd7&is=699e1a57&hm=ac33e9a6ee64b4759dcf8963acfc2ce5e929247a97043b7e5b30626be345448c&=&format=webp&width=604&height=261",
            "Nivel 22": "https://media.discordapp.net/attachments/1475960551615103152/1475975979007742013/IMG-20260224-WA0024.jpg?ex=699f713f&is=699e1fbf&hm=3bb47aa0c412bf0f78ef28bce82c241e0f84272060219d0b122f2ea330496872&=&format=webp&width=598&height=254",
            "Nivel 23": "https://media.discordapp.net/attachments/1475960551615103152/1475978734535184577/IMG-20260224-WA0025.jpg?ex=699f73d0&is=699e2250&hm=6222a4f8fc1fc0903ff1d6dcc69361bdd3216d24cc57efe06dcf4b920b257798&=&format=webp&width=606&height=268",
            "Nivel 24": "https://media.discordapp.net/attachments/1475960551615103152/1475979840837521625/IMG-20260224-WA0028.jpg?ex=699f74d8&is=699e2358&hm=7f945e20b372da2320a29e2101a71a7f8fdb3b98ec5db25973cdcd4771ff30d4&=&format=webp&width=602&height=274",
            "Nivel 25": "https://media.discordapp.net/attachments/1475960551615103152/1475983824398848061/IMG-20260224-WA0029.jpg?ex=699f788e&is=699e270e&hm=ce6805533856c409138ad59c169da16f2c782a02b54c83963e28598bf71bb430&=&format=webp&width=643&height=414",
            "Nivel 26": "https://media.discordapp.net/attachments/1475960551615103152/1476281254453448917/IMG-20260225-WA0019.jpg?ex=69a1364f&is=699fe4cf&hm=73072c3aa42d9394b94e31852d2c27831d23bbd50f4f6aa041b8fd8518864047&=&format=webp&width=624&height=266",
            "Nivel 27": "https://media.discordapp.net/attachments/1475960551615103152/1476704676417245295/IMG-20260226-WA0023.jpg?ex=69a563a6&is=69a41226&hm=6cf41f795bf2710ae282b2d6144f87fd03e28dbfeece0d068b33393f2b8082c5&=&format=webp&width=648&height=383",
            "Nivel 28": "https://media.discordapp.net/attachments/1475960551615103152/1476705348843868192/IMG-20260226-WA0025.jpg?ex=69a56447&is=69a412c7&hm=f7e225a19e1c4a1aba3606775834d06151ff1b32d965d2fed67bf00802bc36ff&=&format=webp&width=615&height=394",
            "Nivel 29": "https://media.discordapp.net/attachments/1475960551615103152/1476707828264734811/IMG-20260226-WA0031.jpg?ex=69a56696&is=69a41516&hm=4c91f7bbc1f01ef91b93f38a538a5ad9584170129dbb4e2fdbf88ae174fc0a01&=&format=webp&width=605&height=424",
            "Nivel 30": "https://media.discordapp.net/attachments/1475960551615103152/1476708759127462112/IMG-20260226-WA0032.jpg?ex=69a56774&is=69a415f4&hm=5e4cbc11bb3aa387d98dcb07e509663becb0d4f0fc780500c81219d944b80ad4&=&format=webp&width=623&height=410",
            "Nivel 31": "https://media.discordapp.net/attachments/1475960551615103152/1476710085689348269/IMG-20260226-WA0035.jpg?ex=69a568b0&is=69a41730&hm=f9a3db569783f7acb460c9649c4e4df44266fc4a17b3743b92bb40091316ca12&=&format=webp&width=594&height=401",
            "Nivel 32": "https://media.discordapp.net/attachments/1475960551615103152/1476711033405182154/IMG-20260226-WA0036.jpg?ex=69a56992&is=69a41812&hm=533f8b667f0348514e5f22705443b8e9fdb2741ded1d8eb50abe70abb97af025&=&format=webp&width=621&height=407",
            "Nivel 33": "https://media.discordapp.net/attachments/1475960551615103152/1476711839030317056/IMG-20260226-WA0039.jpg?ex=69a56a52&is=69a418d2&hm=42d3031dab293ce9fe6b21b51bf2cecdb363c760aa44ed05f4b39c7ed7ecafc0&=&format=webp&width=615&height=409",
            "Nivel 34": "https://media.discordapp.net/attachments/1475960551615103152/1477428411839545516/IMG-20260228-WA00291.jpg?ex=69a562ae&is=69a4112e&hm=5a6bc2b0738d99e4e5aa6b5fb9ca2d0bcafd935db83e837e81d30f50252a8e15&=&format=webp&width=609&height=416",
            "Nivel 35": "https://media.discordapp.net/attachments/1475960551615103152/1477429019438743775/IMG-20260228-WA0030.jpg?ex=69a5633f&is=69a411bf&hm=19bf0bd8b62188c39985a4d352f516ddee2ccc441702008a514df62f959b107f&=&format=webp&width=611&height=401",
            "Nivel 36": "https://media.discordapp.net/attachments/1475960551615103152/1477429835403104266/IMG-20260228-WA0033.jpg?ex=69a56402&is=69a41282&hm=cc0b24be89989051a3ef6a6460b04767f4021ec925280ba19c5e89f682893d20&=&format=webp&width=643&height=412",
            "Nivel 37": "https://media.discordapp.net/attachments/1475960551615103152/1477432165766664316/IMG-20260228-WA0034.jpg?ex=69a5662d&is=69a414ad&hm=f1bd4258ea153c1d049fb78cf17821ff3d0caf3239ffdaee8ff2a2f27ed01848&=&format=webp&width=611&height=410",
            "Nivel 38": "https://media.discordapp.net/attachments/1475960551615103152/1477434627760193606/IMG-20260228-WA0037.jpg?ex=69a56878&is=69a416f8&hm=1561cc4dea2596dff18d75d548f8c196e493c6164d15a8896b62f845dd59b7db&=&format=webp&width=603&height=452",
            "Nivel 39": "https://media.discordapp.net/attachments/1475960551615103152/1477435761270722620/IMG-20260228-WA0039.jpg?ex=69a56986&is=69a41806&hm=893ea9f3ca5f5e443c4521bf9ea4779c1057443bf645a230c02d8efd5923e8a8&=&format=webp&width=618&height=461"
        }
        
        # --- CAJA DE IMÁGENES MODO WAR ---
        imagenes_war = {
            "Nivel 15": "https://media.discordapp.net/attachments/1475960551615103152/1485304218725122108/image.png?ex=69c5fe19&is=69c4ac99&hm=833c3f7bf659c3c6309a481d8552b05b24e826fdd0c13880c536cefe6f8c0903&=&format=webp&quality=lossless&width=441&height=552",
            "Nivel 16": "https://media.discordapp.net/attachments/1475960551615103152/1485304911515095060/image.png?ex=69c5febe&is=69c4ad3e&hm=80976f41585d496f694714eadef0b5c503e9298eeb7a1454af99df7ffd49e9d8&=&format=webp&quality=lossless&width=454&height=576",
            "Nivel 17": "https://media.discordapp.net/attachments/1475960551615103152/1485305703978631364/image.png?ex=69c5ff7b&is=69c4adfb&hm=fb3ca4a8a1e0092c79ae9ff4960be4ea03d1df2762642d32fed96a315ab54516&=&format=webp&quality=lossless&width=466&height=565",
            "Nivel 18": "https://media.discordapp.net/attachments/1475960551615103152/1485306390930128997/image.png?ex=69c6001f&is=69c4ae9f&hm=042818c97671216bc9d7776166e680c136e6ef706b71253bf7666a8aa90eafe3&=&format=webp&quality=lossless&width=445&height=564",
            "Nivel 19": "https://media.discordapp.net/attachments/1475960551615103152/1485306828504957040/image.png?ex=69c60087&is=69c4af07&hm=2c84de2a0fe636f2f2d34d5e6906138befa4a486d0ffed1acdf9e3684ba5cd11&=&format=webp&quality=lossless&width=447&height=573",
            "Nivel 20": "https://media.discordapp.net/attachments/1475960551615103152/1485307306538438786/image.png?ex=69c600f9&is=69c4af79&hm=20edb56618f5424f877941b0d465c44daf82c7522d6686f74663ef8b86085ddc&=&format=webp&quality=lossless&width=447&height=568",
            "Nivel 21": "https://media.discordapp.net/attachments/1475960551615103152/1485307966428155945/image.png?ex=69c60196&is=69c4b016&hm=fc6713d0103372e541c3f1e860736558c80a8e2973ad1342ce557d083d90d457&=&format=webp&quality=lossless&width=453&height=563",
            "Nivel 22": "https://media.discordapp.net/attachments/1475960551615103152/1485309754124402930/image.png?ex=69c60341&is=69c4b1c1&hm=feb7e063cba4b3018a2dcf7c60df3b9051e06f66468d4d04e083cb7fdaa56465&=&format=webp&quality=lossless&width=453&height=562",
            "Nivel 23": "https://media.discordapp.net/attachments/1475960551615103152/1485310272032866414/image.png?ex=69c603bc&is=69c4b23c&hm=77f5bae6cbee344b8fc81881fd77ef93cb102459a592a241484d58fa418741f9&=&format=webp&quality=lossless&width=457&height=559",
            "Nivel 24": "https://media.discordapp.net/attachments/1475960551615103152/1485310565839798465/image.png?ex=69c60402&is=69c4b282&hm=7f80947d359054edb1574674dd3f52cd6b852df0c36e4d26229d4c918e85a7c1&=&format=webp&quality=lossless&width=456&height=564",
            "Nivel 25": "https://media.discordapp.net/attachments/1475960551615103152/1485332084510691388/image.png?ex=69c6180d&is=69c4c68d&hm=85763d520686d7ad63378b6d77f2ee5beb9e20723791586f0938712a79d98fdf&=&format=webp&quality=lossless&width=453&height=559",
            "Nivel 26": "https://media.discordapp.net/attachments/1475960551615103152/1485335721383563364/image.png?ex=69c61b70&is=69c4c9f0&hm=9028f7f5f8a1e828a4c77f50f2f2edd7b027d0d1e807c6b5ccbca660e1607125&=&format=webp&quality=lossless&width=444&height=545",
            "Nivel 27": "https://media.discordapp.net/attachments/1475960551615103152/1485338124916621512/image.png?ex=69c61dad&is=69c4cc2d&hm=38b971a8aa9f0d00d3bbdc08c29ee6601ec71e0eb1bcf2fa157ce192d4aab5f4&=&format=webp&quality=lossless&width=452&height=558",
            "Nivel 28": "https://media.discordapp.net/attachments/1475960551615103152/1485338891920609411/image.png?ex=69c61e64&is=69c4cce4&hm=27a4e8f39488317a7b280172f9d5b03d9e33ff957f839c636511110041d03219&=&format=webp&quality=lossless&width=453&height=562",
            "Nivel 29": "https://media.discordapp.net/attachments/1475960551615103152/1485339182812495883/image.png?ex=69c61ea9&is=69c4cd29&hm=4a3f07419e18a21f09f59c84b792ac75849df8ec787920e435ee73806e864229&=&format=webp&quality=lossless&width=453&height=560",
            "Nivel 30": "https://media.discordapp.net/attachments/1475960551615103152/1485341820157300888/image.png?ex=69c6211e&is=69c4cf9e&hm=fac899d635e664e3f95aa3458b6ce5289f2689dcab3981cc8eeec64ed99cb222&=&format=webp&quality=lossless&width=449&height=562",
            "Nivel 31": "https://media.discordapp.net/attachments/1475960551615103152/1485342569222246462/image.png?ex=69c621d0&is=69c4d050&hm=844f602b772fe9f6b7b69d7e1f3680f7f6043fba8d21a789eda12dd83c53464c&=&format=webp&quality=lossless&width=447&height=558",
            "Nivel 32": "https://media.discordapp.net/attachments/1475960551615103152/1485349182888874155/image.png?ex=69c627f9&is=69c4d679&hm=926dd6f8a62b082ec4c8c6ad63125ef8b181b9e22fd1f6914434d64282c4f455&=&format=webp&quality=lossless&width=449&height=565",
            "Nivel 33": "https://media.discordapp.net/attachments/1475960551615103152/1485349582845120597/image.png?ex=69c62859&is=69c4d6d9&hm=1357ed7a43b6b4ea841a0b3afa22f9e34a1c6aa5436aac23addae9b365b55d97&=&format=webp&quality=lossless&width=443&height=562",
            "Nivel 34": "https://media.discordapp.net/attachments/1475960551615103152/1485349834842968186/image.png?ex=69c62895&is=69c4d715&hm=958608d286ff009f2ac8f5c7d5d325c42075139d677d38d70c7350deba7ca5cc&=&format=webp&quality=lossless&width=445&height=564",
            "Nivel 35": "https://media.discordapp.net/attachments/1475960551615103152/1485350209251967017/image.png?ex=69c628ee&is=69c4d76e&hm=f0654cd094bf03db2bdaac40e5b5fa0099d960a32adce3f8f8b54ef122591329&=&format=webp&quality=lossless&width=441&height=559",
            "Nivel 36": "https://media.discordapp.net/attachments/1475960551615103152/1485350503922798724/image.png?ex=69c62934&is=69c4d7b4&hm=4f1645ce3701cfa395e5a7dbc9cadad701e1989aeaff935493fc35d7955ce8c0&=&format=webp&quality=lossless&width=459&height=565",
            "Nivel 37": "https://media.discordapp.net/attachments/1475960551615103152/1485389846297055263/image.png?ex=69c64dd8&is=69c4fc58&hm=5dd0316c2aeb2c4e8f524447075255fda02d23def66d9c53ea32d1f2d29e0dac&=&format=webp&quality=lossless&width=469&height=570",
            "Nivel 38": "https://media.discordapp.net/attachments/1475960551615103152/1485390392680517712/image.png?ex=69c64e5a&is=69c4fcda&hm=edc0a1e44aa0b342ba5fbfe5a837a602a0f44823dfa763fb0a88f57462394c86&=&format=webp&quality=lossless&width=455&height=563",
            "Nivel 39": "https://media.discordapp.net/attachments/1475960551615103152/1485390636676026418/image.png?ex=69c64e95&is=69c4fd15&hm=21ad53726d0a77b4c0b57e9b88fbe9ed7a5e51511e710ed5a8b22d96fa50f0cc&=&format=webp&quality=lossless&width=456&height=562"
        }

        if self.modo == "ECO":
            link_imagen = imagenes_eco[nivel_seleccionado]
            color_embed = discord.Color.green()
        else:
            link_imagen = imagenes_war[nivel_seleccionado]
            color_embed = discord.Color.red()

        embed = discord.Embed(
            title=f"📊 Build {self.modo} | {nivel_seleccionado}",
            description="Distribuye tus Hability Points exactamente así para optimizar tu personaje:",
            color=color_embed
        )
        embed.set_image(url=link_imagen)
        
        # Al editar la respuesta, mantiene la privacidad (sigue siendo solo para el usuario)
        await interaction.response.edit_message(embed=embed, view=None)

class VistaMenu(discord.ui.View):
    def __init__(self, modo):
        super().__init__(timeout=None)
        self.add_item(MenuNiveles(modo))

# --- BOTONES PRINCIPALES ---
class ModoJuegoBotones(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="MODO ECO", style=discord.ButtonStyle.success, custom_id="btn_eco")
    async def boton_eco(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="🌱 MODO ECO SELECCIONADO",
            description="Selecciona tu nivel exacto en el menú de abajo para ver tu build de farmeo:",
            color=discord.Color.green()
        )
        await interaction.response.edit_message(embed=embed, view=VistaMenu("ECO"))

    @discord.ui.button(label="MODO WAR", style=discord.ButtonStyle.danger, custom_id="btn_war")
    async def boton_war(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="🩸 MODO WAR SELECCIONADO",
            description="Selecciona tu nivel exacto en el menú de abajo para ver tu build de combate:",
            color=discord.Color.red()
        )
        await interaction.response.edit_message(embed=embed, view=VistaMenu("WAR"))

# --- COMANDO SLASH /BUILDS CON PRIVACIDAD ---
@bot.tree.command(name="builds", description="Muestra las guías de Hability Points (Solo tú lo verás)")
async def builds(interaction: discord.Interaction):
    embed = discord.Embed(
        title="🛠️ GUÍA DE BUILDS WAR ERA",
        description="¿Qué ruta deseas seguir hoy?\n\nSelecciona **ECO** (Verde) para priorizar economía o **WAR** (Rojo) para combate PvP.",
        color=discord.Color.blue()
    )
    # ephemeral=True hace que toda la interacción sea privada
    await interaction.response.send_message(embed=embed, view=ModoJuegoBotones(), ephemeral=True)

@bot.event
async def on_ready():
    print(f'Bot {bot.user} listo en Modo Fantasma (Niveles 15 al 39).')

mantener_vivo()
bot.run(TOKEN)



