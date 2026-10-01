import ply.lex as lex
import ply.yacc as yacc
import re
from collections import Counter
import sys

# Variável global para armazenar o texto que está sendo analisado
texto_atual = ""

# 1. analise lexica (Lexer)
tokens = (
    'CARREGAR',
    'CONTAR',
    'FREQUENCIA',
    'SAIR',
    'STRING',
    'NUMERO'
)

# Regras de tokens simples
t_CARREGAR = r'CARREGAR'
t_CONTAR = r'CONTAR'
t_FREQUENCIA = r'FREQUENCIA'
t_SAIR = r'SAIR'

# Ignorar espaços e tabs
t_ignore = ' \t'

# Regra para pegar strings entre aspas duplas (ex: "arquivo.txt")
def t_STRING(t):
    r'"[^"]*"'
    t.value = t.value[1:-1] # Remove as aspas para usar no Python
    return t

# Regra para números inteiros
def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Tratamento de erro léxico
def t_error(t):
    print(f"Erro léxico: Caractere não reconhecido '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()


# 2. analise sintatica (Parser / Interpretador)

def p_comando_carregar(p):
    'comando : CARREGAR STRING'
    global texto_atual
    caminho_arquivo = p[2]
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as f:
            texto_atual = f.read()
        print(f"> Sucesso: Arquivo '{caminho_arquivo}' carregado na memória.")
    except FileNotFoundError:
        print(f"> Erro: Arquivo '{caminho_arquivo}' não encontrado.")
    except Exception as e:
        print(f"> Erro ao ler o arquivo: {e}")

def p_comando_contar(p):
    'comando : CONTAR'
    global texto_atual
    if not texto_atual:
        print("> Aviso: Nenhum texto carregado. Use o comando CARREGAR primeiro.")
        return
    
    # Tokenização simples separando por espaços
    palavras = texto_atual.split()
    print(f"> O texto possui {len(palavras)} palavras no total.")

def p_comando_frequencia(p):
    'comando : FREQUENCIA NUMERO'
    global texto_atual
    if not texto_atual:
        print("> Aviso: Nenhum texto carregado. Use o comando CARREGAR primeiro.")
        return
    
    qtd = p[2]
    # Pega apenas letras e números, ignorando pontuação e jogando pra minúsculo
    palavras = re.findall(r'\b\w+\b', texto_atual.lower())
    contagem = Counter(palavras)
    
    print(f"> As {qtd} palavras mais frequentes são:")
    for palavra, freq in contagem.most_common(qtd):
        print(f"   - {palavra}: {freq} vezes")

def p_comando_sair(p):
    'comando : SAIR'
    print("> Encerrando o TextLex. Até mais!")
    sys.exit(0)

# Tratamento de erro sintático
def p_error(p):
    if p:
        print(f"Erro de sintaxe próximo a '{p.value}'")
    else:
        print("Erro de sintaxe no final do comando")

parser = yacc.yacc()


# 3. interface (REPL - Read-Eval-Print Loop)

def iniciar_interface():
    print("="*40)
    print(" Bem-vindo ao TextLex - Analisador de Textos ")
    print(" Digite 'SAIR' para encerrar.")
    print("="*40)
    
    while True:
        try:
            entrada = input('TextLex> ')
            if not entrada.strip():
                continue
            parser.parse(entrada)
        except EOFError:
            break
        except SystemExit:
            break
        except Exception as e:
            print(f"Erro inesperado: {e}")

if __name__ == '__main__':
    iniciar_interface()