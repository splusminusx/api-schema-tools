
## ConsoleNews

### Описание типа
ConsoleNews<br/>Новости для Пульта оператора.<br/>Таблица 27. Поля новости для Пульта оператора<br/><br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*content*|True|[string](/docs/types/string.md)|Текст.<br/>|
|*title*|True|[string](/docs/types/string.md)|Заголовок.<br/>|
|*image*|True|[file](/docs/types/file.md)|Картинка.<br/>|
|*annotation*|True|[string](/docs/types/string.md)|Анонс.<br/>|
|*is_read*|True|[boolean](/docs/types/boolean.md)|Признак прочитанной новости.<br/>|
|*position*|True|[numeric](/docs/types/numeric.md)|Порядковый номер в списке.<br/>|
|*created_at*|True|[datetime](/docs/types/datetime.md)|Дата и время создания.<br/>|
|*id*|True|[numeric](/docs/types/numeric.md)|ID новости.<br/>|
