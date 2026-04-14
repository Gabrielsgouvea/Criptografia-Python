import os
import sys
import random

# Constantes
C_FANTASMAS = ['#', '$', '&', '@', '!', '%', '*', '?', '=', '+']
C_SEPARADOR = '|'
C_LINHA = '=' * 40


def fct_get_base_dir():
    """Obtém o diretório base onde o script/exe está localizado."""
    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable)
    else:
        return os.path.dirname(os.path.abspath(__file__))


def fct_codificar(a_mensagem):
    """
    Converte cada caractere da mensagem para seu valor ASCII
    e insere caracteres fantasma a cada 10 caracteres ASCII.
    """
    v_resultado = []
    v_contador = 0

    for v_char in a_mensagem:
        v_ascii_val = str(ord(v_char))
        v_resultado.append(v_ascii_val)
        v_contador += 1

        if v_contador == 10:
            v_qtd_fantasmas = random.randint(3, 7)
            v_fantasma = ''.join(random.choices(C_FANTASMAS, k=v_qtd_fantasmas))
            v_resultado.append(v_fantasma)
            v_contador = 0

    return C_SEPARADOR.join(v_resultado)


def fct_decodificar(a_conteudo):
    """
    Remove os caracteres fantasma e reconverte os valores ASCII
    de volta para a mensagem original.
    """
    v_partes = a_conteudo.split(C_SEPARADOR)
    v_mensagem = ''

    for v_parte in v_partes:
        if v_parte.isdigit():
            v_mensagem += chr(int(v_parte))

    return v_mensagem


def fct_salvar_arquivo(a_nome_arquivo, a_conteudo):
    """Salva o conteúdo em um arquivo .txt na pasta atual."""
    v_caminho = os.path.join(fct_get_base_dir(), a_nome_arquivo)
    with open(v_caminho, 'w', encoding='utf-8') as v_arquivo:
        v_arquivo.write(a_conteudo)
    return v_caminho


def fct_ler_arquivo(a_nome_arquivo):
    """Lê o conteúdo de um arquivo .txt da pasta atual."""
    v_caminho = os.path.join(fct_get_base_dir(), a_nome_arquivo)
    with open(v_caminho, 'r', encoding='utf-8') as v_arquivo:
        return v_arquivo.read()


def main():
    print(C_LINHA)
    print("   SISTEMA DE CRIPTOGRAFIA")
    print(C_LINHA)
    print()

    v_opcao = input("Digite 1 para DECODIFICAR ou 2 para CODIFICAR: ").strip()

    if v_opcao == '1':
        v_nome_arquivo = input("\nDigite o nome do arquivo para decodificar: ").strip()
        try:
            v_conteudo = fct_ler_arquivo(v_nome_arquivo)
            v_mensagem = fct_decodificar(v_conteudo)
            print(f"\n{C_LINHA}")
            print(f"Mensagem decodificada:\n{v_mensagem}")
            print(C_LINHA)
        except FileNotFoundError:
            print(f"\nErro: Arquivo '{v_nome_arquivo}' não encontrado.")
        except Exception as v_erro:
            print(f"\nErro ao decodificar: {v_erro}")

    elif v_opcao == '2':
        v_mensagem = input("\nDigite a mensagem para codificar: ")
        v_conteudo_codificado = fct_codificar(v_mensagem)

        v_nome_arquivo = input("Digite o nome do arquivo para salvar (ex: mensagem.txt): ").strip()
        v_caminho = fct_salvar_arquivo(v_nome_arquivo, v_conteudo_codificado)

        print(f"\n{C_LINHA}")
        print(f"Mensagem codificada com sucesso!")
        print(f"Arquivo salvo em: {v_caminho}")
        print(f"Conteúdo: {v_conteudo_codificado}")
        print(C_LINHA)

    else:
        print("\nOpção inválida! Execute o programa novamente.")

    print("\nPressione ENTER para sair...")
    input()


if __name__ == '__main__':
    main()
