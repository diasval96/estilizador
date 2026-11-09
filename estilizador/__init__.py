from . import ct
from . import cf
from . import ft
from . import msg
from . import barr

# Exposição direta do reset global para conveniência
reset = ft.reset

def misturar(texto, cor_texto="", cor_fundo="", estilo=""):
    """Imprime um texto combinando múltiplos estilos e aplica o reset automático no final."""
    print(f"{estilo}{cor_fundo}{cor_texto}{texto}{reset}")

def titulo(texto, largura=40, cor_borda=ct.cinza, cor_titulo=ct.dourado, estilo_borda="="):
    """Gera um cabeçalho sistêmico responsivo e centralizado no terminal."""
    borda = estilo_borda * largura
    texto_centralizado = texto.center(largura)
    print(f"{cor_borda}{borda}{reset}")
    print(f"{ft.negrito}{cor_titulo}{texto_centralizado}{reset}")
    print(f"{cor_borda}{borda}{reset}")
