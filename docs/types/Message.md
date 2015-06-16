
## Message

### Описание типа
Message
Сообщение.
Таблица 54. Поля сообщения


### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|text|True|[string](/docs/types/string.md)|Текст сообщения.<br/>|
|created_at|True|[datetime](/docs/types/datetime.md)|Дата создания.<br/>|
|visitor|False|[Visitor](/docs/types/Visitor.md)|Посетитель, отправивший сообщение.<br/>Если сообщение отправлено оператором, то – null.<br/>|
|is_delivered|True|[boolean](/docs/types/boolean.md)|Признак доставленного сообщения до адресата.<br/>|
|employee|False|[Employee](/docs/types/Employee.md)|Сотрудник, отправивший сообщение.<br/>Если сообщение отправлено посетителем, то – null.<br/>Одно из полей employee или visitor должно быть указано.<br/>|
|id|True|[numeric](/docs/types/numeric.md)|ID сообщения.<br/>|
