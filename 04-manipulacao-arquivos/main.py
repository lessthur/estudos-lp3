# abre o arquivo
arquivo = open("04-manipulacao-arquivos/dados.txt")

print(arquivo)
conteudo = arquivo.read()
print("Conteúdo lido sem formatação: ")
print (conteudo)

# retorna a lista de palavras
# conteudoLines = arquivo.readlines()

linhas = []
for linha in arquivo:
    linhas.append(linha.strip())
    
print("Conteúdo em linhas:")
print(linhas)

arquivo.close()

# alterar o arquivo com with
# w - substitui tudo no arquivo

# bloco with
with open("04-manipulacao-arquivos/dados.txt") as arquivo2:
    conteudo2 = arquivo2.read()
    print("Conteúdo lido em dados.txt:")
    print(conteudo2)

# escrever no arquivo
with open("04-manipulacao-arquivos/dados.txt", "a") as arquivo3:
    print("Escreveu no arquivo dados.txt.")
    arquivo3.write("\nFRUTAS")
    
# a - append adiciona ao arquivo
    
# escrever no arquivo
with open("04-manipulacao-arquivos/dados.txt", "a") as arquivo4:
    arquivo4.write("\nFRUITS\n")
  
  
def linha_para_produto(linha):
    dados = (linha.strip().split(','))
    return {
        "nome": dados[0],
        "descricao": dados[1],
        "preco": float(dados[2]),
        "imagem": dados[3],
    }
    
def obter_produtos():
    with open("04-manipulacao-arquivos/produtos.csv") as arquivo_produtos:    
        produtos = []    
        for linha in arquivo_produtos:
            produto = linha_para_produto(linha)
            produtos.append(produto)
        
        return produtos
    
print(obter_produtos())

def salvar_produto(nome, descricao, preco, imagem):
    texto = f"\n{nome}, {descricao}, {preco}, {imagem}"
    with open("04-manipulacao-arquivos/produtos.csv", "a") as arquivo_produtos:
        arquivo_produtos.write(texto)

salvar_produto("Celular", "Tira fotos", "1500.00", "Celular.jpg")    
print("Salvou celular.\n")
salvar_produto("Sprite", "Bom demais", "4.00", "Sprite.jpg")
print("Salvou Sprite.")


        
    
