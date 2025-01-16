import os

def append_content_txt(folder):
    # Nome do arquivo.txt / file.txt name
    file_txt = "novo_script.txt"

    # Verifica se o arquivo.txt existe / Checks if .txt file exists
    if not os.path.exists(file_txt):
        print(f"Erro: O arquivo '{file_txt}' não foi encontrado.") #Error: .txt file not found
        return

    # Lê o conteúdo do arquivo.txt / Reads .txt file content
    with open(file_txt, 'r', encoding='utf-8') as f:
        content_txt = f.read()

    # Itera sobre os arquivos no diretório especificado / Iterates over the files in the specified directory
    for file in os.listdir(folder):
        if file.endswith('.sql'):
            file_path = os.path.join(folder, file)

            # Lê o conteúdo do arquivo.sql / Reads .sql file
            with open(file_path, 'r', encoding='utf-8') as f:
                content_sql = f.read()

            # Adiciona uma linha em branco e o conteúdo do arquivo.txt / Adds a blank line and the content of the .txt file
            new_content = content_sql + "\n\n" + content_txt

            # Sobrescreve o file .sql com o novo conteúdo / Overwrites the .sql file with the new content
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)

            print(f"Conteúdo adicionado ao arquivo: {file}") #Content added to file
