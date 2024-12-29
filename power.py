import tkinter as tk
from tkinter import messagebox
import datetime

class PasswordGame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Игра 'Создай Пароль'")
        self.geometry("800x600")

        self.all_questions = [
            {"text": "Пароль должен содержать не менее 8 символов", "check": lambda password: len(password) >= 8},
            {"text": "В пароле должна быть хотя бы одна цифра", "check": lambda password: any(char.isdigit() for char in password)},
            {"text": "В пароле должна быть хотя бы одна заглавная буква", "check": lambda password: any(char.isupper() for char in password)},
            {"text": "В пароле должен быть хотя бы один специальный символ (!@#$)", "check": lambda password: any(char in "!@#$" for char in password)},
            {"text": "В пароле должен быть год рождения пользователя (например, 1990)", "check": self.check_year},
            {"text": "В пароле должен быть название месяца", "check": self.check_month},
            {"text": "В пароле должно быть имя пользователя", "check": self.check_username},
            {"text": "Пароль должен содержать кошачий мяук (Мяу)", "check": lambda password: "мяу" in password.lower()},
            {"text": "Пароль должен заканчиваться на имя случайного известного человека (Эйнштейн, Ньютон, Шекспир, Бейонсе, Маск, Стив Джобс, Леонардо да Винчи, Моцарт, Мария Кюри)", "check": self.check_famous_person},
            {"text": "Пароль должен содержать название элемента таблицы Менделеева", "check": self.check_element},
            {"text": "Пароль должен соответствовать текущему времени в формате HH:MM (например, 14:35)", "check": self.check_current_time},
            {"text": "Пароль должен содержать как минимум два одинаковых символа подряд", "check": self.check_duplicate_chars},
            {"text": "Пароль должен содержать слово 'секрет' задом наперед", "check": lambda password: "терекс" in password.lower()},
            {"text": "Пароль не должен содержать пробелы", "check": lambda password: " " not in password},
            {"text": "Пароль должен содержать как минимум слово 'пароль'", "check": lambda password: "пароль" in password.lower()},
            {"text": "Пароль должен содержать текущую дату в формате DD.MM.YYYY", "check": self.check_current_date},
            {"text": "Пароль должен содержать ваше любимое число", "check": self.check_fav_number},
            {"text": "Пароль должен содержать как минимум три разных символа из разных регистров", "check": self.check_three_diff_char},
            {"text": "Пароль должен содержать  день недели", "check": self.check_day_of_week},
            {"text": "Пароль должен содержать как минимум два повторяющихся символа, но не подряд", "check": self.check_two_repeating_chars},
            {"text": "Пароль должен содержать как минимум одну гласную и одну согласную букву", "check": self.check_vowel_consonant},
            {"text": "Пароль должен состоять из 2 слов, разделенных дефисом", "check": self.check_two_word_hyphen},
            {"text": "Пароль должен состоять год рождения СССР", "check": lambda password: "1922" in password.lower()},
            {"text": "Пароль должен состоять кто правил в XVI веке ответ состоит из двух слов через дефис", "check": lambda password: "Иван-Грозный" in password.lower()},
            {"text": "Пароль должен состоять из чего состоит хромосома", "check": lambda password: "ДНК" in password.lower()},
            {"text": "Пароль должен состоять из года рождения Пушкина", "check": lambda password: "1799" in password.lower()},
            {"text": "Пароль должен состоять из год смерти Николай II", "check": lambda password: "1918" in password.lower()},
            {"text": "Пароль должен состоять из последней династии которая была в России", "check": lambda password: "романовы" in password.lower()},
            {"text": "Пароль должен содержать как минимум год создания линукса", "check": lambda password: "1991" in password.lower()},
        ]
        
        self.displayed_questions = []
        self.current_question_index = 0
        self.username = ""
        self.create_widgets()
        self.update_questions_listbox()
    
    def create_widgets(self):
        # Ввод имени пользователя
        tk.Label(self, text="Введите ваше имя:").pack(pady=5)
        self.username_entry = tk.Entry(self)
        self.username_entry.pack(pady=5)
        tk.Button(self, text="Сохранить имя", command=self.set_username).pack(pady=5)
        
        # Ввод пароля (без сокрытия)
        tk.Label(self, text="Введите пароль:").pack(pady=5)
        self.password_entry = tk.Entry(self)
        self.password_entry.pack(pady=5)
        # привязка клавиши Enter
        self.password_entry.bind("<Return>", self.check_password_event)

        # Список правил
        self.questions_listbox = tk.Listbox(self, width=60)
        self.questions_listbox.pack(pady=10)

        # Кнопка проверки
        tk.Button(self, text="Проверить", command=self.check_password).pack(pady=10)
        
        # Сообщения
        self.message_label = tk.Label(self, text="")
        self.message_label.pack()
    
    def set_username(self):
        self.username = self.username_entry.get()
        messagebox.showinfo("Имя", f"Ваше имя: {self.username}")

    def check_year(self, password):
         try:
             return any(str(year) in password for year in range(1900, 2025))
         except ValueError:
             return False
         
    def check_month(self, password):
        months = ["январь", "февраль", "март", "апрель", "май", "июнь", "июль", "август", "сентябрь", "октябрь", "ноябрь", "декабрь"]
        return any(month in password.lower() for month in months)
    
    def check_username(self, password):
        return self.username.lower() in password.lower()
    
    def check_famous_person(self, password):
        famous_people = ["Эйнштейн", "Ньютон", "Шекспир", "Бейонсе", "Маск", "Стив Джобс", "Леонардо да Винчи", "Моцарт", "Мария Кюри"]
        return any(person.lower() in password.lower() for person in famous_people)
    
    def check_element(self, password):
      elements = ["водород", "гелий", "литий", "бериллий", "бор", "углерод", "азот", "кислород", "фтор", "неон", "натрий", "магний", "алюминий", "кремний", "фосфор", "сера", "хлор", "аргон", "калий", "кальций"]
      return any(element.lower() in password.lower() for element in elements)


    def check_current_time(self, password):
       try:
            current_time = datetime.datetime.now().strftime("%H:%M")
            return current_time in password
       except ValueError:
           return False

    def check_duplicate_chars(self, password):
        for i in range(len(password) - 1):
            if password[i] == password[i+1]:
                return True
        return False
    
    def check_palindrome(self, password):
        password = password.lower()
        return password == password[::-1]
    
    def check_current_date(self, password):
        try:
            current_date = datetime.datetime.now().strftime("%d.%m.%Y")
            return current_date in password
        except ValueError:
            return False

    def check_fav_number(self, password):
          fav_number = ["1", "2", "3"]
          return any(number.lower() in password.lower() for number in fav_number)
    
    def check_three_diff_char(self, password):
         upper = any(char.isupper() for char in password)
         lower = any(char.islower() for char in password)
         digit = any(char.isdigit() for char in password)
         return upper + lower + digit >=3
    
    def check_day_of_week(self, password):
         day = ["понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье"]
         return any(days.lower() in password.lower() for days in day)
    
    def check_two_word(self, password):
        return len(password.split()) >=2

    def check_latin_letters(self, password):
            return all('a' <= char <= 'z' or 'A' <= char <= 'Z' for char in password)

    def check_two_repeating_chars(self, password):
        chars = set()
        for char in password:
            if char in chars:
                return True
            chars.add(char)
        return False
    
    def check_vowel_consonant(self, password):
        vowels = "aeiouAEIOU"
        return any(char in vowels for char in password) and any(char.isalpha() and char not in vowels for char in password)
    
    def check_ascii_sum(self, password):
        return sum(ord(char) for char in password) > 1000
    
    def check_two_word_hyphen(self, password):
         parts = password.split('-')
         return len(parts) == 2 and all(part.strip() for part in parts)
    
    def check_ascending_numbers(self, password):
         numbers = [int(char) for char in password if char.isdigit()]
         return all(numbers[i] < numbers[i+1] for i in range(len(numbers)-1)) if len(numbers) > 1 else True
    
    def check_long_word(self, password):
        return any(len(word) > 6 for word in password.split())
    
    def check_no_more_than_two_repeating(self, password):
        for char in password:
            if password.count(char) > 2:
                return False
        return True


    def update_questions_listbox(self):
        self.questions_listbox.delete(0, tk.END)
        
        # Вставляем текущий вопрос в начало списка (если есть)
        if self.current_question_index < len(self.all_questions):
            current_question = self.all_questions[self.current_question_index]
            if not any(q['text'] == current_question['text'] for q in self.displayed_questions):
                 self.displayed_questions.insert(0, current_question)

        for index, question in enumerate(self.displayed_questions):
           text = f"{index + 1}. {question['text']}"
           self.questions_listbox.insert(tk.END, text)
        
        if self.displayed_questions:
            for index, question in enumerate(self.displayed_questions):
                if not question['check'](self.password_entry.get()):
                    self.questions_listbox.itemconfig(index, fg="red")

            if self.current_question_index < len(self.all_questions):
                for index, question in enumerate(self.displayed_questions):
                   if  question == self.displayed_questions[0]:
                    self.questions_listbox.itemconfig(index, fg="green")
            

        if self.current_question_index < len(self.all_questions) and not any(not question['check'](self.password_entry.get()) for question in self.displayed_questions) and not any(q['text'] == self.all_questions[self.current_question_index]['text'] for q in self.displayed_questions):
            self.questions_listbox.insert(tk.END, f"{len(self.displayed_questions) + 1}. {self.all_questions[self.current_question_index]['text']}")
            self.questions_listbox.itemconfig(len(self.displayed_questions), fg="red")
    
    def check_password_event(self, event):
        self.check_password()

    def check_password(self):
         if not self.username:
            self.message_label.config(text="Сначала сохраните имя!")
            return
         
         password = self.password_entry.get()
        
        
        
         if self.current_question_index < len(self.all_questions) :
            current_question = self.all_questions[self.current_question_index]
            
            if current_question["check"](password):
                if current_question not in self.displayed_questions:
                     self.displayed_questions.insert(0, current_question)
                
                self.current_question_index += 1

                self.message_label.config(text="Вопрос пройден! Новый вопрос...")

                self.update_questions_listbox()

                if self.current_question_index == len(self.all_questions):
                    self.message_label.config(text="Поздравляю, все вопросы пройдены!")
                    tk.Button(self, text = "Игра окончена", command=self.quit).pack(pady=10)
                    return
            else:
                 self.message_label.config(text="Пароль не соответствует вопросу.")
            self.update_questions_listbox()
         elif self.current_question_index == len(self.all_questions) and any(not question['check'](password) for question in self.displayed_questions):
             self.update_questions_listbox()
             self.message_label.config(text="Пароль не соответствует вопросу.")
             
            

if __name__ == "__main__":
    game = PasswordGame()
    game.mainloop()
