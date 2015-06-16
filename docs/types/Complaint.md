## Complaint
### Описание типа
Complaint
Жалоба посетителя.
Таблица 26. Поля жалобы посетителя

### Поля
| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|phone|False|string|Номер телефона.<br/>Одно из полей email или phone должно быть указано.<br/>|
|text|True|string|Текст жалобы.<br/>|
|created_at|True|datetime|Дата создания.<br/>|
|updated_at|True|datetime|Дата последнего обновления.<br/>|
|site|True|Site|Сайт.<br/>|
|conversation|True|Conversation|Обращение, в ходе которого отправлена жалоба.<br/>|
|department|False|Department|Отдел.<br/>|
|id|True|string|ID жалобы.<br/>|
|visitor|True|Visitor|Посетитель.<br/>|
|employee|False|Employee|Сотрудник.<br/><br/>|
|email|False|string|Адрес электронной почты.<br/>Одно из полей email или phone должно быть указано.<br/>|
