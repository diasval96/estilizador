from .detector import ATIVO, TRUE_COLOR

# Cores Padrões e Brilhantes
preto        = "\033[30m" if ATIVO else ""
vermelho     = "\033[31m" if ATIVO else ""
verde        = "\033[32m" if ATIVO else ""
amarelo      = "\033[33m" if ATIVO else ""
azul         = "\033[34m" if ATIVO else ""
magenta      = "\033[35m" if ATIVO else ""
ciano        = "\033[36m" if ATIVO else ""
branco       = "\033[37m" if ATIVO else ""
cinza        = "\033[90m" if ATIVO else ""
azul_claro   = "\033[94m" if ATIVO else ""
rosa         = "\033[95m" if ATIVO else ""  

# Escala Estendida (256 Cores)
dourado      = "\033[38;5;220m" if ATIVO else "" 
laranja      = "\033[38;5;208m" if ATIVO else ""
roxo         = "\033[38;5;129m" if ATIVO else ""
turquesa     = "\033[38;5;45m" if ATIVO else ""

def rgb(r, g, b):
    """Gera uma cor de texto customizada usando a escala RGB (24-bit True Color) com proteção."""
    return f"\033[38;2;{r};{g};{b}m" if TRUE_COLOR else ""

def hex(codigo):
    """Gera uma cor de texto customizada a partir de um código Hexadecimal (ex: #FF55FF) com proteção."""
    if not TRUE_COLOR: 
        return ""
    codigo = codigo.lstrip('#')
    r, g, b = tuple(int(codigo[i:i+2], 16) for i in (0, 2, 4))
    return f"\033[38;2;{r};{g};{b}m"

