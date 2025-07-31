import os
from FileManager import FileManager

def main():
    fm = FileManager()
    print("Простой файловый менеджер")
    print("Команды: \n") 
    print("gd -> поулчить директорий \т")
    print("ls <path> -> посмотреть содержимое директория\n")
    print("cd <path> -> сменить директорий \n")
    print("rd <path> -> удалить директорий \n")
    print("mkdir <path> -> создать папку \n")
    print("rm <path> -> удалить файл \n")
    print("read <path> -> прочитать файл \n")
    print("write <path> <data> -> запись в файл \n")
    print("rename <path> <name> -> переименовать файл \n")
    print("stat <path> -> информация о файле \n")
    print("copy <path> <new_path> -> копировать файл в другое место \n")
    print("exit -> выход \n")
    print("ls <file> \n")
    print("ls <file> \n")
    
    while True:
        cmd = input(f"\n[{os.getcwd()}]> ").strip().split()
        if not cmd:
            continue
            
        try:
            if cmd[0] == "exit":
                break
                
            elif cmd[0] == "ls":
                path = cmd[1] if len(cmd) > 1 else "."
                if files := fm.view_directory(path):
                    print("\n".join(files))
                else:
                    print("Папка пуста")
                    
            elif cmd[0] == "gd":
                name = fm.get_directory()
                print(f"Директорий: {name}")
                    
            elif cmd[0] == "mkdir" and len(cmd) > 1:
                fm.create_directory(cmd[1])
                print(f"Создана папка: {cmd[1]}")
                
            elif cmd[0] == "rm" and len(cmd) > 1:
                fm.remove_file(cmd[1])
                print(f"Удалён файл: {cmd[1]}")
                
            elif cmd[0] == "read" and len(cmd) > 1:
                print(fm.read_file(cmd[1]).decode())
                
            elif cmd[0] == "write" and len(cmd) > 2:
                fm.write_file(cmd[1], " ".join(cmd[2:]).encode())
                print(f"Записано в {cmd[1]}")
                
            elif cmd[0] == "cp" and len(cmd) > 2:
                fm.copy_file(cmd[1], cmd[2])
                print(f"Скопировано: {cmd[1]} → {cmd[2]}")
                
            elif cmd[0] == "cd":
                path = cmd[1] if len(cmd) > 1 else os.path.expanduser("~")
                fm.change_directory(path)
                
            elif cmd[0] == "rd" and len(cmd) == 2:
                path = cmd[1] 
                fm.remove_dircetory(path)
                
            elif cmd[0] == "stat" and len(cmd) == 2:
                path = cmd[1]
                stat = fm.get_stat(path)
                print(f"Информация о файле: {stat}")
                
            elif cmd[0] == "rename" and len(cmd) == 2:
                path = cmd[1]
                name = cmd[2]
                fm.rename(path, name)
                print(f"Файл {path} переименован в {name}")
                
            else:
                print("Неизвестная команда")
                
        except Exception as e:
            print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()