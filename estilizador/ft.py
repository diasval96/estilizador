from .detector import ATIVO
from . import ct

negrito     = "\033[1m" if ATIVO else "" 
italico     = "\033[3m" if ATIVO else ""
sublinhado  = "\033[4m" if ATIVO else ""
inverter    = "\033[7m" if ATIVO else ""
reset       = "\033[0m" if ATIVO else ""
esmaecido   = ct.cinza
