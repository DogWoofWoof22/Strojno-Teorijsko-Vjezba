from Menu import Menu

menu = Menu()

while True:
    mode = menu.MainMenu()
    print(mode)
    if mode == "Data Source":
        menu.FilePathInput()
    elif mode == "Topics":
        menu.TopicSelection()
    elif mode == "Mode":
        menu.ModeSelection()