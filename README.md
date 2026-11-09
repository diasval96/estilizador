# estilizador ⚡🎨

<p align="center">
  <!-- Badges Profissionais Dinâmicos -->
  <img src="https://shields.io" alt="Versão no PyPI">
  <img src="https://shields.io" alt="Downloads Mensais">
  <img src="https://shields.io" alt="Versões do Python">
  <img src="https://shields.io" alt="Licença">
</p>

<p align="center">
  <!-- BANNER/GIF DO REPOSITÓRIO -->
  <!-- DICA: Grave a tela do Termux rodando a opção 1 e 3, converta em .gif no ezgif.com e adicione na pasta /docs do seu repositório -->
  <img src="https://githubusercontent.com" width="100%" alt="Demonstração Real do Estilizador no Terminal">
</p>

---

O **estilizador** é um micro-framework nativo, modular e de altíssima velocidade para estilização de interfaces CLI, componentes visuais geométricos e animações em português no Python. Projetado com **zero dependências externas**, ele foi construído sob medida para desenvolvedores focados em performance extrema tanto em servidores quanto no ecossistema mobile (**Termux, Pydroid3, Acode**).

---

## 🪵 Nossa História & Propósito (Por que o Estilizador nasceu?)

Entre os dias 20 e 25 de setembro de 2026, eu estava desenvolvendo algumas automações simples para ferramentas de varredura de rede no celular. No começo, usar os códigos ANSI puros era muito limitado. Migrei para o *Colorama*, mas digitar `Fore.GREEN` o tempo todo no teclado virtual do celular me deixava extremamente lento. Tentei criar apelidos para as variáveis, mas o código começou a ficar confuso e frustrante.

Foi aí que tive um estalo: usar a lógica por trás dessas bibliotecas para criar o meu próprio pacote, totalmente em português, para facilitar a minha vida e a de quem programa pelo celular. Em 1º de outubro de 2026, nasceu o `colorizador v0.1.0`. Funcionava bem, mas eu achava as saídas um pouco pesadas. Pesquisei o *Rich*, mas ele era ainda mais pesado e complexo para o que eu precisava.

Estudando essas ferramentas a fundo, percebi como o ecossistema funcionava por baixo dos panos. Decidi reescrever tudo do zero. Criei a versão `v0.1.1` com **zero dependências externas**. Ficou incrivelmente leve e rápido, mas eu ainda me sentia limitado em relação às opções de cores. Fiquei maturando a ideia por um tempo, até que no dia 8 de novembro lancei a versão final `1.0.0` do `colorizador` para encerrar seu ciclo com chave de ouro.

Percebi que tudo o que eu queria adicionar dali para frente — barras de progresso, animações, layouts complexos — já não combinava mais com o nome "colorizador". Por isso, decidi migrar definitivamente para o **estilizador 2.0**.

O meu objetivo com o **estilizador** é ajudar quem está começando, desenvolvedores mobile e, principalmente, **a comunidade que não fala inglês e quer criar scripts profissionais sem barreiras**.

Este é um projeto feito de coração. Sinta-se totalmente livre para apoiar, usar, dar sugestões ou criticar de forma construtiva!

---

## 🚀 Instalação e Uso Rápido (3 Linhas)

```bash
pip install estilizador
```

```python
from estilizador import ct, cf, msg

msg.sucesso_clean("Estilizador v2.0 carregado com sucesso!")
```

---

## 🎨 Tabelas Visuais de Cores e Estilos

A biblioteca inova ao separar os escopos de customização em namespaces curtos e intuitivos, eliminando a poluição visual do seu código e acelerando drasticamente a digitação no teclado do celular.

### 🔤 Cores de Texto (`ct.nome`)

