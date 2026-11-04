"""Captura a janela visível do navegador e salva em print/navegador.png."""

import ctypes
import time
from ctypes import wintypes
from pathlib import Path

from PIL import ImageGrab

user32 = ctypes.windll.user32
dwmapi = ctypes.windll.dwmapi

try:
    ctypes.windll.shcore.SetProcessDpiAwareness(2)
except Exception:
    user32.SetProcessDPIAware()

BROWSER_CLASSES = {
    "Chrome_WidgetWin_1",
    "MozillaWindowClass",
}
PREFERRED_TITLE = ("gerenciador", "localhost", "streamlit")
DWMWA_EXTENDED_FRAME_BOUNDS = 9
SW_RESTORE = 9


def window_text(hwnd: int) -> str:
    length = user32.GetWindowTextLengthW(hwnd)
    buffer = ctypes.create_unicode_buffer(length + 1)
    user32.GetWindowTextW(hwnd, buffer, length + 1)
    return buffer.value


def window_class(hwnd: int) -> str:
    buffer = ctypes.create_unicode_buffer(256)
    user32.GetClassNameW(hwnd, buffer, 256)
    return buffer.value


def window_bounds(hwnd: int) -> tuple[int, int, int, int]:
    rect = wintypes.RECT()
    dwmapi.DwmGetWindowAttribute(
        hwnd,
        DWMWA_EXTENDED_FRAME_BOUNDS,
        ctypes.byref(rect),
        ctypes.sizeof(rect),
    )
    return rect.left, rect.top, rect.right, rect.bottom


def find_browser() -> int:
    found: list[int] = []

    @ctypes.WINFUNCTYPE(ctypes.c_bool, wintypes.HWND, wintypes.LPARAM)
    def callback(hwnd, _lparam):
        if not user32.IsWindowVisible(hwnd) or user32.IsIconic(hwnd):
            return True
        if window_class(hwnd) not in BROWSER_CLASSES or not window_text(hwnd):
            return True
        found.append(hwnd)
        return True

    user32.EnumWindows(callback, 0)
    if not found:
        raise RuntimeError("Nenhuma janela de navegador visível foi encontrada.")

    def rank(hwnd: int) -> tuple[int, int]:
        title = window_text(hwnd).casefold()
        preferred = 0 if any(part in title for part in PREFERRED_TITLE) else 1
        left, top, right, bottom = window_bounds(hwnd)
        area = (right - left) * (bottom - top)
        return preferred, -area

    return sorted(found, key=rank)[0]


def main() -> None:
    hwnd = find_browser()
    user32.ShowWindow(hwnd, SW_RESTORE)
    user32.SetForegroundWindow(hwnd)
    time.sleep(0.4)

    pasta = Path(__file__).resolve().parent / "print"
    pasta.mkdir(exist_ok=True)
    destino = pasta / "navegador.png"

    ImageGrab.grab(bbox=window_bounds(hwnd)).save(destino)
    print(f"Salvo em {destino} ({window_text(hwnd)})")


if __name__ == "__main__":
    main()
