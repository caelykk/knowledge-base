[Оф. документация (eng)](https://docs.python.org/3/library/shelve.html)

"shelf" - это постоянный объект, похожий на словарь. Разница с базами данных "dbm" заключается в том, что значениями (не ключами!) в полке могут быть по сути произвольные объекты Python - все, что может обработать модуль [`pickle`](https://docs.python.org/3/library/pickle.html#module-pickle "pickle: Преобразование объектов Python в потоки байтов и обратно."). Это включает в себя большинство экземпляров классов, рекурсивные типы данных и объекты, содержащие множество общих подобъектов. Ключи - это обычные строки.

## open()
[docs.python.org](https://docs.python.org/3/library/shelve.html#shelve.open "Permalink to this definition")

`shelve.`**`open`**`(`_`filename`_`,` _`flag='c'`_, _`protocol=None`_, _`writeback=False`_)

Открывает постоянный словарь. Указанное имя файла является базовым именем файла для основной базы данных. В качестве побочного эффекта к имени файла может быть добавлено расширение, и может быть создано более одного файла. По умолчанию файл базовой базы данных открыт для чтения и записи. Необязательный параметр _flag_ имеет ту же интерпретацию, что и параметр _flag_ в [`dbm.open()`](https://docs.python.org/3/library/dbm.html#dbm.open "dbm.open").

По умолчанию для сериализации значений используются pickle, созданные с помощью [`pickle.DEFAULT_PROTOCOL`](https://docs.python.org/3/library/pickle.html#pickle.DEFAULT_PROTOCOL "pickle.DEFAULT_PROTOCOL"). Версия протокола pickle может быть указана с помощью параметра _protocol_.

Из-за семантики Python, shelf не может знать, когда изменяемый элемент постоянного словаря будет изменен. По умолчанию измененные объекты записываются _только_ при назначении на shelf (см. [Пример](https://docs.python.org/3/library/shelve.html#shelve-example)). Если необязательный параметр _writeback_ установлен в `True`, все записи, к которым осуществляется доступ, также кэшируются в памяти и записываются обратно при [`sync()`](https://docs.python.org/3/library/shelve.html#shelve.Shelf.sync "shelve.Shelf.sync") и [`close()`](https://docs.python.org/3/library/shelve.html#shelve.Shelf.close "shelve.Shelf. close"); это может облегчить изменение изменяемых записей в постоянном словаре, но при большом количестве обращений к записям может потребоваться огромное количество памяти для кэша, а операция закрытия может быть очень медленной, так как все обращенные записи записываются обратно (нет способа определить, какие из обращенных записей являются изменяемыми, и какие из них были действительно изменены).

Изменено в версии 3.10: [`pickle.DEFAULT_PROTOCOL`](https://docs.python.org/3/library/pickle.html#pickle.DEFAULT_PROTOCOL "pickle.DEFAULT_PROTOCOL") теперь используется в качестве протокола pickle по умолчанию.

Изменено в версии 3.11: Принимает [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object) для имени файла.

>**Примечание:** Не полагайтесь на то, что shelf будет закрыта автоматически; всегда вызывайте [`close()`](https://docs.python.org/3/library/shelve.html#shelve.Shelf.close "shelve.Shelf.close") явно, когда она вам больше не нужна, или используйте [`helve.open()`](https://docs.python.org/3/library/shelve.html#shelve.open "shelve.open") в качестве менеджера контекста:
```python
with shelve.open('spam') as db:
    db['eggs'] = 'eggs'
```

>==**Предупреждение:**== Поскольку модуль [`shelve`](https://docs.python.org/3/library/shelve.html#module-shelve "shelve: Python object persistence.") основан на модуле [`pickle`](https://docs.python.org/3/library/pickle.html#module-pickle "pickle: Преобразование объектов Python в потоки байтов и обратно."), загрузка shelf из ненадежного источника небезопасна. Как и в случае с pickle, загрузка shelf может привести к выполнению произвольного кода.

Объекты Shelf поддерживают большинство методов и операций, поддерживаемых словарями (кроме копирования, конструкторов и операторов `|` и `|=`). Это облегчает переход от сценариев, основанных на словарях, к сценариям, требующим постоянного хранения.

Поддерживаются два дополнительных метода:

## sync()
[docs.python.org](https://docs.python.org/3/library/shelve.html#shelve.Shelf.sync "Permalink to this definition")

`Shelf.`**`sync`**`()`

Записывает все записи в кэш, если shelf была открыта с _writeback_, установленным на [`True`](https://docs.python.org/3/library/constants.html#True). Также очищает кэш и синхронизирует постоянный словарь на диске, если это возможно. Это вызывается автоматически, когда shelf закрывается с помощью [`close()`](https://docs.python.org/3/library/shelve.html#shelve.Shelf.close "shelve.Shelf.close").

## close()
[docs.python.org](https://docs.python.org/3/library/shelve.html#shelve.Shelf.close "Permalink to this definition")

`Shelf.`**`close`**`()`
Синхронизирует и закрывает постоянный объект _dict_. Операции над закрытой shelf завершатся с ошибкой [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError").

>**См. также:** [Persistent dictionary recipe](https://code.activestate.com/recipes/576642/) с широко поддерживаемыми форматами хранения и обладающий скоростью нативных словарей.

## Ограничения

- Выбор того, какой пакет базы данных будет использоваться (например, [`dbm.ndbm`](https://docs.python.org/3/library/dbm.html#module-dbm.ndbm "dbm.ndbm: Стандартный интерфейс "базы данных", основанный на ndbm. (Unix)") или [`dbm.gnu`](https://docs.python.org/3/library/dbm.html#module-dbm.gnu "dbm.gnu: Переинтерпретация dbm в GNU. (Unix)")) зависит от того, какой интерфейс доступен. Поэтому небезопасно открывать базу данных напрямую, используя [`dbm`](https://docs.python.org/3/library/dbm.html#module-dbm "dbm: Интерфейсы для различных форматов "баз данных" Unix."). База данных также (к сожалению) подвержена ограничениям [`dbm`](https://docs.python.org/3/library/dbm.html#module-dbm "dbm: Interfaces to various Unix "database" formats."), если она используется - это означает, что (pickle представление) объектов, хранящихся в базе данных, должно быть довольно маленьким, и в редких случаях коллизии ключей могут привести к тому, что база данных откажется обновляться.
    
- [`shelve`](https://docs.python.org/3/library/shelve.html#module-shelve "shelve: Python object persistence.") модуль не поддерживает _последовательный_ доступ на чтение/запись к хранящимся на shelf объектам. (Несколько одновременных доступов на чтение безопасны.) Когда программа имеет открытую для записи shelf, никакая другая программа не должна иметь ее открытой для чтения или записи. Для решения этой проблемы можно использовать блокировку файлов Unix, но она отличается в разных версиях Unix и требует знаний об используемой реализации базы данных.

## Shelf()
[docs.python.org](https://docs.python.org/3/library/shelve.html#shelve.Shelf "Permalink to this definition")

_`class`_ `shelve.`**`Shelf`**`(`_`dict`_, _`protocol=None`_`,` _`writeback=False`_, _`keyencoding='utf-8'`_`)`

Подкласс [`collections.abc.MutableMapping`](https://docs.python.org/3/library/collections.abc.html#collections.abc.MutableMapping "collections.abc.MutableMapping"), который хранит сериализованные значения в объекте _dict_.

По умолчанию для сериализации значений используются pickle, созданные с помощью [`pickle.DEFAULT_PROTOCOL`](https://docs.python.org/3/library/pickle.html#pickle.DEFAULT_PROTOCOL "pickle.DEFAULT_PROTOCOL"). Версия протокола pickle может быть указана с помощью параметра _protocol_. См. раздел [`pickle`](https://docs.python.org/3/library/pickle.html#module-pickle "pickle: Преобразование объектов Python в потоки байтов и обратно.") 

Если параметр _writeback_ имеет значение `True`, объект будет хранить кэш всех записей, к которым обращался, и записывать их обратно в _dict_ в моменты синхронизации и закрытия. Это позволяет выполнять обычные операции над изменяемыми записями, но может потреблять гораздо больше памяти и заставлять синхронизацию и закрытие занимать много времени.

Параметр _keyencoding_ - это кодировка, используемая для кодирования ключей перед их использованием с базовым словарем.

Объект [`Shelf`](https://docs.python.org/3/library/shelve.html#shelve.Shelf "shelve.Shelf") также может использоваться в качестве менеджера контекста, в этом случае он будет автоматически закрыт после завершения блока [`with`](https://docs.python.org/3/reference/compound_stmts.html#with).

Изменено в версии 3.2: Добавлен параметр _keyencoding_; ранее ключи всегда кодировались в UTF-8.

Изменено в версии 3.4: Добавлена поддержка контекстного менеджера.

Изменено в версии 3.10: [`pickle.DEFAULT_PROTOCOL`](https://docs.python.org/3/library/pickle.html#pickle.DEFAULT_PROTOCOL "pickle.DEFAULT_PROTOCOL") теперь используется в качестве протокола pickle по умолчанию.

## BsdDbShelf()
[docs.python.org](https://docs.python.org/3/library/shelve.html#shelve.BsdDbShelf "Permalink to this definition")

_`class`_ `shelve.`**`BsdDbShelf`**`(`_`dict`_`,` _`protocol=None`_, _`writeback=False`_`,` _`keyencoding='utf-8'`_`)`

Подкласс [`Shelf`](https://docs.python.org/3/library/shelve.html#shelve.Shelf "shelve.Shelf"), который раскрывает `first()`, `next()`, `previous()`, `last()` и `set_location()`, которые доступны в стороннем модуле `bsddb` из [pybsddb](https://www.jcea.es/programacion/pybsddb.htm), но не в других модулях баз данных. Объект _dict_, передаваемый в конструктор, должен поддерживать эти методы. Обычно это достигается вызовом одного из `bsddb.hashopen()`, `bsddb.btopen()` или `bsddb.rnopen()`. Необязательные параметры _protocol_, _writeback_ и _keyencoding_ имеют ту же интерпретацию, что и для класса [`Shelf`](https://docs.python.org/3/library/shelve.html#shelve.Shelf "shelve.Shelf").

## DbfilenameShelf()
[docs.python.org](https://docs.python.org/3/library/shelve.html#shelve.DbfilenameShelf "Permalink to this definition")

_`class`_ `shelve.`**`DbfilenameShelf`**`(`_`filename`_`,` _`flag='c'`_`,` _`protocol=None`_`,` _`writeback=False`_`)`

Подкласс [`Shelf`](https://docs.python.org/3/library/shelve.html#shelve.Shelf "shelve.Shelf"), который принимает _имя файла_ вместо dict-подобного объекта. Базовый файл будет открыт с помощью [`dbm.open()`](https://docs.python.org/3/library/dbm.html#dbm.open "dbm.open"). По умолчанию файл будет создан и открыт как для чтения, так и для записи. Необязательный параметр _flag_ имеет ту же интерпретацию, что и для функции [`open()`](https://docs.python.org/3/library/shelve.html#shelve.open "shelve.open"). Необязательные параметры _protocol_ и _writeback_ имеют ту же интерпретацию, что и для класса [`Shelf`](https://docs.python.org/3/library/shelve.html#shelve.Shelf "shelve.Shelf").

## Пример использования

Обобщим интерфейс (`ключ` - строка, `данные` - произвольный объект):
```python
import shelve

d = shelve.open(filename)  # open -- file may get suffix added by low-level
                           # library

d[key] = data              # store data at key (overwrites old data if
                           # using an existing key)
data = d[key]              # retrieve a COPY of data at key (raise KeyError
                           # if no such key)
del d[key]                 # delete data stored at key (raises KeyError
                           # if no such key)

flag = key in d            # true if the key exists
klist = list(d.keys())     # a list of all existing keys (slow!)

# as d was opened WITHOUT writeback=True, beware:
d['xx'] = [0, 1, 2]        # this works as expected, but...
d['xx'].append(3)          # *this doesn't!* -- d['xx'] is STILL [0, 1, 2]!

# having opened d without writeback=True, you need to code carefully:
temp = d['xx']             # extracts the copy
temp.append(5)             # mutates the copy
d['xx'] = temp             # stores the copy right back, to persist it

# or, d=shelve.open(filename,writeback=True) would let you just code
# d['xx'].append(5) and have it work as expected, BUT it would also
# consume more memory and make the d.close() operation slower.

d.close()                  # close it
```
>**Смотрите также**:
>
**Модуль** [`dbm`](https://docs.python.org/3/library/dbm.html#module-dbm "dbm: Интерфейсы для различных форматов "баз данных" Unix.")
Общий интерфейс для баз данных в стиле `dbm`.
>
**Модуль** [`pickle`](https://docs.python.org/3/library/pickle.html#module-pickle "pickle: Преобразование объектов Python в потоки байтов и обратно.")
Сериализация объектов, используемая [`shelve`](https://docs.python.org/3/library/shelve.html#module-shelve "shelve: Python object persistence.").