| Visual | Código de Chamada | Aplicação Prática no Terminal |
| :---: | :--- | :--- |
| 🟢 | `ct.verde` | Saídas tradicionais de confirmação e sucesso |
| 🔵 | `ct.azul` | Destaques estruturais de navegação |
| 🟡 | `ct.amarelo` | Alertas visuais preventivos ou avisos |
| 🔴 | `ct.vermelho` | Mensagens de erros sistêmicos |
| ⚫ | `ct.preto` | Texto escuro para contrastar com fundos claros |
| ⚪ | `ct.branco` | Texto padrão límpido do terminal |
| 🔘 | `ct.cinza` | Subtextos ou mensagens secundárias de ajuda |
| 🌀 | `ct.azul_claro` | Identificadores de logs e informações rápidas |
| 🌸 | `ct.rosa` | Destaques neon especiais (Magenta brilhante) |
| 👑 | `ct.dourado` | Tom ouro premium utilizando escala estendida (256-cores) |
| 🍊 | `ct.laranja` | Tom laranja vibrante utilizando escala estendida (256-cores) |
| 🔮 | `ct.roxo` | Tom roxo neon utilizando escala estendida (256-cores) |
| 💎 | `ct.turquesa` | Tom ciano claro utilizando escala estendida (256-cores) |

### 🖼️ Cores de Fundo / Preenchimento (`cf.nome`)

| Bloco | Código de Chamada | Uso Recomendado para Layouts |
| :---: | :--- | :--- |
| 🟩 | `cf.verde` | Banners ou tags de sucesso preenchidos |
| 🟥 | `cf.vermelho` | Blocos de erros críticos ou panes fatais |
| 🟨 | `cf.amarelo` | Chamadas de atenção prioritárias do sistema |
| 🟦 | `cf.azul` | Cabeçalhos e menus de informações estruturadas |
| ⬛ | `cf.preto` | Fundo fosco para blocks de isolamento de código |
| ⬜ | `cf.branco` | Fundo de alto contraste para terminais escuros |

### 🖋️ Tipografia e Efeitos de Fonte (`ft.nome`)

| Código | Efeito no Terminal | Compatibilidade Mobile |
| :--- | :--- | :--- |
| `ft.negrito` | Aplica o peso Bold ao texto | 100% (Termux / Pydroid / PC) |
| `ft.italico` | Inclina o texto (Slant style) | Termux e Terminais Linux modernos |
| `ft.sublinhado` | Adiciona uma linha abaixo da string | 100% (Termux / Pydroid / PC) |
| `ft.inverter` | Troca a cor do texto com a do fundo | Excelente para criar destaques rápidos |
| `ft.reset` | Restaura as configurações originais da janela | Obrigatório para fechamento de estados |

---

## ⚙️ Funcionalidades de Elite

### 💬 1. Mensagens Estruturadas por Intuito (`msg.funcao`)
O estilizador traz três arquiteturas prontas de exibição automática para se adequar ao design do seu software:
*   **Estilo Padrão (`_padrao`):** Pinta o bloco de texto por completo com o ícone clássico.
*   **Estilo Clean (`_clean`):** Mantém a mensagem limpa em branco e destaca apenas a tag identificadora.
*   **Estilo Bloco (`_bloco`):** Gera banners dinâmicos com fundo invertido para alto impacto visual.

```python
from estilizador import msg

msg.info_clean("Iniciando varredura no banco local...")
msg.erro_bloco("A conexão com o servidor caiu repentinamente!")
msg.fatal("Processo encerrado forçadamente pelo sistema.")
```

### 📊 2. Componentes de Progresso Geométricos (`barr.funcao`)
Acompanhe loops, processamentos e downloads pesados diretamente na mesma linha do terminal, utilizando múltiplos formatos visuais integrados (`blocos`, `setas`, `pontos`, `tecnologico` e `pacman`).

```python
import time
from estilizador import barr, ct

# Ícone dinâmico giratório clássico
barr.carregar("Sincronizando tabelas remotas", duracao=1.5, estilo="padrao")

# Renderização de barra progressiva passo a passo dentro de um laço de repetição
total = 20
for passo in range(1, total + 1):
    barr.progresso(passo, total, estilo="tecnologico", cor_barra=ct.turquesa, texto="Executando:")
    time.sleep(0.05)
```

## 🛡️ Engine de Blindagem Universal
Graças a uma camada interna de verificação primitiva baseada em emuladores de terminal (`sys.stdout.isatty()`), o estilizador detecta o ambiente em tempo real. Se o script rodar em IDEs móveis sem suporte nativo à renderização ANSI (como as caixas de output estáticas do **Acode**, **Sublime Text** ou **PyCharm**), a biblioteca **remove automaticamente os códigos de escape**, entregando um texto totalmente limpo e legível ao usuário, livre de bugs visuais de caracteres quebrados.

## 📄 Licença
Este software está distribuído sob as diretrizes da Licença MIT.

