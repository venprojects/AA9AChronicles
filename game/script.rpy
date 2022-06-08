# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define unknown = Character('???', color="#ffffff")
define teller = Character('Рассказчик', color="#ffffff")

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
label start:
    call screen cases_screen with fade

    scene cases bg

    screen cases_screen():
        add "cases bg"
        modal True

        imagebutton auto "case_%s":
            focus_mask True
            hovered SetVariable("screen_tooltip", "Test Case")
            unhovered SetVariable("screen_tooltip", "")
            action Jump ("first_case")


label first_case:
    stop music

    scene empty with fade

    pause 2.0

    unknown "..."
    unknown "Приветствую..."
    unknown "Как тебя зовут?"
    unknown "Хотя... какая разница?"
    unknown "Ты ведь из {color=#ff0000}9\"А\" класса{/color}, верно?"
    unknown "И ты здесь, чтобы узнать историю. Я прав?"
    unknown "Что? Кто я?"

    pause 1.0

    teller "Зови меня \"Рассказчик\"." with fade
    teller "И я здесь, чтобы рассказать тебе о том, с чего все начиналось."
    teller "А, может, здесь всё и закончится."

    pause 1.0

    teller "..."
    teller "Думаю, логичнее будет начать с самого начала."
    teller "А именно... С {color=#ff0000}самого первого дела{/color} в истории {color=#00ff00}\"школьной судебной практики\"{/color}."
    teller "..."
    teller "Что за \"школьная судебная практика\"?"
    teller "Попробую объяснить вкратце."
    teller "ШСП - это практика судебных заседаний, которую ввели в школе №1945 \"Синяя Птица\", для справедливого разъяснения конфликтов между учениками и учителями."
    teller "Данная практика началось в 2019 году."
    teller "И первое дело прозвали \"Суд над Санычем\"."
    teller "Да, новый классный руководитель 6\"А\" класса на тот момент."
    teller "И обвинял его... Его же класс."
