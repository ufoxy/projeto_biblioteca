from services.livro_service import LivroService
from services.usuario_service import UsuarioService
from services.emprestimo_service import EmprestimoService

def menu():
    print("\n=== Biblioteca Digital (MongoDB Atlas) ===")
    print("1 - Cadastrar Livro")
    print("2 - Cadastrar Usuário")
    print("3 - Emprestar Livro")
    print("4 - Devolver Livro")
    print("5 - Consultar Livros")
    print("0 - Sair")

if __name__ == "__main__":
    livro_service = LivroService()
    usuario_service = UsuarioService()
    emprestimo_service = EmprestimoService()

    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            livro_service.cadastrar_livro()
        elif opcao == "2":
            usuario_service.cadastrar_usuario()
        elif opcao == "3":
            emprestimo_service.emprestar_livro()
        elif opcao == "4":
            emprestimo_service.devolver_livro()
        elif opcao == "5":
            livro_service.consultar_livros()
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")
