from . import ct
from . import cf
from .ft import negrito, sublinhado, reset

# --- CATEGORIA A: Padrão (Texto Inteiro Colorido) ---
def sucesso_padrao(mensagem):
    print(f"{negrito}{ct.verde}✓ SUCESSO: {mensagem}{reset}")

def erro_padrao(mensagem):
    print(f"{negrito}{ct.vermelho}✗ ERRO: {mensagem}{reset}")

def aviso_padrao(mensagem):
    print(f"{negrito}{ct.amarelo}⚠ AVISO: {mensagem}{reset}")

def info_padrao(mensagem):
    print(f"{negrito}{ct.azul_claro}ℹ INFO: {mensagem}{reset}")

# --- CATEGORIA B: Clean (Indicador Colorido + Texto Branco) ---
def sucesso_clean(mensagem):
    print(f"{negrito}{ct.verde}[ OK ]{reset} {ct.branco}{mensagem}{reset}")

def erro_clean(mensagem):
    print(f"{negrito}{ct.vermelho}[FAIL]{reset} {ct.branco}{mensagem}{reset}")

def aviso_clean(mensagem):
    print(f"{negrito}{ct.amarelo}[WARN]{reset} {ct.branco}{mensagem}{reset}")

def info_clean(mensagem):
    print(f"{negrito}{ct.azul_claro}[INFO]{reset} {ct.branco}{mensagem}{reset}")

# --- CATEGORIA C: Bloco (Banners com Fundo Invertido) ---
def sucesso_bloco(mensagem):
    print(f"{negrito}{ct.preto}{cf.verde} SUCESSO {reset} {mensagem}")

def erro_bloco(mensagem):
    print(f"{negrito}{ct.branco}{cf.vermelho} ERRO    {reset} {mensagem}")

def aviso_bloco(mensagem):
    print(f"{negrito}{ct.preto}{cf.amarelo} AVISO   {reset} {mensagem}")

def info_bloco(mensagem):
    print(f"{negrito}{ct.branco}{cf.azul} INFO    {reset} {mensagem}")

# --- ALERTAS MÁXIMOS ---
def critico(mensagem):
    print(f"{negrito}{ct.vermelho}[CRÍTICO]{reset} {sublinhado}{ct.vermelho}{mensagem}{reset}")

def fatal(mensagem):
    print(f"{negrito}{ct.preto}{cf.vermelho} FATAL {reset} {negrito}{ct.vermelho} {mensagem}{reset}")

