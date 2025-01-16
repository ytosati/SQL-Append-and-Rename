import os

def rename_files(folder, older_version, new_version):
    # Itera sobre os arquivos no diretório especificado / Iterates over the files in the specified directory
    for file_name in os.listdir(folder):
        if older_version in file_name:
            # Substitui a versão / Replaces version
            new_file_name = file_name.replace(older_version, new_version)

            # Define caminhos antigos e novos / Set old and new paths
            caminho_antigo = os.path.join(folder, file_name)
            new_path = os.path.join(folder, new_file_name)

            # Renomeia o arquivo / Renames files
            os.rename(caminho_antigo, new_path)
            print(f"Renomeado: \"{file_name}\" -> \"{new_file_name}\"")