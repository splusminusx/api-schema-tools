
## Visitor

### Описание типа
Visitor<br/>Посетитель.<br/>Таблица 87. Поля посетителя<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*comment*|False|[string](/docs/types/string.md)|Комментарий сотрудника.<br/>|
|*visitor_variables*|False|[Object](/docs/types/Object.md)|Объект с текущими переменными посетителя.<br/>|
|*last_visit_at*|True|[datetime](/docs/types/datetime.md)|Дата последнего посещения.<br/>|
|*last_ip*|True|[string](/docs/types/string.md)|IP-адрес посетителя при последнем посещении.<br/>|
|*last_country*|False|[string](/docs/types/string.md)|Страна, из которой посетитель последний раз посещал сайт.<br/>Определяется механизмами геолокации LiveTex.<br/>|
|*visit_count*|True|[numeric](/docs/types/numeric.md)|Количество посещений.<br/>|
|*id*|True|[string](/docs/types/string.md)|ID посетителя.<br/>|
|*last_user_agent*|True|[string](/docs/types/string.md)|Сигнатура браузера при последнем посещении.<br/>|
|*lead_count*|True|[numeric](/docs/types/numeric.md)|Количество лидов.<br/>|
|*nickname*|False|[string](/docs/types/string.md)|Имя, указанное сотрудником для посетителя.<br/>|
|*banned_by*|False|[Employee](/docs/types/Employee.md)|Сотрудник, заблокировавший посетителя.<br/>|
|*email*|False|[string](/docs/types/string.md)|Хронологически последний явный email, извлеченный из любого канала: чат, лид, жалоба.<br/>|
|*call_count*|True|[numeric](/docs/types/numeric.md)|Количество звонков.<br/>|
|*banned_at*|False|[datetime](/docs/types/datetime.md)|Дата и время блокировки посетителя.<br/>|
|*phone*|False|[string](/docs/types/string.md)|Хронологически последний явный телефон, извлеченный из любого канала: чат, лид, жалоба.<br/>|
|*is_banned*|True|[boolean](/docs/types/boolean.md)|Признак блокировки посетителя.<br/>|
|*last_visit_pageviews*|False|Array.<[PageView](/docs/types/PageView.md)>|Список просмотров страниц в последнем посещении в хронологическом порядке.<br/>|
|*name*|True|[string](/docs/types/string.md)|Имя, указанное посетителем. <br/>|
|*created_at*|True|[datetime](/docs/types/datetime.md)|Дата создания.<br/>|
|*ban_reason*|False|[string](/docs/types/string.md)|Причина блокировки посетителя.<br/>|
|*chat_count*|True|[numeric](/docs/types/numeric.md)|Количество чатов.<br/>|
|*last_city*|False|[string](/docs/types/string.md)|Город, из которого посетитель последний раз посещал сайт.<br/>Определяется механизмами геолокации LiveTex.<br/>|
