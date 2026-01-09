Модуль [`shutil`](https://docs.python.org/3/library/shutil.html#module-shutil "shutil: Высокоуровневые операции с файлами, включая копирование.") предлагает ряд высокоуровневых операций над файлами и коллекциями файлов. В частности, предоставляются функции, поддерживающие копирование и удаление файлов. Для операций над отдельными файлами см. также [`os`](https://docs.python.org/3/library/os.html#module-os "os: Различные интерфейсы операционной системы.").

>===**Предупреждение**===: Даже функции копирования файлов более высокого уровня ([`shutil.copy()`](https://docs.python.org/3/library/shutil.html#shutil.copy "shutil.copy"), [`shutil.copy2()`](https://docs.python.org/3/library/shutil.html#shutil.copy2 "shutil.copy2")) не могут скопировать все метаданные файла.
>
>На платформах POSIX это означает, что владелец файла и группа теряются, также как и ACL. В Mac OS форк ресурсов и другие метаданные не используются. Это означает, что ресурсы будут потеряны, а коды создателя и типа файла будут неверными. В Windows владельцы файлов, ACL и альтернативные потоки данных не копируются.

## Операции с каталогами и файлами


### copyfileobj()
[docs.python.org](https://docs.python.org/3/library/shutil.html#shutil.copyfileobj "Permalink to this definition")

shutil.**copyfileobj**(_fsrc_, _fdst_\[, _length_\])

Копирует содержимое файлоподобного объекта _fsrc_ в файлоподобный объект _fdst_. Целое число _length_, если задано, является размером буфера. В частности, отрицательное значение _length_ подразумевает копирование данных без перебора исходных данных по частям; по умолчанию данные считываются частями, чтобы избежать неконтролируемого потребления памяти. Обратите внимание, что если текущая позиция файла объекта _fsrc_ не равна 0, будет скопировано содержимое только от текущей позиции файла до конца файла.


### copyfile()
[docs.python.org](https://docs.python.org/3/library/shutil.html#shutil.copyfile "Permalink to this definition")

shutil.**copyfile**(_src_, _dst_, _*_, _follow_symlinks=True_)

Копирует содержимое (без метаданных) файла с именем _src_ в файл с именем _dst_ и возвращает _dst_ самым эффективным из возможных способов. _src_ и _dst_ - это объекты типа path или имена путей, заданные в виде строк.

_dst_ должно быть полным именем целевого файла; смотрите [`copy()`](https://docs.python.org/3/library/shutil.html#shutil.copy "shutil.copy") для копии, которая принимает путь к целевому каталогу. Если _src_ и _dst_ указывают один и тот же файл, будет вызвана ошибка [`SameFileError`](https://docs.python.org/3/library/shutil.html#shutil.SameFileError "shutil.SameFileError").

Место назначения должно быть доступно для записи; в противном случае будет вызвано исключение [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError"). Если _dst_ уже существует, он будет заменен. Специальные файлы, такие как символьные или блочные файлы устройств или каналы не могут быть скопированы с помощью этой функции.

Если _follow_symlinks_ является false и _src_ является символической ссылкой, то вместо копирования файла, на который указывает _src_, будет создана новая символьная ссылка.

Вызывает [событие аудита](https://docs.python.org/3/library/sys.html#auditing) `shutil.copyfile` с аргументами `src`, `dst`.

Изменено в версии 3.3: [`IOError`](https://docs.python.org/3/library/exceptions.html#IOError "IOError") раньше вызывался вместо [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError"). Добавлен аргумент _follow_symlinks_. Теперь возвращает _dst_.

Изменено в версии 3.4: Вызывается [`SameFileError`](https://docs.python.org/3/library/shutil.html#shutil.SameFileError "shutil.SameFileError") вместо [`Error`](https://docs.python.org/3/library/shutil.html#shutil.Error "shutil.Error"). Поскольку первый является подклассом второго, это изменение обратно совместимо.

Изменено в версии 3.8: Для более эффективного копирования файла внутри платформы могут использоваться системные вызовы быстрого копирования. См. раздел [Platform-dependent efficient copy operations](https://docs.python.org/3/library/shutil.html#shutil-platform-dependent-efficient-copy-operations).


### exception shutil.SameFileError
[docs.python.org](https://docs.python.org/3/library/shutil.html#shutil.SameFileError "Permalink to this definition")

_exception_ shutil.**SameFileError** 

Это исключение возникает, если источник и пункт назначения в [`copyfile()`](https://docs.python.org/3/library/shutil.html#shutil.copyfile "shutil.copyfile") являются одним и тем же файлом.

Новинка в версии 3.4.

### copymode()
[docs.python.org](https://docs.python.org/3/library/shutil.html#shutil.copymode "Permalink to this definition")

shutil.**copymode**(_src_, _dst_, _*_, _follow_symlinks=True_) 

Копирует биты прав доступа из _src_ в _dst_. Содержимое файла, владелец и группа не затрагиваются. _src_ и _dst_ - это path-подобные объекты или имена путей, заданные в виде строк. Если _follow_symlinks_ является false, и _src_ и _dst_ являются символическими ссылками, [`copymode()`](https://docs.python.org/3/library/shutil.html#shutil.copymode "shutil.copymode") попытается изменить режим самого _dst_ (а не файла, на который он указывает). Эта функциональность доступна не на всех платформах; пожалуйста, смотрите [`copystat()`](https://docs.python.org/3/library/shutil.html#shutil.copystat "shutil.copystat") для получения дополнительной информации. Если [`copymode()`](https://docs.python.org/3/library/shutil.html#shutil.copymode "shutil.copymode") не может модифицировать символические ссылки на локальной платформе, а его об этом просят, он ничего не делает и возвращается.

Вызывает [событие аудита](https://docs.python.org/3/library/sys.html#auditing) `shutil.copymode` с аргументами `src`, `dst`.

Изменения в версии 3.3: Добавлен аргумент _follow_symlinks_.

### copystat()
[docs.python.org](https://docs.python.org/3/library/shutil.html#shutil.copystat "Permalink to this definition")

shutil.**copystat**(_src_, _dst_, _*_, _follow_symlinks=True_)

Копирует биты прав доступа, время последнего доступа, время последней модификации и флаги из _src_ в _dst_. В Linux, [`copystat()`](https://docs.python.org/3/library/shutil.html#shutil.copystat "shutil.copystat") также копирует "расширенные атрибуты", где это возможно. Содержимое файла, владелец и группа не затрагиваются. _src_ и _dst_ - это path-подобные объекты или имена путей, заданные в виде строк.

Если _follow_symlinks_ равно false, и _src_ и _dst_ оба ссылаются на символические ссылки, [`copystat()`](https://docs.python.org/3/library/shutil.html#shutil.copystat "shutil.copystat") будет работать с самими символическими ссылками, а не с файлами, на которые ссылаются символические ссылки - считывая информацию с символической ссылки _src_ и записывая информацию в символическую ссылку _dst_.

>**Примечание:** Не все платформы предоставляют возможность просматривать и изменять символические ссылки. Python сам может сообщить вам, какая функциональность доступна локально.
>
>- Если `os.chmod в os.supports_follow_symlinks` - `True`, [`copystat()`](https://docs.python.org/3/library/shutil.html#shutil.copystat "shutil.copystat") может изменить биты прав доступа символической ссылки.
>    
>- Если `os.utime в os.supports_follow_symlinks` - `True`, [`copystat()`](https://docs.python.org/3/library/shutil.html#shutil.copystat "shutil.copystat") может изменять время последнего доступа и модификации символической ссылки.
>    
>- Если `os.chflags в os.supports_follow_symlinks` - `True`, [`copystat()`](https://docs.python.org/3/library/shutil.html#shutil.copystat "shutil.copystat") может изменять флаги символьной ссылки. (`os.chflags` доступен не на всех платформах).
  >  
>
На платформах, где некоторые или все эти функции недоступны, при запросе модифицировать символическую ссылку, [`copystat()`](https://docs.python.org/3/library/shutil.html#shutil.copystat "shutil.copystat") скопирует все, что сможет. [`copystat()`](https://docs.python.org/3/library/shutil.html#shutil.copystat "shutil.copystat") никогда не возвращает ошибку.
>
Пожалуйста, смотрите [`os.supports_follow_symlinks`](https://docs.python.org/3/library/os.html#os.supports_follow_symlinks "os.supports_follow_symlinks") для получения дополнительной информации.

Вызывает [событие аудита](https://docs.python.org/3/library/sys.html#auditing) `shutil.copystat` с аргументами `src`, `dst`.

Изменения в версии 3.3: Добавлены аргумент _follow_symlinks_ и поддержка расширенных атрибутов Linux.

### copy()
[docs.python.org](https://docs.python.org/3/library/shutil.html#shutil.copy "Permalink to this definition")

shutil.**copy**(_src_, _dst_, _*_, _follow_symlinks=True_)

Копирует файл _src_ в файл или каталог _dst_. _src_ и _dst_ должны быть [path-like objects](https://docs.python.org/3/glossary.html#term-path-like-object) или строками. Если _dst_ указывает на каталог, файл будет скопирован в _dst_ с использованием базового имени файла из _src_. Если в _dst_ указан уже существующий файл, он будет заменен. Возвращает путь к вновь созданному файлу.

Если _follow_symlinks_ - false и _src_ является символической ссылкой, _dst_ будет создан как символическая ссылка. Если _follow_symlinks_ равно true и _src_ является символической ссылкой, _dst_ будет копией файла, на который ссылается _src_.

[`copy()`](https://docs.python.org/3/library/shutil.html#shutil.copy "shutil.copy") копирует данные файла и режим прав доступа к файлу (см. [`os.chmod()`](https://docs.python.org/3/library/os.html#os.chmod "os.chmod")). Другие метаданные, такие как время создания и модификации файла, не сохраняются. Чтобы сохранить все метаданные оригинального файла, используйте [`copy2()`](https://docs.python.org/3/library/shutil.html#shutil.copy2 "shutil.copy2").

Вызывает [событие аудита](https://docs.python.org/3/library/sys.html#auditing) `shutil.copyfile` с аргументами `src`, `dst`.

Вызывает [событие аудита](https://docs.python.org/3/library/sys.html#auditing) `shutil.copymode` с аргументами `src`, `dst`.

Изменения в версии 3.3: Добавлен аргумент _follow_symlinks_. Теперь возвращает путь к вновь созданному файлу.

Изменения в версии 3.8: Для более эффективного копирования файла внутри платформы могут использоваться системные вызовы быстрого копирования. Смотрите раздел [Platform-dependent efficient copy operations](https://docs.python.org/3/library/shutil.html#shutil-platform-dependent-efficient-copy-operations).

### copy2()
[docs.python.org](https://docs.python.org/3/library/shutil.html#shutil.copy2 "Permalink to this definition")

shutil.**copy2**(_src_, _dst_, _*_, _follow_symlinks=True_)

Identical to [`copy()`](https://docs.python.org/3/library/shutil.html#shutil.copy "shutil.copy") except that [`copy2()`](https://docs.python.org/3/library/shutil.html#shutil.copy2 "shutil.copy2") also attempts to preserve file metadata.

Когда _follow_symlinks_ равно false, а _src_ является символической ссылкой, [`copy2()`](https://docs.python.org/3/library/shutil.html#shutil.copy2 "shutil.copy2") пытается скопировать все метаданные с символической ссылки _src_ во вновь созданную символическую ссылку _dst_. Однако эта функциональность доступна не на всех платформах. На платформах, где частично или полностью эта функциональность недоступна, [`copy2()`](https://docs.python.org/3/library/shutil.html#shutil.copy2 "shutil.copy2") сохранит все метаданные, которые сможет; [`copy2()`](https://docs.python.org/3/library/shutil.html#shutil.copy2 "shutil.copy2") никогда не вызывает исключения, потому что не может сохранить метаданные файла.

[`copy2()`](https://docs.python.org/3/library/shutil.html#shutil.copy2 "shutil.copy2") использует [`copystat()`](https://docs.python.org/3/library/shutil.html#shutil.copystat "shutil.copystat") для копирования метаданных файла. Пожалуйста, смотрите [`copystat()`](https://docs.python.org/3/library/shutil.html#shutil.copystat "shutil.copystat") для получения дополнительной информации о поддержке платформ для изменения метаданных символических ссылок.

Вызывает [событие аудита](https://docs.python.org/3/library/sys.html#auditing) `shutil.copyfile` с аргументами `src`, `dst`.

Вызывает [событие аудита](https://docs.python.org/3/library/sys.html#auditing) `shutil.copystat` с аргументами `src`, `dst`.

Изменения в версии 3.3: Добавлены аргументы _follow_symlinks_, попытка копировать в том числе и расширенные атрибуты файловой системы (пока только для Linux). Теперь возвращает путь к вновь созданному файлу.

Изменения в версии 3.8: Для более эффективного копирования файла могут использоваться системные вызовы быстрого копирования, зависящие от платформы. Смотрите раздел [Platform-dependent efficient copy operations](https://docs.python.org/3/library/shutil.html#shutil-platform-dependent-efficient-copy-operations).

### ignore_patterns()
[docs.python.org](https://docs.python.org/3/library/shutil.html#shutil.ignore_patterns "Permalink to this definition")

shutil.**ignore_patterns**(_*patterns_)

Эта стандартная функция создает функцию, которая может использоваться в качестве вызываемой для аргумента _ignore_ [`copytree()`](https://docs.python.org/3/library/shutil.html#shutil.copytree "shutil.copytree"), игнорируя файлы и каталоги, соответствующие одному из предоставленных _шаблонов_ в стиле glob. См. пример ниже.

### copytree()
[docs.python.org](https://docs.python.org/3/library/shutil.html#shutil.copytree "Permalink to this definition")

shutil.**copytree**(_src_, _dst_, _symlinks=False_, _ignore=None_, _copy_function=copy2_, _ignore_dangling_symlinks=False_, _dirs_exist_ok=False_)

Рекуррентно копирует все древо каталогов с корнем _src_ в каталог с именем _dst_ и возвращает конечный каталог. Все промежуточные каталоги, необходимые для размещения _dst_, также будут созданы по умолчанию.

Права доступа и время каталогов копируются с помощью [`copystat()`](https://docs.python.org/3/library/shutil.html#shutil.copystat "shutil.copystat"), отдельные файлы копируются с помощью [`copy2()`](https://docs.python.org/3/library/shutil.html#shutil.copy2 "shutil.copy2").

Если _symlinks_ равно true, символические ссылки в исходном дереве представляются как символические ссылки в новом дереве, и метаданные исходных ссылок будут скопированы, насколько это позволяет платформа; если false или не указано, содержимое и метаданные связанных файлов копируются в новое дерево.

Когда _symlinks_ false, если файл, на который указывает симлинк, не существует, в список ошибок будет добавлено исключение [`Error`](https://docs.python.org/3/library/shutil.html#shutil.Error "shutil.Error") в конце процесса копирования. Вы можете установить необязательный флаг _ignore_dangling_symlinks_ в значение true, если хотите игнорировать это исключение. Обратите внимание, что эта опция не влияет на платформы, которые не поддерживают [`os.symlink()`](https://docs.python.org/3/library/os.html#os.symlink "os.symlink").

Если указано _ignore_, то это должен быть вызываемый элемент, который в качестве аргументов получит каталог, посещаемый [`copytree()`](https://docs.python.org/3/library/shutil.html#shutil.copytree "shutil.copytree"), и список его содержимого, возвращаемый [`os.listdir()`](https://docs.python.org/3/library/os.html#os.listdir "os.listdir"). Поскольку [`copytree()`](https://docs.python.org/3/library/shutil.html#shutil.copytree "shutil.copytree") вызывается рекурсивно, вызываемая переменная _ignore_ будет вызываться один раз для каждого копируемого каталога. Вызываемая программа должна возвращать последовательность имен каталогов и файлов относительно текущего каталога (т.е. подмножество элементов второго аргумента); эти имена будут игнорироваться в процессе копирования. [`ignore_patterns()`](https://docs.python.org/3/library/shutil.html#shutil.ignore_patterns "shutil.ignore_patterns") может быть использован для создания такого вызываемого модуля, который игнорирует имена, основанные на шаблонах в стиле glob.

Если возникает исключение(я), то возникает [`Error`](https://docs.python.org/3/library/shutil.html#shutil.Error "shutil.Error") со списком причин.

Если указана _copy_function_, то это должна быть вызываемая функция, которая будет использоваться для копирования каждого файла. Она будет вызвана с исходным и целевым путями в качестве аргументов. По умолчанию используется [`copy2()`](https://docs.python.org/3/library/shutil.html#shutil.copy2 "shutil.copy2"), но можно использовать любую функцию, поддерживающую ту же сигнатуру (например, [`copy()`](https://docs.python.org/3/library/shutil.html#shutil.copy "shutil.copy")).

Если _dirs_exist_ok_ равно false (по умолчанию) и _dst_ уже существует, то возникает ошибка [`FileExistsError`](https://docs.python.org/3/library/exceptions.html#FileExistsError "FileExistsError"). Если _dirs_exist_ok_ равен true, операция копирования будет продолжена, если она обнаружит существующие каталоги, а файлы в дереве _dst_ будут перезаписаны соответствующими файлами из дерева _src_.

Вызывает событие [audit event](https://docs.python.org/3/library/sys.html#auditing) `shutil.copytree` с аргументами `src`, `dst`.

Изменено в версии 3.3: Копирование метаданных, когда _symlinks_ равно false. Теперь возвращает _dst_.

Изменения в версии 3.2: Добавлен аргумент _copy_function_ для возможности предоставления пользовательской функции копирования. Добавлен аргумент _ignore_dangling_symlinks_, чтобы исключить ошибки "болтающихся" симлинков, когда _symlinks_ равен false.

Изменения в версии 3.8: Для более эффективного копирования файла внутри платформы могут использоваться системные вызовы быстрого копирования. Смотрите раздел [Platform-dependent efficient copy operations](https://docs.python.org/3/library/shutil.html#shutil-platform-dependent-efficient-copy-operations).

Новое в версии 3.8: Параметр _dirs_exist_ok_.

#### copytree. пример использования

Пример, в котором используется помощник [`ignore_patterns()`](https://docs.python.org/3/library/shutil.html#shutil.ignore_patterns "shutil.ignore_patterns"):
```python
from shutil import copytree, ignore_patterns

copytree(source, destination, ignore=ignore_patterns('*.pyc', 'tmp*'))
```

В результате будет скопировано все, кроме файлов `.pyc` и файлов или каталогов, имя которых начинается с `tmp`.

Другой пример, использующий аргумент _ignore_ для добавления вызова логирования:
```python
from shutil import copytree
import logging

def _logpath(path, names):
    logging.info('Working in %s', path)
    return []   # nothing will be ignored

copytree(source, destination, ignore=_logpath)
```

### rmtree()
[docs.python.org](https://docs.python.org/3/library/shutil.html#shutil.rmtree "Permalink to this definition")

shutil.**rmtree**(_path_, _ignore_errors=False_, _onerror=None_, _*_, _dir_fd=None_)

Удаляет все дерево каталогов; _path_ должен указывать на каталог (но не на символическую ссылку на каталог). Если _ignore_errors_ равно true, ошибки, возникающие при неудачном удалении, будут игнорироваться; если false или не указано, такие ошибки обрабатываются вызовом обработчика, указанного в _onerror_, или, если это значение опущено, вызывают исключение.

Эта функция может поддерживать [пути относительно дескрипторов каталогов](https://docs.python.org/3/library/os.html#dir-fd).

>**Примечание:** На платформах, поддерживающих необходимые функции на основе fd, по умолчанию используется версия [`rmtree()`](https://docs.python.org/3/library/shutil.html#shutil.rmtree "shutil.rmtree"), устойчивая к атакам симлинков. На других платформах реализация [`rmtree()`](https://docs.python.org/3/library/shutil.html#shutil.rmtree "shutil.rmtree") восприимчива к атаке симлинков: при соответствующих обстоятельствах и времени злоумышленники могут манипулировать симлинками в файловой системе для удаления файлов, к которым они не смогли бы получить доступ в других случаях. Приложения могут использовать атрибут функции [`rmtree.avoids_symlink_attacks`](https://docs.python.org/3/library/shutil.html#shutil.rmtree.avoids_symlink_attacks "shutil.rmtree.avoids_symlink_attacks"), чтобы определить, какой сценарий применим.

Если указано _onerror_, это должна быть вызываемая функция, принимающая три параметра: _function_, _path_, and _excinfo_.

Первый параметр, _function_, - это функция, которая вызвала исключение; он зависит от платформы и реализации. Вторым параметром, _path_, будет имя пути, переданное _function_. Третий параметр, _excinfo_, будет информацией об исключении, возвращаемой [`sys.exc_info()`](https://docs.python.org/3/library/sys.html#sys.exc_info "sys.exc_info"). Исключения, вызванные _onerror_, не будут перехвачены.

Поднимает событие [аудита](https://docs.python.org/3/library/sys.html#auditing) `shutil.rmtree` с аргументами `path`, `dir_fd`.

Изменено в версии 3.3: Добавлена версия, устойчивая к атакам на симлинки, которая используется автоматически, если платформа поддерживает функции на основе fd.

Изменено в версии 3.8: В Windows больше не будет удалять содержимое перекрестка каталогов перед удалением самого перекрестка.

Изменено в версии 3.11: Параметр _dir_fd_.

#### rmtree.avoids_symlink_attacks
[docs.python.org](https://docs.python.org/3/library/shutil.html#shutil.rmtree.avoids_symlink_attacks "Permalink to this definition")

rmtree.**avoids_symlink_attacks**

Указывает, поддерживает ли текущая платформа и реализация версию [`rmtree()`](https://docs.python.org/3/library/shutil.html#shutil.rmtree "shutil.rmtree"), устойчивую к атакам симлинков. В настоящее время это верно только для платформ, поддерживающих функции доступа к каталогам на основе fd.

#### rmtree. Пример использования

Этот пример показывает, как удалить дерево каталогов в Windows, где для некоторых файлов установлен бит "только для чтения". Он использует обратный вызов onerror, чтобы убрать бит readonly и повторить попытку удаления. Любой последующий сбой будет распространяться.
```python
from shutil import copytree
import logging

def _logpath(path, names):
    logging.info('Working in %s', path)
    return []   # nothing will be ignored

copytree(source, destination, ignore=_logpath)
```

### move()
[docs.python.org](https://docs.python.org/3/library/shutil.html#shutil.move "Permalink to this definition")

shutil.**move**(_src_, _dst_, _copy_function=copy2_)

Рекурсивно перемещает файл или каталог (_src_) в другое расположение (_dst_) и возвращает место назначения.

Если местом назначения является существующий каталог, то _src_ перемещается внутрь этого каталога. Если место назначения уже существует, но не является каталогом, оно может быть перезаписано в зависимости от семантики [`os.rename()`](https://docs.python.org/3/library/os.html#os.rename "os.rename").

Если место назначения находится в текущей файловой системе, то используется [`os.rename()`](https://docs.python.org/3/library/os.html#os.rename "os.rename"). В противном случае _src_ копируется в _dst_ с помощью _copy_function_ и затем удаляется. В случае симлинков, в _dst_ или в качестве _dst_ будет создан новый симлинк, указывающий на цель _src_, а _src_ будет удален.

Если задана _copy_function_, она должна быть вызываемой, принимающей два аргумента _src_ и _dst_, и будет использоваться для копирования _src_ в _dst_, если [`os.rename()`](https://docs.python.org/3/library/os.html#os.rename "os.rename") не может быть использована. Если источником является каталог, вызывается [`copytree()`](https://docs.python.org/3/library/shutil.html#shutil.copytree "shutil.copytree"), передавая ему `copy_function()`. По умолчанию _copy_функцией_ является [`copy2()`](https://docs.python.org/3/library/shutil.html#shutil.copy2 "shutil.copy2"). Использование [`copy()`](https://docs.python.org/3/library/shutil.html#shutil.copy "shutil.copy") в качестве _copy_function_ позволяет успешно выполнить перемещение, когда невозможно также скопировать метаданные, за счет невозможности копирования каких-либо метаданных.

Вызывает [событие аудита](https://docs.python.org/3/library/sys.html#auditing) `shutil.move` с аргументами `src`, `dst`.

Изменения в версии 3.3: Добавлена явная обработка симлинков для других файловых систем, таким образом адаптируя ее к поведению **mv** от GNU. Теперь возвращает _dst_.

Изменено в версии 3.5: Добавлен аргумент ключевого слова _copy_function_.

Изменено в версии 3.8: Для более эффективного копирования файла могут использоваться системные вызовы быстрого копирования, зависящие от платформы. См. раздел [Platform-dependent efficient copy operations](https://docs.python.org/3/library/shutil.html#shutil-platform-dependent-efficient-copy-operations).

Изменено в версии 3.9: Принимает [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object) для _src_ и _dst_.

### disk_usage()
[docs.python.org](https://docs.python.org/3/library/shutil.html#shutil.disk_usage "Permalink to this definition")

shutil.**disk_usage**(_path_)

Возвращает статистику использования диска по заданному пути в виде [именованного кортежа](https://docs.python.org/3/glossary.html#term-named-tuple) с атрибутами _total_, _used_ и _free_, которые представляют собой объем общего, использованного и свободного пространства в байтах. _path_ может быть файлом или каталогом.

Добавлено в версии 3.3.

Изменено в версии 3.8: В Windows _path_ теперь может быть файлом или каталогом.

[Доступно](https://docs.python.org/3/library/intro.html#availability): Unix, Windows.

### chown()
[docs.python.org](https://docs.python.org/3/library/shutil.html#shutil.chown "Permalink to this definition")

shutil.**chown**(_path_, _user=None_, _group=None_)

Изменяет владельца _user_ и/или _group_ данного _path_.

_user_ может быть именем пользователя системы или uid; то же самое относится к _group_. Требуется как минимум один аргумент.

См. также [`os.chown()`](https://docs.python.org/3/library/os.html#os.chown "os.chown"), базовую функцию.

Вызывает [событие аудита](https://docs.python.org/3/library/sys.html#auditing) `shutil.chown` с аргументами `path`, `user`, `group`.

[Доступно](https://docs.python.org/3/library/intro.html#availability): Unix.

Новинка в версии 3.3.

### which()
[docs.python.org](https://docs.python.org/3/library/shutil.html#shutil.which "Permalink to this definition")

shutil.**which**(_cmd_, _mode=os.F_OK | os.X_OK_, _path=None_)

Возвращает путь к исполняемому файлу, который будет запущен при вызове заданного _cmd_. Если _cmd_ не будет вызвано, возвращается `None`.

_mode_ - это маска прав доступа, передаваемая в [`os.access()`](https://docs.python.org/3/library/os.html#os.access "os.access"), по умолчанию определяющая, существует ли файл и является ли он исполняемым.

Если _path_ не указан, используются результаты [`os.environ()`](https://docs.python.org/3/library/os.html#os.environ "os.environ"), возвращающие либо значение "PATH", либо обратное значение [`os.defpath`](https://docs.python.org/3/library/os.html#os.defpath "os.defpath").

В Windows текущий каталог всегда добавляется к _path_, независимо от того, используете ли вы значение по умолчанию или предоставляете свое собственное, что является поведением командной оболочки при обнаружении исполняемых файлов. Кроме того, при обнаружении _cmd_ в _пути_ проверяется переменная окружения `PATHEXT`. Например, если вы вызываете `shutil.which("python")`, [`which()`](https://docs.python.org/3/library/shutil.html#shutil.which "shutil.which") будет проверять `PATHEXT`, чтобы знать, что он должен искать `python.exe` в каталогах _path_. Например, в Windows:
```python
>>> shutil.which("python")
'C:\\Python33\\python.EXE'
```
Новое в версии 3.3.

Изменено в версии 3.8: Теперь допускается использование типа [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes"). Если тип _cmd_ - [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes"), то тип результата также [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes").

### exception shutil.Error
[docs.python.org](https://docs.python.org/3/library/shutil.html#shutil.Error "Permalink to this definition")

_exception_ shutil.**Error**

Это исключение собирает исключения, возникающие во время многофайловой операции. Для [`copytree()`](https://docs.python.org/3/library/shutil.html#shutil.copytree "shutil.copytree") аргумент exception представляет собой список из трех кортежей (_srcname_, _dstname_, _exception_).

### Платформозависимые эффективные операции копирования
[docs.python.org](https://docs.python.org/3/library/shutil.html#platform-dependent-efficient-copy-operations "Permalink to this headline")

Начиная с Python 3.8, все функции, связанные с копированием файлов ([`copyfile()`](https://docs.python.org/3/library/shutil.html#shutil.copyfile "shutil.copyfile"), [`copy()`](https://docs.python.org/3/library/shutil.html#shutil.copy "shutil.copy"), [`copy2()`](https://docs.python.org/3/library/shutil.html#shutil.copy2 "shutil.copy2"), [`copytree()`](https://docs. python.org/3/library/shutil.html#shutil.copytree "shutil.copytree"), и [`move()`](https://docs.python.org/3/library/shutil.html#shutil.move "shutil.move")) могут использовать специфические для платформы вызовы "fast-copy" для более эффективного копирования файла (см. [bpo-33671](https://bugs.python.org/issue?@action=redirect&bpo=33671)). "fast-copy" означает, что операция копирования происходит внутри ядра, избегая использования буферов среды пользователя в Python, как в случае "`outfd.write(infd.read())`".

В macOS [fcopyfile](http://www.manpagez.com/man/3/copyfile/) используется для копирования содержимого файла (не метаданных).

В Linux [`os.sendfile()`](https://docs.python.org/3/library/os.html#os.sendfile "os.sendfile") используется.

В Windows [`shutil.copyfile()`](https://docs.python.org/3/library/shutil.html#shutil.copyfile "shutil.copyfile") использует больший размер буфера по умолчанию (1 MiB вместо 64 KiB) и используется [`memoryview()`](https://docs.python.org/3/library/stdtypes.html#memoryview "memoryview")-базированный вариант [`shutil.copyfileobj()`](https://docs.python.org/3/library/shutil.html#shutil.copyfileobj "shutil.copyfileobj").

Если операция быстрого копирования завершилась неудачно и в файл назначения не было записано никаких данных, то shutil молча вернется к использованию менее эффективной внутренней функции [`copyfileobj()`](https://docs.python.org/3/library/shutil.html#shutil.copyfileobj "shutil.copyfileobj").

Изменено в версии 3.8.

## Операции архивирования
[docs.python.org](https://docs.python.org/3/library/shutil.html#archiving-operations "Permalink to this headline")

Новое в версии 3.2.

Изменения в версии 3.5: Добавлена поддержка формата _xztar_.

Также представлены высокоуровневые утилиты для создания и чтения сжатых и архивных файлов. Они основываются на [`zipfile`](https://docs.python.org/3/library/zipfile.html#module-zipfile "zipfile: Чтение и запись архивных файлов в формате ZIP.") и [`tarfile`](https://docs.python.org/3/library/tarfile.html#module-tarfile "tarfile: Чтение и запись архивных файлов в формате tar.") модулей.

### make_archive()
[docs.python.org](https://docs.python.org/3/library/shutil.html#shutil.make_archive "Permalink to this definition")

shutil.**make_archive**(_base_name_, _format_\[, _root_dir_\[, _base_dir_\[, _verbose_\[, _dry_run_\[, _owner_\[, _group_\[, _logger_\]\]\]\]\]\]\])

Создает файл архива (например, zip или tar) и возвращает его имя.

_base_name_ - имя создаваемого файла, включая путь, за вычетом расширения, специфичного для формата. _format_ - формат архива: один из "zip" (если используется [`zlib`](https://docs.python.org/3/library/zlib.html#module-zlib "zlib: Low-level interface to compression and decompression routines compatible with gzip."), "tar", "gztar" (если доступен модуль [`zlib`](https://docs.python.org/3/library/zlib.html#module-zlib "zlib: Low-level interface to compression and decompression routines compatible with gzip."), "bztar" (если доступен модуль [`bz2`](https://docs.python.org/3/library/bz2.html#module-bz2 "bz2: Interfaces for bzip2 compression and decompression.") или "xztar" (если доступен модуль [`lzma`](https://docs.python.org/3/library/lzma.html#module-lzma "lzma: Обертка Python для библиотеки сжатия liblzma.").

_root_dir_ - это каталог, который будет корневым каталогом архива, все пути в архиве будут относительными к нему; например, мы обычно chdir в _root_dir_ перед созданием архива.

_base_dir_ - это каталог, с которого мы начнем архивирование; т.е. _base_dir_ будет общим префиксом всех файлов и каталогов в архиве. _base_dir_ должен быть указан относительно _root_dir_. Как использовать _base_dir_ и _root_dir_ вместе, смотрите в [Пример архивирования с base_dir](https://docs.python.org/3/library/shutil.html#shutil-archiving-example-with-basedir).

По умолчанию _root_dir_ и _base_dir_ - это текущий каталог.

Если _dry_run_ равен true, архив не создается, но операции, которые были бы выполнены, записываются в _logger_.

_owner_ и _group_ используются при создании tar-архива. По умолчанию используется текущий владелец и группа.

_logger_ должен быть объектом, совместимым с [**PEP 282**](https://peps.python.org/pep-0282/), обычно это экземпляр [`logging.Logger`](https://docs.python.org/3/library/logging.html#logging.Logger "logging.Logger").

Аргумент _verbose_ не используется и является устаревшим.

Вызывает [событие аудита](https://docs.python.org/3/library/sys.html#auditing) `shutil.make_archive` с аргументами `base_name`, `format`, `root_dir`, `base_dir`.

>**Примечание:** Эта функция не является потокобезопасной, если используются пользовательские архиваторы, зарегистрированные с помощью [`register_archive_format()`](https://docs.python.org/3/library/shutil.html#shutil.register_archive_format "shutil.register_archive_format"). В этом случае он временно изменяет текущий рабочий каталог процесса для выполнения архивации.

Изменено в версии 3.8: Современный формат pax (POSIX.1-2001) теперь используется вместо устаревшего формата GNU для архивов, созданных с `format="tar"`.

Изменено в версии 3.10.6: Эта функция стала потокобезопасной при создании стандартных архивов `.zip` и tar.

### get_archive_formats()
[docs.python.org](https://docs.python.org/3/library/shutil.html#shutil.get_archive_formats "Permalink to this definition")

shutil.**get_archive_formats**()

Возвращает список поддерживаемых форматов для архивирования. Каждый элемент возвращаемой последовательности представляет собой кортеж `(имя, описание)`.

По умолчанию [`shutil`](https://docs.python.org/3/library/shutil.html#module-shutil "shutil: Файловые операции высокого уровня, включая копирование.") предоставляет сдедующие форматы:

-   _zip_: ZIP file (if the [`zlib`](https://docs.python.org/3/library/zlib.html#module-zlib "zlib: Low-level interface to compression and decompression routines compatible with gzip.") module is available).
-   _tar_: Uncompressed tar file. Uses POSIX.1-2001 pax format for new archives.
-   _gztar_: gzip’ed tar-file (if the [`zlib`](https://docs.python.org/3/library/zlib.html#module-zlib "zlib: Low-level interface to compression and decompression routines compatible with gzip.") module is available).
-   _bztar_: bzip2’ed tar-file (if the [`bz2`](https://docs.python.org/3/library/bz2.html#module-bz2 "bz2: Interfaces for bzip2 compression and decompression.") module is available).
-   _xztar_: xz’ed tar-file (if the [`lzma`](https://docs.python.org/3/library/lzma.html#module-lzma "lzma: A Python wrapper for the liblzma compression library.") module is available).

Вы можете зарегистрировать новые форматы или предоставить свой собственный архиватор для любых существующих форматов, используя [`register_archive_format()`](https://docs.python.org/3/library/shutil.html#shutil.register_archive_format "shutil.register_archive_format").

### register_archive_format()
[docs.python.org](https://docs.python.org/3/library/shutil.html#shutil.register_archive_format "Permalink to this definition")

shutil.**register_archive_format**(_name_, _function_\[, _extra_args_\[, _description_\]\])

Регистрирует архиватор для формата _name_.

_function_ - это вызываемая функция, которая будет использоваться для распаковки архивов. Вызываемая функция получает _base_name_ файла для создания, затем _base_dir_ (который по умолчанию равен [`os.curdir`](https://docs.python.org/3/library/os.html#os.curdir "os.curdir")) для начала архивирования. Дальнейшие аргументы передаются в виде ключевых слов: _owner_, _group_, _dry_run_ и _logger_ (как передано в [`make_archive()`](https://docs.python.org/3/library/shutil.html#shutil.make_archive "shutil.make_archive")).

Если задано, _extra_args_ - это последовательность пар `(имя, значение)`, которые будут использоваться в качестве дополнительных ключевых аргументов при использовании вызываемого архиватора.

_description_ используется [`get_archive_formats()`](https://docs.python.org/3/library/shutil.html#shutil.get_archive_formats "shutil.get_archive_formats"), которая возвращает список архиваторов. По умолчанию это пустая строка.

### unregister_archive_format()
[docs.python.org](https://docs.python.org/3/library/shutil.html#shutil.unregister_archive_format "Permalink to this definition")

shutil.**unregister_archive_format**(_name_)

Удаляет формат архива _name_ из списка поддерживаемых форматов.

### unpack_archive()
[docs.python.org](https://docs.python.org/3/library/shutil.html#shutil.unpack_archive "Permalink to this definition")

shutil.**unpack_archive**(_filename_\[, _extract_dir_\[, _format_\]\])

Распаковывает архив. _filename_ - полный путь к архиву.

_extract_dir_ - имя целевого каталога, в который распаковывается архив. Если имя не указано, используется текущий рабочий каталог.

_format_ - формат архива: один из "zip", "tar", "gztar", "bztar" или "xztar". Или любой другой формат, зарегистрированный с помощью [`register_unpack_format()`](https://docs.python.org/3/library/shutil.html#shutil.register_unpack_format "shutil.register_unpack_format"). Если не указано, [`unpack_archive()`](https://docs.python.org/3/library/shutil.html#shutil.unpack_archive "shutil.unpack_archive") будет использовать расширение имени файла архива и проверять, не зарегистрирован ли распаковщик для этого расширения. Если таковой не найден, будет вызвана ошибка [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError").

Вызывает [событие аудита](https://docs.python.org/3/library/sys.html#auditing) `shutil.unpack_archive` с аргументами `filename`, `extract_dir`, `format`.

>===**Предупреждение:**=== Никогда не распаковывайте архивы из ненадежных источников без предварительной проверки. Возможно, что файлы создаются вне пути, указанного в аргументе _extract_dir_, например, элементы, имеющие абсолютные имена, начинающиеся с "/", или имена с двумя точками ".".

Изменено в версии 3.7: Принимает [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object) для _filename_ и _extract_dir_.

### register_unpack_format()
[docs.python.org](https://docs.python.org/3/library/shutil.html#shutil.register_unpack_format "Permalink to this definition")

shutil.**register_unpack_format**(_name_, _extensions_, _function_\[, _extra_args_\[, _description_\]\])

Регистрирует формат распаковки. _name_ - имя формата, а _extensions_ - список расширений, соответствующих формату, например `.zip` для Zip-файлов.

_function_ - это вызываемая функция, которая будет использоваться для распаковки архивов. Вызываемая функция получает путь к архиву, затем к директории, в которую архив должен быть извлечен.

Если указано, _extra_args_ - это последовательность кортежей `(name, value)`, которые будут переданы в качестве ключевых аргументов вызываемой функции.

_description_ может быть предоставлена для описания формата, и будет возвращена функцией [`get_unpack_formats()`](https://docs.python.org/3/library/shutil.html#shutil.get_unpack_formats "shutil.get_unpack_formats").

### unregister_unpack_format()
[docs.python.org](https://docs.python.org/3/library/shutil.html#shutil.unregister_unpack_format "Permalink to this definition")

shutil.**unregister_unpack_format**(_name_)

Снимает с регистрации формат распаковки. _name_ - имя формата.

### get_unpack_formats()
[docs.python.org](https://docs.python.org/3/library/shutil.html#shutil.get_unpack_formats "Permalink to this definition")

shutil.**get_unpack_formats**()

Возвращает список всех зарегистрированных форматов для распаковки. Каждый элемент возвращаемой последовательности представляет собой кортеж `(имя, расширения, описание)`.

По умолчанию [`shutil`](https://docs.python.org/3/library/shutil.html#module-shutil "shutil: Файловые операции высокого уровня, включая копирование.") предоставляет следующие форматы:

-   _zip_: ZIP file (unpacking compressed files works only if the corresponding module is available).
-   _tar_: uncompressed tar file.
-   _gztar_: gzip’ed tar-file (if the [`zlib`](https://docs.python.org/3/library/zlib.html#module-zlib "zlib: Low-level interface to compression and decompression routines compatible with gzip.") module is available).
-   _bztar_: bzip2’ed tar-file (if the [`bz2`](https://docs.python.org/3/library/bz2.html#module-bz2 "bz2: Interfaces for bzip2 compression and decompression.") module is available).
-   _xztar_: xz’ed tar-file (if the [`lzma`](https://docs.python.org/3/library/lzma.html#module-lzma "lzma: A Python wrapper for the liblzma compression library.") module is available).

Вы можете зарегистрировать новые форматы или предоставить свой собственный распаковщик для любых существующих форматов, используя [`register_unpack_format()`](https://docs.python.org/3/library/shutil.html#shutil.register_unpack_format "shutil.register_unpack_format").

### Пример архивирования

В этом примере мы создадим gzip tar-архив, содержащий все файлы, найденные в директории `.ssh` пользователя:
```python
from shutil import make_archive
>>> import os
>>> archive_name = os.path.expanduser(os.path.join('~', 'myarchive'))
>>> root_dir = os.path.expanduser(os.path.join('~', '.ssh'))
>>> make_archive(archive_name, 'gztar', root_dir)
'/Users/tarek/myarchive.tar.gz'
```
Полученный в результате архив содержит:
```shell
$ tar -tzvf /Users/tarek/myarchive.tar.gz
drwx------ tarek/staff       0 2010-02-01 16:23:40 ./
-rw-r--r-- tarek/staff     609 2008-06-09 13:26:54 ./authorized_keys
-rwxr-xr-x tarek/staff      65 2008-06-09 13:26:54 ./config
-rwx------ tarek/staff     668 2008-06-09 13:26:54 ./id_dsa
-rwxr-xr-x tarek/staff     609 2008-06-09 13:26:54 ./id_dsa.pub
-rw------- tarek/staff    1675 2008-06-09 13:26:54 ./id_rsa
-rw-r--r-- tarek/staff     397 2008-06-09 13:26:54 ./id_rsa.pub
-rw-r--r-- tarek/staff   37192 2010-02-06 18:23:10 ./known_hosts
```

### Пример архивирования с использованием _base_dir_

В этом примере, похожем на пример выше, мы покажем, как использовать [`make_archive()`](https://docs.python.org/3/library/shutil.html#shutil.make_archive "shutil.make_archive"), но на этот раз с использованием _base_dir_. Теперь у нас есть следующая структура каталогов:
```shell
$ tree tmp
tmp
└── root
    └── structure
        ├── content
            └── please_add.txt
        └── do_not_add.txt
```

В финальный архив должен быть включен `please_add.txt`, но `do_not_add.txt` не должен. Поэтому мы используем следующее:
```python
from shutil import make_archive
>>> import os
>>> archive_name = os.path.expanduser(os.path.join('~', 'myarchive'))
>>> make_archive(
...     archive_name,
...     'tar',
...     root_dir='tmp/root',
...     base_dir='structure/content',
... )
'/Users/tarek/my_archive.tar'
```

Перечисление файлов в полученном архиве дает нам:
```shell
$ python -m tarfile -l /Users/tarek/myarchive.tar
structure/content/
structure/content/please_add.txt
```

## Запрос размера выходного терминала
[docs.python.org](https://docs.python.org/3/library/shutil.html#querying-the-size-of-the-output-terminal "Permalink to this headline")

### get_terminal_size()
[docs.python.org](https://docs.python.org/3/library/shutil.html#shutil.get_terminal_size "Permalink to this definition")

shutil.**get_terminal_size**(_fallback=(columns, lines)_)

Получение размера окна терминала.

Для каждого из двух размеров проверяется переменная окружения, `COLUMNS` и `LINES` соответственно. Если переменная определена и ее значение является положительным целым числом, то она используется.

Если `COLUMNS` или `LINES` не определены, что является обычным случаем, терминал, подключенный к [`sys.__stdout__`](https://docs.python.org/3/library/sys.html#sys.__stdout__ "sys.__stdout__"), запрашивается вызовом [`os.get_terminal_size()`](https://docs.python.org/3/library/os.html#os.get_terminal_size "os.get_terminal_size").

Если размер терминала не может быть успешно запрошен, либо потому что система не поддерживает запрос, либо потому что мы не подключены к терминалу, используется значение, указанное в параметре `fallback`. По умолчанию `fallback` имеет значение `(80, 24)`, которое является размером по умолчанию, используемым многими эмуляторами терминалов.

Возвращаемое значение представляет собой именованный кортеж типа [`os.terminal_size`](https://docs.python.org/3/library/os.html#os.terminal_size "os.terminal_size").

См. также: Единая спецификация UNIX, версия 2, [Другие переменные окружения](https://pubs.opengroup.org/onlinepubs/7908799/xbd/envvar.html#tag_002_003).

Новое в версии 3.3.

Изменено в версии 3.11: Значения `fallback` также используются, если [`os.get_terminal_size()`](https://docs.python.org/3/library/os.html#os.get_terminal_size "os.get_terminal_size") возвращает нули.