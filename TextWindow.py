from PySide6 import QtWidgets
import PySide6

class HelpWindow(PySide6.QtWidgets.QMainWindow):
    def __init__(self):
        super(HelpWindow, self).__init__()
        help_w = PySide6.QtWidgets.QMainWindow
        HelpWindow.setMinimumSize(self,500, 500)
        HelpWindow.setWindowTitle(self, "Справка")
        intro_tab = PySide6.QtWidgets.QWidget()
        first_tab = PySide6.QtWidgets.QWidget()
        second_tab = PySide6.QtWidgets.QWidget()
        third_tab = PySide6.QtWidgets.QWidget()
        forth_tab = PySide6.QtWidgets.QWidget()
        fifth_tab = PySide6.QtWidgets.QWidget()
        sixth_tab = PySide6.QtWidgets.QWidget()
        self.tab = QtWidgets.QTabWidget()

        # Intro tab
        self.layout_intro_tab = PySide6.QtWidgets.QVBoxLayout()
        self.text_edit_intro_tab = PySide6.QtWidgets.QTextEdit()
        self.text_edit_intro_tab.setReadOnly(True)
        help_text_intro = """
                <h1>Руководство к использованию программы</h1>
                <p>Это окно содержит инструкции по использованию данного приложения. Инструкции расположены
                в соответствии с порядком расположения вкладок программы</p>
                <p>Для навигации вы можете использовать специализированные кнопки навигации расположенные под 
                вкладками либо самостоятельно, нажимая на необходимую вам вкладку.</p>
                <p><a href="https://google.com">Посетите наш сайт приложений</a> для дополнительной информации.</p>
                """
        self.text_edit_intro_tab.setHtml(help_text_intro)
        self.layout_intro_tab.addWidget(self.text_edit_intro_tab)
        intro_tab.setLayout(self.layout_intro_tab)


        # First tab
        self.layout_first_tab = PySide6.QtWidgets.QVBoxLayout()
        self.text_edit_first_tab = PySide6.QtWidgets.QTextEdit()
        self.text_edit_first_tab.setReadOnly(True)
        help_text_first = """
                <h1>Вкладка Данные</h1>
                <p>С этой вкладки начинается работа приложения.
                 </p>
                 <p>Смотрим на единственный активный элемент - гроупбокс "База данных". Нажимаем на
                  кнопку "Выбрать БД". Она открывает нам диалоговое окно, где мы и выбираем заранее подготовленную
                  базу данных.</p>
                 <p>Далее с помощью комбобокса выбираем нужную таблицу (в случае если их несколько).</p>
                 <p>Нажимаем кнопку "Открыть таблицу" после чего программа начинает анализировать таблицу и проводить
                  первичные расчеты</p>
                 <p>Теперь вам стали возможности просмотра данных и манипуляции над ними.</p>
                 <p>Рассмотрим по порядку. С помощью гроупбокса "Имитационное моделирвание" вы можете удалять либо добавлять строки вы таблицу. 
                 Также в гроупбоксе "Параметры имтационной модели" вы можете изменить два важных параметра это "Коэффициент экспоненциального 
                 сглаживания" и "Погрешность измерения".</p>
                 <p><b>ВНИМАНИЕ! После нажатия на кнопки "Применить" либо завершения действия удаления или добавления строки изменения вступят в силу сразу. Вернуть изначальные данные при ошибке уже не получится. 
                 Настоятельно рекомендуем сохранять резервную копию таблицы данных для предотвращения такого рода проблем.</b></p>
                 <p>Для дальнейшего анализа вы можете перейти на следующую вкладку "Первый уровень декомпозиции"</p>
                """
        self.text_edit_first_tab.setHtml(help_text_first)
        self.layout_first_tab.addWidget(self.text_edit_first_tab)
        first_tab.setLayout(self.layout_first_tab)

        # Second tab
        self.layout_second_tab = PySide6.QtWidgets.QVBoxLayout()
        self.text_edit_second_tab = PySide6.QtWidgets.QTextEdit()
        self.text_edit_second_tab.setReadOnly(True)
        help_text_second = """
                        <h1>Вкладка Первый уровень декомпозиции</h1>
                        <p>Слево у нас находятся два гроупбокса с вычислениями "Фазовые координаты" и "Мониторинг состояния".
                         Графическое отображение расчетов координат вы можете наблюдать на графиках в справа, а программный анализ состояния системы происходит в гроупбоксе "Мониторинг состония".
                          По последнему столбцу таблицы вы можете самим оценить ситуацию. В случае чего вы можете нажать кнопку "Рекомендации" и программа сразу скажет, следует ли продолжать анализ.</p>
                        <p>При необходимости дальнейшей декомпозиции нажмите на кнопку "Перейти на второй уровень декомпозиции"</p>
                        """
        self.text_edit_second_tab.setHtml(help_text_second)
        self.layout_second_tab.addWidget(self.text_edit_second_tab)
        second_tab.setLayout(self.layout_second_tab)

        # Third tab
        self.layout_third_tab = PySide6.QtWidgets.QVBoxLayout()
        self.text_edit_third_tab = PySide6.QtWidgets.QTextEdit()
        self.text_edit_third_tab.setReadOnly(True)
        help_text_third = """
                                <h1>Вкладка Второй уровень декомпозиции</h1>
                                <p>Вкладка второго уровня декомпозиции делится таже две вкладки. Вкладка "Распределение контрольных точек по блокам"
                                содержит в себе функционал для разделение системы на нужное вам количество блоков с определенными точками.
                                В спинбоксе "Количество блоков" мы можем указать количество блоков.
                                Далее мы выбираем блок и "наполняем его точками". Ниже слево указаны не распределенные точки, а справа точки 
                                которые принадлежат выбранному блок.</p>
                                <p>После создания и распределение блоков нажимаем кнопку "Подтвердить". В случае если вы всё правильно сделали, то
                                 произойдёт переход на вкладку "Расчеты и функции".</p>
                                <p>Состав вкладки "Расчеты и функции" аналогичен вкладке "Первый уровень декомпозиции", поэтому в случае 
                                 вопросов обращайтесь к соответствующей вкладке справки.</p>
                                 <p>И также переходим на следующую вкладку</p>
                                <p></p>
                                """
        self.text_edit_third_tab.setHtml(help_text_third)
        self.layout_third_tab.addWidget(self.text_edit_third_tab)
        third_tab.setLayout(self.layout_third_tab)

        # Forth tab
        self.layout_forth_tab = PySide6.QtWidgets.QVBoxLayout()
        self.text_edit_forth_tab = PySide6.QtWidgets.QTextEdit()
        self.text_edit_forth_tab.setReadOnly(True)
        help_text_forth = """
                                <h1>Вкладка Третий уровень декомпозиции</h1>
                                <p>Третий уровень декомпозиции также делится на две вкладки.</p>
                                <p>Рассмотрим вкладку "Распределение контрольных точек". Из уже составленых блоков
                                 вы должны выбрать один, который мы будем подвергать декомпозиции. После выбора блока
                                 вы можете отредактировать состав этого блока. Нажимаем на кнопку "Подтвердить" и переходить к гроупбоксу ниже.
                                  Выбираем число подблоков, на которое будет делится блок.</p>
                                <p>В гроупбоксе распредляем точки блок на подблоки и после подтверждения происходит переход на вторую вкладку.</p>
                                <p>Состав вкладки "Расчеты и функции" аналогичен вкладке "Первый уровень декомпозиции", поэтому в случае 
                                 вопросов обращайтесь к соответствующей вкладке справки.</p>
                                 <p>И также переходим на следующую вкладку</p>
                                <p></p>
                                """
        self.text_edit_forth_tab.setHtml(help_text_forth)
        self.layout_forth_tab.addWidget(self.text_edit_forth_tab)
        forth_tab.setLayout(self.layout_forth_tab)

        # Fifth tab
        self.layout_fifth_tab = PySide6.QtWidgets.QVBoxLayout()
        self.text_edit_fifth_tab = PySide6.QtWidgets.QTextEdit()
        self.text_edit_fifth_tab.setReadOnly(True)
        help_text_fifth = """
                                        <h1>Вкладка Четвертый уровень декомпозиции</h1>
                                        <p>Данная вкладка Состоит всего из двух функциональных частей. Список точек слево и  графика справа.
                                        С помощью списка вы выбираете график какой точки необходимо отобразить на графике.</p>
                                        <p></p>
                                        """
        self.text_edit_fifth_tab.setHtml(help_text_fifth)
        self.layout_fifth_tab.addWidget(self.text_edit_fifth_tab)
        fifth_tab.setLayout(self.layout_fifth_tab)

        # Sixth tab
        self.layout_sixth_tab = PySide6.QtWidgets.QVBoxLayout()
        self.text_edit_sixth_tab = PySide6.QtWidgets.QTextEdit()
        self.text_edit_sixth_tab.setReadOnly(True)
        help_text_sixth = """
                                        <h1>Вкладка Тестирование</h1>
                                        <p>Вкладка Тестирование содержит 4 вкладки: "покой", "равномерное движение", "скачок", "циклическое движение".
                                         На каждой вкладке соответственно находятся различные движения данных.</p>
                                        """
        self.text_edit_sixth_tab.setHtml(help_text_sixth)
        self.layout_sixth_tab.addWidget(self.text_edit_sixth_tab)
        sixth_tab.setLayout(self.layout_sixth_tab)

        main_widget = QtWidgets.QWidget()
        main_layout = QtWidgets.QVBoxLayout()


        self.button_back_one = PySide6.QtWidgets.QPushButton("<")
        self.button_next_one = PySide6.QtWidgets.QPushButton(">")
        self.button_start = PySide6.QtWidgets.QPushButton("|<")
        self.button_finish = PySide6.QtWidgets.QPushButton(">|")

        self.button_start.clicked.connect(lambda: self.navigation("|<"))
        self.button_back_one.clicked.connect(lambda: self.navigation("<"))
        self.button_next_one.clicked.connect(lambda: self.navigation(">"))
        self.button_finish.clicked.connect(lambda: self.navigation(">|"))



        self.close_button = PySide6.QtWidgets.QPushButton("Close")
        self.close_button.clicked.connect(self.close)

        self.layout_navigation = PySide6.QtWidgets.QHBoxLayout()
        self.layout_navigation.addWidget(self.button_start)
        self.layout_navigation.addWidget(self.button_back_one)
        self.layout_navigation.addWidget(self.button_next_one)
        self.layout_navigation.addWidget(self.button_finish)


        main_widget.setLayout(main_layout)
        main_layout.addWidget(self.tab)
        main_layout.addLayout(self.layout_navigation)
        main_layout.addWidget(self.close_button)

        self.tab.addTab(intro_tab, "Введение")
        self.tab.addTab(first_tab, "Данные")
        self.tab.addTab(second_tab, "Первый уровень декомпозиции")
        self.tab.addTab(third_tab, "Второй уровень декомпозиции")
        self.tab.addTab(forth_tab, "Третий уровень декомпозиции")
        self.tab.addTab(fifth_tab, "Четвертый уровень декомпозиции")
        self.tab.addTab(sixth_tab, "Тестирование")



        self.setCentralWidget(main_widget)

    def navigation(self, action):
        cur_indx = self.tab.currentIndex()
        max_tabs = 7
        if action == ">" and cur_indx < max_tabs - 1:
            self.tab.setCurrentIndex(cur_indx+1)
        elif action == "<" and cur_indx > 0:
            self.tab.setCurrentIndex(cur_indx - 1)
        elif action == "|<" and cur_indx != 0:
            self.tab.setCurrentIndex(0)
        elif action == ">|" and cur_indx != 6:
            self.tab.setCurrentIndex(max_tabs - 1)