
## Visitor

### Описание типа
Посетитель.<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*comment*|False|[string](/types/string)|Комментарий сотрудника.<br/>|
|*visitor_variables*|False|[Object](/types/Object)|Объект с текущими переменными посетителя.<br/>|
|*last_visit_at*|True|[datetime](/types/datetime)|Дата последнего посещения.<br/>|
|*last_ip*|True|[string](/types/string)|IP-адрес посетителя при последнем посещении.<br/>|
|*last_country*|False|[string](/types/string)|Страна, из которой посетитель последний раз посещал сайт.<br/>Определяется механизмами геолокации LiveTex.<br/>|
|*visit_count*|True|[numeric](/types/numeric)|Количество посещений.<br/>|
|*id*|True|[string](/types/string)|ID посетителя.<br/>|
|*last_user_agent*|True|[string](/types/string)|Сигнатура браузера при последнем посещении.<br/>|
|*lead_count*|True|[numeric](/types/numeric)|Количество лидов.<br/>|
|*nickname*|False|[string](/types/string)|Имя, указанное сотрудником для посетителя.<br/>|
|*banned_by*|False|[Employee](/types/Employee)|Сотрудник, заблокировавший посетителя.<br/>|
|*email*|False|[string](/types/string)|Хронологически последний явный email, извлеченный из любого канала: чат, лид, жалоба.<br/>|
|*call_count*|True|[numeric](/types/numeric)|Количество звонков.<br/>|
|*banned_at*|False|[datetime](/types/datetime)|Дата и время блокировки посетителя.<br/>|
|*phone*|False|[string](/types/string)|Хронологически последний явный телефон, извлеченный из любого канала: чат, лид, жалоба.<br/>|
|*is_banned*|True|[boolean](/types/boolean)|Признак блокировки посетителя.<br/>|
|*last_visit_pageviews*|False|Array.<[PageView](/types/PageView)>|Список просмотров страниц в последнем посещении в хронологическом порядке.<br/>|
|*name*|True|[string](/types/string)|Имя, указанное посетителем. <br/>|
|*created_at*|True|[datetime](/types/datetime)|Дата создания.<br/>|
|*ban_reason*|False|[string](/types/string)|Причина блокировки посетителя.<br/>|
|*chat_count*|True|[numeric](/types/numeric)|Количество чатов.<br/>|
|*last_city*|False|[string](/types/string)|Город, из которого посетитель последний раз посещал сайт.<br/>Определяется механизмами геолокации LiveTex.<br/>|
