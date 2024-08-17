# Contact Manager

**Contact Manager** - це інструмент командного рядка для управління контактами та нотатками. Він дозволяє легко створювати, редагувати, видаляти та переглядати контакти та нотатки, додавати до них деталі, такі як імена, телефонні номери, адреси, електронні пошти, дні народження та теги.

## Встановлення

Щоб встановити проект локально, виконайте наступні кроки:
1. Клонуйте репозиторій:
```
git clone <URL вашого репозиторію> 
cd ContactManager
```
2. Створіть та активуйте віртуальне оточення:
```
python -m venv venv
.\venv\Scripts\activate
```
3. Встановіть необхідні залежності:
```
pip install -r requirements.txt
```
4. Запустіть проект:
```
python main.py
```

## Використання

Після запуску програми у вас з'явиться командний рядок, де ви можете вводити різні команди для управління контактами та нотатками.

### Основні команди:

close / exit: Завершення роботи програми.

help: Отримання списку команд.

add_contact: Додати новий контакт. Програма запросить ввести деталі контакту, такі як ім'я, телефон, адреса, email та день народження.

delete_contact: Видалити контакт за ім'ям.

add_phone_to_contact: Додати новий номер телефону до існуючого контакту.

change_contact_phone: Змінити існуючий номер телефону для контакту.

delete_phone: Видалити номер телефону з контакту.

update_address: Оновити адресу контакту.

update_email: Оновити email контакту.

add_birthday: Додати день народження до контакту.

find_by_upcoming_birthday: Показати контакти з днями народження, які наступають протягом заданої кількості днів.

find_all_contacts: Показати всі контакти.

find_contact_by_name: Показати контакт за іменем.

find_contact_by_part_name: Показати всі контакти, чиї імена містять задану частину.

find_all_notes: Показати всі нотатки.

add_note: Додати нову нотатку. Програма запросить ввести текст нотатки та теги.

find_note_by_tag: Знайти нотатки за тегом.

change_content_by_title: Змінити контент за тайтлом

find_note_by_keywords: Пошук в нотатках по кейворду (шукає в тайтлі, контенті та тегах)

delete_note: Видалити нотатку.

## Додаткова інформація

Проект підтримує збереження даних контактів та нотаток у файли (`addressbook.pkl` і `notebook.pkl`), щоб дані не губилися після закриття програми. Всі зміни автоматично зберігаються при виході з програми.