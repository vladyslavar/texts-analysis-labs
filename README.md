### Lab 1
Створити програму, яка:
1. Зчитує текстовий файл як рядок. За допомогою зрізів виділити частину тексту в окрему змінну-рядок та використати описані в теоретичних відомостях функції та методи для роботи з рядками.
2. За допомогою регулярних виразів знайти всі дати та перевести в один формат. Файл text3.

### Lab 2
1. Зчитати файл text3.
    - порахувати кількість слів в третьому реченні (не враховуючи знаки пунктуації та інші символи);
    - видалити стоп-слова;
    - знайти 10 слів, які зустрічаються найчастіше.
2. Використати корпус Reuters, третій текст категорії cocoa
    - вивести речення з другого до передостаннього;
    - вивести 8 дієслів, що зустрічаються найчастіше.

### Lab 3
Зчитати файл doc13. Вважати кожен рядок окремим документом корпусу. Виконати попередню обробку корпусу.
1. Представити корпус як модель *«Сумка n-грам»*, взяти уні- та біграми. Вивести вектор для Dark chocolate.
2. Представити корпус як модель *TD-IDF*. Спробувати кластеризувати документи за допомогою ієрархічної агломераційної кластеризації.
3. Представити корпус як модель *Word2Vec*. Знайти подібні слова до слів immigration, chocolate.
### Lab 4
Файл bbc-news-data.csv. В якості текстової моделі використати *Word2Vec*. Виконати класифікацію за допомогою алгоритмів *випадковий ліс* та *градієнтний бустинг*, порівняти їх точність. Спробувати покращити модель випадковий ліс за допомогою *GridSearchCV*
### Lab 5
Файл bbc-news-data.csv. Створити програму, яка зчитує заданий набір даних, виділяє текстову частину даних (вони розглядаються як документи), виконує попередню обробку.
1. Застосувати *розклад невід’ємних матриць* для моделювання тем. Обрати три нових документи та визначити їх теми. Вивести терми, що описують кожну з тем.
2. Використати текст edgeworth-parents.txt з корпусу gutenberg бібліотеки nltk та вивести ключові триграми.

### Lab 6
Створити програму, яка:
1. Зчитує заданий набір даних, виконує попередню обробку, розбиває дані на навчальні на тестові. Виконує аналіз настроїв за допомогою алгоритмів класифікації (наприклад, логістичної регресії, опорних векторів і т.д.).
2. Розрахувати матрицю невідповідностей, провести оцінку точності моделі.
3. Використати один з готових лексиконів, наприклад *Textblob*, для аналізу оцінки настроїв. Також розрахувати матрицю невідповідностей, провести оцінку точності моделі.
4. Обрати три випадкові записи та вивести результати оцінки їх настрою за пунктами 1 і 3.

Файл movie1.csv. 0 – негативний коментар, 1 – позитивний. Використати *наївний байєсів класифікатор*
### Lab 7
Створити програму, яка:
1. Виконує завдання №2 лабораторної роботи №1 за допомогою класу Matcher.
2. За допомогою бібліотеки *SpaCy* у файлі lab7-5.txt:
    - Знайти та вивести іменники чоловічого роду, які присутні у тексті.
    - Вивести леми слів першого речення.
    - Знайти та вивести організації, які присутні у тексті.
### Lab 8
1. Створити кілька своїх прикладів у форматі json за тематикою "події" (англійською або українською мовою) для розпізнавання нового типу сутностей (обрати самостійно). Створити програму, що додає ці приклади до існуючої моделі *spaCy*, навчає модель. Продемонструвати роботу.
2. Застосувати компонент TextCategorizer для визначення намірів. Дані для навчання за тематикою варіанту обрати самостійно або скористатись вказаним файлом (utterance містить висловлювання, intent - намір). Дані файли містять приклади діалогів користувачів з системою-помічником за певною тематикою, наприклад, замовлення квитків і т.д. Навчити компонент та продемонструвати роботу.