from Menu import Menu

menu = Menu()

while True:
    mode = menu.MainMenu()
    print(mode)
    if mode == "Data Source":
        menu.FilePathInput()
        print(menu.FilePath)