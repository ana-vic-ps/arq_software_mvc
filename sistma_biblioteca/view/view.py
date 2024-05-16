class View:
    @staticmethod
    def display_livros(livros):
        if not livros:
            print("Nehum livro encontrado.")
        for livro in livros:
            status = 'Emprestado' if livro.emprestado else 'Disponível'
            print(f"Titulo: {livro.titulo}, Autor: {livro.autor}, Numero de registro: {livro.numero_registro}, Status: {status}")

    @staticmethod
    def get_input(prompt):
        return input(prompt)

    @staticmethod
    def mostrar_mensagem(message):
        print(message)
