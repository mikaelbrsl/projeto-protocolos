import socket
import threading
from biblioteca import Biblioteca
from livro import Livro

def processar_comando(comando, biblioteca, conn):
    partes = comando.split("|")
    
    if partes[0] == "LISTAR_LIVROS":
        resposta = biblioteca.listar_livros()
        conn.sendall(resposta.encode())

    elif partes[0] == "BUSCAR_LIVRO":
        if len(partes) < 2:
            conn.sendall("ERRO|400|Uso correto: BUSCAR_LIVRO|<título>".encode())
            return
        
        titulo = partes[1]
        livro = biblioteca.buscar_livro(titulo)

        if livro is None:
            resposta = "ERRO|404|Livro não faz parte do catálogo!"
        elif livro.copias < 1:
            resposta = "ERRO|409|Sem cópias disponíveis."
        else:
            resposta = f"Livro encontrado: {livro.titulo} ({livro.copias} cópias disponíveis). Deseja reservar? (SIM/NAO)"
        conn.sendall(resposta.encode())
        
        escolha = conn.recv(1024).decode().strip().upper()
        if escolha == "SIM":
            conn.sendall("Digite seu nome para a reserva:".encode())
            nome_cliente = conn.recv(1024).decode().strip()
            resposta = biblioteca.reservar_livro(titulo, nome_cliente)
            conn.sendall(resposta.encode())
        else:
            conn.sendall("Reserva cancelada.".encode())

def lidar_com_cliente(conn, addr, biblioteca):
    print(f"Conexão estabelecida com {addr}")
    while True:
        try:
            dados = conn.recv(1024).decode()
            if not dados:
                break
            processar_comando(dados, biblioteca, conn)
        except Exception as e:
            print(f"Erro: {e}")
            break
    conn.close()
    print(f"Conexão encerrada com {addr}")

def iniciar_servidor():
    biblioteca = Biblioteca()
    biblioteca.adicionar_livro(Livro(1, "Dom Casmurro", "Machado de Assis", 3))
    biblioteca.adicionar_livro(Livro(2, "O Hobbit", "J.R.R. Tolkien", 5))
    biblioteca.adicionar_livro(Livro(3, "1984", "George Orwell", 2))
    biblioteca.adicionar_livro(Livro(4, "O Príncipe", "Maquiavel", 4))
    biblioteca.adicionar_livro(Livro(5, "Bíblia", "Diversos Autores", 3))
    biblioteca.adicionar_livro(Livro(6, "Hamlet", "Shakespeare", 2))
    biblioteca.adicionar_livro(Livro(7, "O Alienista", "Machado de Assis", 1))

    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind(("0.0.0.0", 12345))
    servidor.listen(5)
    print("Servidor iniciado. Aguardando conexões...")

    while True:
        conn, addr = servidor.accept()
        thread = threading.Thread(target=lidar_com_cliente, args=(conn, addr, biblioteca))
        thread.start()

iniciar_servidor()




