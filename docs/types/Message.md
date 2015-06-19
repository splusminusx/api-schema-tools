
## Message

### Описание типа
Сообщение.<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*text*|True|[string](/types/string)|Текст сообщения.<br/>|
|*created_at*|True|[datetime](/types/datetime)|Дата создания.<br/>|
|*visitor*|False|[Visitor](/types/Visitor)|Посетитель, отправивший сообщение.<br/>Если сообщение отправлено оператором, то – null.<br/>|
|*is_delivered*|True|[boolean](/types/boolean)|Признак доставленного сообщения до адресата.<br/>|
|*employee*|False|[Employee](/types/Employee)|Сотрудник, отправивший сообщение.<br/>Если сообщение отправлено посетителем, то – null.<br/>Одно из полей employee или visitor должно быть указано.<br/>|
|*id*|True|[numeric](/types/numeric)|ID сообщения.<br/>|
