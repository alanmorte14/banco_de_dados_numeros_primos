import sqlite3
def verificarNumerosPrimo(listaBruta):
    #algoritmo para numeros primos
    aux = 0
    for item in listaBruta:
        aux = 0
        for x in range(1, item+1):
            if(item%x==0):
                aux+=1
            if aux > 2:
                aux = 0
                break
        if aux == 2:
            comando.execute("INSERT INTO numeros_primos(numero) VALUES(?) ", (x,))
            dados.commit() #confirmação 
    printSelectAll()
    
def printSelectAll():
    comando.execute("SELECT * FROM numeros_primos") #selecionando todos os itens da tabela numeros_primos.
    rows = comando.fetchall()
    for row in rows:
        for item in row:
            print(item)
    
def deleteAll():
    comando.execute("DELETE FROM numeros_primos")
    dados.commit()

dados = sqlite3.connect("banco_de_dados.db") #conecanto ao banco de dados criado.
comando = dados.cursor() #objeto do tipo cursor, usado para executar os métodos do sql
comando.execute("CREATE TABLE IF NOT EXISTS numeros_primos (numero)") #criando tabela do banco de dados. Nome da tabela. Campos da tabela e tipo. Nção pode-se rodar mais de uma vez ja que na primeira ja cria a tabela, a não ser que use o if table not exists.
limite = int(input("Digite um limite numérico: "))
lista = list(range(1, limite+1))
verificarNumerosPrimo(lista)
deleteAll()
