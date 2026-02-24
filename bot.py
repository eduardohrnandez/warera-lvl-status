import discord
from discord.ext import commands
from flask import Flask
from threading import Thread
import os

# --- SERVIDOR WEB (Para Render) ---
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

# --- MENÚ DESPLEGABLE (Niveles 16 al 30) ---
class MenuNiveles(discord.ui.Select):
    def __init__(self, modo):
        self.modo = modo
        
        # Generamos las 15 opciones automáticamente (del 16 al 30)
        opciones = []
        emoji_usar = "🌱" if modo == "ECO" else "🩸"
        
        for i in range(16, 31):
            opciones.append(discord.SelectOption(label=f"Nivel {i}", emoji=emoji_usar))
            
        super().__init__(placeholder=f"Selecciona tu Nivel ({modo})...", min_values=1, max_values=1, options=opciones)

    async def callback(self, interaction: discord.Interaction):
        nivel_seleccionado = self.values[0] # Ejemplo: "Nivel 16"
        
        # --- CAJA DE IMÁGENES MODO ECO ---
        imagenes_eco = {
            "Nivel 16": "https://dummyimage.com/600x400/2ecc71/ffffff&text=Build+ECO+Lvl+16",
            "Nivel 17": "https://dummyimage.com/600x400/2ecc71/ffffff&text=Build+ECO+Lvl+17",
            "Nivel 18": "https://dummyimage.com/600x400/2ecc71/ffffff&text=Build+ECO+Lvl+18",
            "Nivel 19": "https://dummyimage.com/600x400/2ecc71/ffffff&text=Build+ECO+Lvl+19",
            "Nivel 20": "https://dummyimage.com/600x400/2ecc71/ffffff&text=Build+ECO+Lvl+20",
            "Nivel 21": "https://dummyimage.com/600x400/2ecc71/ffffff&text=Build+ECO+Lvl+21",
            "Nivel 22": "https://dummyimage.com/600x400/2ecc71/ffffff&text=Build+ECO+Lvl+22",
            "Nivel 23": "https://dummyimage.com/600x400/2ecc71/ffffff&text=Build+ECO+Lvl+23",
            "Nivel 24": "https://dummyimage.com/600x400/2ecc71/ffffff&text=Build+ECO+Lvl+24",
            "Nivel 25": "https://dummyimage.com/600x400/2ecc71/ffffff&text=Build+ECO+Lvl+25",
            "Nivel 26": "https://dummyimage.com/600x400/2ecc71/ffffff&text=Build+ECO+Lvl+26",
            "Nivel 27": "https://dummyimage.com/600x400/2ecc71/ffffff&text=Build+ECO+Lvl+27",
            "Nivel 28": "https://dummyimage.com/600x400/2ecc71/ffffff&text=Build+ECO+Lvl+28",
            "Nivel 29": "https://dummyimage.com/600x400/2ecc71/ffffff&text=Build+ECO+Lvl+29",
            "Nivel 30": "https://dummyimage.com/600x400/2ecc71/ffffff&text=Build+ECO+Lvl+30"
        }
        
        # --- CAJA DE IMÁGENES MODO WAR ---
        imagenes_war = {
            "Nivel 16": "https://dummyimage.com/600x400/e74c3c/ffffff&text=Build+WAR+Lvl+16",
            "Nivel 17": "https://dummyimage.com/600x400/e74c3c/ffffff&text=Build+WAR+Lvl+17",
            "Nivel 18": "https://dummyimage.com/600x400/e74c3c/ffffff&text=Build+WAR+Lvl+18",
            "Nivel 19": "https://dummyimage.com/600x400/e74c3c/ffffff&text=Build+WAR+Lvl+19",
            "Nivel 20": "https://dummyimage.com/600x400/e74c3c/ffffff&text=Build+WAR+Lvl+20",
            "Nivel 21": "https://dummyimage.com/600x400/e74c3c/ffffff&text=Build+WAR+Lvl+21",
            "Nivel 22": "https://dummyimage.com/600x400/e74c3c/ffffff&text=Build+WAR+Lvl+22",
            "Nivel 23": "https://dummyimage.com/600x400/e74c3c/ffffff&text=Build+WAR+Lvl+23",
            "Nivel 24": "https://dummyimage.com/600x400/e74c3c/ffffff&text=Build+WAR+Lvl+24",
            "Nivel 25": "https://dummyimage.com/600x400/e74c3c/ffffff&text=Build+WAR+Lvl+25",
            "Nivel 26": "https://dummyimage.com/600x400/e74c3c/ffffff&text=Build+WAR+Lvl+26",
            "Nivel 27": "https://dummyimage.com/600x400/e74c3c/ffffff&text=Build+WAR+Lvl+27",
            "Nivel 28": "https://dummyimage.com/600x400/e74c3c/ffffff&text=Build+WAR+Lvl+28",
            "Nivel 29": "https://dummyimage.com/600x400/e74c3c/ffffff&text=Build+WAR+Lvl+29",
            "Nivel 30": "https://dummyimage.com/600x400/e74c3c/ffffff&text=Build+WAR+Lvl+30"
        }

        # Elegimos el color y la imagen dependiendo del botón que tocaron
        if self.modo == "ECO":
            link_imagen = imagenes_eco[nivel_seleccionado]
            color_embed = discord.Color.green()
        else:
            link_imagen = imagenes_war[nivel_seleccionado]
            color_embed = discord.Color.red()

        # Armamos el cuadro de respuesta
        embed = discord.Embed(
            title=f"📊 Build {self.modo} | {nivel_seleccionado}",
            description="Distribuye tus Hability Points exactamente así para optimizar tu personaje:",
            color=color_embed
        )
        embed.set_image(url=link_imagen)
        
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

# --- COMANDO SLASH /BUILDS ---
@bot.tree.command(name="builds", description="Muestra las guías de Hability Points según tu modo de juego")
async def builds(interaction: discord.Interaction):
    embed = discord.Embed(
        title="🛠️ GUÍA DE BUILDS WAR ERA",
        description="¿Qué ruta deseas seguir hoy?\n\nSelecciona **ECO** (Verde) para priorizar economía o **WAR** (Rojo) para combate PvP.",
        color=discord.Color.blue()
    )
    await interaction.response.send_message(embed=embed, view=ModoJuegoBotones())

@bot.event
async def on_ready():
    print(f'Bot {bot.user} listo para mostrar builds del 16 al 30.')

mantener_vivo()
bot.run(TOKEN)