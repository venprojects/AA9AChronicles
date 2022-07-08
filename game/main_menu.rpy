# Главное меню

screen cases_screen():
    add "cases bg"
    modal True

    imagebutton auto "case_%s":
        focus_mask True
        hovered SetVariable("screen_tooltip", "Test Case")
        unhovered SetVariable("screen_tooltip", "")
        action Jump ("first_case_init")