from append_content import append_content_txt
from rename_files import rename_files

def main():
    #Definir diretório
    folder = r'C:\Users\Yago\Desktop\Dev\Testes\Teste Github\teste-estudos\Teste de scripts'

    #Adiciona o conteúdo do arquivo 
    append_content_txt(folder)

    # Renomear arquivos
    older_version = 'TESTE'
    new_version = 'teste'
    rename_files(folder, older_version, new_version)

if __name__ == "__main__":
    main()
