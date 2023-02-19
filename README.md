# РЕАЛИЗОВАННЫЕ ТЕСТЫ

### В файле test_sign_in.py(экран авторизации):
1. **test_sign_in_open_sign_in_screen_from_main_page** - открытие формы авторизации с главного экрана + авторизация
2. **test_sign_in_open_sign_in_screen_from_account_page** - открытие формы авторизации после клика по личному кабинету + авторизация
3. **test_sign_in_open_sign_in_screen_from_register_page** - открытие формы авторизации из формы регистрации 
4. **test_sign_in_open_sign_in_screen_from_password_recovery_page** - открытие формы авторизации из формы восстановления пароля 

### В файле test_sections.py(переход к разделам из личного кабинета):
1. **test_move_to_construct_from_account_page_by_section_button** - переход к конструктору из личного кабинета кликом по разделу конструктора в хидере
2. **test_move_to_construct_from_account_page_by_click_on_logo** - переход к конструктору из личного кабинета кликом по лого

### В файле test_registration.py(регистрация):
1. **test_registration_opens_sign_in_screen** - успешная регистрация
2. **test_registration_error_due_to_invalid_password** - ошибка регистрации при вводе пароля некорректного формата

### В файле test_construction.py(разделы конструктора):
1. **test_constuct_choose_sause_section** - выбор раздела соусов в конструкторе 
2. **test_constuct_choose_bun_section** - выбор раздела булок в конструкторе
3. **test_constuct_choose_filling_section** - выбор раздела начинок в конструкторе 

### В файле test_account_page.py(экран личного кабинета):
1. **test_account_page_account_page** - открытие личного кабинета у авторизованного юзера
2. **test_account_page_log_out_from_account** - выход из аккаунта через личный кабинет 