
## IgnoreListItem

### Описание типа
IgnoreListItem<br/>Запись в игнор-листе.<br/>Таблица 46. Поля записи в игнор листе<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|city|False|[string](/docs/types/string.md)|Город.<br/>|
|name|True|[string](/docs/types/string.md)|Имя посетителя.<br/>|
|site_id|True|[numeric](/docs/types/numeric.md)|ID сайта.<br/>|
|created_at|True|[datetime](/docs/types/datetime.md)|Дата и время создания записи.<br/>|
|visitor_id|True|[string](/docs/types/string.md)|ID посетителя.<br/>|
|reason|True|[string](/docs/types/string.md)|Причина добавления в игнор-лист.<br/>|
|chat_id|False|[numeric](/docs/types/numeric.md)|Чат, в котором выполнена блокировка.<br/>|
|ip|True|[string](/docs/types/string.md)|IP-адрес.<br/>|
|employee|True|[Employee](/docs/types/Employee.md)|Сотрудник, выполнивший блокировку.<br/>|
