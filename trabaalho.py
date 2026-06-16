class Livro:
    titulo = None
    autor = None
    ano = None
    codigo = None
    status = "Disponível"

def cadastrar(biblioteca):
    codigo = int(input("digite o código do livro: ")) #checar se o livro já está na biblioteca
    for livro in biblioteca:
        if livro.codigo == codigo:
            print("Livro já cadastrado.")
            return

    obra = Livro()
    obra.titulo = input("Digite o título: ")
    obra.autor = input("Digite o autor: ")
    obra.ano = int(input("Digite o ano: "))
    obra.codigo = codigo
    obra.status = "Disponível"

    biblioteca.append(obra)

def mostrar_livro(livro):
    print(f"Título: {livro.titulo}")
    print(f"Autor: {livro.autor}")
    print(f"Ano: {livro.ano}")
    print(f"Código: {livro.codigo}")
    print(f"Status: {livro.status}")
    print()

def consultar_titulo(biblioteca):
    titulo = input("digite o título do livro: ")
    for livro in biblioteca:
        if livro.titulo == titulo:
            mostrar_livro(livro)
            return
    
    print("Livro não encontrado.")
        
def consultar_autor(biblioteca):
    autor = input("digite o Autor: ")
    encontrou = False
    for livro in biblioteca:
        if livro.autor == autor:
            mostrar_livro(livro)
            encontrou = True
    
    if encontrou == False:
        print("Nenhum livro encontrado.")

def consultar_codigo(biblioteca):
    codigo = int(input("digite o codigo do livro: "))
    for livro in biblioteca:
        if livro.codigo == codigo:
            mostrar_livro(livro)
            return
    print("Livro não encontrado.")
        
def consultar_ano(biblioteca):
    ano = int(input("digite o ano do livro: "))
    encontrou = False
    for livro in biblioteca:
        if livro.ano == ano:
            mostrar_livro(livro)
            encontrou = True
    if encontrou == False:
        print("Nenhum livro encontrado")


def consultar_livro(biblioteca):
    print("Escolha uma opção")
    print()
    print("1 = Título 2 = Código  3 = Autor  4 = Ano ")
    op = int(input("Digite aqui sua escolha: "))
    if op == 1:
        consultar_titulo(biblioteca)
    elif op == 2:
        consultar_codigo(biblioteca)
    elif op == 3:
        consultar_autor(biblioteca)
    elif op == 4:
        consultar_ano(biblioteca)
    else:
        print("Opção inválida.")

def alterar_dados(biblioteca):
    titulo = input("Título do livro que será substituído: ")
    
    for livro in biblioteca:
        if livro.titulo == titulo:
            novocodigo = int(input("Novo código:"))
            for x in biblioteca:
                if x.codigo == novocodigo and x != livro:
                    print("Código já cadastrado.")
                    return
            livro.titulo = input("Digite o título: ")
            livro.autor = input("Digite o autor: ")
            livro.ano = int(input("Digite o ano: "))
            livro.codigo = novocodigo
            livro.status = input("digite o status do livro [Disponível/Emprestado]: ")
            print("Dados alterados")
            return
    print("Livro não encontrado")

def remover_livro(biblioteca):
    titulo = input("Digite o livro que será removido: ")
    for livro in biblioteca:
        if livro.titulo == titulo:
            biblioteca.remove(livro)
            print("Livro removido.")
            return
    
    print("Livro não encontrado.")

def ordenar_titulos(biblioteca):
    if len(biblioteca) == 0:
        print("nenhum livro cadastrado.")
        return
    for i in range(len(biblioteca)):
        menor = i
        for j in range(i + 1, len(biblioteca)):

            if biblioteca[j].titulo.lower() < biblioteca[menor].titulo.lower():
                menor = j

        aux = biblioteca[i]
        biblioteca[i] = biblioteca[menor]
        biblioteca[menor] = aux


def listar_livros(biblioteca):
    if len(biblioteca) == 0:
        print("nenhum livro cadastrado.")
        return

    ordenar_titulos(biblioteca)

    for livro in biblioteca:
        print(f"{livro.titulo} - {livro.ano}")



def emprestar(biblioteca):
    titulo = input("Digite o nome do livro: ")
    for livro in biblioteca:
        if livro.titulo == titulo:
            if livro.status == "Emprestado":
               print("O livro já está emprestado.")
            else:
                livro.status = "Emprestado"
                print("Livro emprestado com sucesso.")
            return
            
    print("Livro não encontrado.")

def devolver(biblioteca):
    titulo = input("Digite o nome do livro: ")
    for livro in biblioteca:
        if livro.titulo == titulo:
            if livro.status == "Disponível":
               print("O livro já está disponível.")
            else:
                livro.status = "Disponível"
                print("Livro devolvido com sucesso.")
            return
            
    print("Livro não encontrado.")


def menu_principal():
    biblioteca = []
    while True:

        print("\n===== BIBLIOTECA =====")
        print("1 - Cadastrar livro")
        print("2 - Consultar livro")
        print("3 - Alterar dados")
        print("4 - Remover livro")
        print("5 - Listar todos")
        print("6 - Realizar empréstimo")
        print("7 - Realizar devolução")
        print("8 - Sair")

        op = int(input("Opção: "))

        if op == 1:
            cadastrar(biblioteca)

        elif op == 2:
            consultar_livro(biblioteca)
        elif op == 3:
            alterar_dados(biblioteca)
        elif op == 4:
            remover_livro(biblioteca)
        elif op == 5:
            listar_livros(biblioteca)
        elif op == 6:
            emprestar(biblioteca)
        elif op == 7:
            devolver(biblioteca)
        elif op == 8:
            print("Programa encerrado.")
            break
        else:
            print("Opção inválida.")
        
menu_principal()
    



