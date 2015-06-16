## Visitor
### Описание типа
Visitor
Посетитель.
Таблица 87. Поля посетителя

### Поля
| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|comment|False|string|Комментарий сотрудника.<br/>|
|visitor_variables|False|Object|Объект с текущими переменными посетителя.<br/>|
|last_visit_at|True|datetime|Дата последнего посещения.<br/>|
|last_ip|True|string|IP-адрес посетителя при последнем посещении.<br/>|
|last_country|False|string|Страна, из которой посетитель последний раз посещал сайт.<br/>Определяется механизмами геолокации LiveTex.<br/>|
|visit_count|True|numeric|Количество посещений.<br/>|
|id|True|string|ID посетителя.<br/>|
|last_user_agent|True|string|Сигнатура браузера при последнем посещении.<br/>|
|lead_count|True|numeric|Количество лидов.<br/>|
|nickname|False|string|Имя, указанное сотрудником для посетителя.<br/>|
|banned_by|False|Employee|Сотрудник, заблокировавший посетителя.<br/>|
|email|False|string|Хронологически последний явный email, извлеченный из любого канала: чат, лид, жалоба.<br/>|
|call_count|True|numeric|Количество звонков.<br/>|
|banned_at|False|datetime|Дата и время блокировки посетителя.<br/>|
|phone|False|string|Хронологически последний явный телефон, извлеченный из любого канала: чат, лид, жалоба.<br/>|
|is_banned|True|boolean|Признак блокировки посетителя.<br/>|
|last_visit_pageviews|False|Array.<PageView>|Список просмотров страниц в последнем посещении в хронологическом порядке.<br/>|
|name|True|string|Имя, указанное посетителем. <br/>|
|created_at|True|datetime|Дата создания.<br/>|
|ban_reason|False|string|Причина блокировки посетителя.<br/>|
|chat_count|True|numeric|Количество чатов.<br/>|
|last_city|False|string|Город, из которого посетитель последний раз посещал сайт.<br/>Определяется механизмами геолокации LiveTex.<br/>|
