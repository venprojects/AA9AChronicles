# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
label start:
    call screen cases_screen with fade

    $ quick_menu = False

    scene cases bg
