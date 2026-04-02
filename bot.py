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
            "Nivel 15": "https://media.discordapp.net/attachments/1475960551615103152/1489266212947890368/image.png?ex=69cfcabe&is=69ce793e&hm=ddafbaf8e64b0478ee64ff5efca6a4759574fcc023cba40af6eb2db2ef09ddf2&=&format=webp&quality=lossless&width=457&height=571",
            "Nivel 16": "https://media.discordapp.net/attachments/1475960551615103152/1489267362757869609/image.png?ex=69cfcbd0&is=69ce7a50&hm=f9dbc976128f9e9d9ac226147fe3c1ac8c8a351597893f3e6777440f223dda82&=&format=webp&quality=lossless&width=445&height=559",
            "Nivel 17": "https://media.discordapp.net/attachments/1475960551615103152/1489267917815156967/image.png?ex=69cfcc54&is=69ce7ad4&hm=2208dc541c6ba663f23dbe45a755821e6ef1bd82400627e4858fced178364232&=&format=webp&quality=lossless&width=455&height=569",
            "Nivel 18": "https://media.discordapp.net/attachments/1475960551615103152/1489268378274107472/image.png?ex=69cfccc2&is=69ce7b42&hm=20e402bde53ab8c175c7139880d9c31ab94150f27ce17b2a34b510107db9f1a4&=&format=webp&quality=lossless&width=445&height=573",
            "Nivel 19": "https://media.discordapp.net/attachments/1475960551615103152/1489268887857135798/image.png?ex=69cfcd3c&is=69ce7bbc&hm=6e4de3b579d56b0085f38781b87a31d9d3e3a2d68302f7b55ed1fb85d31210be&=&format=webp&quality=lossless&width=450&height=568",
            "Nivel 20": "https://media.discordapp.net/attachments/1475960551615103152/1489269392649752626/image.png?ex=69cfcdb4&is=69ce7c34&hm=67b006fa422dd119f7be2023135588f8fa94448473b4057362982e44800802cc&=&format=webp&quality=lossless&width=457&height=565",
            "Nivel 21": "https://media.discordapp.net/attachments/1475960551615103152/1489269731574681630/image.png?ex=69cfce05&is=69ce7c85&hm=3f6e14ad9356595f9825fe488f80d836be5c5d43b76a8414dcbb4d9f30e4d315&=&format=webp&quality=lossless&width=458&height=572",
            "Nivel 22": "https://media.discordapp.net/attachments/1475960551615103152/1489270077340516516/image.png?ex=69cfce57&is=69ce7cd7&hm=c002a7883a2e2305cb252e44d859ead3e33a30370a23f81c2343551247d9bdf2&=&format=webp&quality=lossless&width=448&height=566",
            "Nivel 23": "https://media.discordapp.net/attachments/1475960551615103152/1489270272950407228/image.png?ex=69cfce86&is=69ce7d06&hm=d3b47e27963f47653dddec65c573d195d489b0afa837b7d9eebbfb6ae849dff6&=&format=webp&quality=lossless&width=445&height=564",
            "Nivel 24": "https://media.discordapp.net/attachments/1475960551615103152/1489270422116630578/image.png?ex=69cfcea9&is=69ce7d29&hm=feb4ed89a7073b554ebcd22b187525d18c4f9ef8b127492b20529c0915509c22&=&format=webp&quality=lossless&width=453&height=545",
            "Nivel 25": "https://media.discordapp.net/attachments/1475960551615103152/1489270601041445074/image.png?ex=69cfced4&is=69ce7d54&hm=4a6dff4cfb1ea78c6935f738c268a305e608b10c6d79a6b78f34c6d36273bc9d&=&format=webp&quality=lossless&width=454&height=562",
            "Nivel 26": "https://media.discordapp.net/attachments/1475960551615103152/1489271016365621258/image.png?ex=69cfcf37&is=69ce7db7&hm=c5e51f04b8ad708857d9a6b946ca342ce0ce756d5ff7933458ef0bd300c55d39&=&format=webp&quality=lossless&width=454&height=565",
            "Nivel 27": "https://media.discordapp.net/attachments/1475960551615103152/1489271458768224296/image.png?ex=69cfcfa1&is=69ce7e21&hm=3490cbd9bc00eff1dca2f23f74c06d57cce94f9862324832c52caa3e4cf60cd6&=&format=webp&quality=lossless&width=454&height=560",
            "Nivel 28": "https://media.discordapp.net/attachments/1475960551615103152/1489273157973184563/image.png?ex=69cfd136&is=69ce7fb6&hm=c35b7c396cf1ff7bf56745630568bc86e3ab33a579a1525a6f2edd12c96eca72&=&format=webp&quality=lossless&width=448&height=559",
            "Nivel 29": "https://media.discordapp.net/attachments/1475960551615103152/1489273422423789671/image.png?ex=69cfd175&is=69ce7ff5&hm=0498115ab5b482cb14563d589fb6e8da389a1b058e5703872ab36dc88ea6b5a5&=&format=webp&quality=lossless&width=445&height=562",
            "Nivel 30": "https://media.discordapp.net/attachments/1475960551615103152/1489273549775441981/image.png?ex=69cfd193&is=69ce8013&hm=e6edcceefbc9fabb3c4ae711a9c2fc750b26c5952bbf5cadfd255785dfade821&=&format=webp&quality=lossless&width=454&height=559",
            "Nivel 31": "https://media.discordapp.net/attachments/1475960551615103152/1489273709075370094/image.png?ex=69cfd1b9&is=69ce8039&hm=5d5846eb208c0f42a641916ac0406bc6bb3fe7d4fd7cec0c92aa82020e979d7b&=&format=webp&quality=lossless&width=454&height=548",
            "Nivel 32": "https://media.discordapp.net/attachments/1475960551615103152/1489273947940716635/image.png?ex=69cfd1f2&is=69ce8072&hm=8b86e4a5e109163f60be796fa753888ae32014cd56fa2a3a7fb47be6fa1f09a3&=&format=webp&quality=lossless&width=451&height=558",
            "Nivel 33": "https://media.discordapp.net/attachments/1475960551615103152/1489275327682445402/image.png?ex=69cfd33b&is=69ce81bb&hm=efdba388613766303629a0f7e0a698a60742e3056b2266c655d23e5f46c824f8&=&format=webp&quality=lossless&width=455&height=567",
            "Nivel 34": "https://media.discordapp.net/attachments/1475960551615103152/1489275548382396506/image.png?ex=69cfd370&is=69ce81f0&hm=30f144a9083a692cb2e6d3a8875c0d0830d3d8cfa17915107135d62e3f11aa9e&=&format=webp&quality=lossless&width=449&height=552",
            "Nivel 35": "https://media.discordapp.net/attachments/1475960551615103152/1489275702774857941/image.png?ex=69cfd394&is=69ce8214&hm=490918c8887630a2606ae2e2f6c5bda3e515fe629f7656393ed8ed47f4212816&=&format=webp&quality=lossless&width=450&height=567",
            "Nivel 36": "https://media.discordapp.net/attachments/1475960551615103152/1489275864083464394/image.png?ex=69cfd3bb&is=69ce823b&hm=25cfa59b43087c4264951668f308a413b3619f283348466c1a610cf936db7a3c&=&format=webp&quality=lossless&width=445&height=559",
            "Nivel 37": "https://media.discordapp.net/attachments/1475960551615103152/1489276060217643242/image.png?ex=69cfd3ea&is=69ce826a&hm=2710129902bc175581d2d59b60f73d240f782d54321c3b91b4e2e43e2b7366cd&=&format=webp&quality=lossless&width=453&height=553",
            "Nivel 38": "https://media.discordapp.net/attachments/1475960551615103152/1489277273860341760/image.png?ex=69cfd50b&is=69ce838b&hm=5532e2aa6fea09b632eba199dd58279098e3459596a0ddc8ad540ca2de64c17b&=&format=webp&quality=lossless&width=444&height=546",
            "Nivel 39": "https://media.discordapp.net/attachments/1475960551615103152/1489277391841923234/image.png?ex=69cfd527&is=69ce83a7&hm=e8771df3b77dc71e9e2038158c8ed01e3530d159578abaf97b51758253d0f3f8&=&format=webp&quality=lossless&width=445&height=556"
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



