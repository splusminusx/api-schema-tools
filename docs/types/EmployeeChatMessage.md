
## EmployeeChatMessage

### Описание типа
EmployeeChatMessage<br/>Сообщение в переписке между сотрудниками.<br/>Таблица 37. Поля сообщения в переписке между сотрудниками<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|text|True|[string](/docs/types/string.md)|Текст сообщения.<br/>|
|created_at|True|[datetime](/docs/types/datetime.md)|Дата создания.<br/>|
|employee_to|True|[Employee](/docs/types/Employee.md)|Сотрудник, которому было адресовано сообщение.<br/>|
|employee_from|True|[Employee](/docs/types/Employee.md)|Сотрудник, отправивший сообщение.<br/>|
|id|True|[numeric](/docs/types/numeric.md)|ID сообщения.<br/>|
