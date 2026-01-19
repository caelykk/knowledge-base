**Назначение:**.
Модуль shelve реализует постоянное хранилище для произвольных объектов Python, которые могут быть выбраны, используя API, подобный словарю.

Модуль `shelve` можно использовать как простой вариант постоянного хранилища для объектов Python, когда не требуется реляционная база данных. Доступ к shelf осуществляется по ключам, как и в словаре. Значения собираются и записываются в базу данных, созданную и управляемую [`dbm`](https://pymotw.com/3/dbm/index.html#module-dbm "dbm: Unix Key-Value Databases").

## Создание нового Shelf

Самый простой способ использования `shelve` - это класс `DbfilenameShelf`. Он использует [`dbm`](https://pymotw.com/3/dbm/index.html#module-dbm "dbm: Unix Key-Value Databases") для хранения данных. Класс можно использовать напрямую или вызвав `shelve.open()`.
```python
# shelve_create.py
import shelve

with shelve.open('test_shelf.db') as s:
    s['key1'] = {
        'int': 10,
        'float': 9.5,
        'string': 'Sample data',
    }
```

Чтобы снова получить доступ к данным, откройте shelf и используйте его как словарь.
```python
# shelve_existing.py
import shelve

with shelve.open('test_shelf.db') as s:
    existing = s['key1']

print(existing)
```

Запуск обоих примеров скриптов дает следующий результат.
```shell
$ python3 shelve_create.py
$ python3 shelve_existing.py

{'int': 10, 'float': 9.5, 'string': 'Sample data'}
```

Модуль [`dbm`](https://pymotw.com/3/dbm/index.html#module-dbm "dbm: Модуль Unix Key-Value Databases") не поддерживает одновременную запись нескольких приложений в одну и ту же базу данных, но поддерживает одновременную работу с клиентами только для чтения. Если клиент не будет изменять shelf, укажите `shelve` открыть базу данных только для чтения, передав `flag='r'`.
```python
# shelve_readonly.py
import dbm
import shelve

with shelve.open('test_shelf.db', flag='r') as s:
    print('Existing:', s['key1'])
    try:
        s['key1'] = 'new value'
    except dbm.error as err:
        print('ERROR: {}'.format(err))
```

Если программа пытается изменить базу данных, когда она открыта только для чтения, генерируется исключение об ошибке доступа. Тип исключения зависит от модуля базы данных, выбранного [`dbm`](https://pymotw.com/3/dbm/index.html#module-dbm "dbm: Unix Key-Value Databases") при создании базы данных.
```shell
$ python3 shelve_readonly.py

Existing: {'int': 10, 'float': 9.5, 'string': 'Sample data'}
ERROR: cannot add item to database
```

## Write-back

По умолчанию хранилища не отслеживают изменения изменчивых объектов. Это означает, что если содержимое элемента, хранящегося в shelf, изменяется, то shelf должен быть обновлен явным образом путем повторного сохранения всего элемента.
```python
# shelve_withoutwriteback.py
import shelve

with shelve.open('test_shelf.db') as s:
    print(s['key1'])
    s['key1']['new_value'] = 'this was not here before'

with shelve.open('test_shelf.db', writeback=True) as s:
    print(s['key1'])
```
IВ этом примере словарь по адресу `'key1'` повторно не сохраняется, поэтому при повторном открытии полки изменения не будут учтены.
```shell
$ python3 shelve_create.py
$ python3 shelve_withoutwriteback.py

{'int': 10, 'float': 9.5, 'string': 'Sample data'}
{'int': 10, 'float': 9.5, 'string': 'Sample data'}
```

Чтобы автоматически отслеживать изменения в изменчивых объектах, хранящихся в shelf, откройте его, установив флаг `writeback`. Флаг `writeback` заставляет shelf запоминать все объекты, извлеченные из базы данных, используя кэш в памяти. Каждый объект кэша также записывается обратно в базу данных при закрытии shelf.
```python
# shelve_writeback.py
import shelve
import pprint

with shelve.open('test_shelf.db', writeback=True) as s:
    print('Initial data:')
    pprint.pprint(s['key1'])

    s['key1']['new_value'] = 'this was not here before'
    print('\nModified:')
    pprint.pprint(s['key1'])

with shelve.open('test_shelf.db', writeback=True) as s:
    print('\nPreserved:')
    pprint.pprint(s['key1'])
```

Хотя это снижает вероятность ошибки программиста и может сделать сохранение объектов более прозрачным, использование режима записи может быть нежелательным в любой ситуации. Кэш потребляет дополнительную память пока shelf открыт, а пауза для записи каждого кэшированного объекта обратно в базу данных при закрытии замедляет работу приложения. Все кэшированные объекты записываются обратно в базу данных, потому что нет способа определить, были ли они изменены. Если приложение читает данных больше, чем записывает, запись обратно будет оказывать излишнее влияние на производительность.
```shell
$ python3 shelve_create.py
$ python3 shelve_writeback.py

Initial data:
{'float': 9.5, 'int': 10, 'string': 'Sample data'}

Modified:
{'float': 9.5,
 'int': 10,
 'new_value': 'this was not here before',
 'string': 'Sample data'}

Preserved:
{'float': 9.5,
 'int': 10,
 'new_value': 'this was not here before',
 'string': 'Sample data'}
```

## Специфические типы shelf

Все предыдущие примеры использовали реализацию shelf по умолчанию. Использование `shelve.open()` вместо одной из реализаций shelf напрямую - это обычная схема использования, особенно если не важно, какой тип базы данных используется для хранения данных. Однако бывают случаи, когда формат базы данных важен. В таких ситуациях используйте `DbfilenameShelf` или `BsdDbShelf` напрямую, или даже подкласс `Shelf` для реализации собственного решения.

**Смотрите также**

- [Документация стандартной библиотеки для shelve](https://docs.python.org/3.7/library/shelve.html)
- [`dbm`](https://pymotw.com/3/dbm/index.html#module-dbm "dbm: Unix Key-Value Databases") - Модуль `dbm` находит доступную библиотеку DBM для создания новой базы данных.
- [feedcache](https://bitbucket.org/dhellmann/feedcache) - Модуль `feedcache` использует `shelve` как вариант хранения по умолчанию.
- [shove](http://pypi.python.org/pypi/shove/) - Shove реализует аналогичный API с большим количеством форматов back-end.