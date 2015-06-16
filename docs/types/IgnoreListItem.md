## IgnoreListItem
### Описание типа
IgnoreListItem
Запись в игнор-листе.
Таблица 46. Поля записи в игнор листе

### Поля
| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|city|False|string|Город.<br/>|
|name|True|string|Имя посетителя.<br/>|
|site_id|True|numeric|ID сайта.<br/>|
|created_at|True|datetime|Дата и время создания записи.<br/>|
|visitor_id|True|string|ID посетителя.<br/>|
|reason|True|string|Причина добавления в игнор-лист.<br/>|
|chat_id|False|numeric|Чат, в котором выполнена блокировка.<br/>|
|ip|True|string|IP-адрес.<br/>|
|employee|True|Employee|Сотрудник, выполнивший блокировку.<br/>|
