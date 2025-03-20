- Título: Biblioteca Online

- Autores: Mario Jose do Nascimento Neto (mario.neto@academico.ifpb.edu.br), Mikael Brasil de Moura (mikael.brasil@academico.ifpb.edu.br), Victor Belfort de Aquino Bezerra (victor.belfort@academico.ifpb.edu.br);

-  Disciplinas: Protocolos e Interconexão de Redes de Computadores - Professor: Leonidas Francisco de Lima Junior;

-  Descrição: O projeto consiste no desenvolvimento de uma biblioteca online, permitindo que os usuários listem os livros, pesquisem e realizem empréstimos. A aplicação será realizada através da linguagem Python e baseada em uma arquitetura cliente/servidor, utilizando comunicação via API de Sockets com um protocolo de aplicação próprio e o protocolo de transporte HTTP;

-  Protocolo de aplicação: O protocolo da aplicação consiste em uma série de comandos que o cliente pode enviar ao servidor. São eles: LISTAR_LIVROS: retorna a lista de livros cadastrados e suas cópias; BUSCAR_LIVRO <titulo>: retorna informações sobre o livro pesquisado; e ENCERRAR: encerra a conexão com o servidor

-  Pré-requisitos para execução: Python 3.x: Linguagem de programação usada para desenvolver o projeto. Pode ser instalado a partir do site oficial do Python. Biblioteca socket: biblioteca padrão do Python, utilizada para criar conexões de rede. Biblioteca threading: usada para permitir que o servidor lide com múltiplos clientes simultaneamente. Nenhuma das bibliotecas utilizadas requerem instalação adicional.

-  Arquivos do projeto:
servidor.py: Inicia o servidor e gerencia conexões com os clientes.
Processa comandos recebidos do cliente (listar livros, buscar livros, reservar).
Envia respostas estruturadas seguindo o protocolo de mensagens.

cliente.py:
Conecta-se ao servidor e permite que o usuário envie comandos.
Processa respostas do servidor e exibe as mensagens.
Permite a interação com a reserva de livros.

livro.py:
Define a classe Livro, que representa um livro na biblioteca.
Contém atributos como título e número de cópias disponíveis.

biblioteca.py:
Gerencia o catálogo de livros e as reservas.
Permite listar livros disponíveis, buscar por título e fazer reserva de cópia.
Controla reservas garantindo integridade dos dados com um semáforo.

-  Instruções de execução: Execute o arquivo servidor.py para iniciar o servidor. Em um terminal separado, execute o arquivo cliente.py para iniciar o cliente. Comandos disponíveis:

  LISTAR_LIVROS: lista os livros disponíveis e a quantidade de cópias.
  BUSCAR_LIVRO <titulo>: retorna informações sobre o livro pesquisado.
  ENCERRAR: Encerra a conexão com o servidor.
