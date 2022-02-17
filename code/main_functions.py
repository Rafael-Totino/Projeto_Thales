import pathlib
import os
import shutil
import time
import json

# --------------------------------------------------
#   function that reads information from the config file
# --------------------------------------------------


def read_configs():
    with open('config.json', 'r', encoding='utf8') as f:
        dados = json.load(f)

    prefix_archive = dados['regx']
    path_A = dados['folder_origin']
    path_B = dados['folder_dest']
    execution_time = dados['execution_period']


# --------------------------------------------------
#   Function that goes through all the files in a directory, analyzing if the names of the files
#   contains the prefix searched for by the user !
# --------------------------------------------------
def search_files(path_A, prefix_file, path_B):

    for (root, dirs, file) in os.walk(path_A):
        for archives in file:
            if prefix_file in archives:
                copy_files_to_pathB(path_A, path_B, archives)
            else:
                print("any file that contains '" + prefix_file + "' was found")


# --------------------------------------------------
#   Function that copies the file found by search_files() from one directory to another
# --------------------------------------------------
def copy_files_to_pathB(path_A, path_B, archives):

    try:
        shutil.copy(path_A + "/" + archives, path_B)
        write_log(path_A, path_B, archives)
        return 1
    except:
        print("could not copy the file" + archives)
        return 0


# --------------------------------------------------
#   Function that writes the log file
#   Is called every time a file is copied
# --------------------------------------------------
def write_log(path_A, path_B, archive):
    file = open("log_teste1.txt", "a")

    info_list = list()
    info_list.append("file name -> \n" + archive)
    info_list.append("origin folder -> \n" + path_A)
    info_list.append("destination folder -> \n" + path_B)
    info_list.append(time.strftime('%d-%m-%y %H:%M:%S', time.localtime()))
    info_list.append(
        "\n ///////////////////////////////////////////////////////////////////////////// \n")

    file.writelines(info_list)


# --------------------------------------------------
#   Function that writes the settings file, 'config.json'
#
# --------------------------------------------------
def write_config_file(exec_period, regx, origin_folder, dest_folder):

    print(exec_period)
    print(regx)
    print(origin_folder)
    print(dest_folder)

    dictionary = {
        "execution_period": exec_period,
        "regx": regx,
        "folder_origin": origin_folder,
        "folder_dest": dest_folder
    }

    json_object = json.dumps(
        dictionary, ensure_ascii=False, indent=4, separators=(',', ':'))
    print(json_object)

    with open('config.json', 'w') as json_file:
        json_file.write(json_object)


# --------------------------------------------------
#   Main functions
# --------------------------------------------------
def main(execution_time, path_A, prefix_archive, path_B):

    search_files(path_A, prefix_archive, path_B)
    time.sleep(execution_time)


# --------------------------------------------------
#   Python best practices
# --------------------------------------------------
if __name__ == '__main__':
    main()
