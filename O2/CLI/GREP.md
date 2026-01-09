`grep` (сокращение от _global regular expression print_) – эта утилита выполняет поиск определенного текста по файлу или файлам.

Слово «грепать» входит в топ самых популярных терминов, используемых разработчиками. Для разработчиков «грепать» — то же самое, что гуглить для активных пользователей интернета. Как правило, грепают файлы с исходным кодом или логи во время отладки:

```
man grep

SYNOPSIS
       grep [OPTIONS] PATTERN [FILE...]
       grep [OPTIONS] [-e PATTERN]...  [-f FILE]...  [FILE...]
```

- `PATTERN` — это то, что мы хотим найти. Это может быть конкретная строчка или определенный шаблон с регулярными выражениями
- `FILE` — путь до файла, в котором нужно искать

```
# Поиск всех строк в файле .profile, в которых встречается слово PATH
grep PATH .profile

# set PATH so it includes user's private bin if it exists
    PATH="$HOME/bin:$PATH"
# set PATH so it includes user's private bin if it exists
    PATH="$HOME/.local/bin:$PATH"
```

В примере выше утилита `grep` нашла четыре строки. Найденные строчки выводятся на экран в том же порядке, в котором они встречаются в исходном файле.

Количество выводимых соседних строк регулируется тремя опциями:
- Количество отображаемых строк до искомой строки — `-B` или `--before-context`
- Количество отображаемых строк после искомой — `-A` или `--after-context`
- Количество отображаемых строк до и после искомой строки — `-C` или `--context`

```
grep -C 1 PATH .profile


# set PATH so it includes user's private bin if it exists
if [ -d "$HOME/bin" ] ; then
    PATH="$HOME/bin:$PATH"
fi

# set PATH so it includes user's private bin if it exists
if [ -d "$HOME/.local/bin" ] ; then
    PATH="$HOME/.local/bin:$PATH"
fi
```

Иногда мы не знаем, в каком файле находится то, что мы ищем. При этом мы можем знать директорию, в которой лежит этот файл.

В такой ситуации нужно сделать два изменения:
1. Добавить опцию `-r` — она указывает, что надо искать внутри директории. Обратите внимание, что поиск идет рекурсивно, то есть с включением всех поддиректорий.
2. Указать путь до директории, а не файла.

```
grep -r PATH .

./.profile:# set PATH so it includes user's private bin if it exists
./.profile:    PATH="$HOME/bin:$PATH"
./.profile:# set PATH so it includes user's private bin if it exists
./.profile:    PATH="$HOME/.local/bin:$PATH"
```

При таком поиске в выводе указывается файл, в котором была найдена строка. Если добавить опцию `n`, то дополнительно отобразится номер строки:
```
grep -rn PATH .

./.profile:19:# set PATH so it includes user's private bin if it exists
./.profile:21:    PATH="$HOME/bin:$PATH"
./.profile:24:# set PATH so it includes user's private bin if it exists
./.profile:26:    PATH="$HOME/.local/bin:$PATH"
```