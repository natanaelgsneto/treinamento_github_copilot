from pathlib import Path

from PIL import ImageGrab

pasta = Path(__file__).resolve().parent / "print"
pasta.mkdir(exist_ok=True)
destino = pasta / "tela.png"

ImageGrab.grab().save(destino)
print(f"Salvo em {destino}")
