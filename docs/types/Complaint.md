
## Complaint

### Описание типа
Жалоба посетителя.<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*phone*|False|[string](/types/string)|Номер телефона.<br/>Одно из полей email или phone должно быть указано.<br/>|
|*text*|True|[string](/types/string)|Текст жалобы.<br/>|
|*created_at*|True|[datetime](/types/datetime)|Дата создания.<br/>|
|*updated_at*|True|[datetime](/types/datetime)|Дата последнего обновления.<br/>|
|*site*|True|[Site](/types/Site)|Сайт.<br/>|
|*conversation*|True|[Conversation](/types/Conversation)|Обращение, в ходе которого отправлена жалоба.<br/>|
|*department*|False|[Department](/types/Department)|Отдел.<br/>|
|*id*|True|[string](/types/string)|ID жалобы.<br/>|
|*visitor*|True|[Visitor](/types/Visitor)|Посетитель.<br/>|
|*employee*|False|[Employee](/types/Employee)|Сотрудник.<br/><br/>|
|*email*|False|[string](/types/string)|Адрес электронной почты.<br/>Одно из полей email или phone должно быть указано.<br/>|
