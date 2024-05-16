from model.model import Livro, Biblioteca
from view.view import View

class Controller:
    def __init__(self):
        self.biblioteca = Biblioteca()
        self.view = View()

    def adcionar_livro(self):
        titulo = self.view.get_input("Digite o título do livro: ")
        autor = self.view.get_input("Digite o autor: ")
        numero_registro = self.view.get_input("Digite o número de registro: ")
        livro = Livro(titulo, autor, numero_registro)
        self.biblioteca.adcionar_livro(livro)
        self.view.mostrar_mensagem("Livro adicionado com sucesso!")

    def buscar_livros(self):
        query = self.view.get_input("Digite o título ou autor para busca: ")
        search_by = self.view.get_input("Buscar por título ou autor? (default = titulo): ")
        if search_by.lower() not in ['titulo', 'autor']:
            search_by = 'titulo'
        livros = self.biblioteca.buscar_livros(query, search_by)
        self.view.display_livros(livros)

    def alugar_livro(self):
        numero_registro = self.view.get_input("Digite o numero de registro do livro para alugar: ")
        livro = self.biblioteca.alugar_livro(numero_registro)
        if livro:
            self.view.mostrar_mensagem(f"Você alugou: {livro.titulo}")
        else:
            self.view.mostrar_mensagem("O livro noa está disponível ou não existe.")

    def devolver_livro(self):
        numero_registro = self.view.get_input("Digite o numero de registro do livro para devolução: ")
        livro = self.biblioteca.devolver_livro(numero_registro)
        if livro:
            self.view.mostrar_mensagem(f"Você devolveu: {livro.titulo}")
        else:
            self.view.mostrar_mensagem("O livro não foi alugado ou não existe")

    def run(self):
        while True:
            opcao = self.view.get_input(
                "1. Adicionar livro\n2. Buscar livros\n3. Alugar livro\n4. Devolver livro\n5. Sair\nEscolha uma opção: ")
            if opcao == '1':
                self.adcionar_livro()
            elif opcao == '2':
                self.buscar_livros()
            elif opcao == '3':
                self.alugar_livro()
            elif opcao == '4':
                self.devolver_livro()
            elif opcao == '5':
                break
            else:
                self.view.mostrar_mensagem("Opção inválida. Tente novamente.")
