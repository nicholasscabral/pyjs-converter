from tkinter import filedialog

entrada = filedialog.askopenfile(title="SELECIONE O ARQUIVO DE ENTRADA")
saida = open("davi/saida.js", "w")

tabs = 0

for linha in entrada:
    novaLinha = ""
    if "while" in linha:
        novaLinha += "while ("
        for c in linha:
            if c == ":":
                novaLinha += ") {"
                tabs += 1
                break
            elif c == " ":
                novaLinha += c
            else:
                novaLinha += c
        novaLinha = novaLinha[:6] + novaLinha[9:]
        saida.write(novaLinha + "\n")

    if "print" in linha:
        novaLinha = linha.replace("print", "console.log")
        saida.write(novaLinha)

    elif "input" in linha:
        novaLinha = linha.replace("input", "prompt")
        saida.write(novaLinha)

    elif "if" in linha:
        if "or" in linha:
            linha = linha.replace("or", "||")
        if "and" in linha:
            linha = linha.replace("and", "&&")
        novaLinha += "if ("
        for c in linha:
            if c == ":":
                novaLinha += ") {"
                tabs += 1
                break
            elif c == " ":
                novaLinha += c
            else:
                novaLinha += c
        novaLinha = novaLinha[:4] + novaLinha[7:]
        saida.write(novaLinha + "\n")
        
    elif "else" in linha:
        novaLinha = "\t" * (tabs-1) + "} else {"
        saida.write(novaLinha + "\n")
        tabs += 1
        
    else:
        novaLinha = "\t" * tabs + linha
        saida.write(novaLinha)

        if "}" in linha:
            tabs -= 1
        
saida.write("\t" * tabs + "\n}")
entrada.close()
saida.close()
