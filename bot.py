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
            "Nivel 27": "https://dummyimage.com/600x400/2ecc71/ffffff&text=ECO+Lvl+27",
            "Nivel 28": "https://dummyimage.com/600x400/2ecc71/ffffff&text=ECO+Lvl+28",
            "Nivel 29": "https://dummyimage.com/600x400/2ecc71/ffffff&text=ECO+Lvl+29",
            "Nivel 30": "https://dummyimage.com/600x400/2ecc71/ffffff&text=ECO+Lvl+30",
            "Nivel 31": "https://dummyimage.com/600x400/2ecc71/ffffff&text=ECO+Lvl+31",
            "Nivel 32": "https://dummyimage.com/600x400/2ecc71/ffffff&text=ECO+Lvl+32",
            "Nivel 33": "https://dummyimage.com/600x400/2ecc71/ffffff&text=ECO+Lvl+33",
            "Nivel 34": "https://dummyimage.com/600x400/2ecc71/ffffff&text=ECO+Lvl+34",
            "Nivel 35": "https://dummyimage.com/600x400/2ecc71/ffffff&text=ECO+Lvl+35",
            "Nivel 36": "https://dummyimage.com/600x400/2ecc71/ffffff&text=ECO+Lvl+36",
            "Nivel 37": "https://dummyimage.com/600x400/2ecc71/ffffff&text=ECO+Lvl+37",
            "Nivel 38": "https://dummyimage.com/600x400/2ecc71/ffffff&text=ECO+Lvl+38",
            "Nivel 39": "https://dummyimage.com/600x400/2ecc71/ffffff&text=ECO+Lvl+39"
        }
        
        # --- CAJA DE IMÁGENES MODO WAR ---
        imagenes_war = {
            "Nivel 15": "https://media.discordapp.net/attachments/1475960551615103152/1475960672591544410/IMG-20260224-WA0012.jpg?ex=699f62fe&is=699e117e&hm=ef095336140cf0116410bcfe6a45eaf4351e060a81567fc2c0b1e23e1dc9c439&=&format=webp&width=601&height=642",
            "Nivel 16": "https://media.discordapp.net/attachments/1475960551615103152/1475960723485102232/IMG-20260224-WA0011.jpg?ex=699f630a&is=699e118a&hm=b3d6d2ec8af7c6ede8b99927420f94c8fcb8df7450e02eb969caa90ba1e44b3d&=&format=webp&width=589&height=644",
            "Nivel 17": "https://media.discordapp.net/attachments/1475960551615103152/1475961696098189463/IMG-20260224-WA0013.jpg?ex=699f63f2&is=699e1272&hm=0e68a5ece27f2f6559cc5d257911c85401316545d4c98ad70ff3d47a74956a8d&=&format=webp&width=609&height=641",
            "Nivel 18": "https://media.discordapp.net/attachments/1475960551615103152/1475962295031955466/IMG-20260224-WA0016.jpg?ex=699f6481&is=699e1301&hm=a8c08d60542e56757346c8c23358144c3b2886871ae8712c926addcb0d316fa9&=&format=webp&width=612&height=646",
            "Nivel 19": "https://media.discordapp.net/attachments/1475960551615103152/1475963870899212371/IMG-20260224-WA0017.jpg?ex=699f65f8&is=699e1478&hm=a193420e7d7f3ede140e6b1e3d6cb04b4f6abe903d93329102bd29f582f70657&=&format=webp&width=602&height=645",
            "Nivel 20": "https://media.discordapp.net/attachments/1475960551615103152/1475966402480312481/IMG-20260224-WA0020.jpg?ex=699f6854&is=699e16d4&hm=6180bd2bcf28199d6f698eb020658d28361581f4eb632a95e7c44ccb903ad4b4&=&format=webp&width=604&height=645",
            "Nivel 21": "https://media.discordapp.net/attachments/1475960551615103152/1475970172836778187/IMG-20260224-WA0021.jpg?ex=699f6bd7&is=699e1a57&hm=f921066a73cebd1dc223d3125d2ac9c50560144e7b431dc778dbd3236aee3969&=&format=webp&width=606&height=646",
            "Nivel 22": "https://media.discordapp.net/attachments/1475960551615103152/1475975979733221438/IMG-20260224-WA0023.jpg?ex=699f713f&is=699e1fbf&hm=b20268714abd197a29a52ecef6ad96aa4ba225518d6369b05ce89db50916cf26&=&format=webp&width=610&height=651",
            "Nivel 23": "https://media.discordapp.net/attachments/1475960551615103152/1475978734086656111/IMG-20260224-WA0026.jpg?ex=699f73d0&is=699e2250&hm=6538aa8a36ff5bfba30cbdec6d86ad04b58e3d7d3fc22b47f2805602ce3c89d6&=&format=webp&width=608&height=646",
            "Nivel 24": "https://media.discordapp.net/attachments/1475960551615103152/1475979841366134917/IMG-20260224-WA0027.jpg?ex=699f74d8&is=699e2358&hm=ad1f5886c7655d53e0fbd6b88f30d0a5e9bab3d48e02c82ebf5fabd28a8b5158&=&format=webp&width=598&height=648",
            "Nivel 25": "https://media.discordapp.net/attachments/1475960551615103152/1476280137023623329/IMG-20260225-WA0017.jpg?ex=69a13544&is=699fe3c4&hm=73c7851023e8fca4e150656c0932104eafa978d23a19ca5437312c1b791d369f&=&format=webp&width=606&height=661",
            "Nivel 26": "https://media.discordapp.net/attachments/1475960551615103152/1476281255023611965/IMG-20260225-WA0018.jpg?ex=69a1364f&is=699fe4cf&hm=fd2ef327a7994857873e15f43f56724abe58b384451eaa1a01707051ea3e3d2e&=&format=webp&width=607&height=643",
            "Nivel 27": "https://dummyimage.com/600x400/e74c3c/ffffff&text=WAR+Lvl+27",
            "Nivel 28": "https://dummyimage.com/600x400/e74c3c/ffffff&text=WAR+Lvl+28",
            "Nivel 29": "https://dummyimage.com/600x400/e74c3c/ffffff&text=WAR+Lvl+29",
            "Nivel 30": "https://dummyimage.com/600x400/e74c3c/ffffff&text=WAR+Lvl+30",
            "Nivel 31": "https://dummyimage.com/600x400/e74c3c/ffffff&text=WAR+Lvl+31",
            "Nivel 32": "https://dummyimage.com/600x400/e74c3c/ffffff&text=WAR+Lvl+32",
            "Nivel 33": "https://dummyimage.com/600x400/e74c3c/ffffff&text=WAR+Lvl+33",
            "Nivel 34": "https://dummyimage.com/600x400/e74c3c/ffffff&text=WAR+Lvl+34",
            "Nivel 35": "https://dummyimage.com/600x400/e74c3c/ffffff&text=WAR+Lvl+35",
            "Nivel 36": "https://dummyimage.com/600x400/e74c3c/ffffff&text=WAR+Lvl+36",
            "Nivel 37": "https://dummyimage.com/600x400/e74c3c/ffffff&text=WAR+Lvl+37",
            "Nivel 38": "https://dummyimage.com/600x400/e74c3c/ffffff&text=WAR+Lvl+38",
            "Nivel 39": "https://dummyimage.com/600x400/e74c3c/ffffff&text=WAR+Lvl+39"
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


