import pathlib
import os
import shutil
import time

prefix_archive = "doc"
path_A = "C:/Users/Rafael/Documents/Projetinho_Thalesinho/path_A"
path_B = "C:/Users/Rafael/Documents/Projetinho_Thalesinho/path_B"
execution_time = 1


# --------------------------------------------------
#   Função que percorre todos os arquivos de um diretorio analisando se os nomes dos arquivos
#   contem o prefixo procurado pelo usuario !
# --------------------------------------------------
def search_files(path_A, prefix_file, path_B):

    for (root, dirs, file) in os.walk(path_A):
        for archives in file:
            if prefix_file in archives:
                copy_files_to_pathB(path_B, archives)
            else:
                print("any file that contains '" + prefix_file + "' was found")


def copy_files_to_pathB(archives):

    try:
        shutil.copy(path_A + "/" + archives, path_B)
        write_log()
        return 1
    except:
        print("could not copy the file" + archives)
        return 0


def write_log(archive):
    file = open("log_teste1.txt", "a")

    info_list = list()
    info_list.append("file name -> " + archive)
    info_list.append("origin folder -> " + path_A)
    info_list.append("destination folder -> " + path_B)
    info_list.append(time.strftime('%d-%m-%y %H:%M:%S', time.localtime()))

    file.writelines(info_list)
