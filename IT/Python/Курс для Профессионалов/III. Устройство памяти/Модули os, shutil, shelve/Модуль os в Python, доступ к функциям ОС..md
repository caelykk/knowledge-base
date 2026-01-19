[os: Miscellaneous operating system interfaces](https://docs.python.org/3/library/os.html#module-os "Permalink to this headline")

[Модуль os в Python, доступ к функциям ОС.](https://docs-python.ru/standart-library/modul-os-python/)



## Интерфейсы операционной системы.

[Модуль `os`](https://docs-python.ru/standart-library/modul-os-python/ "Модуль os в Python, доступ к функциям ОС.") обеспечивает портативный способ использования функциональных возможностей, зависящих от операционной системы.

-   если нужно просто прочитать или записать файл, то лучше воспользоваться [встроенной функцией `open()`](https://docs-python.ru/tutorial/vstroennye-funktsii-interpretatora-python/funktsija-open/ "Функция open() в Python, открывает файл на чтение/запись."),
-   для различных манипуляций с путями, то удобнее будет использовать [модуль `os.path`](https://docs-python.ru/standart-library/modul-os-path-python/ "Модуль os.path в Python, операции с путями ОС.") или [`pathlib`](https://docs-python.ru/standart-library/modul-pathlib-python/ "Модуль pathlib в Python, операции с путями ОС."),
-   если необходимо прочитать все строки в файлах, указанных в командной строке, посмотрите на [модуль `fileinput`](https://docs-python.ru/standart-library/modul-fileinput-python/ "Модуль fileinput в Python, чтение списка файлов."),
-   для создания временных файлов и каталогов смотрите [модуль `tempfile`](https://docs-python.ru/standart-library/modul-tempfile-python/ "Модуль tempfile в Python, временные файлы и каталоги."),
-   для операций с файлами и каталогами (копирование, перемещение, создание, удаление) используйте [модуль `shutil`](https://docs-python.ru/standart-library/modul-shutil-python/ "Модуль shutil в Python, операций над файлами/каталогами.").

Примечания о доступности функций модуля `os`:

-   Конструкция всех зависимых от Python модулей, встроенных в операционную систему, такова, что при наличии одинаковых функциональных возможностей он использует один и тот же интерфейс. Например, [функция `os.stat(path)`](https://docs-python.ru/standart-library/modul-os-python/funktsija-stat-modulja-os/ "Функция stat() модуля os в Python.") возвращает статистическую информацию о пути в том же формате, который произошел от интерфейса POSIX.
-   Расширения, характерные для конкретной операционной системы, также доступны через [модуль `os`](https://docs-python.ru/standart-library/modul-os-python/ "Модуль os в Python, доступ к функциям ОС."), но их использование является угрозой переносимости ПО между системами.
-   Все функции, принимающие пути или имена файлов, принимают как [байтовые строки](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-bytes-bajtovye-stroki/ "Байтовые строки bytes в Python."), так и [строковые объекты](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-str-tekstovye-stroki/ "Текстовые строки str в Python.") и приводят к объекту одного типа, если возвращается путь или имя файла.

**Заметка**. Все функции в этом модуле поднимают исключение `OSError` или их подклассы в случае недопустимых или недоступных имен и путей к файлам или других аргументов, которые имеют правильный тип, но не принимаются операционной системой.

#### os.error

Исключение `os.error` это псевдоним для [встроенного исключения `OSError`](https://docs-python.ru/tutorial/vstroennye-iskljuchenija-interpretator-python/oshibki-operatsionnoj-sistemy-oserror/ "Исключения операционной системы: OSError в Python.").

#### os.name:

`os.name` это имя импортируемого модуля, зависящего от операционной системы. В настоящее время зарегистрированы следующие имена: `'posix'`, `'nt'`, `'java'`.

Смотрите также [`sys.platform`](https://docs-python.ru/standart-library/modul-sys-python/imja-ispolzuemoj-os/ "Имя используемой OS.") имеет более тонкую детализацию, [`os.uname()`](https://docs-python.ru/standart-library/modul-os-python/funktsija-uname-modulja-os/ "Функция uname() модуля os в Python.") дает системно-зависимую информацию о версии системы. [Модуль `platform`](https://docs-python.ru/standart-library/modul-platform-python/ "Модуль platform в Python, информация о системе.") содержит подробные проверки идентичности системы.

## Имена файлов, аргументы командной строки и переменные окружения.

В Python имена файлов, аргументы командной строки и переменные окружения представлены с использованием [строкового типа](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-str-tekstovye-stroki/ "Текстовые строки str в Python."). В некоторых системах, перед передачей их операционной системе необходимо декодирование строк в байты и обратно. Python использует кодировку файловой системы для выполнения этого преобразования (смотрите [`sys.getfilesystemencoding()`](https://docs-python.ru/standart-library/modul-sys-python/kodirovka-ispolzuemaja/ "Кодировка, используемая Python.")).

В некоторых системах преобразование с использованием кодировки файловой системы может завершиться ошибкой. В этом случае Python использует [обработчик ошибок кодирования](https://docs-python.ru/standart-library/modul-codecs-python/obrabotchiki-oshibok-kodirovki/ "Обработчики ошибок кодировки.") `surrogateescape`. Это означает, что некодируемые байты заменяются символом Unicode `U + DCxx` при декодировании, и они снова преобразуются в исходный байт при кодировании.

Кодировка файловой системы должна гарантировать успешное декодирование всех байтов ниже 128. Если кодировка файловой системы не обеспечивает эту гарантию, функции API могут вызывать [ошибки `UnicodeErrors`](https://docs-python.ru/tutorial/vstroennye-iskljuchenija-interpretator-python/oshibka-kodirovki-unicodeerror/ "Ошибка кодировки: UnicodeError в Python.").


## Управление переменной средой окружения системы в Python
[Переменные среды окружения системы (environment) в Python.](https://docs-python.ru/standart-library/modul-os-python/upravlenie-sredoj-okruzhenija-koda/ )

Управление переменными средами environment из кода Python. Переменные среды обычно используются для значений конфигурации, таких как пути поиска, расположение файлов и т.д.


## Представление пути в файловой системе в Python.
[Кодирование пути в файловой системе в Python.](https://docs-python.ru/standart-library/modul-os-python/predstavlenie-puti-fajlovoj-sisteme/)

Функция os.fsencode() кодирует имя файла filename в виде пути. Функция os.fsencode() декодирует имя файла filename в виде пути.


## Извлечение/установка uid, gid и pid процесса в Python.
[Извлечение/установка uid, gid и pid процесса в Python.](https://docs-python.ru/standart-library/modul-os-python/izvlechenie-ustanovka-uid-gid-pid-protsessa/ )

Функции для различных манипуляций с uid, gid и pid процесса. Чаще всего они используются авторами демонов или специальных системных программ, которым необходимо изменять уровень разрешений, а не запускаться от имени пользователя root.


## Наследование файловых дескрипторов в Python.
[Наследование файловых дескрипторов в Python](https://docs-python.ru/standart-library/modul-os-python/nasledovanie-fajlovyh-deskriptorov/)

Файловый дескриптор имеет "наследуемый" флаг, который указывает, может ли файловый дескриптор наследоваться дочерними процессами. Начиная с Python-3.4, файловые дескрипторы, созданные Python, по умолчанию не наследуются.


## Создание дескриптора файла, чтение, запись и его закрытие в Python.
[Создание файлового объекта из дескриптора файла в Python.](https://docs-python.ru/standart-library/modul-os-python/sozdanie-deskriptora-chtenie-zapis-zakrytie/)

Создание файлового объекта средствами модуля os. Чтение, запись и закрытие файлового дескриптора, изменение прав доступа к нему. Получение статистики файлового дескриптора.


## listdir()
[Получить список файлов в директории/каталоге в Python.](https://docs-python.ru/standart-library/modul-os-python/funktsija-listdir-modulja-os/ )

Функция `listdir()` модуля os возвращает список, содержащий имена файлов и директорий в каталоге, заданном путем `path`. Список приведен в произвольном порядке и не содержит специальных обозначений

**Синтаксис:**
```python
import os

os.listdir(path='.')
```
**Параметры:**
-   `path` - путь в виде [строки](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-str-tekstovye-stroki/ "Текстовые строки str в Python.") или [дескриптор каталога](https://docs-python.ru/standart-library/modul-os-python/funktsija-supports-dir-fd-modulja-os/ "Функция supports_dir_fd модуля os в Python.").

**Возвращаемое значение:**
-   [список](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-list-spisok/ "Список list в Python.") имен файлов в каталоге.

**Описание:**

Функция [`listdir()`](https://docs-python.ru/standart-library/modul-os-python/funktsija-listdir-modulja-os/ "Функция listdir() модуля os в Python.") модуля [`os`](https://docs-python.ru/standart-library/modul-os-python/ "Модуль os в Python, доступ к функциям ОС.") возвращает список, содержащий имена файлов и директорий в каталоге, заданном путем `path`. Список будет в произвольном порядке и не содержит [специальных обозначений](https://docs-python.ru/standart-library/modul-os-python/znachenija-ispolzuemye-podderzhki-operatsij-putjami/ "Константы для поддержки операций с путями.") `'.'` и `'..'`, даже если они присутствуют в каталоге.

Аргумент `path` принимает объекты, реализующих интерфейс [`os.PathLike`](https://docs-python.ru/standart-library/modul-os-python/predstavlenie-puti-fajlovoj-sisteme/ "Представление пути в файловой системе."). Если путь `path` имеет байтовый тип, переданный прямо или косвенно через интерфейс `os.PathLike`, возвращаемые имена файлов также будут [байтовыми типами](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-bytes-bajtovye-stroki/ "Байтовые строки bytes в Python."), во всех остальных случаях они будут иметь [строковой тип](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-str-tekstovye-stroki/ "Текстовые строки str в Python.").

Эта функция также поддерживает указание [файлового дескриптора](https://docs-python.ru/standart-library/modul-os-python/funktsija-supports-dir-fd-modulja-os/ "Функция supports_dir_fd модуля os в Python."), дескриптор должен ссылаться на каталог `path`.

Вызывает [событие аудита](https://docs-python.ru/standart-library/modul-sys-python/sobytie-audita-c/ "События аудита CPython.") `os.listdir` с аргументом `path`.

**Примеры получения списка имен файлов и директорий в каталоге.**

```python
import os

path = '.'

rez = sorted(os.listdir(path))
for n, item in enumerate(rez):
    print(n+1, item) 

# 1 docs-python-replace.py
# 2 reg-exp.py
# 3 script.py
# 4 sys.float_info.py
# 5 test-gid-uid.py
# 6 test_settracel.py
# 7 tt.py
# 8 venv
```

Чтобы получить полный путь к файлам каталога нужно просто объединить передаваемый аргумент `path` с каждым значением из списка внутри цикла [`for ... in`](https://docs-python.ru/tutorial/tsikly-upravlenie-vetvleniem-python/tsikl-for-in/ "Цикл for ... in ...: в Python."), например `item = os.path.join(path, item)`

## walk() 
[Рекурсивное получение имен файлов в дереве каталогов в Python.](https://docs-python.ru/standart-library/modul-os-python/funktsija-walk-modulja-os/ )

Функция walk() модуля os генерирует имена файлов в дереве каталогов, обходя дерево сверху вниз или снизу вверх. Для каждого каталога в дереве с корнем в вершине каталога top, включая саму вершину top, она выдает тройной кортеж (dirpath, dirnames, filenames).

**Синтаксис:**
```python
import os

os.walk(top, topdown=True, onerror=None, followlinks=False)
```

**Параметры:**
-   `top` - [строка](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-str-tekstovye-stroki/ "Текстовые строки str в Python."), вершинa каталога,
-   `topdown=True` - [`bool`](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/bool-logicheskij-tip-dannyh/ "Логический тип данных bool в Python."), направление обхода,
-   `onerror=None` - [функция](https://docs-python.ru/tutorial/opredelenie-funktsij-python/ "Функции в Python, определение функций."), которая сообщает об ошибке,
-   `followlinks=False` - [`bool`](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/bool-logicheskij-tip-dannyh/ "Логический тип данных bool в Python."), переходить ли по символическим ссылкам.

**Возвращаемое значение:**
-   тройной [кортеж](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-tuple-kortezh/ "Кортеж tuple в Python.").

**Описание:**

Функция [`walk()`](https://docs-python.ru/standart-library/modul-os-python/funktsija-walk-modulja-os/ "Функция walk() модуля os в Python.") модуля [`os`](https://docs-python.ru/standart-library/modul-os-python/ "Модуль os в Python, доступ к функциям ОС.") генерирует имена файлов в дереве каталогов, обходя дерево сверху вниз или снизу вверх. Для каждого каталога в дереве с корнем в вершине каталога `top`, включая саму вершину `top`, она выдает тройной [кортеж](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-tuple-kortezh/ "Кортеж tuple в Python.") `(dirpath, dirnames, filenames)`.

-   `dirpath` - это строка, путь к каталогу.
-   `dirnames` - это список имен подкаталогов в `dirpath`, исключая [особые символы](https://docs-python.ru/standart-library/modul-os-python/znachenija-ispolzuemye-podderzhki-operatsij-putjami/ "Константы для поддержки операций с путями.") `'.'` и `'..'`.
-   `filenames` - это список имен файлов в `dirpath` (не-каталогов).

Обратите внимание, что имена в списках не содержат компонентов пути. Чтобы получить полный путь, который начинается с `top`, к файлу или каталогу в `dirpath`, выполните [`os.path.join(dirpath, name)`](https://docs-python.ru/standart-library/modul-os-path-python/funktsija-join-modulja-os-path/ "Функция join() модуля os.path в Python.").

Аргумент `top` может принимать объекты, представляющие путь к файловой системе, такие как [`pathlib.PurePath`](https://docs-python.ru/standart-library/modul-pathlib-python/klass-pathlib-purepath-podklassy/ "Класс pathlib.PurePath() и его подклассы.").

Если необязательный аргумент `topdown` имеет значение `True` или не указан, тройной [кортеж](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-tuple-kortezh/ "Кортеж tuple в Python.") для каталога создается перед тройным кортежем для любого из его подкаталогов, т. е. каталоги создаются сверху вниз. Если `topdown` имеет значение `False`, тройной [кортеж](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-tuple-kortezh/ "Кортеж tuple в Python.") для каталога создается после тройного кортежа для всех его подкаталогов, т. е. каталоги создаются снизу вверх. Независимо от значения `topdown`, список подкаталогов извлекается до создания кортежей для каталога и его подкаталогов.

Когда `topdown` имеет значение `True`, вызывающий объект может изменить список `dirnames` на месте, используя например [`del`](https://docs-python.ru/tutorial/instruktsija-del-python/ "Инструкция del в Python") или [`slice`](https://docs-python.ru/tutorial/obschie-operatsii-posledovatelnostjami-list-tuple-str-python/izvlechenie-sreza-sequence-posledovatelnosti/ "Получение среза sequence[i:j] в Python.") и функция [`os.walk()`](https://docs-python.ru/standart-library/modul-os-python/funktsija-walk-modulja-os/ "Функция walk() модуля os в Python.") будет возвращаться только в подкаталоги, чьи имена остаются в `dirnames`. Такое поведение может быть использовано для сокращения поиска, наложения определенного порядка посещения или даже для информирования `os.walk()` о каталогах, которые вызывающий абонент создает или переименовывает, прежде чем возобновится генерация имен файлов в дереве каталогов. Изменение `dirnames`, когда `topdown` имеет значение `False` не влияет на поведение обхода, поскольку в режиме снизу вверх каталоги с именами `dirname` генерируются до того, как генерируется сам `dirpath`.

По умолчанию ошибки из вызова [`os.scandir()`](https://docs-python.ru/standart-library/modul-os-python/funktsija-scandir-modulja-os/ "Функция scandir() модуля os в Python.") игнорируются. Если указан необязательный аргумент `onerror`, это должна быть функция, которая будет вызвана с одним аргументом - экземпляром [`OSError`](https://docs-python.ru/tutorial/vstroennye-iskljuchenija-interpretator-python/oshibki-operatsionnoj-sistemy-oserror/ "Исключения операционной системы: OSError в Python."). Функция может сообщить об ошибке, на основе которой можно будет принять решение о продолжении обхода дерева каталогов или прервать обход. Обратите внимание, что имя файла доступно как атрибут имени файла объекта исключения.

По умолчанию функция `os.walk()` не будет переходить по символическим ссылкам, которые ссылаются на каталоги. Установите для аргумента `followlinks` значение `True`, чтобы посещать каталоги, на которые указывают символические ссылки, в системах, которые их поддерживают.

**Примечания**:
-   Доступность: Unix.
-   Имейте в виду, что установка `followlinks=True` может привести к бесконечной рекурсии, если ссылка указывает на родительский каталог. Функция `os.walk()` не отслеживает уже посещенные каталоги.
-   Если вы передадите относительный путь, не меняйте текущий рабочий каталог между повторными выполнениями функции [`os.walk()`](https://docs-python.ru/standart-library/modul-os-python/funktsija-walk-modulja-os/ "Функция walk() модуля os в Python."). Функция `os.walk()` никогда не изменяет текущий каталог и предполагает, что его вызывающая сторона тоже не изменяет.

**Примеры практического применения функции `os.walk()`.**
В этом примере считается количество байтов, занятое файлами, не являющимися каталогами в каждом начальном каталоге, за исключением того, что не будем просматривать каталог `CVS` ни в одном подкаталоге:
```python
import os
from os.path import join, getsize

for root, dirs, files in os.walk('python/Lib/email'):
    print(root, "consumes", end=" ")
    print(sum(getsize(join(root, name)) for name in files), end=" ")
    print("bytes in", len(files), "non-directory files")
    if 'CVS' in dirs:
        # не просматриваем каталог `CVS`
        dirs.remove('CVS')
```

В следующем примере простая реализация функции [`shutil.rmtree()`](https://docs-python.ru/standart-library/modul-shutil-python/funktsija-rmtree-modulja-shutil/ "Функция rmtree() модуля shutil в Python."). В функции `os.walk()` указан обход дерева каталогов снизу вверх, это очень важно, т. к. [функция `os.rmdir()`](https://docs-python.ru/standart-library/modul-os-python/funktsija-rmdir-modulja-os/ "Функция rmdir() модуля os в Python.") не позволяет удалить каталог, пока он не пуст:

**ВНИМАНИЕ!** В примере удаляется все из каталога, указанного в переменной `top`, при условии, что нет символических ссылок. **Это опасно!** Например, если `top == '/'`, это может удалить все файлы на диске.
```python
import os

for root, dirs, files in os.walk(top, topdown=False):
    for name in files:
        os.remove(os.path.join(root, name))
    for name in dirs:
        os.rmdir(os.path.join(root, name))
```


## scandir()
[Получение информации о всех файлах в каталоге/директории в Python.](https://docs-python.ru/standart-library/modul-os-python/funktsija-scandir-modulja-os/ )

Функция `scandir()` модуля os возвращает итератор объектов `os.DirEntry`, соответствующих записям в каталоге, заданном путем path. Записи приводятся в произвольном порядке, а специальные символы `'.'` и `'..'` не включены.

**Синтаксис:**
```python
import os

os.scandir(path='.')
```

**Параметры:**
-   `path` - путь к каталогу, может принимать [`str`](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-str-tekstovye-stroki/ "Текстовые строки str в Python.") или [`bytes`](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-bytes-bajtovye-stroki/ "Байтовые строки bytes в Python.")

**Возвращаемое значение:**
-   [итератор](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-iterator-iterator/ "Итератор Iterator, протокол итератора в Python.") объектов [`os.DirEntry`](https://docs-python.ru/standart-library/modul-os-python/obekt-direntry-modulja-os/ "Объект DirEntry() модуля os в Python.")

**Описание:**

Функция [`scandir()`](https://docs-python.ru/standart-library/modul-os-python/funktsija-scandir-modulja-os/ "Функция scandir() модуля os в Python.") модуля [`os`](https://docs-python.ru/standart-library/modul-os-python/ "Модуль os в Python, доступ к функциям ОС.") возвращает итератор `entry_it` объектов [`os.DirEntry`](https://docs-python.ru/standart-library/modul-os-python/obekt-direntry-modulja-os/ "Объект DirEntry() модуля os в Python."), соответствующих записям в каталоге, заданном путем `path`. Записи приводятся в произвольном порядке, а [специальные символы](https://docs-python.ru/standart-library/modul-os-python/znachenija-ispolzuemye-podderzhki-operatsij-putjami/ "Константы для поддержки операций с путями.") `'.'` и `'..'` не включены.

Использование `os.scandir()` вместо [`os.listdir()`](https://docs-python.ru/standart-library/modul-os-python/funktsija-listdir-modulja-os/ "Функция listdir() модуля os в Python.") может значительно повысить производительность кода, который нуждается в информации о типе файла или атрибуте файла, поскольку объекты [`os.DirEntry`](https://docs-python.ru/standart-library/modul-os-python/obekt-direntry-modulja-os/ "Объект DirEntry() модуля os в Python.") предоставляют эту информацию, если операционная система предоставляет ее при сканировании каталога.

Все методы объекта `os.DirEntry` могут выполнять системный вызов, но для методов `os.DirEntry.is_dir()` и `os.DirEntry.is_file()` обычно требуется только системный вызов для символических ссылок. `os.DirEntry.stat()` всегда требует системного вызова в Unix, в Windows требуется только один системный вызов для символических ссылок.

Аргумент `path` может принимать объекты, представляющие путь к файловой системе, такие как [`pathlib.PurePath`](https://docs-python.ru/standart-library/modul-pathlib-python/klass-pathlib-purepath-podklassy/ "Класс pathlib.PurePath() и его подклассы."). Если путь имеет [байтовый типа](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-bytes-bajtovye-stroki/ "Байтовые строки bytes в Python."), переданный прямо с качестве байтовой строки или косвенно через интерфейс PathLike, тип атрибутов `name` и `path` каждого объекта `os.DirEntry` будет [байтовой строкой](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-bytes-bajtovye-stroki/ "Байтовые строки bytes в Python."), во всех остальных случаях они будут иметь [строковой тип](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-str-tekstovye-stroki/ "Текстовые строки str в Python.").

В OS Unix аргумент `path` также поддерживает [файловые дескрипторы](https://docs-python.ru/standart-library/modul-os-python/funktsija-supports-dir-fd-modulja-os/ "Функция supports_dir_fd модуля os в Python."), при этом дескриптор должен ссылаться на каталог `path`.

Функция [`scandir()`](https://docs-python.ru/standart-library/modul-os-python/funktsija-scandir-modulja-os/ "Функция scandir() модуля os в Python.") вызывает [событие аудита](https://docs-python.ru/standart-library/modul-sys-python/sobytie-audita-c/ "События аудита CPython.") `os.scandir` с аргументом `path`.

[Итератор](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-iterator-iterator/ "Итератор Iterator, протокол итератора в Python.") `os.scandir()` поддерживает [протокол менеджера контекста](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/kontekstnyj-menedzher-with/ "Контекстный менеджер with в Python") и имеет следующий метод:

**_`scandir.close()`_:**

Метод `scandir.close()` закрывает итератор и освобождает полученные ресурсы.

Этот метод вызывается автоматически, когда итератор исчерпан или когда происходит ошибка во время итерации. Однако рекомендуется вызывать его явно или использовать [оператор with](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/kontekstnyj-menedzher-with/ "Контекстный менеджер with в Python").

**Пример отображения всех файлов при помощи `scandir()`:**

В примере показано простое использование `scandir()` для отображения всех файлов, за исключением каталогов по указанному пути, которые не начинаются с `'.'`. Вызов `entry.is_file()` обычно не вызывает дополнительного системного вызова:

```python
with os.scandir(path) as it:
    for entry in it:
        if not entry.name.startswith('.') and entry.is_file():
            print(entry.name)
```

## DirEntry()
[Пути к файлу и другие атрибуты файлов os.scandir() в Python.](https://docs-python.ru/standart-library/modul-os-python/obekt-direntry-modulja-os/)

Объект `DirEntry()` модуля os получается в результате работы функции `os.scandir()`. Методы объекта `DirEntry()` предоставляют пути к файлу и другие атрибуты файлов, расположенных в сканируемом каталоге.

**Синтаксис:**
```python
import os

os.DirEntry

dirent = os.scandir(path)
```

**Описание:**

Объект [`DirEntry()`](https://docs-python.ru/standart-library/modul-os-python/obekt-direntry-modulja-os/ "Объект DirEntry() модуля os в Python.") модуля [`os`](https://docs-python.ru/standart-library/modul-os-python/ "Модуль os в Python, доступ к функциям ОС.") является результатом работы [функции `os.scandir()`](https://docs-python.ru/standart-library/modul-os-python/funktsija-scandir-modulja-os/ "Функция scandir() модуля os в Python."). Методы объекта `DirEntry()` предоставляют пути к файлу и другие атрибуты файлов, расположенных в сканируемом каталоге.

Функция `os.scandir()` предоставит как можно больше этой информации без дополнительных системных вызовов. Когда выполняется системный вызов `stat()` или `lstat()`, объект `os.DirEntry` будет кэшировать результат.

Экземпляры `os.DirEntry` не предназначены для хранения в долгоживущих структурах данных, если вы знаете, что метаданные файла изменились или прошло много времени с момента вызова `os.scandir()`, вызовите [`os.stat(entry.path)`](https://docs-python.ru/standart-library/modul-os-python/funktsija-stat-modulja-os/ "Функция stat() модуля os в Python.") для получения актуальной информации.

Поскольку методы `os.DirEntry` могут выполнять вызовы операционной системы, они также могут вызывать [исключение `OSError`](https://docs-python.ru/tutorial/vstroennye-iskljuchenija-interpretator-python/oshibki-operatsionnoj-sistemy-oserror/ "Исключения операционной системы: OSError в Python."). Если вам нужен очень детальный контроль над ошибками, вы можете перехватить исключение `OSError` при вызове одного из методов `os.DirEntry` и обработать его соответствующим образом.

Для использования [пути к файлам в качестве объекта](https://docs-python.ru/standart-library/modul-pathlib-python/klass-pathlib-purepath-podklassy/ "Класс pathlib.PurePath() и его подклассы.") [`os.DirEntry`](https://docs-python.ru/standart-library/modul-os-python/obekt-direntry-modulja-os/ "Объект DirEntry() модуля os в Python.") реализует [интерфейс `os.PathLike`](https://docs-python.ru/standart-library/modul-os-python/predstavlenie-puti-fajlovoj-sisteme/ "Представление пути в файловой системе.").

**Атрибуты и методы экземпляра `os.DirEntry`:**

**_`dirent.name`_:**

Атрибут `name` это базовое имя файла записи относительно аргумента пути [функции `os.scandir()`](https://docs-python.ru/standart-library/modul-os-python/funktsija-scandir-modulja-os/ "Функция scandir() модуля os в Python.").

Атрибут `name` будет [байтовым](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-bytes-bajtovye-stroki/ "Байтовые строки bytes в Python."), если аргумент пути `os.scandir()` имеет тип `bytes` и [строковым](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-str-tekstovye-stroki/ "Текстовые строки str в Python.") в противном случае. Используйте [`os.fsdecode()`](https://docs-python.ru/standart-library/modul-os-python/predstavlenie-puti-fajlovoj-sisteme/ "Представление пути в файловой системе.") для декодирования байтовых имен файлов.

**_`dirent.path`_:**

Атрибут `path` это полный путь к элементу в каталоге: эквивалент `os.path.join(scandir_path, entry.name)`, где `scandir_path` - аргумент пути функции `os.scandir()`. Путь является абсолютным, только если аргумент пути `os.scandir()` был абсолютным. Если аргумент пути `os.scandir()` был [дескриптором файла](https://docs-python.ru/standart-library/modul-os-python/funktsija-supports-dir-fd-modulja-os/ "Функция supports_dir_fd модуля os в Python."), то атрибут пути `path` будет совпадает с атрибутом имени `name`.

Атрибут `path` будет [байтовым](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-bytes-bajtovye-stroki/ "Байтовые строки bytes в Python."), если аргумент пути `os.scandir()` имеет тип `bytes` и [строковым](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-str-tekstovye-stroki/ "Текстовые строки str в Python.") в противном случае. Используйте [`os.fsdecode()`](https://docs-python.ru/standart-library/modul-os-python/predstavlenie-puti-fajlovoj-sisteme/ "Представление пути в файловой системе.") для декодирования байтовых имен файлов.

**_`dirent.inode()`_:**

Метод `inode()` вернет номер индекса записи. Результат кэшируется в объекте `os.DirEntry`. Используйте `os.stat(entry.path, follow_symlinks=False).st_ino` для получения актуальной информации.

При первом некэшированном вызове системный вызов требуется в Windows, но не в Unix.

**_`dirent.is_dir(*, follow_symlinks=True)`_:**

Метод `is_dir()` вернет `True`, если эта запись является каталогом или символической ссылкой, указывающей на каталог. Вернет `False`, если запись соответствует или указывает на любой другой тип файла или если каталог больше не существует.

Если `follow_symlinks=False`, то вернет `True` только если запись является каталогом, а не символической ссылкой на каталог. Вернет `False`, если запись представляет собой файл любого другого типа или каталог больше не существует.

Результат кэшируется в объекте `os.DirEntry`, с отдельным кешем для `follow_symlinks` `True` и `False`. Вызовите [`os.stat()`](https://docs-python.ru/standart-library/modul-os-python/funktsija-stat-modulja-os/ "Функция stat() модуля os в Python.") вместе с [функцией тестирования `stat.S_ISDIR()`](https://docs-python.ru/standart-library/konstanty-funktsii-os-stat/ "Модуль stat в Python, извлечение информации из stat_result."), чтобы получить актуальную информацию.

При первом вызове без кэширования в большинстве случаев не требуется системный вызов, за исключением некоторых файловых систем Unix, таких как сетевые файловые системы, которые возвращают `entry.d_type == DT_UNKNOWN`. Если запись является символической ссылкой и `follow_symlinks=True`, то системный вызов должен следовать по символической ссылке.

Этот метод может вызвать [исключение `OSError`](https://docs-python.ru/tutorial/vstroennye-iskljuchenija-interpretator-python/oshibki-operatsionnoj-sistemy-oserror/ "Исключения операционной системы: OSError в Python."), например `PermissionError`, но исключение `FileNotFoundError` перехватывается и не вызывается.

**_`dirent.is_file(*, follow_symlinks=True)`_:**

Метод `is_file()` вернет `True`, если эта запись является файлом или символической ссылкой, указывающей на файл. Вернет `False`, если запись является или указывает на каталог или другую нефайловую запись, или если она больше не существует.

Если `follow_symlinks=False`, возвращать `True` только если эта запись является файлом, а не символической ссылкой, указывающей на файл. Вернет `False`, если запись является каталогом или другой нефайловой записью, или если она больше не существует.

Результат кэшируется в объекте `os.DirEntry`. Кэширование, системные вызовы и создаваемые исключения соответствуют методу `entry.is_dir()`.

**_`dirent.is_symlink()`_:**

Метод `is_symlink()` вернет `True`, если эта запись является символической ссылкой, даже если она не работает. Вернет `False`, если запись указывает на каталог или какой-либо файл, или если символическая ссылка больше не существует.

Результат кэшируется в объекте `os.DirEntry`. Вызовите [`os.path.islink()`](https://docs-python.ru/standart-library/modul-os-path-python/funktsija-islink-modulja-os-path/ "Функция islink() модуля os.path в Python.") для получения актуальной информации.

При первом вызове без кэширования в большинстве случаев не требуется системный вызов, за исключением некоторых файловых систем Unix, таких как сетевые файловые системы, которые возвращают `dirent.d_type == DT_UNKNOWN`.

Этот метод может вызвать [исключение `OSError`](https://docs-python.ru/tutorial/vstroennye-iskljuchenija-interpretator-python/oshibki-operatsionnoj-sistemy-oserror/ "Исключения операционной системы: OSError в Python."), например `PermissionError`, но исключение `FileNotFoundError` перехватывается и не вызывается.

**_`dirent.stat(*, follow_symlinks=True)`_:**

Метод `stat()` вернет объект [`os.stat_result`](https://docs-python.ru/standart-library/modul-os-python/obekt-stat-result-modulja-os/ "Объект stat_result в Python, результаты выполнения os.stat().") для этой записи. Метод следует по символическим ссылкам по умолчанию, чтобы не переходить по символическим ссылкам, добавьте аргумент `follow_symlinks=False`.

В Unix, метод `stat()` всегда требует системного вызова. В Windows системный вызов требуется только в том случае, если `follow_symlinks` имеет значение `True`, а запись является точкой повторной обработки, например символическая ссылка или ссылка каталога.

В Windows атрибуты `os.stat_result.st_ino`, `os.stat_result.st_dev` и `os.stat_result.st_nlink` всегда устанавливаются на ноль. Вызовите [`os.stat()`](https://docs-python.ru/standart-library/modul-os-python/funktsija-stat-modulja-os/ "Функция stat() модуля os в Python."), чтобы получить эти атрибуты.

Результат кэшируется в объекте `os.DirEntry`, с отдельным кешем для `follow_symlinks` `True` и `False`. Вызовите [`os.stat()`](https://docs-python.ru/standart-library/modul-os-python/funktsija-stat-modulja-os/ "Функция stat() модуля os в Python."), чтобы получить актуальную информацию.

Обратите внимание, что существует хорошее соответствие между несколькими атрибутами и методами [`os.DirEntry`](https://docs-python.ru/standart-library/modul-os-python/obekt-direntry-modulja-os/ "Объект DirEntry() модуля os в Python.") и [`pathlib.Path`](https://docs-python.ru/standart-library/modul-pathlib-python/klass-pathlib-path-podklassy/ "Класс pathlib.Path() и его подклассы."). В частности, атрибут `name` имеет то же значение, что и методы `entry.is_dir()`, `entry.is_file()`, `entry.is_symlink()` и `entry.stat()`.

**Примеры использования:**

Функция `os.scandir()` возвращает последовательность экземпляров `os.DirEntry` для элементов в каталоге. Объект `os.DirEntry` имеет несколько атрибутов и методов для доступа к метаданным о файле. В этом примере будет осуществлен вывод элементов каталога `path` и его типа в файловой системе.

```python
import os
import sys

path = '.'
 t = 'unknown'
for entry in os.scandir(path):
    if entry.is_dir():
        t = 'dir'
    elif entry.is_file():
        t = 'file'
    elif entry.is_symlink():
        t = 'link'

    print(f'{entry.name} {t}')
```

## stat()
[Получить статистическую информацию о файле в Python.](https://docs-python.ru/standart-library/modul-os-python/funktsija-stat-modulja-os/)

Функция `stat()` модуля os получает статистическую информацию файла или дескриптора файла. Выполняет эквивалент системного вызова `stat()`. Функция `stat()` может поддерживать указание дескриптора файла и не следовать символическим ссылкам.

**Синтаксис:**
```python
import os

stat_result = os.stat(path, *, dir_fd=None, follow_symlinks=True)
```

**Параметры:**
-   `path` - путь до файла [строка](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-str-tekstovye-stroki/ "Текстовые строки str в Python.") или [bytes](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-bytes-bajtovye-stroki/ "Байтовые строки bytes в Python."),
-   `dir_fd=None` - [дескриптор каталога](https://docs-python.ru/standart-library/modul-os-python/funktsija-supports-dir-fd-modulja-os/ "Функция supports_dir_fd модуля os в Python."),
-   `follow_symlinks=True` - [bool](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/bool-logicheskij-tip-dannyh/ "Логический тип данных bool в Python."), переходить ли по символическим ссылкам.

**Возвращаемое значение:**
-   объект [`os.stat_result`](https://docs-python.ru/standart-library/modul-os-python/obekt-stat-result-modulja-os/ "Объект stat_result в Python, результаты выполнения os.stat().")

**Описание:**

Функция [`stat()`](https://docs-python.ru/standart-library/modul-os-python/funktsija-stat-modulja-os/ "Функция stat() модуля os в Python.") модуля [`os`](https://docs-python.ru/standart-library/modul-os-python/ "Модуль os в Python, доступ к функциям ОС.") получает статистическую информацию файла или дескриптора файла. Выполняет эквивалент системного вызова `stat()` по заданному пути. Путь `path` может быть указан в виде [строки](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-str-tekstovye-stroki/ "Текстовые строки str в Python.") или [bytes](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-bytes-bajtovye-stroki/ "Байтовые строки bytes в Python."), переданных прямо или косвенно через [интерфейс `os.PathLike`](https://docs-python.ru/standart-library/modul-os-python/predstavlenie-puti-fajlovoj-sisteme/ "Представление пути в файловой системе.") или как дескриптор открытого файла. Функция `stat()` вернет объект [`os.stat_result`](https://docs-python.ru/standart-library/modul-os-python/obekt-stat-result-modulja-os/ "Объект stat_result в Python, результаты выполнения os.stat().").

Функция `os.lstat()` эквивалентна вызову функции `os.stat()` с установленным аргументом `follow_symlinks=False`, например `os.stat(path, dir_fd=dir_fd, follow_symlinks=False)`.

Функция [`os.stat()`](https://docs-python.ru/standart-library/modul-os-python/funktsija-stat-modulja-os/ "Функция stat() модуля os в Python.") обычно переходит по символическим ссылкам к итоговому каталогу, чтобы получить информацию о символической ссылке добавьте аргумент `follow_symlinks=False` или используйте [функцию `os.lstat()`](https://docs-python.ru/standart-library/modul-os-python/funktsija-lstat-modulja-os/ "Функция lstat() модуля os в Python.").

Функция `stat()` может поддерживать пути относительно дескрипторов каталогов `dir_fd` и [не следовать символическим ссылкам](https://docs-python.ru/standart-library/modul-os-python/funktsija-supports-follow-symlinks-modulja-os/ "Функция supports_follow_symlinks модуля os в Python.") `follow_symlinks=None`.

Функция `oc.lchown()` эквивалентна вызову функции `oc.chown()` с установленным аргументом `follow_symlinks=False`, например `os.chown(path, uid, gid, follow_symlinks=False)`.

В Windows передача `follow_symlinks=False` отключит следование по всем точкам повторной обработки, включая символические ссылки и ссылки каталогов. Другие типы точек повторной обработки, которые не похожи на ссылки или которые операционная система не может выполнить, будут открыты напрямую. При переходе по цепочке из нескольких ссылок это может привести к возврату исходной ссылки, а не ссылки, которая помешала полному обходу. Чтобы получить результаты статистики для окончательного пути в этом случае, используйте функцию [os.path.realpath()](https://docs-python.ru/standart-library/modul-os-path-python/funktsija-realpath-modulja-os-path/ "Функция realpath() модуля os.path в Python."), чтобы максимально разрешить имя пути и вызовите [`os.lstat()`](https://docs-python.ru/standart-library/modul-os-python/funktsija-lstat-modulja-os/ "Функция lstat() модуля os в Python."). Это не относится к битым символическим ссылкам или точкам соединения, которые вызовут обычные исключения.

**Примеры использования:**
```python
>>> import os
>>> statinfo = os.stat('somefile.txt')
>>> statinfo
os.stat_result(st_mode=33188, st_ino=7876932, st_dev=234881026,
st_nlink=1, st_uid=501, st_gid=501, st_size=264, st_atime=1297230295,
st_mtime=1297230027, st_ctime=1297230027)
>>> statinfo.st_size
264
```


## Объект stat_result в Python, результаты выполнения os.stat().
[Получение результатов вызова os.stat() в Python.](https://docs-python.ru/standart-library/modul-os-python/obekt-stat-result-modulja-os/)

Объект `stat_result` модуля `os` имеет атрибуты, которые примерно соответствуют членам структуры системного вызова `stat`.

**Синтаксис:**

```python
import os

os.stat_result

stat_info = os.stat(...)
```

**Описание:**

Объект [`stat_result`](https://docs-python.ru/standart-library/modul-os-python/obekt-stat-result-modulja-os/ "Объект stat_result в Python, результаты выполнения os.stat().") модуля [`os`](https://docs-python.ru/standart-library/modul-os-python/ "Модуль os в Python, доступ к функциям ОС.") имеет атрибуты, которые примерно соответствуют членам структуры системного вызова `stat`. Объект `os.stat_result` является результатом выполнения таких функций, как [`os.stat()`](https://docs-python.ru/standart-library/modul-os-python/funktsija-stat-modulja-os/ "Функция stat() модуля os в Python."), [`os.fstat()`](https://docs-python.ru/standart-library/modul-os-python/sozdanie-deskriptora-chtenie-zapis-zakrytie/ "Создание дескриптора файла, чтение, запись и его закрытие.") и [`os.lstat()'](https://docs-python.ru/standart-library/modul-os-python/funktsija-lstat-modulja-os/ "Функция lstat() модуля os в Python.").

Для обратной совместимости экземпляр `os.stat_result` также доступен [в виде кортежа](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-tuple-kortezh/ "Кортеж tuple в Python.") из не менее 10 [целых чисел](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-int-tselye-chisla/ "Целые числа int в Python."), дающих наиболее важные и переносимые члены структуры `stat`, в следующем порядке: `st_mode`, `st_ino`, `st_dev`, `st_nlink`, `st_uid`, `st_gid`, `st_size`, `st_atime`, `st_mtime`, `st_ctime`. В конце некоторых реализаций может быть добавлено больше элементов. Для совместимости со старыми версиями Python доступ к `stat_result` [в виде кортежа](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-tuple-kortezh/ "Кортеж tuple в Python.") всегда возвращает целые числа.

[Стандартный модуль `stat`](https://docs-python.ru/standart-library/konstanty-funktsii-os-stat/ "Модуль stat в Python, извлечение информации из stat_result.") определяет функции и константы, которые полезны для извлечения информации из структуры системного вызова `stat`. В Windows некоторые элементы заполнены фиктивными значениями.

**Атрибуты объекта `os.stat_result`:**

_`stat_info.st_mode`_:

Режим файла: биты типа файла и разрешения файла.

_`stat_info.st_ino`_:

Зависит от платформы, но если не ноль, однозначно идентифицирует файл для данного значения `st_dev`.

Как правило:
-   номер inode в Unix,
-   индекс файла в Windows

_`stat_info.st_dev`_:

Идентификатор устройства, на котором находится этот файл.

_`stat_info.st_nlink`_:

Количество жестких ссылок.

_`stat_info.st_uid`_:

Идентификатор пользователя владельца файла.

_`stat_info.st_gid`_:

Групповой идентификатор владельца файла.

_`stat_info.st_size`_:

Размер файла в байтах, если это обычный файл или символическая ссылка. Размер символической ссылки - это длина имени пути, которое он содержит, без завершающего нулевого байта.

**Отметки времени `timestamp`:**

_`stat_info.st_atime`_:

Время последнего доступа, выраженное в секундах.

_`stat_info.st_mtime`_:

Время последней модификации контента, выраженное в секундах.

_`stat_info.st_ctime`_:

Зависимость от платформы:

-   время последнего изменения метаданных в Unix,
-   время создания в Windows, выраженное в секундах.

_`stat_info.st_atime_ns`_:

Время последнего доступа, выраженное в наносекундах как целое число.

_`stat_info.st_mtime_ns`_:

Время последней модификации контента, выраженное в наносекундах как целое число.

_`stat_info.st_ctime_ns`_:

**Зависимость от платформы:**
-   время последнего изменения метаданных в Unix,
-   время создания в Windows, выраженное в наносекундах как целое число.

**Обратите внимание**, что точное значение и разрешение атрибутов `st_atime`, `st_mtime` и `st_ctime` зависят от операционной системы и файловой системы. Например в системах Windows, использующих файловые системы `FAT` или `FAT32`, разрешение `st_mtime` составляет 2 секунды, а разрешение `st_atime` только 1 день. Дополнительные сведения смотрите в документации по операционной системе.

Аналогично `st_time_ns`, `st_mtime_ns` и `st_ctime_ns` всегда выражаются в наносекундах, многие системы не обеспечивают наносекундной точности. В системах, которые действительно обеспечивают наносекундную точность, объект с плавающей точкой, используемый для хранения `st_atime`, `st_mtime` и `st_ctime` не может сохранить все это и поэтому будет немного неточным. Если вам нужны точные временные метки, вы всегда должны использовать `st_time_ns`, `st_mtime_ns` и `st_ctime_ns`.

В некоторых системах Unix, например Linux, доступны атрибуты:

_`stat_info.st_blocks`_:

Количество 512-байтовых блоков, выделенных для файла. Это может быть меньше, чем `st_size/512`, когда файл имеет ошибки.

_`stat_info.st_blksize`_:

Предпочтительный размер блока для эффективного ввода/вывода файловой системы. Запись в файл небольшими порциями может привести к неэффективному чтению/изменению/перезаписи.

_`stat_info.st_rdev`_:

Тип устройства, если устройство inode.

_`stat_info.st_flags`_:

Пользовательские флаги для файла.

**В других системах Unix, таких как FreeBSD, доступны атрибуты пользователю root:**

_`stat_info.st_gen`_:

Номер генерации файла.

_`stat_info.st_birthtime`_:

Время создания файла.

**В Solaris и производных от него доступны атрибуты:**

_`stat_info.st_fstype`_:

Строка, которая однозначно определяет тип файловой системы, в которой находится файл.

**В системах Mac OS доступны атрибуты:**

_`stat_info.st_rsize`_:

Реальный размер файла.

_`stat_info.st_creator`_:

Создатель файла.

_`stat_info.st_type`_:

Тип файла.

**В системах Windows доступны атрибуты:**

_`stat_info.st_file_attributes`_:

Атрибуты файла Windows: `dwFileAttributes` член структуры `BY_HANDLE_FILE_INFORMATION`, возвращаемой функцией `GetFileInformationByHandle()`. Смотрите константы `FILE_ATTRIBUTE_*` в модуле статистики.

_`stat_info.st_reparse_tag`_:

Когда `st_file_attributes` имеет установленный `FILE_ATTRIBUTE_REPARSE_POINT`, это поле содержит тег, идентифицирующий тип точки повторной обработки. Смотрите константы `IO_REPARSE_TAG_*` в модуле статистики.

**Примеры получения результатов из объекта `stat_result`:**
```python
import os
import time

filename = 'stat_result.py'
stat_info = os.stat(filename)

print(f'os.stat({filename}):)
print('  Size:', stat_info.st_size)
print('  Permissions:', oct(stat_info.st_mode))
print('  Owner:', stat_info.st_uid)
print('  Device:', stat_info.st_dev)
print('  Created      :', time.ctime(stat_info.st_ctime))
print('  Last modified:', time.ctime(stat_info.st_mtime))
print('  Last accessed:', time.ctime(stat_info.st_atime))

# os.stat(stat_result.py):
#   Size: 593
#   Permissions: 0o100644
#   Owner: 527
#   Device: 16777218
#   Created      : Wen Mar 18 12:09:51 2020
#   Last modified: Wen Mar 18 12:09:51 2020
#   Last accessed: Wen Mar 18 12:33:19 2020
```

## lstat()
[Выполнить системный вызов lstat() в Python.](https://docs-python.ru/standart-library/modul-os-python/funktsija-lstat-modulja-os/)

Функция `lstat()` модуля `os` выполняет эквивалент системного вызова `lstat()` для данного пути. Похож на `os.stat()`, но не следует по символическим ссылкам.

**Синтаксис:**
```python
import os

os.lstat(path, *, dir_fd=None)
```

**Параметры:**
-   `path` - путь до файла,
-   `dir_fd=None` - дескриптор каталога

**Возвращаемое значение:**
-   объект [`os.stat_result`](https://docs-python.ru/standart-library/modul-os-python/obekt-stat-result-modulja-os/ "Объект stat_result в Python, результаты выполнения os.stat().")

**Описание:**

Функция [`lstat()`](https://docs-python.ru/standart-library/modul-os-python/funktsija-lstat-modulja-os/ "Функция lstat() модуля os в Python.") модуля [`os`](https://docs-python.ru/standart-library/modul-os-python/ "Модуль os в Python, доступ к функциям ОС.") выполняет эквивалент системного вызова `lstat()` для данного пути. Похож на [`os.stat()`](https://docs-python.ru/standart-library/modul-os-python/funktsija-stat-modulja-os/ "Функция stat() модуля os в Python."), но не следует по символическим ссылкам. Функция `os.lstat()` возвращает [объект `os.stat_result`](https://docs-python.ru/standart-library/modul-os-python/obekt-stat-result-modulja-os/ "Объект stat_result в Python, результаты выполнения os.stat().").

На платформах, которые не поддерживают символические ссылки, это псевдоним [`os.stat()`](https://docs-python.ru/standart-library/modul-os-python/funktsija-stat-modulja-os/ "Функция stat() модуля os в Python.").

Функция `os.lstat()` эквивалентно вызову функции с указанием параметров по умолчанию `os.stat(path, dir_fd=dir_fd, follow_symlinks=False)`.

Функция также может поддерживать пути относительно дескрипторов каталогов `dir_fd`.

Аргумент `path` может принимать объекты, представляющие путь файловой системы, такие как [`pathlib.PurePath`](https://docs-python.ru/standart-library/modul-pathlib-python/klass-pathlib-purepath-podklassy/ "Класс pathlib.PurePath() и его подклассы.").

**Примеры использования:**
```python
# stat_result.py

import os
import time

filename = 'stat_result.py'
stat_info = os.lstat(filename)

print(f'os.lstat({filename}):')
print('  Size:', stat_info.st_size)
print('  Permissions:', oct(stat_info.st_mode))
print('  Owner:', stat_info.st_uid)
print('  Device:', stat_info.st_dev)
print('  Created      :', time.ctime(stat_info.st_ctime))
print('  Last modified:', time.ctime(stat_info.st_mtime))
print('  Last accessed:', time.ctime(stat_info.st_atime))

# os.lstat(stat_result.py):
#   Size: 446
#   Permissions: 0o100664
#   Owner: 1000
#   Device: 66305
#   Created      : Wed Mar 18 09:36:36 2020
#   Last modified: Wed Mar 18 09:36:36 2020
#   Last accessed: Wed Mar 18 09:36:36 2020
```


## access()
[Проверить доступ пользователя к файлу или директории в Python.](https://docs-python.ru/standart-library/modul-os-python/funktsija-access-modulja-os/ )

Функция `access()` проверяет доступ к пути `path` для реальных `uid`/`gid`. Эту процедуру можно использовать в среде `suid`/`sgid` для проверки, имеет ли вызывающий пользователь указанный доступ к пути `path`

**Синтаксис:**
```python
import os

os.access(path, mode, *, dir_fd=None, effective_ids=False, follow_symlinks=True)
```

**Параметры:**
-   `path` - [`str`](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-str-tekstovye-stroki/ "Текстовые строки str в Python.") путь в файловой системе,
-   `mode` - [проверяемый доступ](https://docs-python.ru/standart-library/modul-os-python/funktsija-access-modulja-os/#rwx_ok),
-   `dir_fd=None` - путь относительно [дескриптор каталога](https://docs-python.ru/standart-library/modul-os-python/funktsija-supports-dir-fd-modulja-os/ "Функция supports_dir_fd модуля os в Python."),
-   `effective_ids=False` - [`bool`](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/bool-logicheskij-tip-dannyh/ "Логический тип данных bool в Python."), использование эффективных или реальных `uid`/`gid`,
-   `follow_symlinks=True` - [`bool`](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/bool-logicheskij-tip-dannyh/ "Логический тип данных bool в Python."), переходить ли по ссылкам.

**Возвращаемое значение:**
-   [bool](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/bool-logicheskij-tip-dannyh/ "Логический тип данных bool в Python.").

**Описание:**

Функция [`access()`](https://docs-python.ru/standart-library/modul-os-python/funktsija-access-modulja-os/ "Функция access() модуля os в Python.") модуля [`os`](https://docs-python.ru/standart-library/modul-os-python/ "Модуль os в Python, доступ к функциям ОС.") проверяет доступ к пути `path` для [реальных `uid`/`gid`](https://docs-python.ru/standart-library/modul-os-python/izvlechenie-ustanovka-uid-gid-pid-protsessa/ "Извлечение/установка uid, gid и pid процесса."). Обратите внимание, что в большинстве операций используется [эффективный `uid`/`gid`](https://docs-python.ru/standart-library/modul-os-python/izvlechenie-ustanovka-uid-gid-pid-protsessa/ "Извлечение/установка uid, gid и pid процесса."), поэтому эту процедуру можно использовать в среде `suid`/`sgid` для проверки, имеет ли вызывающий пользователь указанный доступ к пути `path`.

Аргумент `path` может принимать объекты, представляющие путь к файловой системе, такие как [`pathlib.PurePath`](https://docs-python.ru/standart-library/modul-pathlib-python/klass-pathlib-purepath-podklassy/ "Класс pathlib.PurePath() и его подклассы.").

Аргумент `mode` должен быть `os.F_OK` для проверки существования пути. для проверки прав доступа режимы проверки [`os.R_OK`, `os.W_OK` и `os.X_OK`](https://docs-python.ru/standart-library/modul-os-python/funktsija-access-modulja-os/#rwx_ok) можно объединять при помощи побитового ИЛИ `'|'`.

Функция `os.access()` вернет `True`, если доступ разрешен, `False`, если нет.

Функция может поддерживать указание путей относительно [дескрипторов каталогов `dir_fd`](https://docs-python.ru/standart-library/modul-os-python/funktsija-supports-dir-fd-modulja-os/ "Функция supports_dir_fd модуля os в Python.") и [не следовать по символическими ссылками](https://docs-python.ru/standart-library/modul-os-python/funktsija-supports-follow-symlinks-modulja-os/ "Функция supports_follow_symlinks модуля os в Python.") `follow_symlinks=True`.

Если значение `effective_ids` равно `True`, то [`os.access()`](https://docs-python.ru/standart-library/modul-os-python/funktsija-access-modulja-os/ "Функция access() модуля os в Python.") выполнит свои проверки доступа, используя эффективный `uid`/`gid` вместо реального `uid`/`gid`. Аргумент `effective_ids` может не поддерживаться на вашей платформе. Вы можете проверить, доступен ли он, используя [`os.supports_effective_ids`](https://docs-python.ru/standart-library/modul-os-python/funktsija-supports-effective-ids-modulja-os/ "Функция supports_effective_ids модуля os в Python."). Если он недоступен, его использование вызовет [исключение `NotImplementedError`](https://docs-python.ru/tutorial/vstroennye-iskljuchenija-interpretator-python/vstroennye-iskljuchenija/ "Исключения наследуемые от Exception в Python.").

**Примечание**. НЕ используйте `os.access()` для проверки того, возможно ли [открыть файл функцией `open()`](https://docs-python.ru/tutorial/vstroennye-funktsii-interpretatora-python/funktsija-open/ "Функция open() в Python, открывает файл на чтение/запись.") перед тем как прочитать его. Используя функцию `os.access()` можно создать дыру в безопасности, потому что пользователь может использовать короткий промежуток времени между проверкой и открытием файла, чтобы манипулировать им.
```python
# не используйте такую проверку
if os.access("myfile", os.R_OK):
    with open("myfile") as fp:
        return fp.read()
return "some default data"

# лучше сделать так
try:
    fp = open("myfile")
except PermissionError:
    return "some default data"
else:
    with fp:
        return fp.read()
```

**Примечание**. Операции ввода-вывода могут завершаться ошибкой, даже если `os.access()` покажет, что они будут выполнены успешно, особенно для операций с сетевыми файловыми системами, у которых может быть семантика разрешений, выходящая за рамки обычной модели битов разрешений POSIX.

**Пример:**
```python
# test_access.py
import os

print('Testing:', __file__)
print('Exists:', os.access(__file__, os.F_OK))
print('Readable:', os.access(__file__, os.R_OK))
print('Writable:', os.access(__file__, os.W_OK))
print('Executable:', os.access(__file__, os.X_OK))

# Testing: test_access.py
# Exists: True
# Readable: True
# Writable: True
# Executable: False
```

**Константы прав доступа.**

`os.F_OK`,  
`os.R_OK`,  
`os.W_OK`,  
`os.X_OK`_:

Это значения для передачи в качестве параметра `mode` в функцию проверки режима доступа [`os.access()`](https://docs-python.ru/standart-library/modul-os-python/funktsija-access-modulja-os/ "Функция access() модуля os в Python.").

-   `os.F_OK` - проверка существования файла или каталога,
-   `os.R_OK` - проверка возможности чтения,
-   `os.W_OK` - проверка возможности записи,
-   `os.X_OK` - проверка выполнения файла или открытия директории

## chdir()
[Смена рабочей директории из кода в Python.](https://docs-python.ru/standart-library/modul-os-python/funktsija-chdir-modulja-os/)

Функция `chdir()` модуля `os` изменяет текущий рабочий каталог.

**Синтаксис:**
```python
import os

os.chdir(path)
```
**Параметры:**
-   `path` - [`str`](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-str-tekstovye-stroki/ "Текстовые строки str в Python."), путь файловой системы.

**Возвращаемое значение:**
-   None

**Описание:**
Функция [`chdir()`](https://docs-python.ru/standart-library/modul-os-python/funktsija-chdir-modulja-os/ "Функция chdir() модуля os в Python.") модуля [`os`](https://docs-python.ru/standart-library/modul-os-python/ "Модуль os в Python, доступ к функциям ОС.") изменяет текущий рабочий каталог. Аргумент `path` может принимать объекты, представляющие путь файловой системы, такие как [`pathlib.PurePath`](https://docs-python.ru/standart-library/modul-pathlib-python/klass-pathlib-purepath-podklassy/ "Класс pathlib.PurePath() и его подклассы.")
Эта функция может поддерживать указание [дескриптора файла `dir_fd`](https://docs-python.ru/standart-library/modul-os-python/funktsija-supports-dir-fd-modulja-os/ "Функция supports_dir_fd модуля os в Python."). Дескриптор должен ссылаться на открытый каталог, а не на открытый файл.

Эта функция может вызывать [исключение `OSError`](https://docs-python.ru/tutorial/vstroennye-iskljuchenija-interpretator-python/oshibki-operatsionnoj-sistemy-oserror/ "Исключения операционной системы: OSError в Python.") и подклассы, такие как [`FileNotFoundError`, `PermissionError` и `NotADirectoryError`](https://docs-python.ru/tutorial/vstroennye-iskljuchenija-interpretator-python/oshibki-operatsionnoj-sistemy-oserror/ "Исключения операционной системы: OSError в Python.").

Вызывает [событий аудита](https://docs-python.ru/standart-library/modul-sys-python/sobytie-audita-c/ "События аудита CPython.") os.chdir с аргументом `path`.

**Примеры использования:**
```python
>>> import os
>>> os.getcwd()
# '/home/docs-python'

>>> os.chdir(os.pardir)
>>> os.getcwd()
# '/home'
```

## chmod() 
[Изменить режим доступа к файлу/директории в Python.](https://docs-python.ru/standart-library/modul-os-python/funktsija-chmod-modulja-os/ )

Функция `chmod()` модуля `os` изменяет режим доступа к файлу или директории, указанного в `path`

**Синтаксис:**
```python
import os

os.chmod(path, mode, *, dir_fd=None, follow_symlinks=True)
os.lchmod(path, mode)
```
**Параметры:**
-   `path` - [`str`](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-str-tekstovye-stroki/ "Текстовые строки str в Python.") путь в файловой системе,
-   `mode` - [режим доступа](https://docs-python.ru/standart-library/modul-os-python/funktsija-chmod-modulja-os/#mode),
-   `dir_fd=None` - путь относительно [дескриптор каталога](https://docs-python.ru/standart-library/modul-os-python/funktsija-supports-dir-fd-modulja-os/ "Функция supports_dir_fd модуля os в Python."),
-   `follow_symlinks=True` - [`bool`](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/bool-logicheskij-tip-dannyh/ "Логический тип данных bool в Python."), переходить ли по ссылкам.

**Возвращаемое значение:**
-   `None`

**Описание:**

Функция [`chmod()`](https://docs-python.ru/standart-library/modul-os-python/funktsija-chmod-modulja-os/ "Функция chmod() модуля os в Python.") модуля [`os`](https://docs-python.ru/standart-library/modul-os-python/ "Модуль os в Python, доступ к функциям ОС.") изменяет режим доступа к файлу или директории, указанного в `path`.Функция `os.lchmod()` эквивалентна вызову функции с следующими установленными аргументами `os.chmod(path, mode, follow_symlinks=False)`.

Аргумент `mode` может принимать последние 3 цифры восьмеричного представления числа, например `0o755` или одно или несколько из следующих значений, значения которых приведены в [модуле `stat`](https://docs-python.ru/standart-library/konstanty-funktsii-os-stat/ "Модуль stat в Python, извлечение информации из stat_result."):

**Возможные значения `mode`:**

-   `stat.S_ISUID` - Устанавливает бит идентификатора пользователя.
-   `stat.S_ISGID` - Устанавливает бит идентификатора группы. Этот бит имеет несколько специальных применений.
    - Для каталога это означает, что файлы наследуют идентификатор своей группы из каталога, а не от эффективного идентификатора группы процесса создания, и созданные там каталоги также получат установленный бит S_ISGID.
    - Для файла, который не имеет установленного бита выполнения группы `S_IXGRP`, бит set-group-ID указывает на обязательную блокировку файла/записей (смотрите также `S_ENFMT`).
-   `stat.S_ISVTX` - Липкий бит. Когда этот бит установлен в каталоге, это означает, что файл в этом каталоге может быть переименован или удален только владельцем файла, владельцем каталога или привилегированным процессом.
-   `stat.S_IRWXU` - Маска устанавливает для пользователя права `rwx`.
-   `stat.S_IRUSR` - Владелец имеет разрешение на чтение.
-   `stat.S_IWUSR` - Владелец имеет разрешение на запись.
-   `stat.S_IXUSR` - Владелец имеет разрешение на исполнение.,
-   `stat.S_IRWXG` - Маска устанавливает для группы права `rwx`.
-   `stat.S_IRGRP` - Группа имеет разрешение на чтение.
-   `stat.S_IWGRP` - Группа имеет разрешение на запись.
-   `stat.S_IXGRP` - Группа имеет разрешение на исполнение.
-   `stat.S_IRWXO` - Маска устанавливает для других (не в группе) права `rwx`.
-   `stat.S_IROTH` - Другие имеет разрешение на чтение.
-   `stat.S_IWOTH` - Другие имеет разрешение на запись.
-   `stat.S_IXOTH` - Другие имеет разрешение на исполнение.
-   `stat.S_ENFMT` - Система V принудительно блокирует файлы. Этот флаг используется совместно с SISGID: блокировка файлов/записей применяется к файлам, для которых не установлен бит выполнения группы (SIXGRP),
-   `stat.S_IREAD` - Unix V7 синоним для S_IRUSR.
-   `stat.S_IWRITE` - Unix V7 синоним для S_IWUSR.
-   `stat.S_IEXEC` - Unix V7 синоним для S_IXUSR.

Приведенные выше значения можно комбинировать побитовым ИЛИ `'|'`, например `stat.S_IRWXU|stat.S_IRGRP|stat.S_IXGRP|stat.S_IROTH`. Данная комбинация установит разрешение `rwxr-xr--` для пути, указанного в `path`.

Аргумент `path` может принимать объекты, представляющие путь файловой системы, такие как [`pathlib.PurePath`](https://docs-python.ru/standart-library/modul-pathlib-python/klass-pathlib-purepath-podklassy/ "Класс pathlib.PurePath() и его подклассы.").

Функция [`chmod()`](https://docs-python.ru/standart-library/modul-os-python/funktsija-chmod-modulja-os/ "Функция chmod() модуля os в Python.") может поддерживать указание [дескриптора файла](https://docs-python.ru/standart-library/modul-os-python/funktsija-supports-fd-modulja-os/ "Функция supports_fd модуля os в Python."), [пути относительно дескрипторов](https://docs-python.ru/standart-library/modul-os-python/funktsija-supports-dir-fd-modulja-os/ "Функция supports_dir_fd модуля os в Python.") каталога и [не следовать символическим ссылкам](https://docs-python.ru/standart-library/modul-os-python/funktsija-supports-follow-symlinks-modulja-os/ "Функция supports_follow_symlinks модуля os в Python.") `follow_symlinks=False`.

**Примечание**. Несмотря на то, что Windows поддерживает `os.chmod()`, можно установить для него флаг только для чтения через константы [`stat.S_IWRITE` и `stat.S_IREAD`](https://docs-python.ru/standart-library/modul-os-python/funktsija-chmod-modulja-os/#mode) или соответствующее целочисленное значение. Все остальные биты игнорируются.

Вызывает [событие аудита](https://docs-python.ru/standart-library/modul-sys-python/sobytie-audita-c/ "События аудита CPython.") `os.chmod` с аргументами `path`, `mode`, `dir_fd`.

**Примеры использования:**
```python
>>> import os, stat
>>> f = 'tt.py'
>>> st = os.stat(f).st_mode
>>> stat.filemode(st)
# '-rw-rw-r--'

>>> os.chmod(f, 0o754)
>>> st = os.stat(f).st_mode
>>> stat.filemode(st)
# '-rwxr-xr--'
```
Этот пример переключает бит разрешения пользователя на выполнение:
```python
import os
import stat

filename = 'tt.txt'
if os.path.exists(filename):
    os.unlink(filename)
with open(filename, 'wt') as f:
    f.write('contents')

# Определим установленные разрешения
existing_permissions = stat.S_IMODE(os.stat(filename).st_mode)

if not os.access(filename, os.X_OK):
    print('Добавим разрешение на запуск "x"')
    new_permissions = existing_permissions | stat.S_IXUSR
else:
    print('Удалим разрешения на выполнение "x"')
    # use xor to remove the user execute permission
    new_permissions = existing_permissions ^ stat.S_IXUSR

os.chmod(filename, new_permissions)
```

## chown()
[Изменить пользователя и группу у файла или каталога в Python.](https://docs-python.ru/standart-library/modul-os-python/funktsija-chown-modulja-os/)

Функция `chown()` изменяет владельца и идентификатор группы пути на числовые значения `uid` и `gid`

**Синтаксис:**
```python
import os

os.chown(path, uid, gid, *, dir_fd=None, follow_symlinks=True)
os.lchown(path, uid, gid)
```

**Параметры:**
-   `path` - [`str`](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-str-tekstovye-stroki/ "Текстовые строки str в Python.") путь в файловой системе.
-   `uid` - [числовой](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-int-tselye-chisla/ "Целые числа int в Python.") идентификатор пользователя
-   `gid` - [числовой](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-int-tselye-chisla/ "Целые числа int в Python.") идентификатор группы
-   `dir_fd=None` - [дескрипторов каталога](https://docs-python.ru/standart-library/modul-os-python/funktsija-supports-dir-fd-modulja-os/ "Функция supports_dir_fd модуля os в Python.")
-   `follow_symlinks=True` - [`bool`](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/bool-logicheskij-tip-dannyh/ "Логический тип данных bool в Python."), переходить ли по ссылкам.

**Возвращаемое значение:**
-   `None`

**Описание**:

Функция [`chown()`](https://docs-python.ru/standart-library/modul-os-python/funktsija-chown-modulja-os/ "Функция chown() модуля os в Python.") модуля [`os`](https://docs-python.ru/standart-library/modul-os-python/ "Модуль os в Python, доступ к функциям ОС.") изменяет владельца и идентификатор группы пути на числовые значения `uid` и `gid`. Чтобы оставить один из идентификаторов без изменений, установите его на -1.

Функция `os.lchown()` эквивалентна вызову функции `os.chown()` с установленным аргументом `follow_symlinks=False`, например `os.chown(path, uid, gid, follow_symlinks=False)`.

Аргумент `path` в обоих функциях может принимать объекты, представляющие путь файловой системы, такие как [`pathlib.PurePath`](https://docs-python.ru/standart-library/modul-pathlib-python/klass-pathlib-purepath-podklassy/ "Класс pathlib.PurePath() и его подклассы.").

Функция `os.chown()` может поддерживать указание [дескриптора файла `fd`](https://docs-python.ru/standart-library/modul-os-python/funktsija-supports-fd-modulja-os/ "Функция supports_fd модуля os в Python."), пути относительно [дескрипторов каталога `dir_fd`](https://docs-python.ru/standart-library/modul-os-python/funktsija-supports-dir-fd-modulja-os/ "Функция supports_dir_fd модуля os в Python.") и может [не следовать символическим ссылкам](https://docs-python.ru/standart-library/modul-os-python/funktsija-supports-follow-symlinks-modulja-os/ "Функция supports_follow_symlinks модуля os в Python.") `follow_symlinks=False`.

Смотрите функцию более высокого уровня [`shutil.chown()`](https://docs-python.ru/standart-library/modul-shutil-python/funktsija-chown-modulja-shutil/ "Функция chown() модуля shutil в Python.") которая принимает имена пользователей и групп в дополнение к числовым идентификаторам.

Вызывает [событие аудита](https://docs-python.ru/standart-library/modul-sys-python/sobytie-audita-c/ "События аудита CPython.") `os.chown` с аргументами `path`, `uid`, `gid`, `dir_fd`. Обе функции требуют привилегии суперпользователя root.

Доступность: Unix.

**Примеры использования:**
```python
import os
f = 'tt.py'
os.stat(f).st_gid
# 1000
os.stat(f).st_uid
# 1000

os.chown(f, -1, 1001)
os.stat(f).st_gid
# 1001
os.stat(f).st_uid
# 1000
```


## chroot()
[Изменить корневой каталог текущего процесса в Python.](https://docs-python.ru/standart-library/modul-os-python/funktsija-chroot-modulja-os/ )

Функция `chroot()` модуля `os` изменяет корневой каталог текущего процесса на путь файловой системы `path`.

**Синтаксис:**
```python
import os

os.chroot(path)
````

**Параметры:**
- `path` - [`str`](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-str-tekstovye-stroki/ "Текстовые строки str в Python.") путь в файловой системе.

**Возвращаемое значение:**
- `None`

**Описание:**

Функция [`chroot()`](https://docs-python.ru/standart-library/modul-os-python/funktsija-chroot-modulja-os/ "Функция chroot() модуля os в Python.") модуля [`os`](https://docs-python.ru/standart-library/modul-os-python/ "Модуль os в Python, доступ к функциям ОС.") изменяет корневой каталог текущего процесса на путь файловой системы `path`. Требуются права суперпользователя root.

Аргумент `path` может принимать объекты, представляющие путь файловой системы, такие как [`pathlib.PurePath`](https://docs-python.ru/standart-library/modul-pathlib-python/klass-pathlib-purepath-podklassy/ "Класс pathlib.PurePath() и его подклассы.").

Доступность: Unix.

**Примеры использования:**
```python
>>> import os
>>> os.chroot(os.getcwd() + '/venv')
```


## getcwd()
[Узнать текущий рабочий каталог в Python.](https://docs-python.ru/standart-library/modul-os-python/funktsija-getcwd-modulja-os/)

Функция `getcwd()` вернет строку, а функция `getcwdb()` вернет строку байтов представляющую текущий рабочий каталог.

**Синтаксис:**
```python
import os

os.getcwd()
os.getcwdb()
```

**Параметры:**
-   Нет.

**Возвращаемое значение:**
-   текущий рабочий каталог.

**Описание:**

Функция [`getcwd()`](https://docs-python.ru/standart-library/modul-os-python/funktsija-getcwd-modulja-os/ "Функция getcwd() модуля os в Python.") модуля [`os`](https://docs-python.ru/standart-library/modul-os-python/ "Модуль os в Python, доступ к функциям ОС.") вернет [строку](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-str-tekstovye-stroki/ "Текстовые строки str в Python."), представляющую текущий рабочий каталог.Функция `getcwdb()` вернет [строку байтов](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-bytes-bajtovye-stroki/ "Байтовые строки bytes в Python."), представляющую текущий рабочий каталог.

Функция `getcwdb()` использует кодировку UTF-8 в Windows, а не кодовую страницу ANSI.

**Примеры использования:**
```python
>>> import os
>>> os.getcwd()
'/home/docs-python'
```

## link()
[Создать жесткую ссылку из кода в Python.](https://docs-python.ru/standart-library/modul-os-python/funktsija-link-modulja-os/)

Функция `link()` модуля `os` создает жесткую ссылку, указывающую на `src` с именем `dst`.

**Синтаксис:**
```python
import os

os.link(src, dst, *, src_dir_fd=None, dst_dir_fd=None, follow_symlinks=True)
```
**Параметры:**
-   `src` - [`str`](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-str-tekstovye-stroki/ "Текстовые строки str в Python."), путь в файловой системе на который указывает ссылка,
-   `dst` - имя ссылки ([`str`](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-str-tekstovye-stroki/ "Текстовые строки str в Python.") путь в файловой системе),
-   `src_dir_fd=None` - [`int`](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-int-tselye-chisla/ "Целые числа int в Python.") дескрипторов каталогов на который указывает ссылка,
-   `dst_dir_fd=None` - [`int`](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-int-tselye-chisla/ "Целые числа int в Python.") имя ссылки, дескрипторов каталогов,
-   `follow_symlinks=True` - [`bool`](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/bool-logicheskij-tip-dannyh/ "Логический тип данных bool в Python."), переходить ли по ссылкам.

**Возвращаемое значение:**
-   `None`

**Описание:**

Функция [`link()`](https://docs-python.ru/standart-library/modul-os-python/funktsija-link-modulja-os/ "Функция link() модуля os в Python.") модуля [`os`](https://docs-python.ru/standart-library/modul-os-python/ "Модуль os в Python, доступ к функциям ОС.") создает жесткую ссылку, указывающую на `src` с именем `dst`.

Аргументы `src` и `dst` могут принимать объекты, представляющие путь файловой системы, такой как [`pathlib.PurePath`](https://docs-python.ru/standart-library/modul-pathlib-python/klass-pathlib-purepath-podklassy/ "Класс pathlib.PurePath() и его подклассы.").

Эта функция может поддерживать указание `src_dir_fd` и/или `dst_dir_fd` для предоставления путей относительно [дескрипторов каталогов](https://docs-python.ru/standart-library/modul-os-python/funktsija-supports-dir-fd-modulja-os/ "Функция supports_dir_fd модуля os в Python."), а так же может [не следовать символическим ссылкам](https://docs-python.ru/standart-library/modul-os-python/funktsija-supports-follow-symlinks-modulja-os/ "Функция supports_follow_symlinks модуля os в Python.") `follow_symlinks=False`.

Вызывает [событие аудита](https://docs-python.ru/standart-library/modul-sys-python/sobytie-audita-c/ "События аудита CPython.") `os.link` с аргументами `src`, `dst`, `src_dir_fd`, `dst_dir_fd`.

Доступность: Unix, Windows.

**Примеры использования:**
```python
>>> import os
>>> scr = 'tt.py'
>>> dst = 'link_tt.py'
>>> os.link(scr, dst)
>>> os.path.isfile(dst)
# True
```

## mkdir()
[Создать каталог и установить режим доступа к нему в Python.](https://docs-python.ru/standart-library/modul-os-python/funktsija-mkdir-modulja-os/)

Функция `mkdir()` модуля `os` создает каталог с именем `path` с режимом доступа к нему `mode`. Режим `mode` устанавливается последними 3 цифрами восьмеричного представления режима.

**Синтаксис:**
```python
import os

os.mkdir(path, mode=0o777, *, dir_fd=None)
```

**Параметры:**
-   `path` - имя каталога ([`str`](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-str-tekstovye-stroki/ "Текстовые строки str в Python.") путь в файловой системе),
-   `mode=0o777` - [режимом доступа к каталогу](https://docs-python.ru/standart-library/modul-os-python/funktsija-mkdir-modulja-os/#mode),
-   `dir_fd=None` - [дескриптор каталога](https://docs-python.ru/standart-library/modul-os-python/funktsija-supports-dir-fd-modulja-os/ "Функция supports_dir_fd модуля os в Python.")

**Возвращаемое значение:**
-   `None`

**Описание:**

Функция [`mkdir()`](https://docs-python.ru/standart-library/modul-os-python/funktsija-mkdir-modulja-os/ "Функция mkdir() модуля os в Python.") модуля [`os`](https://docs-python.ru/standart-library/modul-os-python/ "Модуль os в Python, доступ к функциям ОС.") создает каталог с именем `path` с режимом доступа к нему `mode`. Аргумент `path` может принимать объекты, представляющие путь файловой системы, такие как [`pathlib.PurePath`](https://docs-python.ru/standart-library/modul-pathlib-python/klass-pathlib-purepath-podklassy/ "Класс pathlib.PurePath() и его подклассы.").

Если каталог уже существует, вызывается [исключение `FileExistsError`](https://docs-python.ru/tutorial/vstroennye-iskljuchenija-interpretator-python/oshibki-operatsionnoj-sistemy-oserror/ "Исключения операционной системы: OSError в Python.").

Если установлены биты, отличные от последних 9 (то есть последние 3 цифры восьмеричного представления режима), их значение зависит от платформы.

В некоторых системах режим `mode` игнорируется и необходимо явно вызвать [`os.chmod()`](https://docs-python.ru/standart-library/modul-os-python/funktsija-chmod-modulja-os/ "Функция chmod() модуля os в Python."), чтобы установить режим доступа. Там, где он используется, текущее значение [`umask`](https://docs-python.ru/standart-library/modul-os-python/funktsija-umask-modulja-os/ "Функция umask() модуля os в Python.") сначала маскируется.

Аргумент режима доступа `mode` может принимать последние 3 цифры восьмеричного представления числа, например `0o755`. По умолчанию `mode=0o777`. Также `mode` может принимать одно или несколько из следующих значений, значения которых приведены в [модуле `stat`](https://docs-python.ru/standart-library/konstanty-funktsii-os-stat/ "Модуль stat в Python, извлечение информации из stat_result."):

**Возможные значения `mode`:**

-   `stat.S_ISUID` - Устанавливает бит идентификатора пользователя.
-   `stat.S_ISGID` - Устанавливает бит идентификатора группы. Этот бит имеет несколько специальных применений.
    - Для каталога это означает, что файлы наследуют идентификатор своей группы из каталога, а не от эффективного идентификатора группы процесса создания, и созданные там каталоги также получат установленный бит S_ISGID.
    - Для файла, который не имеет установленного бита выполнения группы `S_IXGRP`, бит set-group-ID указывает на обязательную блокировку файла/записей (смотрите также `S_ENFMT`).
-   `stat.S_ISVTX` - Липкий бит. Когда этот бит установлен в каталоге, это означает, что файл в этом каталоге может быть переименован или удален только владельцем файла, владельцем каталога или привилегированным процессом.
-   `stat.S_IRWXU` - Маска устанавливает для пользователя права `rwx`.
-   `stat.S_IRUSR` - Владелец имеет разрешение на чтение.
-   `stat.S_IWUSR` - Владелец имеет разрешение на запись.
-   `stat.S_IXUSR` - Владелец имеет разрешение на исполнение.,
-   `stat.S_IRWXG` - Маска устанавливает для группы права `rwx`.
-   `stat.S_IRGRP` - Группа имеет разрешение на чтение.
-   `stat.S_IWGRP` - Группа имеет разрешение на запись.
-   `stat.S_IXGRP` - Группа имеет разрешение на исполнение.
-   `stat.S_IRWXO` - Маска устанавливает для других (не в группе) права `rwx`.
-   `stat.S_IROTH` - Другие имеет разрешение на чтение.
-   `stat.S_IWOTH` - Другие имеет разрешение на запись.
-   `stat.S_IXOTH` - Другие имеет разрешение на исполнение.
-   `stat.S_ENFMT` - Система V принудительно блокирует файлы. Этот флаг используется совместно с SISGID: блокировка файлов/записей применяется к файлам, для которых не установлен бит выполнения группы (SIXGRP),
-   `stat.S_IREAD` - Unix V7 синоним для S_IRUSR.
-   `stat.S_IWRITE` - Unix V7 синоним для S_IWUSR.
-   `stat.S_IEXEC` - Unix V7 синоним для S_IXUSR.

Приведенные выше значения можно комбинировать побитовым ИЛИ `'|'`, например `stat.S_IRWXU|stat.S_IRGRP|stat.S_IXGRP|stat.S_IROTH`. Данная комбинация установит разрешение `rwxr-xr--` для `path`.

Эта функция также может поддерживать пути относительно [дескрипторов каталогов `dir_fd`](https://docs-python.ru/standart-library/modul-os-python/funktsija-supports-dir-fd-modulja-os/ "Функция supports_dir_fd модуля os в Python.").

Также возможно создание временных каталогов, смотрите функцию [`tempfile.mkdtemp()`](https://docs-python.ru/standart-library/modul-tempfile-python/funktsija-mkdtemp-modulja-tempfile/ "Функция mkdtemp() модуля tempfile в Python.") [модуля tempfile](https://docs-python.ru/standart-library/modul-tempfile-python/ "Модуль tempfile в Python, временные файлы и каталоги.").

Функция [`os.mkdir()`](https://docs-python.ru/standart-library/modul-os-python/funktsija-mkdir-modulja-os/ "Функция mkdir() модуля os в Python.") вызывает [событие аудита](https://docs-python.ru/standart-library/modul-sys-python/sobytie-audita-c/ "События аудита CPython.") `os.mkdir` с аргументами `path`, `mode`, `dir_fd`.

**Примеры использования:**
```python
>>> import os, stat
>>> d = 'test_dir'
>>> os.mkdir(d, 0o754)
>>> os.path.isdir(d)
# True
>>> st = os.stat(d).st_mode
>>> stat.filemode(st)
# 'drwxrw-r--'
```
При создании нового каталога с помощью `os.mkdir()` все родительские каталоги должны уже существовать:
```python
import os

dir_name = 'test_dir'

print('Creating', dir_name)
os.makedirs(dir_name)

file_name = os.path.join(dir_name, 'example.txt')
print('Creating', file_name)
with open(file_name, 'wt') as f:
    f.write('example file')

print('Cleaning up')
os.unlink(file_name)
os.rmdir(dir_name)
```


## makedirs()
[Создать директорию со всеми промежуточными каталогами в Python.](https://docs-python.ru/standart-library/modul-os-python/funktsija-makedirs-modulja-os/)

Функция `makedirs()` модуля `os` рекурсивно создает все промежуточные каталоги, если они не существуют. Функция работает подобно `os.mkdir()`, но создает все каталоги промежуточного уровня

**Синтаксис:**
```python
import os

os.makedirs(name, mode=0o777, exist_ok=False)
```

**Параметры:**
-   `name` - имя каталога ([`str`](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-str-tekstovye-stroki/ "Текстовые строки str в Python.") путь в файловой системе),
-   `mode=0o777` - режимом доступа к каталогу,
-   `exist_ok=False` - [`bool`](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/bool-logicheskij-tip-dannyh/ "Логический тип данных bool в Python."), управление ошибкой.

**Возвращаемое значение:**
-   `None`

**Описание:**

Функция [`makedirs()`](https://docs-python.ru/standart-library/modul-os-python/funktsija-makedirs-modulja-os/ "Функция makedirs() модуля os в Python.") модуля [`os`](https://docs-python.ru/standart-library/modul-os-python/ "Модуль os в Python, доступ к функциям ОС.") рекурсивно создает все промежуточные каталоги, если они не существуют. Функция работает подобно `os.mkdir()`, но создает все каталоги промежуточного уровня, необходимые для хранения конечного каталога.

Параметр `mode` передается в функцию [`os.mkdir()`](https://docs-python.ru/standart-library/modul-os-python/funktsija-mkdir-modulja-os/ "Функция mkdir() модуля os в Python.") для создания _конечного каталога_. Чтобы установить биты прав доступа к файлам, любых вновь созданных родительских каталогов, можно установить `umask` перед вызовом `os.makedirs()`. Биты прав доступа к файлам _существующих родительских каталогов_ не изменяются.

Если `exist_ok` имеет значение False (по умолчанию) и целевой каталог уже существует, то возникает [ошибка `FileExistsError`](https://docs-python.ru/tutorial/vstroennye-iskljuchenija-interpretator-python/oshibki-operatsionnoj-sistemy-oserror/ "Исключения операционной системы: OSError в Python.").

Заметьте, что функция [`os.makedirs()`](https://docs-python.ru/standart-library/modul-os-python/funktsija-makedirs-modulja-os/ "Функция makedirs() модуля os в Python.") запутается, если элементы пути для создания включают [`os.pardir`](https://docs-python.ru/standart-library/modul-os-python/znachenija-ispolzuemye-podderzhki-operatsij-putjami/ "Константы для поддержки операций с путями."), например `'..'` в системах UNIX. Эта функция правильно обрабатывает UNC-пути.

Аргумент `name` может принимать объекты, представляющие путь файловой системы, такие как [`pathlib.PurePath`](https://docs-python.ru/standart-library/modul-pathlib-python/klass-pathlib-purepath-podklassy/ "Класс pathlib.PurePath() и его подклассы.").

Вызывает [событие аудита](https://docs-python.ru/standart-library/modul-sys-python/sobytie-audita-c/ "События аудита CPython.") `os.mkdir` с аргументами `path`, `mode`, `dir_fd`.

**Примеры использования:**
```python
>>> import os, stat
>>> d = 'a/b/c/d/test_dir'
>>> os.makedirs(d, 0o774)
>>> os.path.isdir(d)
# True

>>> st = os.stat(d).st_mode
>>> stat.filemode(st)
# 'drwxrwxr--'

>>> os.chdir(d)
>>> os.getcwd()
# '/home/docs-python/a/b/c/d/test_dir'
```

## symlink()

[Создать символическую ссылку из кода в Python.](https://docs-python.ru/standart-library/modul-os-python/funktsija-symlink-modulja-os/)

Функция `symlink()` модуля `os` создает символическую ссылку, указывающую на `src` с именем `dst`.

**Синтаксис:**
```python
import os

os.symlink(src, dst, target_is_directory=False, *, dir_fd=None)
```

**Параметры:**
-   `src` - [`str`](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-str-tekstovye-stroki/ "Текстовые строки str в Python."), путь в файловой системе на который указывает ссылка,
-   `dst` - имя ссылки ([`str`](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-str-tekstovye-stroki/ "Текстовые строки str в Python.") путь в файловой системе),
-   `target_is_directory=False` - [`bool`](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/bool-logicheskij-tip-dannyh/ "Логический тип данных bool в Python."), в Windows ссылка как каталог.
-   `dir_fd=None` - [`int`](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-int-tselye-chisla/ "Целые числа int в Python."), [дескрипторов каталогов](https://docs-python.ru/standart-library/modul-os-python/funktsija-supports-dir-fd-modulja-os/ "Функция supports_dir_fd модуля os в Python.").

**Возвращаемое значение:**
-   `None`

**Описание:**

Функция [`symlink()`](https://docs-python.ru/standart-library/modul-os-python/funktsija-symlink-modulja-os/ "Функция symlink() модуля os в Python.") модуля [`os`](https://docs-python.ru/standart-library/modul-os-python/ "Модуль os в Python, доступ к функциям ОС.") создает символическую ссылку, указывающую на `src` с именем `dst`.

Аргументы `src` и `dst` могут принимать объекты, представляющие путь файловой системы, такой как [`pathlib.PurePath`](https://docs-python.ru/standart-library/modul-pathlib-python/klass-pathlib-purepath-podklassy/ "Класс pathlib.PurePath() и его подклассы.").

Функция `os.symlink()` может поддерживать пути относительно [дескрипторов каталогов `dir_fd`](https://docs-python.ru/standart-library/modul-os-python/funktsija-supports-dir-fd-modulja-os/ "Функция supports_dir_fd модуля os в Python.").

На платформах, отличных от Windows, `target_is_directory` игнорируется. В Windows символическая ссылка представляет собой либо файл, либо каталог и не преобразуется в целевой объект динамически. Если цель присутствует, то будет создан соответствующий тип символической ссылки. В противном случае символическая ссылка будет создана как каталог, если `target_is_directory` имеет значение `True` или файловая символическая ссылка (по умолчанию).

**Примечание**. В более новых версиях Windows 10 непривилегированные учетные записи могут создавать символические ссылки, если включен режим разработчика. Когда режим разработчика недоступен/не включен, требуется привилегия `SeCreateSymbolicLinkPrivilege` или процесс должен выполняться от имени администратора. Когда функция вызывается непривилегированным пользователем вызывается [исключение `OSError`](https://docs-python.ru/tutorial/vstroennye-iskljuchenija-interpretator-python/oshibki-operatsionnoj-sistemy-oserror/ "Исключения операционной системы: OSError в Python.").

Вызывает событие аудита os.symlink с аргументами src, dst, dir_fd.

Доступность: Unix, Windows.

**Примеры использования:**
```python
>>> import os
>>> src = '/usr/bin/python'
>>> dst = '/tmp/python'

>>> os.symlink(src, dst)
>>> os.readlink(dst)
# '/usr/bin/python'

>>> os.path.islink(dst)
# True
```

Создадим файл `symlinks.py` следующего содержания:
```python
# symlinks.py
import os

link_name = '/tmp/' + os.path.basename(__file__)

print(f'Creating link {link_name} -> {__file__}')
os.symlink(__file__, link_name)

stat_info = os.lstat(link_name)
print('Permissions:', oct(stat_info.st_mode))

print('Points to:', os.readlink(link_name))

# Очистим
os.unlink(link_name)
```

Запустим файл:
```bash
$ python3 symlinks.py
Creating link /tmp/symlinks.py -> symlinks.py
Permissions: 0o120755
Points to: symlinks.py
```


## readlink()
[Определить файл или каталог на который указывает символическая ссылка в Python.](https://docs-python.ru/standart-library/modul-os-python/funktsija-readlink-modulja-os/)

Функция `readlink()` модуля `os` вернет строку, представляющую путь, на который указывает символическая ссылка.

**Синтаксис:**
```python
import os

os.readlink(path, *, dir_fd=None)
```
**Параметры:**
-   `path` - [`str`](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-str-tekstovye-stroki/ "Текстовые строки str в Python.") или [`bytes`](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-bytes-bajtovye-stroki/ "Байтовые строки bytes в Python."), символическая ссылка,
-   `dir_fd=None` - [`int`](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-int-tselye-chisla/ "Целые числа int в Python."), дескриптор каталога.

**Возвращаемое значение:**
-   [`str`](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-str-tekstovye-stroki/ "Текстовые строки str в Python.") или [`bytes`](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-bytes-bajtovye-stroki/ "Байтовые строки bytes в Python."), путь на который указывает символическая ссылка.

**Описание:**

Функция [`readlink()`](https://docs-python.ru/standart-library/modul-os-python/funktsija-readlink-modulja-os/ "Функция readlink() модуля os в Python.") модуля [`os`](https://docs-python.ru/standart-library/modul-os-python/ "Модуль os в Python, доступ к функциям ОС.") вернет [строку](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-str-tekstovye-stroki/ "Текстовые строки str в Python."), представляющую путь, на который указывает символическая ссылка.

Результатом может быть абсолютный или относительный путь. Если путь относительный, он может быть преобразован в абсолютный путь, используя `os.path.join(os.path.dirname(path), result)`.

Если путь `path` является [строковым объектом](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-str-tekstovye-stroki/ "Текстовые строки str в Python."), то прямым или косвенным результатом также будет строковый объект, а вызов может вызвать [исключение `UnicodeDecodeError`](https://docs-python.ru/tutorial/vstroennye-iskljuchenija-interpretator-python/oshibka-kodirovki-unicodeerror/ "Ошибка кодировки: UnicodeError в Python."). Если путь является [байтовым объектом](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-bytes-bajtovye-stroki/ "Байтовые строки bytes в Python."), то прямым или косвенным результатом будет байтовый объект.

Аргумент `path` может принимать объекты, представляющие путь файловой системы, такие как [`pathlib.PurePath`](https://docs-python.ru/standart-library/modul-pathlib-python/klass-pathlib-purepath-podklassy/ "Класс pathlib.PurePath() и его подклассы.").

Функция `os.readlink()` также может поддерживать пути относительно [дескрипторов каталогов](https://docs-python.ru/standart-library/modul-os-python/funktsija-supports-dir-fd-modulja-os/ "Функция supports_dir_fd модуля os в Python.").

При попытке определить путь, который может содержать ссылки, используйте [функцию `os.path.realpath()`](https://docs-python.ru/standart-library/modul-os-path-python/funktsija-realpath-modulja-os-path/ "Функция realpath() модуля os.path в Python.") для правильной обработки рекурсии и различий платформы.

Доступность: Unix, Windows.

**Примеры использования:**
```python
>>> import os
>>> src = '/usr/bin/python'
>>> dst = '/tmp/python'
>>> os.symlink(src, dst)
>>> os.readlink(dst)
# '/usr/bin/python'
```


## remove()
[Удалить файл из кода в Python.](https://docs-python.ru/standart-library/modul-os-python/funktsija-remove-modulja-os/)

Функция `remove()` модуля `os` удаляет путь `path` к файлу. Если путь является каталогом, возникает исключение `IsADirectoryError`. Функция `os.remove()` семантически идентична `os.unlink()`.

**Синтаксис:**
```python
import os

os.remove(path, *, dir_fd=None)
os.unlink(path, *, dir_fd=None)
```

**Параметры:**
-   `path` - [`str`](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-str-tekstovye-stroki/ "Текстовые строки str в Python."), путь к файлу,
-   `dir_fd=None` - [`int`](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-int-tselye-chisla/ "Целые числа int в Python."), дескриптор каталога.

**Возвращаемое значение:**
-   `None`

**Описание:**

Функция [`remove()`](https://docs-python.ru/standart-library/modul-os-python/funktsija-remove-modulja-os/ "Функция remove() модуля os в Python.") модуля [`os`](https://docs-python.ru/standart-library/modul-os-python/ "Модуль os в Python, доступ к функциям ОС.") удаляет путь `path` к файлу. Если путь является каталогом, возникает исключение `IsADirectoryError`. Используйте [`os.rmdir()`](https://docs-python.ru/standart-library/modul-os-python/funktsija-rmdir-modulja-os/ "Функция rmdir() модуля os в Python.") для удаления каталогов.

Функция `os.remove()` семантически идентична `os.unlink()`.

Обе функции могут поддерживать пути относительно [дескрипторов каталогов](https://docs-python.ru/standart-library/modul-os-python/funktsija-supports-dir-fd-modulja-os/ "Функция supports_dir_fd модуля os в Python."). Аргумент `path` может принимать объекты, представляющие путь файловой системы, такие как [`pathlib.PurePath`](https://docs-python.ru/standart-library/modul-pathlib-python/klass-pathlib-purepath-podklassy/ "Класс pathlib.PurePath() и его подклассы.").

В Windows попытка удалить используемый файл приводит к возникновению исключения. В Unix запись из каталога удаляется, но хранилище, выделенное для файла, становится недоступным, пока исходный файл больше не используется.

Вызывает [событие аудита](https://docs-python.ru/standart-library/modul-sys-python/sobytie-audita-c/ "События аудита CPython.") `os.remove` с аргументами `path`, `dir_fd`.

**Примеры использования:**
```python
import os

f = 'test_delete.txt'
# создадим файл
with open(f, 'w') as fp:
    fp.write('data string')

# удалим файл, если существует
if os.path.isfile(f):
    remove(f)
```

## removedirs()
[Рекурсивно удалить пустые каталоги в Python.](https://docs-python.ru/standart-library/modul-os-python/funktsija-removedirs-modulja-os/)

Функция `removedirs()` модуля `os` удаляет каталоги рекурсивно. Если конечный каталог успешно удален, `os.removedirs()` пытается последовательно удалить каждый родительский каталог, указанный в пути, до появления ошибки. Появления ошибки обычно означает, что родительский каталог не пуст.

**Синтаксис:**
```python
import os

os.removedirs(path)
```
**Параметры:**
-   `path` - [`str`](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-str-tekstovye-stroki/ "Текстовые строки str в Python.") путь в файловой системе до каталога.

**Возвращаемое значение:**
-   `None`

**Описание:**

Функция [`removedirs()`](https://docs-python.ru/standart-library/modul-os-python/funktsija-removedirs-modulja-os/ "Функция removedirs() модуля os в Python.") модуля [`os`](https://docs-python.ru/standart-library/modul-os-python/ "Модуль os в Python, доступ к функциям ОС.") удаляет каталоги рекурсивно. Работает подобно [функции `os.rmdir()][os.rmdir] за исключением того, что, если конечный каталог успешно удален,`os.removedirs()` пытается последовательно удалить каждый родительский каталог, указанный в пути, до появления ошибки. Появления ошибки обычно означает, что родительский каталог не пуст.

Например, `os.removedirs('foo/bar/ baz')` сначала удалит каталог `'foo/bar/baz'`, затем удалит 'foo/bar' и `'foo'`, если они пусты. Вызывает [исключение `OSError`](https://docs-python.ru/tutorial/vstroennye-iskljuchenija-interpretator-python/oshibki-operatsionnoj-sistemy-oserror/ "Исключения операционной системы: OSError в Python."), если конечный каталог не может быть успешно удален.

Аргумент `path` может принимать объекты, представляющие путь файловой системы, такие как [`pathlib.Path`](https://docs-python.ru/standart-library/modul-pathlib-python/klass-pathlib-path-podklassy/ "Класс pathlib.Path() и его подклассы.").

Вызывает [событие аудита](https://docs-python.ru/standart-library/modul-sys-python/sobytie-audita-c/ "События аудита CPython.") `os.remove` с аргументами `path`, `dir_fd`.

**Примеры использования:**
```python
>>> import os
>>> d = 'a/b/c/d/test_dir'
>>> os.makedirs(d, 0o774)
>>> os.path.isdir(d)
# True

# удаляем рекурсивно пустые директории
>>> os.removedirs(d)
>>> os.path.isdir(d)
False
```


## rename()
[Переименовать файл или пустой каталог в Python.](https://docs-python.ru/standart-library/modul-os-python/funktsija-rename-modulja-os/)

Функция rename() модуля os переименовывает файл или каталог с именем src в dst. Если имя dst существует, операция, в ряде случаев, завершится с подклассом исключения OSError.

**Синтаксис:**
```python
import os

os.rename(src, dst, *, src_dir_fd=None, dst_dir_fd=None)
```
**Параметры**:
-   `src` - [`str`](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-str-tekstovye-stroki/ "Текстовые строки str в Python."), исходное имя файла или каталога,
-   `dst` - [`str`](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-str-tekstovye-stroki/ "Текстовые строки str в Python."), новое имя файла или каталога,
-   `src_dir_fd=None` - [`int`](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-int-tselye-chisla/ "Целые числа int в Python."), исходный дескриптор каталога,
-   `dst_dir_fd=None` - [`int`](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-int-tselye-chisla/ "Целые числа int в Python."), новый дескриптор каталога,

**Возвращаемое значение:**
-   `None`

**Описание:**

Функция [`rename()`](https://docs-python.ru/standart-library/modul-os-python/funktsija-rename-modulja-os/ "Функция rename() модуля os в Python.") модуля [`os`](https://docs-python.ru/standart-library/modul-os-python/ "Модуль os в Python, доступ к функциям ОС.") переименовывает файл или каталог с именем `src` в `dst`. Если имя `dst` уже существует, то операция `os.rename()`, в ряде случаев, может завершится с подклассом [исключения `OSError`](https://docs-python.ru/tutorial/vstroennye-iskljuchenija-interpretator-python/oshibki-operatsionnoj-sistemy-oserror/ "Исключения операционной системы: OSError в Python.").

В Windows, если `dst` уже существует, всегда возникает [ошибка `FileExistsError`](https://docs-python.ru/tutorial/vstroennye-iskljuchenija-interpretator-python/oshibki-operatsionnoj-sistemy-oserror/ "Исключения операционной системы: OSError в Python.").

В Unix, если `src` - это файл, а `dst` - это каталог или наоборот, то поднимаются [исключения `IsADirectoryError` или `NotADirectoryError`](https://docs-python.ru/tutorial/vstroennye-iskljuchenija-interpretator-python/oshibki-operatsionnoj-sistemy-oserror/ "Исключения операционной системы: OSError в Python.") соответственно.

Если оба являются каталогами и `dst` пуст, то `dst` будет заменен без уведомления.Если `dst` является непустым каталогом, возникает `OSError`.Если оба являются файлами, то `dst` будет заменен без уведомления, если у пользователя есть разрешение.

Операция может завершиться с ошибкой на некоторых разновидностях Unix, если `src` и `dst` находятся на разных файловых системах. В случае успеха, переименование будет атомарной операцией, это требование POSIX.

Аргументы `src` и `dst` могут принимать объекты, представляющие путь файловой системы, такие как [`pathlib.PurePath`](https://docs-python.ru/standart-library/modul-pathlib-python/klass-pathlib-purepath-podklassy/ "Класс pathlib.PurePath() и его подклассы.").

Функция `os.rename()` может поддерживать указание `src_dir_fd` и/или `dst_dir_fd` для предоставления путей относительно [дескриптора каталога](https://docs-python.ru/standart-library/modul-os-python/funktsija-supports-dir-fd-modulja-os/ "Функция supports_dir_fd модуля os в Python.").

Если необходимо кросс-платформенное переименование, то используйте [функцию `os.replace()`](https://docs-python.ru/standart-library/modul-os-python/funktsija-replace-modulja-os/ "Функция replace() модуля os в Python.").

**Примеры использования:**
```python
>>> import os
>>> scr_dir, dst_dir = 'test_dir', 'rename_dir'
>>> os.mkdir(scr_dir, 0o774)
# переименовывание
>>> os.rename(scr_dir, dst_dir)
>>> os.path.isdir(dst_dir)
# True
>>> os.rmdir(dst_dir)

>>> scr_f, dst_f = 'test_file.txt', 'rename_file.txt'
# создадим файл
>>> fp = open(scr_f, 'w')
>>> fp.write('data string')
>>> fp.close()
# переименовывание
>>> os.rename(scr_f, dst_f)
>>> os.path.isfile(dst_f)
# True
>>> os.unlink(dst_f)
```


## renames()
[Рекурсивно переименовать пустые директории в Python.](https://docs-python.ru/standart-library/modul-os-python/funktsija-renames-modulja-os/)

Функция `renames()` модуля `os` рекурсивно переименовывает пустые директории или переименовывает конечный файл.

**Синтаксис:**
```python
import os

os.renames(old, new)
```
**Параметры:**
-   `old` - [`str`](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-str-tekstovye-stroki/ "Текстовые строки str в Python."), старый путь в файловой системе,
-   `new` - [`str`](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-str-tekstovye-stroki/ "Текстовые строки str в Python."), новый путь в файловой системе.

**Возвращаемое значение:**
-   `None`

**Описание:**

Функция [`renames()`](https://docs-python.ru/standart-library/modul-os-python/funktsija-renames-modulja-os/ "Функция renames() модуля os в Python.") модуля [`os`](https://docs-python.ru/standart-library/modul-os-python/ "Модуль os в Python, доступ к функциям ОС.") рекурсивно переименовывает пустые директории или переименовывает конечный файл.

Работает подобно [`os.rename()`](https://docs-python.ru/standart-library/modul-os-python/funktsija-rename-modulja-os/ "Функция rename() модуля os в Python."), за исключением того, что сначала пытается создать любые промежуточные каталоги, необходимые для создания нового пути файловой системы. После переименования каталоги, соответствующие крайним правым сегментам пути старого имени, будут удалены с помощью [функции `os.removedirs()`](https://docs-python.ru/standart-library/modul-os-python/funktsija-removedirs-modulja-os/ "Функция removedirs() модуля os в Python.").

Аргументы `old` и `new` могут принимать объекты, представляющие путь файловой системы, такие как [`pathlib.PurePath`](https://docs-python.ru/standart-library/modul-pathlib-python/klass-pathlib-purepath-podklassy/ "Класс pathlib.PurePath() и его подклассы.").

**Примечание**. Эта функция может не работать с созданной новой структурой каталогов, если у вас нет прав, необходимых для удаления конечного каталога или файла.

Вызывает [событие аудита](https://docs-python.ru/standart-library/modul-sys-python/sobytie-audita-c/ "События аудита CPython.") `os.rename` с аргументами `src`, `dst`, `src_dir_fd`, `dst_dir_fd`.

**Примеры использования:**
```python
>>> import os
>>> old = 'a/b/c/old'
>>> new = 'foo/bar/baz/new'
>>> os.makedirs(old, 0o774)
>>> os.path.isdir(old)
# True

# рекурсивно переименовываем пустые директории
>>> os.renames(old, new)
>>> os.path.isdir(new)
# True

# Очистка
>>> os.removedirs(new)
>>> os.path.isdir(new)
# False
```

## replace()
[Заменить имя файл из кода Python.](https://docs-python.ru/standart-library/modul-os-python/funktsija-replace-modulja-os/)

Функция `replace()` модуля `os` переименовывает файл или пустой каталог с исходным именем `src` в `dst`.

**Синтаксис:**
```python
import os

os.replace(src, dst, *, src_dir_fd=None, dst_dir_fd=None)
```

**Параметры:**
-   `src` - [`str`](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-str-tekstovye-stroki/ "Текстовые строки str в Python."), исходное имя файла или каталога,
-   `dst` - [`str`](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-str-tekstovye-stroki/ "Текстовые строки str в Python."), новое имя файла или каталога,
-   `src_dir_fd=None` - [`int`](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-int-tselye-chisla/ "Целые числа int в Python."), исходный дескриптор каталога,
-   `dst_dir_fd=None` - [`int`](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-int-tselye-chisla/ "Целые числа int в Python."), новый дескриптор каталога,

**Возвращаемое значение:**
-  `None`

**Описание:**

Функция [`replace()`](https://docs-python.ru/standart-library/modul-os-python/funktsija-replace-modulja-os/ "Функция replace() модуля os в Python.") модуля [`os`](https://docs-python.ru/standart-library/modul-os-python/ "Модуль os в Python, доступ к функциям ОС.") переименовывает файл или пустой каталог с исходным именем `src` в `dst`.

Аргумент `src` и `dst` могут принимать объекты, представляющие путь файловой системы, такие как [`pathlib.PurePath`](https://docs-python.ru/standart-library/modul-pathlib-python/klass-pathlib-purepath-podklassy/ "Класс pathlib.PurePath() и его подклассы.").

-   Если `src` - это файл, а `dst` - это каталог или наоборот, то будет вызвано [исключение `OSError`](https://docs-python.ru/tutorial/vstroennye-iskljuchenija-interpretator-python/oshibki-operatsionnoj-sistemy-oserror/ "Исключения операционной системы: OSError в Python.").
-   Если `dst` существует и является файлом, он будет автоматически заменен, если у пользователя есть разрешение.
-   Операция может завершиться ошибкой, если `src` и `dst` находятся в разных файловых системах.
-   В случае успеха переименование будет атомарной операцией (это требование POSIX).

Функция `os.replace()` может поддерживать указание `src_dir_fd` и/или `dst_dir_fd` для предоставления путей относительно [дескриптора каталога](https://docs-python.ru/standart-library/modul-os-python/funktsija-supports-dir-fd-modulja-os/ "Функция supports_dir_fd модуля os в Python.").

Вызывает [событие аудита](https://docs-python.ru/standart-library/modul-sys-python/sobytie-audita-c/ "События аудита CPython.") `os.rename` с аргументами `src`, `dst`, `src_dir_fd`, `dst_dir_fd`.

**Примеры использования:**
```python
>>> import os
>>> scr_dir, dst_dir = 'test_dir', 'rename_dir'
>>> os.mkdir(scr_dir, 0o774)
# переименовывание
>>> os.replace(scr_dir, dst_dir)
>>> os.path.isdir(dst_dir)
# True
>>> os.rmdir(dst_dir)

>>> scr_f, dst_f = 'test_file.txt', 'rename_file.txt'
# создадим файл
>>> fp = open(scr_f, 'w')
>>> fp.write('data string')
>>> fp.close()
# переименовывание
>>> os.replace(scr_f, dst_f)
>>> os.path.isfile(dst_f)
# True
>>> os.unlink(dst_f)
```


## rmdir()
[Удалить пустой каталог в файловой системе в Python.](https://docs-python.ru/standart-library/modul-os-python/funktsija-rmdir-modulja-os/)

Функция `rmdir()` модуля `os` удаляет путь к каталогу `path`. Если директория `path` не существует или не является пустым каталогом, то возникает исключение.

**Синтаксис:**
```python
import os

os.rmdir(path, *, dir_fd=None)
```
**Параметры:**
-   `path` - [`str`](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-str-tekstovye-stroki/ "Текстовые строки str в Python."), путь в файловой системе до каталога,
-   `dir_fd=None` - [`int`](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-int-tselye-chisla/ "Целые числа int в Python."), дескриптор каталога,

**Возвращаемое значение:**
-   `None`

**Описание:**

Функция [`rmdir()`](https://docs-python.ru/standart-library/modul-os-python/funktsija-rmdir-modulja-os/ "Функция rmdir() модуля os в Python.") модуля [`os`](https://docs-python.ru/standart-library/modul-os-python/ "Модуль os в Python, доступ к функциям ОС.") удаляет путь к каталогу `path`. Если директория `path` не существует или не является пустым каталогом, соответственно возникает исключение [`FileNotFoundError или OSError`](https://docs-python.ru/tutorial/vstroennye-iskljuchenija-interpretator-python/oshibki-operatsionnoj-sistemy-oserror/ "Исключения операционной системы: OSError в Python.").

Аргумент `path` может принимать объекты, представляющие путь файловой системы, такие как [`pathlib.PurePath`](https://docs-python.ru/standart-library/modul-pathlib-python/klass-pathlib-purepath-podklassy/ "Класс pathlib.PurePath() и его подклассы.").

Для удаления целых деревьев каталогов можно использовать [функцию `shutil.rmtree()`](https://docs-python.ru/standart-library/modul-shutil-python/funktsija-rmtree-modulja-shutil/ "Функция rmtree() модуля shutil в Python.").

Эта функция может поддерживать пути относительно [дескрипторов каталогов](https://docs-python.ru/standart-library/modul-os-python/funktsija-supports-dir-fd-modulja-os/ "Функция supports_dir_fd модуля os в Python.").

Вызывает [событие аудита](https://docs-python.ru/standart-library/modul-sys-python/sobytie-audita-c/ "События аудита CPython.") `os.rmdir` с аргументами `path`, `dir_fd`.

**Примеры использования:**
```python
>>> import os
>>> path = 'test_dir'
# Создадим каталог
>>> os.mkdir(path, 0o774)
>>> os.path.isdir(path)
# True

# Удалим каталог
>>> os.rmdir(path)
>>> os.path.isdir(path)
# False
```

## strerror()
[Конвертирует код ошибки в сообщение об ошибке в Python.](https://docs-python.ru/standart-library/modul-os-python/funktsija-strerror-modulja-os/)

Функция strerror() модуля os возвращает сообщение об ошибке, соответствующее коду ошибки, которая появляется при сбое в коде приложения.

**Синтаксис:**
```python
import os

os.strerror(code)
```
**Параметры:**
-   `code` - код ошибки при сбое в приложении.

**Возвращаемое значение:**
-   [строка](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-str-tekstovye-stroki/ "Текстовые строки str в Python.") с сообщением об ошибке.

**Описание:**

Функция [`strerror()`](https://docs-python.ru/standart-library/modul-os-python/funktsija-strerror-modulja-os/ "Функция strerror() модуля os в Python.") модуля [`os`](https://docs-python.ru/standart-library/modul-os-python/ "Модуль os в Python, доступ к функциям ОС.") возвращает сообщение об ошибке, соответствующее коду ошибки, которая появляется при сбое в коде приложения.

Код ошибки при сбое приложения необходимо перехватывать.

На платформах, где функция `os.strerror()` возвращает `NULL` при получении неизвестного номера ошибки, возникает [исключение `ValueError`](https://docs-python.ru/tutorial/vstroennye-iskljuchenija-interpretator-python/vstroennye-iskljuchenija/ "Исключения наследуемые от Exception в Python.").

**Примеры использования:**
```python
>>> import os
# получение сообщения об ошибке из кода ошибки
>>> os.strerror(0)
# 'Success'
>>> os.strerror(1)
# 'Operation not permitted'
>>> os.strerror(19)
# 'No such process'
>>> os.strerror(50)
# 'No CSI structure available'
>>> os.strerror(19)
# 'No such device'
>>> os.strerror(113)
#  'No route to host'
```


## supports_dir_fd
[Доступность пути относительно дескриптора каталога в Python.](https://docs-python.ru/standart-library/modul-os-python/funktsija-supports-dir-fd-modulja-os/)

Функция `supports_dir_fd` модуля `os` возвращает объект `set`, указывающий, какие функции в модуле os принимают дескриптор открытого файла для своего параметра `dir_fd`.

**Пути относительно дескриптора каталога**: если `dir_fd` не `None`, это должен быть дескриптор файла, ссылающийся на каталог, а путь для работы должен быть задан относительно этого каталога. Если путь абсолютный, `dir_fd` игнорируется. Для систем POSIX Python будет вызывать вариант функции с суффиксом `'at'` и возможно, с префиксом `'f'`. Например, вызовет `faccessat` вместо `access`.

Вы можете проверить, поддерживается ли `dir_fd` для конкретной функции на вашей платформе, используя функцию, описанной ниже.

**Синтаксис:**
```python
import os

os.supports_dir_fd
```

**Возвращаемое значение:**
-   [`bool`](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/bool-logicheskij-tip-dannyh/ "Логический тип данных bool в Python.")

**Описание:**

Функция [`supports_dir_fd`](https://docs-python.ru/standart-library/modul-os-python/funktsija-supports-dir-fd-modulja-os/ "Функция supports_dir_fd модуля os в Python.") модуля [`os`](https://docs-python.ru/standart-library/modul-os-python/ "Модуль os в Python, доступ к функциям ОС.") возвращает [объект `set`](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-set-frozenset-mnozhestva/ "Множество set и frozenset в Python."), указывающий, какие функции в [модуле os](https://docs-python.ru/standart-library/modul-os-python/ "Модуль os в Python, доступ к функциям ОС.") принимают дескриптор открытого файла для своего параметра `dir_fd` - путь относительно дескриптора каталога.

Базовая функциональность, которую Python использует для реализации параметра `dir_fd`, доступна не на всех платформах, поддерживаемых Python. Ради согласованности функции, которые могут поддерживать `dir_fd`, Python всегда позволяют указывать этот параметр, но будет выдавать исключение, когда она не доступна на локальной ОС. Указание `None` для `dir_fd` всегда поддерживается на всех платформах.

Чтобы проверить, принимает ли конкретная функция дескриптор открытого файла для своего параметра `dir_fd`, используйте оператор `in` для `support_dir_fd`. Например, это выражение оценивается как `True`, если [функция `os.stat()`](https://docs-python.ru/standart-library/modul-os-python/funktsija-stat-modulja-os/ "Функция stat() модуля os в Python.") принимает дескрипторы открытого файла для `dir_fd` на локальной платформе:

```python
os.stat in os.supports_dir_fd
```

В настоящее время параметры `dir_fd` работают только на платформах Unix и не работает на Windows.

**Примеры использования:**
```python
>>> import os
>>> os.stat in os.supports_dir_fd
# True
```

## supports_effective_ids
[Доступность эффективных идентификаторов в функции в Python.](https://docs-python.ru/standart-library/modul-os-python/funktsija-supports-effective-ids-modulja-os/)

Функция `supports_effective_ids` модуля `os` возвращает множество `set`, указывающее, разрешает ли функция `os.access()` указывать `True` для своего параметр `аffective_ids` на локальной платформе.

**Синтаксис:**
```python
import os

os.supports_effective_ids
```
**Возвращаемое значение:**
-   [множество `set`](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-set-frozenset-mnozhestva/ "Множество set и frozenset в Python.").

**Описание:**

Функция [`supports_effective_ids`](https://docs-python.ru/standart-library/modul-os-python/funktsija-supports-effective-ids-modulja-os/ "Функция supports_effective_ids модуля os в Python.") модуля [`os`](https://docs-python.ru/standart-library/modul-os-python/ "Модуль os в Python, доступ к функциям ОС.") возвращает [множество `set`](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-set-frozenset-mnozhestva/ "Множество set и frozenset в Python."), указывающее, разрешает ли функция [`os.access()`](https://docs-python.ru/standart-library/modul-os-python/funktsija-access-modulja-os/ "Функция access() модуля os в Python.") указывать `True` для своего параметр `аffective_ids` на локальной платформе.

Задание `False` для `ffective_ids` всегда поддерживается на всех платформах. Если локальная платформа поддерживает это, множество будет содержать имя функции `os.access()`, в противном случае оно будет пустым.

Это выражение имеет значение `True`, если `os.access()` поддерживает `ffective_ids=True` на локальной платформе:

```python
os.access in os.supports_effective_ids
```

В настоящее время эффективные идентификаторы поддерживаются только на платформах Unix и не работают на Windows.

**Примеры использования:**
```python
>>> import os
>>> os.access in os.supports_effective_ids
# True
```

## supports_fd
[Доступность дескриптора открытого файла в функции в Python.](https://docs-python.ru/standart-library/modul-os-python/funktsija-supports-fd-modulja-os/)

Функция `supports_fd` модуля `os` возвращает объект `set`, указывающий, какие функции в модуле os позволяют указывать параметр пути в качестве дескриптора открытого файла на локальной платформе.

**Указание дескриптора файла**: обычно аргумент пути, предоставляемый функциям в [модуле `os`](https://docs-python.ru/standart-library/modul-os-python/ "Модуль os в Python, доступ к функциям ОС."), должен быть [строкой](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-str-tekstovye-stroki/ "Текстовые строки str в Python."), указывающей путь к файлу.

Некоторые функции теперь альтернативно принимают дескриптор открытого файла в качестве аргумента пути. Затем функция будет работать с файлом, на который ссылается дескриптор. Для систем POSIX Python будет вызывать вариант функции с префиксом `'f'`, например вызывать `fchdir` вместо `chdir`.

Вы можете проверить, можно ли указать путь в качестве дескриптора файла для конкретной функции на вашей платформе при помощи функции, описанной ниже

**Синтаксис:**
```python
import os

os.supports_fd
```
**Возвращаемое значение:**
-   [множество `set`](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-set-frozenset-mnozhestva/ "Множество set и frozenset в Python.").

**Описание:**

Функция [`supports_fd`](https://docs-python.ru/standart-library/modul-os-python/funktsija-supports-fd-modulja-os/ "Функция supports_fd модуля os в Python.") модуля [`os`](https://docs-python.ru/standart-library/modul-os-python/ "Модуль os в Python, доступ к функциям ОС.") возвращает [объект `set`](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-set-frozenset-mnozhestva/ "Множество set и frozenset в Python."), указывающий, какие функции в [модуле os](https://docs-python.ru/standart-library/modul-os-python/ "Модуль os в Python, доступ к функциям ОС.") позволяют указывать параметр пути в качестве дескриптора открытого файла на локальной платформе.

Базовая функциональность, которую Python использует для принятия дескрипторов открытых файлов в качестве аргументов пути, доступна не на всех платформах, поддерживаемых Python.

Чтобы определить, разрешает ли конкретная функция указывать дескриптор открытого файла для параметра пути, используйте оператор `in` для `support_fd`. Например, это выражение оценивается как `True`, если [функция `os.chdir()`](https://docs-python.ru/standart-library/modul-os-python/funktsija-chdir-modulja-os/ "Функция chdir() модуля os в Python.") принимает дескрипторы открытого файла для пути на вашей локальной платформе:

**Примеры использования:**
```python
>>> import os
>>> os.chdir in os.supports_fd
# True
```


## supports_follow_symlinks
[Поддержка платформой аргумента follow_symlinks в Python.](https://docs-python.ru/standart-library/modul-os-python/funktsija-supports-follow-symlinks-modulja-os/)

Функция `os.supports_follow_symlinks()` возвращает множество `set`, которое указывает какие функции в модуле `os` принимают `False` для их параметра `follow_symlinks` на локальной платформе.

**Следовать или НЕ следовать символическим ссылкам**: Если `follow_symlinks` имеет значение `False` и последний элемент пути является символической ссылкой, функция будет работать с самой символической ссылкой, а не с файлом, на который указывает ссылка. Для систем POSIX Python будет вызывать вариант функции c префиксом `'l'`, например [`os.lstat()`](https://docs-python.ru/standart-library/modul-os-python/funktsija-lstat-modulja-os/ "Функция lstat() модуля os в Python.").

Вы можете проверить, поддерживается ли аргумент `follow_symlinks` для определенной функции на вашей платформе при помощи описанной ниже функции.

**Синтаксис:**
```python
import os

os.supports_follow_symlinks
```

**Возвращаемое значение:**
-   [множество `set`](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-set-frozenset-mnozhestva/ "Множество set и frozenset в Python.").

**Описание:**

Функция [`os.supports_follow_symlinks()`](https://docs-python.ru/standart-library/modul-os-python/funktsija-supports-follow-symlinks-modulja-os/ "Функция supports_follow_symlinks модуля os в Python.") возвращает [множество `set`](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-set-frozenset-mnozhestva/ "Множество set и frozenset в Python."), которое указывает какие функции в [модуле `os`](https://docs-python.ru/standart-library/modul-os-python/ "Модуль os в Python, доступ к функциям ОС.") принимают `False` для их параметра `follow_symlinks` на локальной платформе.

Базовая функциональность, которую Python использует для реализации `follow_symlinks`, доступна не на всех платформах, поддерживаемых Python. Ради согласованности функции, которые могут поддерживать `follow_symlinks`, всегда позволяют указывать этот параметр, но выдают исключение, если функциональность не доступна локально. Указание `True` для `follow_symlinks` всегда поддерживается на всех платформах.

Чтобы проверить, принимает ли конкретная функция значение `False` для своего параметра `follow_symlinks`, используйте оператор `in` для `os.support_follow_symlinks`. Например, это выражение оценивается как `True`, если вы можете указать `follow_symlinks=False` при вызове [функции `os.stat()`](https://docs-python.ru/standart-library/modul-os-python/funktsija-stat-modulja-os/ "Функция stat() модуля os в Python.") на локальной платформе:

```python
os.stat in os.supports_follow_symlinks
```

**Примеры использования:**
```python
>>> import os
>>> os.stat in os.supports_follow_symlinks
# True
```


## truncate()
[Обрезать файл до определенного количества байт в Python.](https://docs-python.ru/standart-library/modul-os-python/funktsija-truncate-modulja-os/)

Функция `truncate()` модуля `os` обрезает файл, соответствующий пути `path`, так, чтобы он имел длину не более `length` байтов.

**Синтаксис:**
```python
import os

os.truncate(path, length)
```
**Параметры:**
-   `path` - [`str`](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-str-tekstovye-stroki/ "Текстовые строки str в Python."), путь в файловой системе до файла,
-   `length` - [`int`](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-int-tselye-chisla/ "Целые числа int в Python."), размер в байтах.

**Возвращаемое значение:**
-   `None`

**Описание:**

Функция [`truncate()`](https://docs-python.ru/standart-library/modul-os-python/funktsija-truncate-modulja-os/ "Функция truncate() модуля os в Python.") модуля [`os`](https://docs-python.ru/standart-library/modul-os-python/ "Модуль os в Python, доступ к функциям ОС.") обрезает файл, соответствующий пути `path`, так, чтобы он имел длину не более `length` [байтов](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-bytes-bajtovye-stroki/ "Байтовые строки bytes в Python.").

Аргумент `path` может принимать объекты, представляющие путь файловой системы, такие как [`pathlib.PurePath`](https://docs-python.ru/standart-library/modul-pathlib-python/klass-pathlib-purepath-podklassy/ "Класс pathlib.PurePath() и его подклассы."), так же может поддерживать указание [дескриптора файла](https://docs-python.ru/standart-library/modul-os-python/funktsija-supports-fd-modulja-os/ "Функция supports_fd модуля os в Python.").

Вызывает [событие аудита](https://docs-python.ru/standart-library/modul-sys-python/sobytie-audita-c/ "События аудита CPython.") `os.truncate` с аргументами `path`, `length`.

Доступность: Unix, Windows.

**Примеры использования:**
```python
>>> import os
>>> path = 'test_truncate.txt'
# создадим файл и запишем строку
>>> fp = open(path, 'w')
>>> fp.write('truncate data string')
>>> fp.close()
# обрезаем
>>> os.truncate(path, 8)
>>> fp = open(path, 'r')
>>> print(fp.read())
# `truncate`
>>> fp.close()
# очистка
>>> os.unlink(path)
```


## utime()
[Изменить время доступа и модификации файла в Python.](https://docs-python.ru/standart-library/modul-os-python/funktsija-utime-modulja-os/)

Функция `utime()` модуля `os` устанавливает/изменяет время доступа к файлу и время изменения файла, указанного в `path`.

**Синтаксис:**
```python
import os

os.utime(path, times=None, *, [ns, ]dir_fd=None, follow_symlinks=True)
```

**Параметры:**
-   `path` - [`str`](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-str-tekstovye-stroki/ "Текстовые строки str в Python."), путь в файловой системе до файла,
-   `times=None` - [кортеж](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-tuple-kortezh/ "Кортеж tuple в Python.") в форме `(atime, mtime)`
-   `ns` - [кортеж](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-tuple-kortezh/ "Кортеж tuple в Python.") в форме `(atime_ns, mtime_ns)`,
-   `dir_fd=None` - [`int`](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-int-tselye-chisla/ "Целые числа int в Python."), дескриптор каталога,
-   `follow_symlinks=True` - [`bool`](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/bool-logicheskij-tip-dannyh/ "Логический тип данных bool в Python."), переходить ли по ссылкам.

**Возвращаемое значение:**
-   `None`

**Описание:**

Функция [`utime()`](https://docs-python.ru/standart-library/modul-os-python/funktsija-utime-modulja-os/ "Функция utime() модуля os в Python.") модуля [`os`](https://docs-python.ru/standart-library/modul-os-python/ "Модуль os в Python, доступ к функциям ОС.") устанавливает/изменяет время доступа к файлу и время изменения файла, указанного в `path`.

Аргумент `path` может принимать объекты, представляющие путь файловой системы, такие как [`pathlib.PurePath`](https://docs-python.ru/standart-library/modul-pathlib-python/klass-pathlib-purepath-podklassy/ "Класс pathlib.PurePath() и его подклассы.").

Функция `os.utime()` принимает два необязательных параметра: `times` и `ns`. Они определяют время, которое устанавливается на файл и используются следующим образом:

-   Если указано `ns`, то это должен быть двойной [кортеж](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-tuple-kortezh/ "Кортеж tuple в Python.") в форме `(atime_ns, mtime_ns)`, где каждый член является [целым числом](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-int-tselye-chisla/ "Целые числа int в Python."), выражающим наносекунды.
-   Если `times` не равно `None`, то это должен двойной [кортеж](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-tuple-kortezh/ "Кортеж tuple в Python.") в форме `(atime, mtime)`, где каждый член является [целым числом](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-int-tselye-chisla/ "Целые числа int в Python.") или [`float`](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-float-veschestvennye-chisla/ "Вещественные числа float в Python.") в секундах.
-   Если `times` равно `None`, а `ns` не указано, то это эквивалентно указанию `ns=(atime_ns, mtime_ns)`, где оба элемента - текущее время.
-   Указывать кортежи как для `times`, так и для `ns` - это ошибка.

Обратите внимание, что точное время, установленное здесь, может не быть возвращено последующим вызовом [функцией `os.stat()`](https://docs-python.ru/standart-library/modul-os-python/funktsija-stat-modulja-os/ "Функция stat() модуля os в Python."), в зависимости от разрешения, с которым ваша операционная система записывает время доступа и изменения. Лучший способ сохранить точное время - это использовать поля `st_atime_ns` и `st_mtime_ns` из объекта результата `os.stat()` с параметром `ns` для `utime`.

Эта функция может поддерживать указание [дескриптора файла](https://docs-python.ru/standart-library/modul-os-python/funktsija-supports-fd-modulja-os/ "Функция supports_fd модуля os в Python.") и пути относительно [дескрипторов каталога](https://docs-python.ru/standart-library/modul-os-python/funktsija-supports-dir-fd-modulja-os/ "Функция supports_dir_fd модуля os в Python.") и может [не следовать символическим ссылкам](https://docs-python.ru/standart-library/modul-os-python/funktsija-supports-follow-symlinks-modulja-os/ "Функция supports_follow_symlinks модуля os в Python.") `follow_symlinks=False`.

Вызывает [событие аудита](https://docs-python.ru/standart-library/modul-sys-python/sobytie-audita-c/ "События аудита CPython.") `os.utime` с аргументами `path`, `times`, `ns`, `dir_fd`.

**Примеры использования:**
```python
>>> import os, time
>>> f = 'test_utime.txt'
>>> fp = open(f, 'w')
>>> fp.write('content')
>>> fp.close()
>>> atime = os.stat(f).st_atime
>>> mtime = os.stat(f).st_mtime
>>> print(time.ctime(atime), time.ctime(mtime))
# Thu Mar 19 12:20:05 2020, Thu Mar 19 12:20:14 2020

# изменим время
>>> delta = 60*60*24*15
>>> new_atime = atime - delta
>>> new_mtime = mtime - delta
>>> os.utime(f, times=(new_atime, new_mtime))
>>> atime = os.stat(f).st_atime
>>> mtime = os.stat(f).st_mtime
>>> print(time.ctime(atime), time.ctime(mtime))
# Wed Mar  4 12:20:05 2020, Wed Mar  4 12:20:14 2020

# Очистка
>>> os.unlink(f)
```


## Манипулирование списком контроля доступа ACL в Linux в Python.
[Установка, чтение и изменение расширенных атрибутов OS Linux в Python.](https://docs-python.ru/standart-library/modul-os-python/manipulirovanie-spiskom-kontrolja-dostupa-acl-linux/)

Примером использования [расширенных атрибутов](https://docs-python.ru/standart-library/modul-os-python/manipulirovanie-spiskom-kontrolja-dostupa-acl-linux/ "Манипулирование списком контроля доступа ACL в Linux.") является реализация списков контроля доступа POSIX ACL.

Чтобы определить, включена ли в вашей файловой системе поддержка `xattr`, проверьте файл параметров соответствующего устройства:

```bash
$ cat /proc/fs/ext4/sda1/options | grep xattr
user_xattr
```

**Все перечисленные здесь функции доступны только в Linux.**

-   [`os.getxattr`](https://docs-python.ru/standart-library/modul-os-python/manipulirovanie-spiskom-kontrolja-dostupa-acl-linux/#os.getxattr),
-   [`os.listxattr`](https://docs-python.ru/standart-library/modul-os-python/manipulirovanie-spiskom-kontrolja-dostupa-acl-linux/#os.listxattr),
-   [`os.removexattr`](https://docs-python.ru/standart-library/modul-os-python/manipulirovanie-spiskom-kontrolja-dostupa-acl-linux/#os.removexattr),
-   [`os.setxattr`](https://docs-python.ru/standart-library/modul-os-python/manipulirovanie-spiskom-kontrolja-dostupa-acl-linux/#os.setxattr),
-   [Возможные значения аргумента `flags`](https://docs-python.ru/standart-library/modul-os-python/manipulirovanie-spiskom-kontrolja-dostupa-acl-linux/#xattr-flag)

Аргумент во всех функциях `path` может принимать объекты, представляющие путь файловой системы, такие как [`pathlib.PurePath`](https://docs-python.ru/standart-library/modul-pathlib-python/klass-pathlib-purepath-podklassy/ "Класс pathlib.PurePath() и его подклассы.").

Так же все функции могут поддерживать указание [дескриптора файла](https://docs-python.ru/standart-library/modul-os-python/funktsija-supports-fd-modulja-os/ "Функция supports_fd модуля os в Python.") и [не следовать символическим ссылкам](https://docs-python.ru/standart-library/modul-os-python/funktsija-supports-follow-symlinks-modulja-os/ "Функция supports_follow_symlinks модуля os в Python.") `follow_symlinks=False`.

 **_`os.getxattr(path, attribute, *, follow_symlinks=True)`_:**

Функция [`os.getxattr()`](https://docs-python.ru/standart-library/modul-os-python/manipulirovanie-spiskom-kontrolja-dostupa-acl-linux/#os.getxattr) вернет значение расширенного атрибута `attribute` файловой системы для пути `path`.

Аргумент `attribute` может быть [`bytes`](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-bytes-bajtovye-stroki/ "Байтовые строки bytes в Python.") или [`str`](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-str-tekstovye-stroki/ "Текстовые строки str в Python."), переданный прямо или косвенно через [интерфейс PathLike](https://docs-python.ru/standart-library/modul-os-python/predstavlenie-puti-fajlovoj-sisteme/ "Представление пути в файловой системе."). Если это [строка](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-str-tekstovye-stroki/ "Текстовые строки str в Python."), то она кодируется с помощью кодировки файловой системы.

Функция `os.getxattr()` вызывает [событие аудита](https://docs-python.ru/standart-library/modul-sys-python/sobytie-audita-c/ "События аудита CPython.") `os.getxattr` с аргументами `path`, `attribute`.

**_`os.listxattr(path=None, *, follow_symlinks=True)`_:**

Функция [`os.listxattr()`](https://docs-python.ru/standart-library/modul-os-python/manipulirovanie-spiskom-kontrolja-dostupa-acl-linux/#os.listxattr) вернет [список](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-list-spisok/ "Список list в Python.") расширенных атрибутов файловой системы по пути `path`. Атрибуты в списке представлены в виде [строк](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-str-tekstovye-stroki/ "Текстовые строки str в Python."), декодированных в кодировке файловой системы. Если путь отсутствует, то `os.listxattr()` будет проверять текущий каталог.

Функция `os.listxattr()` вызывает [событие аудита](https://docs-python.ru/standart-library/modul-sys-python/sobytie-audita-c/ "События аудита CPython.") `os.listxattr` с аргументом `path`.

 **_`os.removexattr(path, attribute, *, follow_symlinks=True)`_:**

Функция [`os.removexattr()`](https://docs-python.ru/standart-library/modul-os-python/manipulirovanie-spiskom-kontrolja-dostupa-acl-linux/#os.removexattr) удаляет расширенный атрибут `attribute` из пути `path` файловой системы.

Аргумент `attribute` может быть [`bytes`](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-bytes-bajtovye-stroki/ "Байтовые строки bytes в Python.") или [`str`](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-str-tekstovye-stroki/ "Текстовые строки str в Python."), переданный прямо или косвенно через [интерфейс PathLike](https://docs-python.ru/standart-library/modul-os-python/predstavlenie-puti-fajlovoj-sisteme/ "Представление пути в файловой системе."). Если это [строка](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-str-tekstovye-stroki/ "Текстовые строки str в Python."), то она кодируется с помощью кодировки файловой системы.

Функция `os.removexattr()` вызывает [событие аудита](https://docs-python.ru/standart-library/modul-sys-python/sobytie-audita-c/ "События аудита CPython.") `os.removexattr` с аргументами `path`, `attribute`.

 **_`os.setxattr(path, attribute, value, flags=0, *, follow_symlinks=True)`_:**

Функция [`os.setxattr()`](https://docs-python.ru/standart-library/modul-os-python/manipulirovanie-spiskom-kontrolja-dostupa-acl-linux/#os.setxattr) установит атрибут `attribute` расширенной файловой системы на путь `path` на значение `value`.

Атрибут `attribute` должен быть [`bytes`](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-bytes-bajtovye-stroki/ "Байтовые строки bytes в Python.") или [`str`](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-str-tekstovye-stroki/ "Текстовые строки str в Python.") без встроенных `NUL`, переданный прямо или косвенно через [интерфейс PathLike](https://docs-python.ru/standart-library/modul-os-python/predstavlenie-puti-fajlovoj-sisteme/ "Представление пути в файловой системе."). Если это [строка](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-str-tekstovye-stroki/ "Текстовые строки str в Python."), то она кодируется с помощью кодировки файловой системы.

Флаги могут быть `os.XATTR_REPLACE` или `XATTR_CREATE`.

-   Если задано `os.XATTR_REPLACE` и атрибут не существует, то будет вызван `EEXISTS`.
-   Если задано `os.XATTR_CREATE` и атрибут уже существует, атрибут не будет создан и будет вызван `ENODATA` .

**Примечание**. Ошибка в версиях ядра Linux ниже 2.6.39 приводила к игнорированию аргумента `flags` в некоторых файловых системах.

Функция `os.setxattr()` вызывает [событие аудита](https://docs-python.ru/standart-library/modul-sys-python/sobytie-audita-c/ "События аудита CPython.") `os.setxattr` с аргументами `path`, `attribute`, `value`, `flags`.

**Возможные значения аргумента `flags`:**

**_`os.XATTR_SIZE_MAX`_:**

Максимальный размер значения расширенного атрибута может быть. В настоящее время это 64 КиБ в Linux.

**_`os.XATTR_CREATE`_:**

Это возможное значение для аргумента `flags` в [функции `os.setxattr()`](https://docs-python.ru/standart-library/modul-os-python/manipulirovanie-spiskom-kontrolja-dostupa-acl-linux/#os.setxattr) и означает, что операция должна создать атрибут.

**_`os.XATTR_REPLACE`_:**

Это возможное значение для аргумента `flags` в [функции `os.setxattr()`](https://docs-python.ru/standart-library/modul-os-python/manipulirovanie-spiskom-kontrolja-dostupa-acl-linux/#os.setxattr) и означает, что операция должна заменить существующий атрибут.

## abort()
[Сигнал abort для текущего процесса в Python.](https://docs-python.ru/standart-library/modul-os-python/funktsija-abort-modulja-os/)

Функция `abort()` модуля `os` генерирует сигнала `SIGABRT` для текущего процесса.

**Синтаксис:**
```python
import os

os.abort()
```
**Параметры:**
Нет

**Возвращаемое значение:**
-   `None`

**Описание:**

Функция [`abort()`](https://docs-python.ru/standart-library/modul-os-python/funktsija-abort-modulja-os/ "Функция abort() модуля os в Python.") модуля [`os`](https://docs-python.ru/standart-library/modul-os-python/ "Модуль os в Python, доступ к функциям ОС.") генерирует сигнала `SIGABRT` для текущего процесса.

-   В Unix стандартным поведением является создание дампа ядра.
-   В Windows процесс немедленно возвращает код завершения 3.

Имейте в виду, что вызов этой функции не вызовет обработчик сигнала Python, зарегистрированный для `SIGABRT` с вызовом [функции `signal.signal()`](https://docs-python.ru/standart-library/modul-signal-python/funktsija-signal-modulja-signal/ "Функция signal() модуля signal в Python.").

## exec*()
[Выполнить программу с заменой текущего процесса в Python.](https://docs-python.ru/standart-library/modul-os-python/funktsija-exec-modulja-os/)

[Функции `os.exec*()`](https://docs-python.ru/standart-library/modul-os-python/funktsija-exec-modulja-os/ "Функция exec*() модуля os в Python.") принимают список аргументов для новой программы, загруженной в процесс. В каждом случае первый из этих аргументов передается новой программе как собственное имя, а не как аргумент, который пользователь мог ввести в командной строке. Для программиста на Си это `argv[0]`, переданный в `main()` программы. Например, `os.execv('/bin/echo', ['foo', 'bar'])` будет печатать строку только при стандартном выводе, `foo` будет казаться проигнорированным.

**Синтаксис:**
```python
import os

os.execl(path, arg0, arg1, ...)
os.execle(path, arg0, arg1, ..., env)
os.execlp(file, arg0, arg1, ...)
os.execlpe(file, arg0, arg1, ..., env)
os.execv(path, args)
os.execve(path, args, env)
os.execvp(file, args)
os.execvpe(file, args, env)
```

**Параметры:**
-   `path` - [`str`](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-str-tekstovye-stroki/ "Текстовые строки str в Python."), путь в файловой системе запускаемой программы,
-   `arg0`, `arg1` - аргументы командной строки запускаемой программы,
-   `file` - [`str`](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-str-tekstovye-stroki/ "Текстовые строки str в Python."), файла запускаемой программы,
-   `args` - [список](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-list-spisok/ "Список list в Python.") аргументов командной строки запускаемой программы,
-   `env` - [`dict`](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-dict-slovar/ "Словарь dict в Python.") - переменная среда для выполнения программы.

**Возвращаемое значение:**
-   `None`

**Описание:**

Все эти функции выполняют новую программу, заменяя текущий процесс. Они ничего не возвращают. В Unix новый исполняемый файл загружается в текущий процесс и будет иметь тот же [идентификатор процесса](https://docs-python.ru/standart-library/modul-os-python/izvlechenie-ustanovka-uid-gid-pid-protsessa/ "Извлечение/установка uid, gid и pid процесса."), что и вызывающая программа. Ошибки будут сообщаться как [исключения `OSError`](https://docs-python.ru/tutorial/vstroennye-iskljuchenija-interpretator-python/oshibki-operatsionnoj-sistemy-oserror/ "Исключения операционной системы: OSError в Python.").

Текущий процесс заменяется немедленно. Объекты и дескрипторы открытого файла не сбрасываются, поэтому, если в этих открытых файлах могут быть буферизованные данные, то перед вызовом [функции `os.exec*()`](https://docs-python.ru/standart-library/modul-os-python/funktsija-exec-modulja-os/ "Функция exec*() модуля os в Python.") необходимо их очистить с помощью [`sys.stdout.flush()`](https://docs-python.ru/standart-library/modul-sys-python/obekty-stdin-stdout-stderr-modulja-sys/ "Объекты stdin, stdout, stderr модуля sys в Python.") или `os.fsync()`.

Варианты `'l'` и `'v'` функций `exec*()` отличаются тем, как передаются аргументы командной строки. С вариантами `'l'` работать легче всего, если число параметров фиксировано при написании кода, отдельные параметры просто становятся дополнительными параметрами для функций `os.execl*()`. Варианты `'v'` хороши, когда число параметров является переменным, а аргументы передаются в [списке](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-list-spisok/ "Список list в Python.") или [кортеже](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-tuple-kortezh/ "Кортеж tuple в Python.") в качестве параметра `args`. В любом случае аргументы дочернего процесса должны начинаться с имени выполняемой команды, но это не применяется.

Варианты, которые включают `'p'` в конце (`os.execlp()`, `os.execlpe()`, `os.execvp()` и `os.execvpe()`), будут использовать переменную среды `PATH` для определения местоположения файла `file` программы. Когда среда выполнения заменяется с использованием одного из вариантов `os.exec*e()`, описанного в следующем параграфе, новая среда выполнения `env` используется в качестве источника переменной `PATH`. Другие варианты, `os.execl()`, `os.execle()`, `os.execv()` и `os.execve()`, не будут использовать переменную `PATH` для поиска исполняемого файла. Путь должен содержать соответствующий абсолютный или относительный путь.

Для `os.execle()`, `os.execlpe()`, `os.execve()` и `os.execvpe()`, обратите внимание, что все они заканчиваются на `'e'`, параметр `env` должен быть [словарем](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-dict-slovar/ "Словарь dict в Python."), который используется для определения переменной среды для нового процесса, т. е. `env` будет использоваться вместо среды текущего процесса. Функции `os.execl()`, `os.execlp()`, `os.execv()` и `os.execvp()` заставляют новый процесс наследовать среду текущего процесса.

Для `os.execve()` на некоторых платформах путь `path` также может быть указан как [дескриптор открытого файла](https://docs-python.ru/standart-library/modul-os-python/funktsija-supports-fd-modulja-os/ "Функция supports_fd модуля os в Python."). Эта функциональность может не поддерживаться на вашей платформе. Вы можете проверить, доступен ли он, используя [`os.supports_fd`](https://docs-python.ru/standart-library/modul-os-python/funktsija-supports-fd-modulja-os/ "Функция supports_fd модуля os в Python."). Если он недоступен, его использование вызовет [исключение `NotImplementedError`](https://docs-python.ru/tutorial/vstroennye-iskljuchenija-interpretator-python/vstroennye-iskljuchenija/ "Исключения наследуемые от Exception в Python.").

Все эти функции вызывают [событие аудита](https://docs-python.ru/standart-library/modul-sys-python/sobytie-audita-c/ "События аудита CPython.") `os.exec` с аргументами `path`, `args`, `env`.

Доступность: Unix, Windows.


## popen()
[Открыть канал ввода-вывода запущенной программы в Python.](https://docs-python.ru/standart-library/modul-os-python/funktsija-popen-modulja-os/)

Функция popen() модуля os откроет канал для чтения или записи стандартного ввода-вывода запущенной команды cmd.

**Синтаксис:**
```python
import os

os.popen(cmd, mode='r', buffering=-1)
```

**Параметры:**
-   `cmd` - [`str`](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-str-tekstovye-stroki/ "Текстовые строки str в Python."), запущенная команда,
-   `mode` - [`str`](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-str-tekstovye-stroki/ "Текстовые строки str в Python."), режим открытия канала,
-   `buffering` - [`str`](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-str-tekstovye-stroki/ "Текстовые строки str в Python."), буферизация.

**Возвращаемое значение:**
-   [объект файла](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-file-object-fajly-potoki/ "Файловый объект file object в Python.").

**Описание:**

Функция [`popen()`](https://docs-python.ru/standart-library/modul-os-python/funktsija-popen-modulja-os/ "Функция popen() модуля os в Python.") модуля [`os`](https://docs-python.ru/standart-library/modul-os-python/ "Модуль os в Python, доступ к функциям ОС.") откроет канал для чтения или записи стандартного ввода-вывода запущенной команды `cmd`.

Возвращаемое значение - это открытый [объект файла](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-file-object-fajly-potoki/ "Файловый объект file object в Python."), подключенный к каналу, который может быть прочитан или записан в зависимости от того, является ли режим `mode` `'r'` или `'w'`.

Аргумент буферизации `buffering` имеет то же значение, что и соответствующий аргумент [встроенной функции `open()`](https://docs-python.ru/tutorial/vstroennye-funktsii-interpretatora-python/funktsija-open/ "Функция open() в Python, открывает файл на чтение/запись."). Возвращенный объект файла читает или записывает [текстовые строки](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-str-tekstovye-stroki/ "Текстовые строки str в Python."), а не байты.

Метод [`file.close()`](https://docs-python.ru/tutorial/metody-fajlovogo-obekta-potoka-python/metod-file-close/ "Метод file.close() в Python, закрывает файл.") возвращает `None`, если субпроцесс `subprocess` завершился успешно или вернет код возврата подпроцесса ([`int`](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-int-tselye-chisla/ "Целые числа int в Python.")) , если произошла ошибка. В системах POSIX, если код возврата положительный, он представляет возвращаемое значение процесса, сдвинутое влево на один байт. Если код возврата отрицателен, процесс был прерван сигналом, заданным отрицательным значением кода возврата. Например, возвращаемое значение может быть - `signal.SIGKILL`, если субпроцесс был убит. В системах Windows возвращаемое значение содержит целочисленный код возврата со знаком от дочернего процесса.

Более удобный вариант функции `os.popen()` реализован в модуле [`subprocess.Popen`](https://docs-python.ru/standart-library/modul-subprocess-python/klass-popen-modulja-subprocess/ "Класс Popen() модуля subprocess в Python."). Модуль [`subprocess`](https://docs-python.ru/standart-library/modul-subprocess-python/ "Модуль subprocess в Python, запуск новых процессов.") предлагает более мощные способы управления и взаимодействия с подпроцессами.

**Примеры запуска программ функцией `os.popen()`:**
```python
>>> import os
# указывайте полный путь к запускаемой 
# программе/команде или она не будет работать
# листинг каталога 'ls -l'
>>> cmd = '/bin/ls -l'
>>> output = os.popen(cmd, 'r')
>>> for line in output:
...     print(line, end='')
...

# итого 3184
# drwxrwxr-x 10 docs-python docs-python    4096 ноя 17 17:47 ansible
# drwxrwxr-x  15 docs-python docs-python    4096 дек 19 10:05 MyDocuments
# drwxr-xr-x  2 docs-python docs-python    4096 мар 20 12:34 Desktop
# drwxrwxr-x  2 docs-python docs-python    4096 фев  9 19:02 DOCS
# drwxr-xr-x 17 docs-python docs-python    4096 мар 19 17:49 Downloads
# ... 
# ...
```

## system()
[Запустить/выполнить внешнюю команду в оболочке в Python.](https://docs-python.ru/standart-library/modul-os-python/funktsija-system-modulja-os/)

Функция `system()` модуля os выполяет команду `command` в подоболочке (subshell). Это реализуется путем вызова стандартной функции языка Си `system()` и имеет те же ограничения.

**Синтаксис:**
```python
import os

os.system(command)
```

**Параметры:**
-   `command` - [`str`](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-str-tekstovye-stroki/ "Текстовые строки str в Python."), команда.

**Возвращаемое значение:**
-   индикация состояния выхода.

**Описание:**

Функция [`system()`](https://docs-python.ru/standart-library/modul-os-python/funktsija-system-modulja-os/ "Функция system() модуля os в Python.") модуля [`os`](https://docs-python.ru/standart-library/modul-os-python/ "Модуль os в Python, доступ к функциям ОС.") выполняет команду `command` в подоболочке (`subshell`). Это реализуется путем вызова стандартной функции языка Си `system()` и имеет те же ограничения. Изменения в [`sys.stdin`](https://docs-python.ru/standart-library/modul-sys-python/obekty-stdin-stdout-stderr-modulja-sys/ "Объекты stdin, stdout, stderr модуля sys в Python.") и т. д. не отражаются в среде выполняемой команды. Если команда генерирует какой-либо вывод, он будет отправлен в стандартный поток вывода интерпретатора.

В Unix возвращаемое значение является состоянием выхода процесса, закодированного в формате, указанном как для функции [`os.wait()`](https://docs-python.ru/standart-library/modul-os-python/funktsija-wait-modulja-os/ "Функция wait() модуля os в Python."). Обратите внимание, что POSIX не определяет значение возвращаемого значения функции Си `system()`, поэтому возвращаемое значение функции Python зависит от системы.

В Windows возвращаемое значение возвращается системной оболочкой после выполнения команды. Оболочка задается переменной среды Windows COMSPEC: обычно это `cmd.exe`, который возвращает состояние завершения выполнения команды. В системах, использующих не нативную оболочку, смотрите документацию по вашей оболочке.

Используйте эту функцию, если надо тупо запустить что-то из кода Python и не ждать результатов выполнения, по принципу - запустил и забыл.

Другими словами, запуская команду функцией `os.system(cmd)` **НЕ получится получить/перенаправить вывод**, который дает команда/программа `cmd`. Для извлечения данных из стандартного потока вывода воспользуйтесь [модулем `subprocess`](https://docs-python.ru/standart-library/modul-subprocess-python/ "Модуль subprocess в Python, запуск новых процессов.") или по крайней мере [функцией `os.popen()`](https://docs-python.ru/standart-library/modul-os-python/funktsija-popen-modulja-os/ "Функция popen() модуля os в Python."):
```python
from subprocess import run, STDOUT, PIPE
# указывайте полный путь к запускаемой 
# программе/команде или она не будет работать
cmd = '/bin/ls -l /path/to/ls-dir'
# перенаправляем `stdout` и `stderr` в переменную `output`
output = run(cmd.split(), stdout=PIPE, stderr=STDOUT, text=True)
print(output)
```
[Модуль `subprocess`](https://docs-python.ru/standart-library/modul-subprocess-python/ "Модуль subprocess в Python, запуск новых процессов.") предоставляет более мощные средства для порождения новых процессов и **получения их результатов**. Использование модуля `subprocess` предпочтительнее, чем использование этой функции.

Вызывает [событие аудита](https://docs-python.ru/standart-library/modul-sys-python/sobytie-audita-c/ "События аудита CPython.") `os.system` с аргументом `command`.

Доступность: Unix, Windows.

**Примеры запуска программ функцией `os.system(cmd)`:**
```python
import os
# указывайте полный путь к запускаемой 
# программе/команде или она не будет работать
>>> cmd = '/path/from/your/programm-or-cmd'
>>> code_exit = os.system(cmd)
>>> code_exit
# выведет:
# 0 - успех выполнения команды,
# что означает код завершения программы.
```

## exit()
[Выход из процесса без вызова обработчиков очистки в Python.](https://docs-python.ru/standart-library/modul-os-python/funktsija-exit-modulja-os/)

Функция `_exit()` модуля `os` осуществляет выход из процесса со статусом `n`, без вызова обработчиков очистки, сброса буферов `stdio` и т. д.

**Синтаксис:**
```python
import os

os._exit(n)
```
**Параметры:**
-   `n` - [код выхода](https://docs-python.ru/standart-library/modul-os-python/funktsija-exit-modulja-os/#exit_code).

**Возвращаемое значение:**
-   [`int`](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-int-tselye-chisla/ "Целые числа int в Python.") статус выхода.

**Описание:**

Функция [`_exit()`](https://docs-python.ru/standart-library/modul-os-python/funktsija-exit-modulja-os/ "Функция _exit() модуля os в Python.") модуля [`os`](https://docs-python.ru/standart-library/modul-os-python/ "Модуль os в Python, доступ к функциям ОС.") осуществляет выход из процесса со статусом `n`, без вызова обработчиков очистки, сброса буферов `stdio` и т. д.

**Примечание**. Стандартный способ выхода это [sys.exit(n)](https://docs-python.ru/standart-library/modul-sys-python/funktsija-exit-modulja-sys/ "Функция exit() модуля sys в Python."). Функция `os._exit()` обычно следует использовать только в дочернем процессе после выполнения [`os.fork()`](https://docs-python.ru/standart-library/modul-os-python/funktsija-fork-modulja-os/ "Функция fork() модуля os в Python.").

**Коды выхода:**

Определены следующие коды выхода, которые могут использоваться с [`os._exit()`](https://docs-python.ru/standart-library/modul-os-python/funktsija-exit-modulja-os/ "Функция _exit() модуля os в Python."), хотя они не обязательны. Обычно они используются для системных программ, написанных на Python, таких как внешняя программа доставки команд почтового сервера.

**Примечание**. Некоторые из них могут быть доступны не на всех платформах Unix, поскольку есть некоторые различия. Эти константы определяются там, где они определяются базовой платформой.

**_`os.EX_OK`_:**
Код выхода, который означает, что ошибка не произошла. Доступность: Unix.

**_`os.EX_USAGE`_:**
Код выхода, который означает, что команда использовалась неправильно, например, когда задано неправильное количество аргументов. Доступность: Unix.

**_`os.EX_DATAERR`_:**
Код выхода, который означает, что входные данные были неверными. Доступность: Unix.

**_`os.EX_NOINPUT`_:**
Код выхода, означающий, что входной файл не существует или недоступен для чтения. Доступность: Unix.

**_`os.EX_NOUSER`_:**
Код выхода, означающий, что указанный пользователь не существует. Доступность: Unix.

**_`os.EX_NOHOST`_:**
Код выхода, означающий, что указанный хост не существует. Доступность: Unix.

**_`os.EX_UNAVAILABLE`_:**
Код выхода, который означает, что требуемая служба недоступна. Доступность: Unix.

**_`os.EX_SOFTWARE`_:**
Код выхода, который означает, что была обнаружена внутренняя программная ошибка. Доступность: Unix.

**_`os.EX_OSERR`_:**
Код выхода, который означает, что обнаружена ошибка операционной системы, например, невозможность разветвления или создания канала. Доступность: Unix.

**_`os.EX_OSFILE`_:**
Код выхода, который означает, что какой-то системный файл не существует, не может быть открыт или произошла какая-либо другая ошибка. Доступность: Unix.

**_`os.EX_CANTCREAT`_:**
Код выхода, означающий, что указанный пользователем файл вывода не может быть создан. Доступность: Unix.

**_`os.EX_IOERR`_:**
Код выхода, который означает, что произошла ошибка при выполнении ввода-вывода в каком-либо файле. Доступность: Unix.

**_`os.EX_TEMPFAIL`_:**
Код выхода, означающий, что произошел временный сбой. Это указывает на то, что на самом деле не может быть ошибкой, например, на сетевое соединение, которое не может быть установлено во время повторяющейся операции. Доступность: Unix.

**_`os.EX_PROTOCOL`_:**
Код выхода, означающий, что обмен протоколом был недопустимым, недействительным или непонятным. Доступность: Unix.

**_`os.EX_NOPERM`_:**
Выйдите из кода, что означает, что для выполнения операции было недостаточно прав (но не предназначено для проблем с файловой системой). Доступность: Unix.

**_`os.EX_CONFIG`_:**
Код выхода, который означает, что произошла какая-то ошибка конфигурации. Доступность: Unix.

**_`os.EX_NOTFOUND`_:**
Код выхода, который означает что-то вроде «запись не найдена». Доступность: Unix.


## fork()
[Создание дочернего процесса в Python.](https://docs-python.ru/standart-library/modul-os-python/funktsija-fork-modulja-os/)

Функция `fork()` модуля `os` форкает дочерний процесс. Возвращает `0` в дочернем элементе и идентификатор дочернего процесса в родительском элементе.

**Синтаксис:**
```python
import os

os.fork()
```

**Параметры:**
-   Нет

**Описание:**

Функция [`fork()`](https://docs-python.ru/standart-library/modul-os-python/funktsija-fork-modulja-os/ "Функция fork() модуля os в Python.") модуля [`os`](https://docs-python.ru/standart-library/modul-os-python/ "Модуль os в Python, доступ к функциям ОС.") создает клон текущего процесса как дочерний процесс. Возвращает `0` в дочернем процессе и идентификатор дочернего процесса в родительском элементе. Если возникает ошибка, то возникает [исключение `OSError`](https://docs-python.ru/tutorial/vstroennye-iskljuchenija-interpretator-python/oshibki-operatsionnoj-sistemy-oserror/ "Исключения операционной системы: OSError в Python.").

Обратите внимание, что некоторые платформы, включая FreeBSD <= 6.3 и Cygwin, имеют известные проблемы при использовании `os.fork()` из потока.

Вызывает [событие аудита](https://docs-python.ru/standart-library/modul-sys-python/sobytie-audita-c/ "События аудита CPython.") `os.fork` без аргументов.

Много литературы написано о надежном использовании системных вызовов `fork()` и `exec()` в Mac OS X, Linux и других вариантах Unix, поэтому советуем почитать немного дополнительной литературы.

**Примеры использования создания дочерних процессов:**

После разветвления, два процесса выполняют один и тот же код. Чтобы программа узнала, в каком она находится, она должна проверить возвращаемое значение [`os.fork()`](https://docs-python.ru/standart-library/modul-os-python/funktsija-fork-modulja-os/ "Функция fork() модуля os в Python."). Если значение равно `0`, текущий процесс является дочерним. Если это не `0`, программа выполняется в родительском процессе, а возвращаемое значение является идентификатором процесса дочернего процесса.
```python
# test_fork.py
import os

pid = os.fork()

if pid:
    print('Child process id:', pid)
else:
    print('I am the child')

# $ python3 test_fork.py
# Child process id: 20131
# I am the child
```

Родитель может отправлять сигналы дочернему процессу, используя [функцию `os.kill()`](https://docs-python.ru/standart-library/modul-os-python/funktsija-kill-modulja-os/ "Функция kill() модуля os в Python.") используя [модуль `signal`](https://docs-python.ru/standart-library/modul-signal-python/ "Модуль signal в Python, создание обработчиков сигналов."). В этом примере используется короткая пауза, чтобы дать дочернему процессу время для настройки обработчика сигнала. Реальное приложение, не будет нуждаться в вызове [`time.sleep()`](https://docs-python.ru/standart-library/modul-time-python/funktsija-sleep-modulja-time/ "Функция sleep() модуля time в Python."). В дочернем процессе установим обработчик сигнала и сделаем небольшую паузу, чтобы предоставить родительскому процессу достаточно времени для отправки сигнала.
```python
# test_kill.py
import os
import signal
import time

def signal_usr1(signum, frame):
    "Обратный вызов вызывается при получении сигнала"
    pid = os.getpid()
    print(f'Получен USR1 в процессе {pid}')

print('Forking...')
child_pid = os.fork()
if child_pid:
    print('PARENT: Пауза перед отправкой сигнала ...')
    time.sleep(1)
    print(f'PARENT: передача сигналов {child_pid}')
    os.kill(child_pid, signal.SIGUSR1)
else:
    print('CHILD: Настройка обработчика сигнала')
    signal.signal(signal.SIGUSR1, signal_usr1)
    print('CHILD: Пауза в ожидании сигнала')
    time.sleep(5)

# $ python3 test_kill.py
# Forking...
# PARENT: Пауза перед отправкой сигнала ...
# CHILD: Настройка обработчика сигнала
# CHILD: Пауза в ожидании сигнала
# PARENT: передача сигналов 21168
# Получен USR1 в процессе 21168
```

Простой способ обработать отдельное поведение в дочернем процессе - проверить возвращаемое значение `os.fork()` и `branch`. Более сложное поведение может потребовать большего разделения кода, чем простая ветвь. В других случаях может существовать программа, которую необходимо обернуть. Для обеих этих ситуаций можно использовать серию [функций `os.exec*()`](https://docs-python.ru/standart-library/modul-os-python/funktsija-exec-modulja-os/ "Функция exec*() модуля os в Python.") для запуска другой программы.
```python
# test_exec.py
import os

child_pid = os.fork()
if child_pid:
    os.waitpid(child_pid, 0)
else:
    os.execlp('pwd', 'pwd', '-P')

# $ python3 test_exec.py
# /home/docs-python
```

Когда программа запускается функцией `os.exec()`, код из этой программы заменяет код из существующего процесса.

**Примеры использования ожидания дочерних процессов:**

Много ресурсоемких программ, используется несколько процессов, чтобы обойти ограничения многопоточности в Python и [глобальную блокировку интерпретатора GIL](https://docs-python.ru/tutorial/mnogopotochnost-python/global-interpreter-lock-gil/ "Global Interpreter Lock (GIL) в Python."). При запуске нескольких процессов для выполнения отдельных задач мастеру нужно будет дождаться завершения одного или нескольких из них, прежде чем запускать новые, чтобы избежать перегрузки сервера. Существует несколько различных способов сделать это с помощью [функции `os.wait()`](https://docs-python.ru/standart-library/modul-os-python/funktsija-wait-modulja-os/ "Функция wait() модуля os в Python.") и связанных с ней функций.

Когда не имеет значения, какой дочерний процесс может завершиться первым, используйте `os.wait()`. Он возвращается, как только завершается любой дочерний процесс.
```python
# test_wait.py
import os
import sys
import time

for i in range(2):
    print(f'PARENT {os.getpid()}: Forking {i}')
    worker_pid = os.fork()
    if not worker_pid:
        print(f'WORKER {i}: Starting')
        time.sleep(2 + i)
        print(f'WORKER {i}: Finishing')
        sys.exit(i)

for i in range(2):
    print(f'PARENT: Waiting for {i}')
    done = os.wait()
    print(f'PARENT: Child done: {done}')

# $ python3 test_wait.py 
# PARENT 24512: Forking 0
# PARENT 24512: Forking 1
# WORKER 0: Starting
# PARENT: Waiting for 0
# WORKER 1: Starting
# WORKER 0: Finishing
# PARENT: Child done: (24513, 0)
# PARENT: Waiting for 1
# WORKER 1: Finishing
# PARENT: Child done: (24514, 256)
```

Функция `os.wait()` возвращает идентификатор процесса и код завершения, упакованный в 16-битовое значение. Младший байт представляет номер сигнала, прекратившего выполнение процесса, а старший - код состояния, возвращенный процессом по его завершении.

Чтобы дождаться определенного процесса, используйте [функцию `os.waitpid()`](https://docs-python.ru/standart-library/modul-os-python/funktsija-waitpid-modulja-os/ "Функция waitpid() модуля os в Python.").

Функция `os.waitpid()`, которой передан идентификатор целевого процесса, будет блокироваться до тех пор, пока процесс не завершится.
```python
# test_waitpid.py
import os
import sys
import time

workers = []
for i in range(2):
    print(f'PARENT {os.getpid()}: Forking {i}')
    worker_pid = os.fork()
    if not worker_pid:
        print(f'WORKER {i}: Starting')
        time.sleep(2 + i)
        print(f'WORKER {i}: Finishing')
        sys.exit(i)
    workers.append(worker_pid)

for pid in workers:
    print(f'PARENT: Waiting for {pid}')
    done = os.waitpid(pid, 0)
    print(f'PARENT: Child done: {done}')

# $ python3 test_waitpid.py 
# PARENT 25144: Forking 0
# PARENT 25144: Forking 1
# WORKER 0: Starting
# PARENT: Waiting for 25145
# WORKER 1: Starting
# WORKER 0: Finishing
# PARENT: Child done: (25145, 0)
# PARENT: Waiting for 25146
# WORKER 1: Finishing
# PARENT: Child done: (25146, 256)
```


## kill() 
[Послать сигнал процессу или группе процессов в Python.](https://docs-python.ru/standart-library/modul-os-python/funktsija-kill-modulja-os/)

Функция `kill()` модуля `os` послает сигнал `sig` на процессу `pid`.

**Синтаксис:**
```python
import os

os.kill(pid, sig)
os.killpg(pgid, sig)
```

**Параметры:**
-   `pid` - [сигнал](https://docs-python.ru/standart-library/modul-signal-python/ "Модуль signal в Python, создание обработчиков сигналов."),
-   `sig` - [`int`](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-int-tselye-chisla/ "Целые числа int в Python.") процесс,
-   `pgid` - [`int`](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-int-tselye-chisla/ "Целые числа int в Python.") группа процессов,

**Возвращаемое значение:**
-   `None`

Вызывает событие аудита os.killpg с аргументами pgid, sig.

**Описание:**

**Функция [`kill()`](https://docs-python.ru/standart-library/modul-os-python/funktsija-kill-modulja-os/ "Функция kill() модуля os в Python.")** модуля [`os`](https://docs-python.ru/standart-library/modul-os-python/ "Модуль os в Python, доступ к функциям ОС.") посылает сигнал `sig` процессу `pid`. Константы для конкретных сигналов, доступных на хост-платформе, определяются в [модуле `signal`](https://docs-python.ru/standart-library/modul-signal-python/ "Модуль signal в Python, создание обработчиков сигналов.").

Функция `os.kill()` [событие аудита](https://docs-python.ru/standart-library/modul-sys-python/sobytie-audita-c/ "События аудита CPython.") `os.kill` с аргументами `pid`, `sig`.

**Функция [`killpg()`](https://docs-python.ru/standart-library/modul-os-python/funktsija-kill-modulja-os/ "Функция kill() модуля os в Python.")** посылает сигнал `sig` в группу процессов `pgid`. Константы для конкретных сигналов, доступных на хост-платформе, определяются в [модуле `signal`](https://docs-python.ru/standart-library/modul-signal-python/ "Модуль signal в Python, создание обработчиков сигналов.").

Функция `os.killpg()` [событие аудита](https://docs-python.ru/standart-library/modul-sys-python/sobytie-audita-c/ "События аудита CPython.") `os.killpg` с аргументами `pgid`, `sig`.

Windows: сигналы `signal.CTRL_C_EVENT` и `signal.CTRL_BREAK_EVENT` являются специальными сигналами, которые могут отправляться только в консольные процессы, которые совместно используют общее окно консоли, например некоторые подпроцессы. Любое другое значение для `sig` приведет к безоговорочному завершению процесса API-интерфейсом `TerminateProcess`, а для кода выхода будет установлено значение `sig`. Версия [`os.kill()`](https://docs-python.ru/standart-library/modul-os-python/funktsija-kill-modulja-os/ "Функция kill() модуля os в Python.") для Windows дополнительно использует дескрипторы процессов для уничтожения.

Смотрите также [`signal.pthread_kill()`](https://docs-python.ru/standart-library/modul-signal-python/funktsija-pthread-kill-modulja-signal/ "Функция pthread_kill() модуля signal в Python.").

**Примеры использования:**

Родитель может отправлять сигналы дочернему процессу, используя [функцию `os.kill()`](https://docs-python.ru/standart-library/modul-os-python/funktsija-kill-modulja-os/ "Функция kill() модуля os в Python.") используя [модуль `signal`](https://docs-python.ru/standart-library/modul-signal-python/ "Модуль signal в Python, создание обработчиков сигналов."). В этом примере используется короткая пауза, чтобы дать дочернему процессу время для настройки обработчика сигнала. Реальное приложение, не будет нуждаться в вызове [`time.sleep()`](https://docs-python.ru/standart-library/modul-time-python/funktsija-sleep-modulja-time/ "Функция sleep() модуля time в Python."). В дочернем процессе установим обработчик сигнала и сделаем небольшую паузу, чтобы предоставить родительскому процессу достаточно времени для отправки сигнала.
```python
import os
import signal
import time

def signal_usr1(signum, frame):
    "Обратный вызов вызывается при получении сигнала"
    pid = os.getpid()
    print(f'Получен USR1 в процессе {pid}')

print('Forking...')
child_pid = os.fork()
if child_pid:
    print('PARENT: Пауза перед отправкой сигнала ...')
    time.sleep(1)
    print(f'PARENT: передача сигналов {child_pid}')
    os.kill(child_pid, signal.SIGUSR1)
else:
    print('CHILD: Настройка обработчика сигнала')
    signal.signal(signal.SIGUSR1, signal_usr1)
    print('CHILD: Пауза в ожидании сигнала')
    time.sleep(5)

# $ python3 test_kill.py
# Forking...
# PARENT: Пауза перед отправкой сигнала ...
# CHILD: Настройка обработчика сигнала
# CHILD: Пауза в ожидании сигнала
# PARENT: передача сигналов 21168
# Получен USR1 в процессе 21168
```


## spawn()
[Выполнить программу в новом процессе в Python.](https://docs-python.ru/standart-library/modul-os-python/funktsija-spawn-modulja-os/)

Функции `os.spawn*()` запускают программу, расположенную по указанному пути в файловой системе в новом процессе.

**Синтаксис:**
```python
import os

os.spawnl(mode, path, ...)
os.spawnle(mode, path, ..., env)
os.spawnlp(mode, file, ...)
os.spawnlpe(mode, file, ..., env)
os.spawnv(mode, path, args)
os.spawnve(mode, path, args, env)
os.spawnvp(mode, file, args)
os.spawnvpe(mode, file, args, env)
```

**Параметры:**
-   `mode` - [режим запуска](https://docs-python.ru/standart-library/modul-os-python/funktsija-spawn-modulja-os/#mode-run),
-   `path` - [`str`](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-str-tekstovye-stroki/ "Текстовые строки str в Python."), путь в файловой системе запускаемой программы,
-   `file` - [`str`](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-str-tekstovye-stroki/ "Текстовые строки str в Python."), файла запускаемой программы,
-   `args` - [список](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-list-spisok/ "Список list в Python.") аргументов командной строки запускаемой программы,
-   `env` - [`dict`](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-dict-slovar/ "Словарь dict в Python.") - переменная среда для выполнения программы.

**Возвращаемое значение:**
-   [`int`](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-int-tselye-chisla/ "Целые числа int в Python."), идентификатор процесса нового процесса

**Описание:**

Функции [`os.spawn*()`](https://docs-python.ru/standart-library/modul-os-python/funktsija-spawn-modulja-os/ "Функция spawn() модуля os в Python.") запускают программу, расположенную по указанному пути в файловой системе в новом процессе.

**_Обратите внимание_**, что [модуль `subprocess`](https://docs-python.ru/standart-library/modul-subprocess-python/ "Модуль subprocess в Python, запуск новых процессов.") предоставляет более мощные средства для порождения новых процессов и получения их результатов. Использование этого модуля предпочтительнее, чем использование этих функций.

Если режим `mode=P_NOWAIT`, эта функция возвращает идентификатор процесса нового процесса. Если `mode` - P_WAIT, возвращает код завершения процесса, если он завершается нормально или - signal, где signal - это сигнал, который убил процесс. В Windows идентификатор процесса фактически будет дескриптором процесса, поэтому может использоваться с [функцией `os.waitpid()`](https://docs-python.ru/standart-library/modul-os-python/funktsija-waitpid-modulja-os/ "Функция waitpid() модуля os в Python.").

Обратите внимание на `VxWorks`, эта функция не возвращает `signal`, когда новый процесс завершается. Вместо этого возникает [исключение `OSError`](https://docs-python.ru/tutorial/vstroennye-iskljuchenija-interpretator-python/oshibki-operatsionnoj-sistemy-oserror/ "Исключения операционной системы: OSError в Python.").

Варианты `'l'` и `'v'` функций `os.spawn*()` отличаются тем, как передаются аргументы командной строки. С вариантами `'l'` работать легче всего, если число параметров фиксировано при написании кода, отдельные параметры просто становятся дополнительными параметрами для функций `os.spawnl*()`. Варианты `'v'` хороши, когда число параметров является переменным, а аргументы передаются в [списке](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-list-spisok/ "Список list в Python.") или [кортеже](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-tuple-kortezh/ "Кортеж tuple в Python.") в качестве параметра `args`. В любом случае аргументы дочернего процесса должны начинаться с имени запускаемой команды.

Варианты, которые включают `'p'` в конце (`os.spawnlp()`, `os.spawnlpe()`, `os.spawnvp()` и `os.spawnvpe()`), будут использовать переменную среды `PATH` для определения местоположения файла `file` программы. Когда среда выполнения заменяется с использованием одного из вариантов `os.spawn*e()`, описанного в следующем параграфе, новая среда выполнения `env` используется в качестве источника переменной `PATH`. Другие варианты, `os.spawnl()`, `os.spawnle()`, `os.spawnv()` и `os.spawnve()`, не будут использовать переменную `PATH` для поиска исполняемого файла. Путь должен содержать соответствующий абсолютный или относительный путь.

Для `os.spawnle()`, `os.spawnlpe()`, `os.spawnve()` и `os.spawnvpe()`, обратите внимание, что все они заканчиваются на `'e'`, параметр `env` должен быть [словарем](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-dict-slovar/ "Словарь dict в Python."), который используется для определения переменной среды для нового процесса, т. е. `env` будет использоваться вместо среды текущего процесса. Функции `os.spawnl()`, `os.spawnlp()`, `os.spawnv()` и `os.spawnvp()` заставляют новый процесс наследовать среду текущего процесса. Обратите внимание, что ключи и значения в словаре `env` должны быть строками. Неверные ключи или значения приведут к сбою функции с возвращаемым значением 127.

Например, следующие вызовы `os.spawnlp()` и `os.spawnvpe()` эквивалентны:
```python
import os
os.spawnlp(os.P_WAIT, 'cp', 'cp', 'index.html', '/dev/null')

L = ['cp', 'index.html', '/dev/null']
os.spawnvpe(os.P_WAIT, 'cp', L, os.environ)
```

Вызывает событие аудита os.spawn с аргументами mode, path, args, env.

Доступность: Unix, Windows.


**Поддерживаемые режимы запуска:**

**_`os.P_NOWAIT`,  
`os.P_NOWAITO`_:**

Возможные значения параметра `mode` для семейства функций `os.spawn*()`. Если задано любое из этих значений, функции `os.spawn*()` вернутся, как только будет создан новый процесс, с идентификатором процесса в качестве возвращаемого значения.

Доступность: Unix, Windows.

**_`os.P_WAIT`_:**

Возможные значения параметра `mode` для семейства функций `os.spawn*()`. Если это задано как `mode`, функции `os.spawn*()` не будут возвращать значения до тех пор, пока новый процесс не завершится и вернет код завершения процесса, который был выполнен успешно, или `signal`, если сигнал убил процесс.

Доступность: Unix, Windows.

**_`os.P_DETACH`,  
`os.P_OVERLAY`_:**

Возможные значения параметра `mode` для семейства функций `os.spawn*()`. Они менее портативны, чем перечисленные выше. `P_DETACH` похож на `P_NOWAIT`, но новый процесс отсоединяется от консоли вызывающего процесса. Если используется `P_OVERLAY`, текущий процесс будет заменен. Функция `os.spawn*()` ничего не вернет.

Доступность: Windows.


## umask()
[Установить новое значение umask в Python.](https://docs-python.ru/standart-library/modul-os-python/funktsija-umask-modulja-os/)

Функция `umask()` модуля `os` устанавливает текущий `umask` пользователя в числовое значение `mask` и возвращает предыдущий `umask`.

**Синтаксис:**
```python
import os

os.umask(mask)
```

**Параметры:**
-   `mask` - новое значение `umask`.

**Возвращаемое значение:**
-   [int](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-int-tselye-chisla/ "Целые числа int в Python."), предыдущее значение `umask`.

**Описание:**

Функция [`umask()`](https://docs-python.ru/standart-library/modul-os-python/funktsija-umask-modulja-os/ "Функция umask() модуля os в Python.") модуля [`os`](https://docs-python.ru/standart-library/modul-os-python/ "Модуль os в Python, доступ к функциям ОС.") устанавливает текущий `umask` пользователя в числовое значение `mask` и возвращает предыдущий `umask`.

Аргумент `mask` может принимать последние 3 цифры восьмеричного представления числа, например `0o0022`

**Примеры использования:**
```python
>>> import os
>>> os.umask(0o0022)
# 18
>>> oct(18)
#'0o22'
```


## uname()
[Определение текущей операционной системы в Python.](https://docs-python.ru/standart-library/modul-os-python/funktsija-uname-modulja-os/)

Функция os.uname() возвращает информацию, идентифицирующую текущую операционную систему. Возвращаемое значение - это объект с пятью атрибутами

**Синтаксис:**
```python
import os

os.uname()
```
**Параметры:**
-   Нет

**Возвращаемое значение:**
-   [итерируемый](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-iterator-iterator/ "Итератор Iterator, протокол итератора в Python.") объект с пятью атрибутами

**Описание:**

Функция [`os.uname()`](https://docs-python.ru/standart-library/modul-os-python/funktsija-uname-modulja-os/ "Функция uname() модуля os в Python.") возвращает информацию, идентифицирующую текущую операционную систему. Возвращаемое значение - это объект с пятью атрибутами:

-   `sysname` - имя операционной системы,
-   `nodename` - имя машины в сети (определяется реализацией),
-   `release` - релиз операционной системы,
-   `version` - версия операционной системы,
-   `machine` - аппаратный идентификатор.

Для обратной совместимости этот объект также является [итерируемым](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-iterator-iterator/ "Итератор Iterator, протокол итератора в Python."), ведя себя как [кортеж](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-tuple-kortezh/ "Кортеж tuple в Python.") из пяти элементов, содержащий `sysname`, `nodename`, `release`, `version` и `machine` в указанном порядке.

Некоторые системы усекают имя узла `nodename` до 8 символов или до ведущего компонента. Лучший способ получить имя хоста это [`socket.gethostname()`](https://docs-python.ru/standart-library/modul-socket-setevoj-interfejs-python/funktsija-gethostname-modulja-socket/ "Функция gethostname() модуля socket в Python.").

Доступность: последние версии Unix.

**Примеры использования:**
```python
>>> import os
>>> os.uname()[0]
# 'Linux'
>>> os.uname().release
# '5.3.0-42-generic'
>>> os.uname().machine
# 'x86_64'
```


## wait()
[Ждет завершения дочернего процесса в Python.](https://docs-python.ru/standart-library/modul-os-python/funktsija-wait-modulja-os/)

Функция `os.wait()` возвращает идентификатор процесса и код завершения, упакованный в 16-битовое значение. Младший байт представляет номер сигнала, прекратившего выполнение процесса, а старший - код состояния, возвращенный процессом по его завершении.

**Синтаксис:**
```python
import os

os.wait()
```
**Параметры:**
-   Нет.

**Возвращаемое значение:**
-   [кортеж](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-tuple-kortezh/ "Кортеж tuple в Python.").

**Описание:**

Функция [`wait()`](https://docs-python.ru/standart-library/modul-os-python/funktsija-wait-modulja-os/ "Функция wait() модуля os в Python.") модуля [`os`](https://docs-python.ru/standart-library/modul-os-python/ "Модуль os в Python, доступ к функциям ОС.") ждет завершения дочернего процесса и возвращает [кортеж](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-tuple-kortezh/ "Кортеж tuple в Python."), содержащий его `pid` и индикацию состояния выхода: 16-битное число, младший байт которого является номером сигнала, который убил процесс и старший байт которого является состоянием выхода (если номер сигнала равен нулю). Старший бит младшего байта устанавливается, если был создан файл дампа ядра.

Для преобразования состояния выхода в код выхода можно использовать функцию [`os.waitstatus_to_exitcode()`](https://docs-python.ru/standart-library/modul-os-python/funktsija-waitstatus-to-exitcode-modulja-os/ "Функция waitstatus_to_exitcode() модуля os в Python.").

Доступность: Unix.

**Примеры завершения дочернего процесса.**

Когда не имеет значения, какой дочерний процесс может завершиться первым, используйте `os.wait()`. Он возвращается, как только завершается любой дочерний процесс.
```python
# test_wait.py
import os
import sys
import time

for i in range(2):
    print(f'PARENT {os.getpid()}: Forking {i}')
    worker_pid = os.fork()
    if not worker_pid:
        print(f'WORKER {i}: Starting')
        time.sleep(2 + i)
        print(f'WORKER {i}: Finishing')
        sys.exit(i)

for i in range(2):
    print(f'PARENT: Waiting for {i}')
    done = os.wait()
    print(f'PARENT: Child done: {done}')

# $ python3 test_wait.py 
# PARENT 24512: Forking 0
# PARENT 24512: Forking 1
# WORKER 0: Starting
# PARENT: Waiting for 0
# WORKER 1: Starting
# WORKER 0: Finishing
# PARENT: Child done: (24513, 0)
# PARENT: Waiting for 1
# WORKER 1: Finishing
# PARENT: Child done: (24514, 256)
```

Функция `os.wait()` возвращает идентификатор процесса и код завершения, упакованный в 16-битовое значение. Младший байт представляет номер сигнала, прекратившего выполнение процесса, а старший - код состояния, возвращенный процессом по его завершении.


## waitpid()
[Ждет завершения процесса с определенным PID в Python.](https://docs-python.ru/standart-library/modul-os-python/funktsija-waitpid-modulja-os/)

Функция waitpid() модуля os в Unix: ждет завершения дочернего процесса, заданного идентификатором процесса pid, и возвращает кортеж, содержащий его идентификатор процесса и индикацию состояния выхода, закодированную как для os.wait().

**Детали этой функции различаются в Unix и Windows.**

**Синтаксис:**
```python
import os

os.waitpid(pid, options)
```

**Параметры:**
-   `pid` - [`int`](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-int-tselye-chisla/ "Целые числа int в Python."), идентификатор процесса,
-   `options` - [`int`](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-int-tselye-chisla/ "Целые числа int в Python."), опции ожидания.

**Возвращаемое значение:**
-  кортеж

**Описание:**

**Функция [`waitpid()`](https://docs-python.ru/standart-library/modul-os-python/funktsija-waitpid-modulja-os/ "Функция waitpid() модуля os в Python.") модуля [`os`](https://docs-python.ru/standart-library/modul-os-python/ "Модуль os в Python, доступ к функциям ОС.") в Unix**: ждет завершения дочернего процесса, заданного идентификатором процесса `pid`, и возвращает [кортеж](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-tuple-kortezh/ "Кортеж tuple в Python."), содержащий его идентификатор процесса и индикацию состояния выхода, закодированную как для [`os.wait()`](https://docs-python.ru/standart-library/modul-os-python/funktsija-wait-modulja-os/ "Функция wait() модуля os в Python."). На семантику вызова влияет значение [целочисленных](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-int-tselye-chisla/ "Целые числа int в Python.") опций `options`, которое для нормальной работы должно быть `0`.

-   Если `pid` больше `0`, то `os.waitpid()` запрашивает информацию о состоянии для этого конкретного процесса.
-   Если `pid` равен `0`, запрос относится к статусу любого дочернего элемента в группе процессов текущего процесса.
-   Если `pid` равен `-1`, запрос относится к любому дочернему элементу текущего процесса.
-   Если `pid` меньше `-1`, состояние запрашивается для любого процесса в группе процессов `pid` (абсолютное значение `pid`).

[Ошибка `OSError`](https://docs-python.ru/tutorial/vstroennye-iskljuchenija-interpretator-python/oshibki-operatsionnoj-sistemy-oserror/ "Исключения операционной системы: OSError в Python.") вызывается со значением `errno`, когда системный вызов возвращает `-1`.

**Функция [`waitpid()`](https://docs-python.ru/standart-library/modul-os-python/funktsija-waitpid-modulja-os/ "Функция waitpid() модуля os в Python.") модуля [`os`](https://docs-python.ru/standart-library/modul-os-python/ "Модуль os в Python, доступ к функциям ОС.") в Windows**: ждет завершения процесса, заданного дескриптором процесса `pid`. Возвращает [кортеж](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-tuple-kortezh/ "Кортеж tuple в Python."), содержащий `pid`, а его состояние выхода сместится влево на 8 бит (смещение облегчает кросс-платформенное использование функции). `Pid` меньший или равный `0` не имеет особого значения в Windows и вызывает исключение. Значение целочисленных опций не имеет никакого эффекта. `pid` может относиться к любому процессу, чей идентификатор известен, но не обязательно к дочернему процессу. [Функции `os.spawn*()`](https://docs-python.ru/standart-library/modul-os-python/funktsija-spawn-modulja-os/ "Функция spawn() модуля os в Python."), вызываемые с помощью `P_NOWAIT`, возвращают подходящие дескрипторы процесса.

Для преобразования состояния выхода в код выхода можно использовать функцию [`os.waitstatus_to_exitcode()`](https://docs-python.ru/standart-library/modul-os-python/funktsija-waitstatus-to-exitcode-modulja-os/ "Функция waitstatus_to_exitcode() модуля os в Python.").

## Примеры ожидания завершения процесса с определенным PID.

Чтобы дождаться завершения определенного процесса, используйте [функцию `os.waitpid()`](https://docs-python.ru/standart-library/modul-os-python/funktsija-waitpid-modulja-os/ "Функция waitpid() модуля os в Python.").

Функция `os.waitpid()`, которой передан идентификатор целевого процесса, будет блокироваться до тех пор, пока процесс не завершится.
```python
# test_waitpid.py
import os
import sys
import time

workers = []
for i in range(2):
    print(f'PARENT {os.getpid()}: Forking {i}')
    worker_pid = os.fork()
    if not worker_pid:
        print(f'WORKER {i}: Starting')
        time.sleep(2 + i)
        print(f'WORKER {i}: Finishing')
        sys.exit(i)
    workers.append(worker_pid)

for pid in workers:
    print(f'PARENT: Waiting for {pid}')
    done = os.waitpid(pid, 0)
    print(f'PARENT: Child done: {done}')

# $ python3 test_waitpid.py 
# PARENT 25144: Forking 0
# PARENT 25144: Forking 1
# WORKER 0: Starting
# PARENT: Waiting for 25145
# WORKER 1: Starting
# WORKER 0: Finishing
# PARENT: Child done: (25145, 0)
# PARENT: Waiting for 25146
# WORKER 1: Finishing
# PARENT: Child done: (25146, 256)
```


## Определение состояния процесса в Python.
[Определение состояния процесса в Python.](https://docs-python.ru/standart-library/modul-os-python/opredelenie-sostojanija-protsessa/)

Следующие функции принимают в качестве параметра `status` код состояния процесса, возвращаемый `os.system()`, `os.wait()` или `os.waitpid()`. Они могут быть использованы для определения диспозиции процесса.

**_`os.WCOREDUMP(status)`_:**

Функция `os.WCOREDUMP()` вернет `True`, если для процесса был создан дамп ядра, в противном случае вернет `False`.

Доступность: Unix.

 **_`os.WIFCONTINUED(status)`_:**

Функция `os.WIFCONTINUED()` вернет `True`, если процесс был продолжен с остановки управления заданием, в противном случае вернет `False`.

Доступность: Unix.

**_`os.WIFSTOPPED(status)`_:**

Функция `os.WIFSTOPPED()` вернет `True`, если процесс был остановлен, в противном случае вернет `False`.

Доступность: Unix.

**_`os.WIFSIGNALED(status)`_:**

Функция `os.WIFSIGNALED()` вернет `True`, если процесс завершился из-за сигнала, в противном случае вернет `False`.

Доступность: Unix.

**_`os.WIFEXITED(status)`_:**

Функция `os.WIFEXITED()` вернет `True`, если процесс завершился с использованием системного вызова [`exit(2)`](https://manpages.debian.org/exit(2)), в противном случае вернет `False`.

Доступность: Unix.

**_`os.WEXITSTATUS(status)`_:**

Если [`os.WIFEXITED()`](https://docs-python.ru/standart-library/modul-os-python/opredelenie-sostojanija-protsessa/#os.WIFEXITED) равно `True`, то функция `os.WEXITSTATUS()` вернет [целочисленный](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-int-tselye-chisla/ "Целые числа int в Python.") параметр в системный вызов [`exit(2)`](https://manpages.debian.org/exit(2)). В противном случае возвращаемое значение не имеет смысла.

Доступность: Unix.

**_`os.WSTOPSIG(status)`_:**

Функция `os.WSTOPSIG()` вернет сигнал ([int](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-int-tselye-chisla/ "Целые числа int в Python.")), вызвавший остановку процесса.

Доступность: Unix.

**_`os.WTERMSIG(status)`_:**

Функция `os.WTERMSIG()` вернет сигнал ([int](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-int-tselye-chisla/ "Целые числа int в Python.")), из-за которого процесс завершился.

Доступность: Unix.

## Константы для поддержки операций с путями в Python.
[Константы для поддержки операций с путями в Python.](https://docs-python.ru/standart-library/modul-os-python/znachenija-ispolzuemye-podderzhki-operatsij-putjami/)

В этом разделе представлены [константы для поддержки операций с путями](https://docs-python.ru/standart-library/modul-os-python/znachenija-ispolzuemye-podderzhki-operatsij-putjami/ "Константы для поддержки операций с путями.").

Операции более высокого уровня над именами путей определены в [модуле `os.path`](https://docs-python.ru/standart-library/modul-os-path-python/ "Модуль os.path в Python, операции с путями ОС.").

**_`os.curdir`_:**

[Строковая](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-str-tekstovye-stroki/ "Текстовые строки str в Python.") константа, используемая операционной системой для ссылки на текущий каталог. Это `'.'` для Windows и POSIX.

**_`os.pardir`_:**

[Строковая](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-str-tekstovye-stroki/ "Текстовые строки str в Python.") константа, используемая операционной системой для ссылки на родительский каталог. Это `'..'` для Windows и POSIX. Также доступно через модуль `os.path`.

**_`os.sep`_:**

Символ, используемый операционной системой для разделения компонентов имени пути. Это `'/'` для POSIX и `'\\'` для Windows. _Обратите внимание_, что знания этого недостаточно для анализа или объединения имен путей. Для анализа или объединения имен путей используйте `os.path.split()` и `os.path.join()` соответственно.

**_`os.altsep`_:**

Альтернативный символ, используемый операционной системой для разделения компонентов имени пути или `None`, если существует только один символ-разделитель. Устанавливается в `'/'` в системах Windows, где `sep` является обратной косой чертой. Также доступно через модуль `os.path`.

**_`os.extsep`_:**

Символ, который отделяет базовое имя файла от расширения. Например `'.'` в `os.py`. Также доступно через модуль `os.path`.

**_`os.pathsep`_:**

Символ, обычно используемый операционной системой для разделения компонентов пути поиска, как в `PATH`, например `':'` для POSIX или `';'` для Windows. Также доступно через модуль `os.path`.

**_`os.defpath`_:**

Путь поиска по умолчанию, используемый функциями [`os.exec*p*()`](https://docs-python.ru/standart-library/modul-os-python/funktsija-exec-modulja-os/ "Функция exec*() модуля os в Python.") и [`os.spawn*p*()`](https://docs-python.ru/standart-library/modul-os-python/funktsija-spawn-modulja-os/ "Функция spawn() модуля os в Python."), если в среде нет переменной `PATH`. Также доступно через модуль `os.path`.

_`os.linesep`_:

Строка, используемая для разделения или завершения строк на текущей платформе. Это может быть один символ, например `'\n'` для POSIX, или несколько символов, например `'\r\n'` для Windows. Не используйте `os.linesep` в качестве ограничителя строки при записи файлов, открытых в текстовом режиме, вместо этого используйте один `'\n'` на всех платформах.

**_`os.devnull`_:**

Путь к файлу нулевого устройства. Например: `/dev/null` для POSIX, `nul` для Windows. Также доступно через модуль `os.path`.

## Генератор случайных байтов на основе модуля os в Python.
[Генерация случайных байтов средствами OS в Python.](https://docs-python.ru/standart-library/modul-os-python/generator-sluchajnyh-bajtov-osnove-modulja-os/ )

Генерация случайных байтов операционной системой.

**_`os.getrandom(size, flags=0)`_:**

[Функция `os.getrandom()`](https://docs-python.ru/standart-library/modul-os-python/generator-sluchajnyh-bajtov-osnove-modulja-os/#os.getrandom) возвращает случайные [байты](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-bytes-bajtovye-stroki/ "Байтовые строки bytes в Python.") до размера `size`. Функция может вернуть меньше байтов, чем запрошено.

Эти байты могут использоваться для заполнения генераторов случайных чисел в пространстве пользователя или для криптографических целей.

Функция `os.getrandom()` использует энтропию, полученную от драйверов устройств и других источников шума окружающей среды. Чрезмерное чтение больших объемов данных будет иметь негативное влияние на других пользователей устройств `/dev/random` и `/dev/urandom`.

Аргумент `flags` представляет собой битовую маску, которая может содержать ноль или более следующих значений `ORed` вместе: [`os.GRND_RANDOM`](https://docs-python.ru/standart-library/modul-os-python/generator-sluchajnyh-bajtov-osnove-modulja-os/#os.GRND_RANDOM) и [`os.GRND_NONBLOCK`](https://docs-python.ru/standart-library/modul-os-python/generator-sluchajnyh-bajtov-osnove-modulja-os/#os.GRND_NONBLOCK).

Смотрите также страницу руководства Linux по `getrandom()`.

Доступность: Linux 3.17 и новее.

**_`os.urandom(size)`_:**

[Функция `os.urandom()`](https://docs-python.ru/standart-library/modul-os-python/generator-sluchajnyh-bajtov-osnove-modulja-os/#os.urandom) возвращает [строку](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-str-tekstovye-stroki/ "Текстовые строки str в Python.") случайных [байтов](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-bytes-bajtovye-stroki/ "Байтовые строки bytes в Python.") размером `size`, пригодную для криптографического использования.

Эта функция возвращает случайные байты из специфичного для операционной системы источника случайности. Возвращаемые данные должны быть достаточно непредсказуемыми для криптографических приложений, хотя их точное качество зависит от реализации ОС.

В Linux, если доступна системный вызов `getrandom()`, то она используется в режиме блокировки: блокируется до инициализации системного пула энтропии `urandom` (ядро собирает 128 бит энтропии). В Linux [функция `os.getrandom()`](https://docs-python.ru/standart-library/modul-os-python/generator-sluchajnyh-bajtov-osnove-modulja-os/#os.getrandom) может использоваться для получения случайных байтов в неблокирующем режиме, используя флаг [`os.GRND_NONBLOCK`](https://docs-python.ru/standart-library/modul-os-python/generator-sluchajnyh-bajtov-osnove-modulja-os/#os.GRND_NONBLOCK) или для опроса до тех пор, пока не будет инициализирован системный пул энтропии `urandom`.

В Unix-подобной системе случайные байты считываются с устройства `/dev/urandom`. Если устройство `/dev/urandom` недоступно или не читается, возникает [исключение `NotImplementedError`](https://docs-python.ru/tutorial/vstroennye-iskljuchenija-interpretator-python/vstroennye-iskljuchenija/ "Исключения наследуемые от Exception в Python.").

_Изменено в Python 3.11_: в Windows используется `BCryptGenRandom()` вместо устаревшего `CryptGenRandom()`.

Смотрите также:

-   [модуль `secrets`](https://docs-python.ru/standart-library/modul-secrets-python/ "Модуль secrets в Python, генерация паролей и токенов.") предоставляет функции более высокого уровня.
-   Простой в использовании интерфейс генератора случайных чисел, предоставляемый вашей платформой [`random.SystemRandom`](https://docs-python.ru/standart-library/modul-random-python/klassy-predostavljaemye-modulem-random/ "Классы Random() и SystemRandom() модуля random в Python.").

**_`os.GRND_NONBLOCK`_:**

Значение [`os.GRND_NONBLOCK`](https://docs-python.ru/standart-library/modul-os-python/generator-sluchajnyh-bajtov-osnove-modulja-os/#os.GRND_NONBLOCK) стоит по умолчанию при чтении из `/dev/random` блокирует [`os.getrandom()`](https://docs-python.ru/standart-library/modul-os-python/generator-sluchajnyh-bajtov-osnove-modulja-os/#os.getrandom), если нет доступных случайных байтов, а при чтении из `/dev/urandom` блокируется, если пул энтропии еще не был инициализирован.

Если установлен флаг [`os.GRND_RANDOM`](https://docs-python.ru/standart-library/modul-os-python/generator-sluchajnyh-bajtov-osnove-modulja-os/#os.GRND_RANDOM), то [`os.getrandom()`](https://docs-python.ru/standart-library/modul-os-python/generator-sluchajnyh-bajtov-osnove-modulja-os/#os.getrandom) в этих случаях не блокируется, а немедленно вызывает [исключение `BlockingIOError`](https://docs-python.ru/tutorial/vstroennye-iskljuchenija-interpretator-python/oshibki-operatsionnoj-sistemy-oserror/ "Исключения операционной системы: OSError в Python.").

**_`os.GRND_RANDOM`_:**

Если этот бит установлен, то случайные байты извлекаются из пула `/dev/random` вместо пула `/dev/urandom`.

## startfile()
[Запускает файл в Windows с помощью связанного приложения на основе расширения в Python.](https://docs-python.ru/standart-library/modul-os-python/funktsija-startfile-modulja-os/)

Функция startfile() модуля os запускает файл в Windows с помощью связанного с ним приложения на основе расширения.

**Синтаксис:**
```python
import os

os.startfile(path[, operation])
```

**Параметры:**
-   `path` - относительный путь до запускаемого файла,
-   `operation` - задокументированный в Microsoft командный глагол.

**Возвращаемое значение:**
-   нет.

**Описание:**

Функция [`startfile()`](https://docs-python.ru/standart-library/modul-os-python/funktsija-startfile-modulja-os/ "Функция startfile() модуля os в Python.") модуля [`os`](https://docs-python.ru/standart-library/modul-os-python/ "Модуль os в Python, доступ к функциям ОС.") запускает файл с помощью связанного с ним приложения на основе расширения.

Если аргумент `operation` не указан или `'open'`, то это действует как двойной щелчок по файлу в проводнике Windows или указание имени файла в качестве аргумента для команды запуска из интерактивной командной оболочки: файл открывается в любом приложении, а его расширение ассоциировано.

Когда задается другая операция `operation`, то она должна быть "командным глаголом", который указывает, что следует делать с файлом. Общие глаголы, задокументированные Microsoft, - это `'print'` и `'edit'` (для использования в файлах), а также `'explore'` и `'find'` (для использования в каталогах).

Как только запускается связанное приложение, функция `os.startfile()` завершается и нет возможности дождаться закрытия приложения и получить статус выхода приложения.

Аргумент пути `path` указывается относительно текущего каталога. Если вы хотите использовать абсолютный путь, то необходимо убедится, что первый символ не является косой чертой `'/'`, т. к. базовая функция Win32 `ShellExecute()` с ним работать не будет. Чтобы убедиться в правильности пути для Win32 - используйте функцию [`os.path.normpath()`](https://docs-python.ru/standart-library/modul-os-path-python/funktsija-normpath-modulja-os-path/ "Функция normpath() модуля os.path в Python.").

Чтобы уменьшить накладные расходы на запуск интерпретатора, функция Win32 `ShellExecute()` не разрешается до первого вызова функции `os.startfile()`. Если функция не может быть разрешена, то будет вызвано [исключение `NotImplementedError`].

Вызывает [событие аудита](https://docs-python.ru/standart-library/modul-sys-python/sobytie-audita-c/ "События аудита CPython.") `os.startfile` с аргументом `path`, `operation`.

Доступность: Windows.

**Пример открытия файла `.docx` для редактирования в приложении Microsoft Word.**
```python
>>> import os
# файл откроется в приложении Microsoft Word
>>> os.startfile('test.docx', 'edit')

# файл откроется в блокноте, если с расширением 
# `.txt` не ассоциировано другое приложение.
>>> os.startfile('test.txt', 'edit')
```


## times()
[Текущее время глобального процесса в Python.](https://docs-python.ru/standart-library/modul-os-python/funktsija-times-modulja-os/)

Функция times() модуля os возвращает текущее время глобального процесса.

**Синтаксис:**
```python
import os

os.times()
```

**Параметры:**
-   нет.

**Возвращаемое значение:**
-   объект `(user, system, children_user, children_system)`.

**Описание:**

Функция [`times()`](https://docs-python.ru/standart-library/modul-os-python/funktsija-times-modulja-os/ "Функция times() модуля os в Python.") модуля [`os`](https://docs-python.ru/standart-library/modul-os-python/ "Модуль os в Python, доступ к функциям ОС.") возвращает текущее время глобального процесса.

Возвращаемое значение - это объект с пятью атрибутами:

-   `user` - время пользователя,
-   `system` - системное время функции [`os.system()`](https://docs-python.ru/standart-library/modul-os-python/funktsija-system-modulja-os/ "Функция system() модуля os в Python."),
-   `children_user` - пользовательское время всех дочерних процессов,
-   `children_system` - системное время всех дочерних процессов,
-   `elapsed` - истекшее время в реальном времени с фиксированной точки в прошлом.

Для обратной совместимости этот объект ведет себя также, как кортеж из пяти элементов `(user, system, children_user, children_system)`.

Смотрите документацию по Unix [times](https://manpages.debian.org/buster/manpages-dev/times.2.en.html) или [`GetProcessTimes` MSDN](https://docs.microsoft.com/ru-ru/windows/win32/api/processthreadsapi/nf-processthreadsapi-getprocesstimes) в Windows.

В Windows известны только пользователь и система, остальные атрибуты равны нулю.

Доступность: Unix, Windows.

## getloadavg() и cpu_count()
[Определение количества ядер сервера и уровень загрузки системы (load average) в Python.](https://docs-python.ru/standart-library/modul-os-python/funktsii-getloadavg-cpu-count-modulja-os/)

В этом разделе представлены функции определения [количества ядер сервера и уровня загрузки системы](https://docs-python.ru/standart-library/modul-os-python/funktsii-getloadavg-cpu-count-modulja-os/ "Функции getloadavg() и cpu_count() модуля os в Python.") (load average).

**_`os.getloadavg()`_:**

Функция `os.getloadavg()` возвращает среднее количество процессов в системной очереди выполнения за последние 1, 5 и 15 минут или вызывает [исключение `OSError`](https://docs-python.ru/tutorial/vstroennye-iskljuchenija-interpretator-python/oshibki-operatsionnoj-sistemy-oserror/ "Исключения операционной системы: OSError в Python."), если средняя загрузка была не определена.

Другими словами, в Unix системах выводит значение "load average".

Доступность: Unix.

**_`os.cpu_count`_:**

Функция `os.cpu_count()` возвращает количество ядер в системе. Если не определено, то возвращает `None`.

Это число не эквивалентно количеству ядер сервера, которые может использовать текущий процесс. Количество используемых ядер текущим процессом можно получить с помощью выражения [`len(os.sched_getaffinity(0))`](https://docs-python.ru/standart-library/modul-os-python/funktsii-getloadavg-cpu-count-modulja-os/os.sched_getaffinity)

**_`os.sched_getaffinity(pid)`_:**

Функция `os.sched_getaffinity()` возвращает [множество](https://docs-python.ru/tutorial/osnovnye-vstroennye-tipy-python/tip-dannyh-set-frozenset-mnozhestva/ "Множество set и frozenset в Python.") ядер процессора, на которые ограничен процесс с PID `pid` или текущий процесс, если он равен нулю.

**Примеры определения количества процессоров и загрузки системы.**
```python
>>> import os
# определяем load average
>>> loadavg = os.getloadavg()
>>> loadavg
# (0.31, 0.44, 0.36)
>>> loadavg[0]
# 0.31

# определяем количество ядер в системе
>>> os.cpu_count()
# 6

# или
>>> os.sched_getaffinity(0)
# {0, 1, 2, 3, 4, 5}
>>> len(os.sched_getaffinity(0))
# 6
```


## waitstatus_to_exitcode()
[Преобразует статус ожидания процесса в код выхода в Python.](https://docs-python.ru/standart-library/modul-os-python/funktsija-waitstatus-to-exitcode-modulja-os/)

Функция waitstatus_to_exitcode() модуля os преобразует статус ожидания процесса в код выхода.

**Синтаксис:**
```python
import os

# Новое в Python 3.9.
os.waitstatus_to_exitcode(status)
```

**Параметры:**
-   `status` - статус ожидания процесса.

**Возвращаемое значение:**
-   статус выхода процесса или номер сигнала прервавшего процесс.

**Описание:**

Функция [`waitstatus_to_exitcode()`](https://docs-python.ru/standart-library/modul-os-python/funktsija-waitstatus-to-exitcode-modulja-os/ "Функция waitstatus_to_exitcode() модуля os в Python.") модуля [`os`](https://docs-python.ru/standart-library/modul-os-python/ "Модуль os в Python, доступ к функциям ОС.") преобразует статус ожидания процесса в код выхода.

В Unix системах:

-   Если процесс завершился нормально (если [`os.WIFEXITED(status)`](https://docs-python.ru/standart-library/modul-os-python/opredelenie-sostojanija-protsessa/ "Определение состояния процесса.") равен `True`), то возвращает статус выхода процесса `os.WEXITSTATUS(status)`: результат больше или равен 0.
-   Если процесс был завершен сигналом (если [`os.WIFSIGNALED(status)`](https://docs-python.ru/standart-library/modul-os-python/opredelenie-sostojanija-protsessa/ "Определение состояния процесса.") равен `True`), то возвращает - `signum`, где `signum` - номер сигнала, который вызвал завершение процесса `os.WTERMSIG(status)`: результат меньше 0.
-   В противном случае вызывает [исключение `ValueError`](https://docs-python.ru/tutorial/vstroennye-iskljuchenija-interpretator-python/vstroennye-iskljuchenija/ "Исключения наследуемые от Exception в Python.").

В Windows статус возврата сдвинут вправо на 8 бит.

В Unix, если процесс отслеживается или если [`os.waitpid()`](https://docs-python.ru/standart-library/modul-os-python/funktsija-waitpid-modulja-os/ "Функция waitpid() модуля os в Python.") был вызван с опцией `os.WUNTRACED`, вызывающий должен сначала проверить, истинно ли `os.WIFSTOPPED(status)`.

Функцию `os.waitstatus_to_exitcode()` нельзя вызывать, если [`os.WIFSTOPPED(status)`](https://docs-python.ru/standart-library/modul-os-python/opredelenie-sostojanija-protsessa/ "Определение состояния процесса.") имеет значение `True`.
