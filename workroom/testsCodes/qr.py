import pyqrcode
from pyqrcode import QRCode
# Enter information to be encoded
packet = """My poem website: https://qswalker.trinket.io/sites/quira-s-poems
            My Python Discord Server: https://discord.gg/hu8nvWtTBs
            My GitHub Repository: https://github.com/Quiras-DisHub/Github4Discord
            """
#         ^^^  
pack = pyqrcode.create(packet)
# Enter Title of QR code
pack.svg("Quira's Links", scale = 8)
#         ^^^