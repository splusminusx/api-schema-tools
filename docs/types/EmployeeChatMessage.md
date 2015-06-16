
## EmployeeChatMessage

### Описание типа
EmployeeChatMessage
Сообщение в переписке между сотрудниками.
Таблица 37. Поля сообщения в переписке между сотрудниками


### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|text|True|string|Текст сообщения.<br/>|
|created_at|True|datetime|Дата создания.<br/>|
|employee_to|True|Employee|Сотрудник, которому было адресовано сообщение.<br/>|
|employee_from|True|Employee|Сотрудник, отправивший сообщение.<br/>|
|id|True|numeric|ID сообщения.<br/>|
