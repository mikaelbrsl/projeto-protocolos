import threading

class Biblioteca:
    def __init__(self):
        self.livros = []
        self.reservas = {}
        self.semaforo = threading.Semaphore(1)  # Para controle de concorrência

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def listar_livros(self):
        if not self.livros:
            return "Nenhum livro disponível."
        resposta = "=== Livros disponíveis ===\n"
        for livro in self.livros:
            resposta += f"{livro.titulo} ({livro.copias} cópias)\n"
        return resposta.strip()

    def buscar_livro(self, titulo):
        for livro in self.livros:
            if livro.titulo.lower() == titulo.lower():
                return livro
        return None

    def reservar_livro(self, titulo, cliente_nome):
        with self.semaforo:
            livro = self.buscar_livro(titulo)
            if livro is None:
                return "Livro não faz parte do catálogo!"
            elif livro.copias < 1:
                return "Sem cópias disponíveis"
            else:
                livro.copias -= 1
                self.reservas[cliente_nome] = titulo
                return f"Reserva realizada! {cliente_nome} reservou '{titulo}'."