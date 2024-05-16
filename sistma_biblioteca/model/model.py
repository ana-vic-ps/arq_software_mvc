class Livro:
    def __init__(self, titulo, autor, numero_registro):
        self.titulo = titulo
        self.autor = autor
        self.numero_registro = numero_registro
        self.emprestado = False

class Biblioteca:
    def __init__(self):
        self.livros = []

    def adcionar_livro(self, livro):
        self.livros.append(livro)

    def buscar_livros(self, query, search_by='titulo'):
        if search_by == 'titulo':
            return [livro for livro in self.livros if query.lower() in livro.titulo.lower()]
        elif search_by == 'autor':
            return [livro for livro in self.livros if query.lower() in livro.autor.lower()]

    def alugar_livro(self, numero_registro):
        for livro in self.livros:
            if livro.numero_registro == numero_registro and not livro.emprestado:
                livro.emprestado = True
                return livro
        return None

    def devolver_livro(self, numero_registro):
        for livro in self.livros:
            if livro.numero_registro == numero_registro and livro.emprestado:
                livro.emprestado = False
                return livro
        return None