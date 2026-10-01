# TextLex - Analisador de Textos

## Objetivo
O TextLex é uma linguagem de programação simples, construída utilizando a biblioteca PLY (Python Lex-Yacc) para realizar a análise léxica e sintática. O objetivo da linguagem é processar arquivos de texto e extrair estatísticas rápidas, como a contagem de palavras e a frequência (nuvem de palavras) dos termos mais utilizados.

## Arquivos Entregues
- `textlex.py`: Código fonte principal contendo as regras léxicas (Lexer), regras sintáticas (Parser) e a Interface de interação (REPL).
- `teste.txt`: Arquivo de texto de exemplo para facilitar o teste da linguagem.
- `README.md`: Documentação completa dos comandos e instruções de uso.

## Pré-requisitos
Para executar o projeto, é necessário ter o Python instalado e a biblioteca PLY.
Instale a dependência rodando o seguinte comando no terminal:
> pip install ply

## Como Executar a Interface
1. Abra o terminal na pasta raiz onde os arquivos estão salvos.
2. Execute o comando: `python textlex.py`
3. A interface interativa (REPL) do TextLex será iniciada e aguardará os comandos.

---

## Documentação dos Comandos

A linguagem possui uma sintaxe direta e aceita as seguintes instruções:

### 1. CARREGAR
- **Sintaxe:** `CARREGAR "nome_do_arquivo.extensao"`
- **Descrição:** Lê um arquivo de texto local e o carrega na memória do programa para que possa ser analisado. É estritamente necessário o uso de aspas duplas em volta do nome do arquivo.
- **Exemplo de uso:** `CARREGAR "teste.txt"`

### 2. CONTAR
- **Sintaxe:** `CONTAR`
- **Descrição:** Realiza a tokenização básica do texto carregado na memória e exibe a quantidade total de palavras presentes no documento.
- **Exemplo de uso:** `CONTAR`

### 3. FREQUENCIA
- **Sintaxe:** `FREQUENCIA <numero_inteiro>`
- **Descrição:** Analisa o texto carregado, ignora pontuações, converte tudo para letras minúsculas e exibe um ranking com as palavras que mais se repetem no documento, limitado ao número informado.
- **Exemplo de uso:** `FREQUENCIA 5` (Exibe as 5 palavras mais repetidas)

### 4. SAIR
- **Sintaxe:** `SAIR`
- **Descrição:** Encerra a interface da linguagem de forma segura.