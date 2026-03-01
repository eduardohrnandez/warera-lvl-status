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
            "Nivel 27": "https://media.discordapp.net/attachments/1475960551615103152/1476704677432394003/IMG-20260226-WA0022.jpg?ex=69a563a6&is=69a41226&hm=e925dc045d82a9f3caab981a202bb367d8de9159edda4923b3310d7f5109919f&=&format=webp&width=607&height=691",
            "Nivel 28": "https://media.discordapp.net/attachments/1475960551615103152/1476705349200511070/IMG-20260226-WA0026.jpg?ex=69a56447&is=69a412c7&hm=7ce7ebb415c89e2e316477dae41b793df2646afacb44384c6617e09ecdaa6ac1&=&format=webp&width=601&height=693",
            "Nivel 29": "https://media.discordapp.net/attachments/1475960551615103152/1476707827945836574/IMG-20260226-WA0030.jpg?ex=69a56696&is=69a41516&hm=9ec300d568e555720e004e4a11071a72680054e9ddb1a11505a37b81f6088e66&=&format=webp&width=633&height=658",
            "Nivel 30": "https://media.discordapp.net/attachments/1475960551615103152/1476708758834118730/IMG-20260226-WA0033.jpg?ex=69a56774&is=69a415f4&hm=5c197e5e534bc95576ace4dfd444b33ebd1324e366e8ae68ef5d030ab230efbb&=&format=webp&width=607&height=652",
            "Nivel 31": "https://media.discordapp.net/attachments/1475960551615103152/1476710085995528504/IMG-20260226-WA0034.jpg?ex=69a568b0&is=69a41730&hm=03570e4679bf84119a547c5dd625648c5a5c3c09f48fec0a4d27d01939288a14&=&format=webp&width=610&height=643",
            "Nivel 32": "https://media.discordapp.net/attachments/1475960551615103152/1476711032687951942/IMG-20260226-WA0037.jpg?ex=69a56992&is=69a41812&hm=aafe7f67a71a4b5b0e09ed4179cd9c2a429b5b64b564168b04744eb2fb1ec71b&=&format=webp&width=613&height=677",
            "Nivel 33": "https://media.discordapp.net/attachments/1475960551615103152/1476711839420121241/IMG-20260226-WA0038.jpg?ex=69a56a52&is=69a418d2&hm=ff0b23fe2d1e852b24cdccfabe2c12e0cde9fc07705a0c005d56ca2f64fd5b89&=&format=webp&width=604&height=645",
            "Nivel 34": "https://media.discordapp.net/attachments/1475960551615103152/1477428412145602743/IMG-20260228-WA0028.jpg?ex=69a562ae&is=69a4112e&hm=f271451d9fb865caac58e6c7d787d981058db135a542ea1585a710c2d91ab06d&=&format=webp&width=600&height=652",
            "Nivel 35": "https://media.discordapp.net/attachments/1475960551615103152/1477429019048939580/IMG-20260228-WA0031.jpg?ex=69a5633f&is=69a411bf&hm=aa54cba074e5673923121022b71c3d1ca7a702b253f28f786644b9f1ed8c2d8e&=&format=webp&width=625&height=641",
            "Nivel 36": "https://media.discordapp.net/attachments/1475960551615103152/1477429835931320431/IMG-20260228-WA0032.jpg?ex=69a56402&is=69a41282&hm=9cd59e41a002e336e12d2062c0ffe8142bfb740956603db5addf8cc535f5fc9e&=&format=webp&width=614&height=651",
            "Nivel 37": "https://media.discordapp.net/attachments/1475960551615103152/1477432165481320538/IMG-20260228-WA0035.jpg?ex=69a5662d&is=69a414ad&hm=f2ab8c8dc700179760336d39481f99b3849443926aa3823a29d62be1d30cf7f0&=&format=webp&width=595&height=634",
            "Nivel 38": "https://media.discordapp.net/attachments/1475960551615103152/1477434628095869092/IMG-20260228-WA0036.jpg?ex=69a56878&is=69a416f8&hm=e6e31ce2d26c8949ec01b9558f7fe379644078d81644142b4164ee1d7f48e9ae&=&format=webp&width=625&height=698",
            "Nivel 39": "https://media.discordapp.net/attachments/1475960551615103152/1477435760922853437/IMG-20260228-WA0040.jpg?ex=69a56986&is=69a41806&hm=c49a085ce17f52e8d944b66d11bcbae3c80e593673fa3e8f3308c8f663b7808e&=&format=webp&width=609&height=691"
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



