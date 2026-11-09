import sys
import time
from . import ct
from . import ft
from .detector import ATIVO

# --- 1. ANIMAÇÕES DE CARREGAMENTO ROTATIVAS ---

def carregar(texto="Processando", duracao=1.5, estilo="padrao"):
    """Exibe um ícone giratório animado na mesma linha por um tempo determinado."""
    if not ATIVO:
        print(f"{texto}...")
        time.sleep(duracao)
        return
        
    # Frames de animação modernos
    frames_dict = {
        "padrao": ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"],
        "setas":  ["➔", "➔", "➔", "➔"], # Simula pulsação de movimento
        "blocos": [" ", "▃", "▄", "▅", "▆", "▇", "█", "▇", "▆", "▅", "▄", "▃"]
    }
    
    frames = frames_dict.get(estilo, frames_dict["padrao"])
    fim = time.time() + duracao
    i = 0
    
    # Loop de animação temporizado
    while time.time() < fim:
        sys.stdout.write(f"\r{ct.azul_claro}{frames[i % len(frames)]}{ft.reset} {texto}...")
        sys.stdout.flush()
        time.sleep(0.08)
        i += 1
    # Limpa a linha de forma invisível ao terminar
    sys.stdout.write("\r" + " " * (len(texto) + 20) + "\r")


# --- 2. BARRAS DE PROGRESSO GEOMÉTRICAS E MODERNAS ---

def progresso(passo, total_passos, estilo="blocos", cor_barra=ct.verde, texto=""):
    """Renderiza barras de progresso avançadas atualizadas passo a passo."""
    percentual = int((passo / total_passos) * 100)
    largura_barra = 20 # Comprimento visual da barra no terminal
    
    # Se o terminal não tiver suporte ANSI, exibe apenas a saída em formato limpo
    if not ATIVO:
        if passo == total_passos:
            print(f"{texto} {percentual}% Concluído.")
        return

    # Mapeamento de designs geométricos modernos para as barras
    if estilo == "blocos":
        # Blocos cheios de alta densidade
        preenchido = int(passo / total_passos * largura_barra)
        barra = "█" * preenchido + "░" * (largura_barra - preenchido)
        sys.stdout.write(f"\r{texto} |{cor_barra}{barra}{ft.reset}| {percentual}%")
        
    elif estilo == "setas":
        # Indicador de fluxo dinâmico de processo
        preenchido = int(passo / total_passos * largura_barra)
        barra = "=" * max(0, preenchido - 1) + ">" + " " * (largura_barra - preenchido)
        sys.stdout.write(f"\r{texto} [{ct.turquesa}{barra}{ft.reset}] {percentual}%")
        
    elif estilo == "pontos":
        # Carregador pontilhado minimalista (ideal para scripts de rede)
        preenchido = int(passo / total_passos * largura_barra)
        barra = "•" * preenchido + " " * (largura_barra - preenchido)
        sys.stdout.write(f"\r{texto} ({ct.laranja}{barra}{ft.reset}) {percentual}%")
        
    elif estilo == "tecnologico":
        # Estilo de ficção científica / Cyberpunk
        preenchido = int(passo / total_passos * largura_barra)
        barra = "■" * preenchido + "□" * (largura_barra - preenchido)
        sys.stdout.write(f"\r{texto} ⚡ [{cor_barra}{barra}{ft.reset}] 🛠️ {percentual}%")
        
    elif estilo == "pacman":
        # Animação retrô clássica de jogo arcade
        preenchido = int(passo / total_passos * largura_barra)
        boca = "👉" if passo % 2 == 0 else "💪" # Simula movimento
        barra = "•" * preenchido + boca + " " * (largura_barra - preenchido)
        sys.stdout.write(f"\r{texto} {ct.amarelo}●{ft.reset} {ct.dourado}{barra}{ft.reset}")

    sys.stdout.flush()
    
    # Salta uma linha automaticamente ao atingir 100% de conclusão
    if passo >= total_passos:
        print()
