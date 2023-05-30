import re
from tkinter import filedialog

entrada = filedialog.askopenfile(title="SELECIONE O ARQUIVO DE ENTRADA")
saida = open("davi/saida.js", "w")

tabs = 0
tabsContados = 0

def darTabs(linha):
    global tabs
    global tabsContados
    num_spaces = len(re.match(r'^\s*', linha).group(0))
    tabsContados = num_spaces // 4
    if tabsContados < tabs:
        while tabsContados < tabs:
            tabs -= 1
            novaLinha = '\t' * tabs + '}\n'
            saida.write(novaLinha)
            tabsContados += 1

for linha in entrada:
    novaLinha = ""
    darTabs(linha)

    if "while" in linha:
        linha = linha.replace(":", ") {")
        linha = linha.replace("while", "while (")
        tabs += 1
        saida.write(linha)
    else:
        saida.write(linha)

entrada.close()
saida.close()
