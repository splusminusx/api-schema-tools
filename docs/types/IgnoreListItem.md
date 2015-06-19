
## IgnoreListItem

### Описание типа
Запись в игнор-листе.<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*city*|False|[string](/types/string)|Город.<br/>|
|*name*|True|[string](/types/string)|Имя посетителя.<br/>|
|*site_id*|True|[numeric](/types/numeric)|ID сайта.<br/>|
|*created_at*|True|[datetime](/types/datetime)|Дата и время создания записи.<br/>|
|*visitor_id*|True|[string](/types/string)|ID посетителя.<br/>|
|*reason*|True|[string](/types/string)|Причина добавления в игнор-лист.<br/>|
|*chat_id*|False|[numeric](/types/numeric)|Чат, в котором выполнена блокировка.<br/>|
|*ip*|True|[string](/types/string)|IP-адрес.<br/>|
|*employee*|True|[Employee](/types/Employee)|Сотрудник, выполнивший блокировку.<br/>|
