from .detector import ATIVO

preto    = "\033[40m" if ATIVO else ""
vermelho = "\033[41m" if ATIVO else ""
verde    = "\033[42m" if ATIVO else ""
amarelo  = "\033[43m" if ATIVO else ""
azul     = "\033[44m" if ATIVO else ""
magenta  = "\033[45m" if ATIVO else ""
ciano    = "\033[46m" if ATIVO else ""
branco   = "\033[47m" if ATIVO else ""
cinza    = "\033[100m" if ATIVO else ""

