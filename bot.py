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
            "Nivel 16": "https://dummyimage.com/600x400/2ecc71/ffffff&text=ECO+Lvl+16",
            "Nivel 17": "https://dummyimage.com/600x400/2ecc71/ffffff&text=ECO+Lvl+17",
            "Nivel 18": "https://dummyimage.com/600x400/2ecc71/ffffff&text=ECO+Lvl+18",
            "Nivel 19": "https://dummyimage.com/600x400/2ecc71/ffffff&text=ECO+Lvl+19",
            "Nivel 20": "https://dummyimage.com/600x400/2ecc71/ffffff&text=ECO+Lvl+20",
            "Nivel 21": "https://dummyimage.com/600x400/2ecc71/ffffff&text=ECO+Lvl+21",
            "Nivel 22": "https://dummyimage.com/600x400/2ecc71/ffffff&text=ECO+Lvl+22",
            "Nivel 23": "https://dummyimage.com/600x400/2ecc71/ffffff&text=ECO+Lvl+23",
            "Nivel 24": "https://dummyimage.com/600x400/2ecc71/ffffff&text=ECO+Lvl+24",
            "Nivel 25": "https://dummyimage.com/600x400/2ecc71/ffffff&text=ECO+Lvl+25",
            "Nivel 26": "https://dummyimage.com/600x400/2ecc71/ffffff&text=ECO+Lvl+26",
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
            "Nivel 16": "https://dummyimage.com/600x400/e74c3c/ffffff&text=WAR+Lvl+16",
            "Nivel 17": "https://dummyimage.com/600x400/e74c3c/ffffff&text=WAR+Lvl+17",
            "Nivel 18": "https://dummyimage.com/600x400/e74c3c/ffffff&text=WAR+Lvl+18",
            "Nivel 19": "https://dummyimage.com/600x400/e74c3c/ffffff&text=WAR+Lvl+19",
            "Nivel 20": "https://dummyimage.com/600x400/e74c3c/ffffff&text=WAR+Lvl+20",
            "Nivel 21": "https://dummyimage.com/600x400/e74c3c/ffffff&text=WAR+Lvl+21",
            "Nivel 22": "https://dummyimage.com/600x400/e74c3c/ffffff&text=WAR+Lvl+22",
            "Nivel 23": "https://dummyimage.com/600x400/e74c3c/ffffff&text=WAR+Lvl+23",
            "Nivel 24": "https://dummyimage.com/600x400/e74c3c/ffffff&text=WAR+Lvl+24",
            "Nivel 25": "https://dummyimage.com/600x400/e74c3c/ffffff&text=WAR+Lvl+25",
            "Nivel 26": "https://dummyimage.com/600x400/e74c3c/ffffff&text=WAR+Lvl+26",
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
