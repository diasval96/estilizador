import sys
import os

def verificar_suporte():
    """Detecta universalmente se o terminal suporta as formatações ANSI básicas"""
    if not sys.stdout.isatty():
        return False
    if "NO_COLOR" in os.environ:
        return False
    if "idlelib" in sys.modules:
        return False
        
    term = os.environ.get("TERM", "").lower()
    if any(t in term for t in ["xterm", "screen", "vt100", "linux", "color", "ansi"]):
        return True
        
    if os.name == "nt" and os.environ.get("WT_SESSION"):
        return True
        
    if "com.termux" in os.environ.get("PREFIX", ""):
        return True
        
    return False

def verificar_true_color():
    """Detecta se o terminal suporta a escala estendida de 16 milhões de cores Hex/RGB"""
    if not verificar_suporte():
        return False
    if os.environ.get("COLORTERM", "").lower() in ["truecolor", "24bit"]:
        return True
    if "com.termux" in os.environ.get("PREFIX", ""):
        return True
    return False

# Chaves de ativação globais do motor
ATIVO = verificar_suporte()
TRUE_COLOR = verificar_true_color()

