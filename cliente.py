import socket

def cliente():
    cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente_socket.connect(("localhost", 12345))

    print("Digite um comando (LISTAR_LIVROS, BUSCAR_LIVRO <titulo>, ENCERRAR): ")
    while True:
        comando = input().strip()

        if comando.upper() == "ENCERRAR":
            cliente_socket.sendall(comando.encode())
            break

        elif comando.upper().startswith("BUSCAR_LIVRO "):
            partes = comando.split(" ", 1)
            if len(partes) < 2:
                print("Uso correto: BUSCAR_LIVRO <título>")
                continue
            titulo = partes[1]
            cliente_socket.sendall(f"BUSCAR_LIVRO|{titulo}".encode())

            resposta = cliente_socket.recv(1024).decode()
            print(resposta)

            if "Deseja reservar?" in resposta:
                escolha = input().strip().upper()
                cliente_socket.sendall(escolha.encode())
                
                if escolha == "SIM":
                    resposta = cliente_socket.recv(1024).decode()
                    print(resposta)
                    nome_cliente = input().strip()
                    cliente_socket.sendall(nome_cliente.encode())

                resposta = cliente_socket.recv(1024).decode()
                print(resposta)

        elif comando.upper() == "LISTAR_LIVROS":
            cliente_socket.sendall(comando.encode())
            resposta = cliente_socket.recv(1024).decode()
            print(resposta)
        
        else:
            print("Comando inválido! Utilize LISTAR_LIVROS, BUSCAR_LIVRO <titulo> ou ENCERRAR.")
            continue

    cliente_socket.close()

if __name__ == "__main__":
    cliente()




