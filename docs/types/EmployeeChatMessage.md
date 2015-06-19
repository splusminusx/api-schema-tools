
## EmployeeChatMessage

### Описание типа
Сообщение в переписке между сотрудниками.<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*text*|True|[string](/types/string)|Текст сообщения.<br/>|
|*created_at*|True|[datetime](/types/datetime)|Дата создания.<br/>|
|*employee_to*|True|[Employee](/types/Employee)|Сотрудник, которому было адресовано сообщение.<br/>|
|*employee_from*|True|[Employee](/types/Employee)|Сотрудник, отправивший сообщение.<br/>|
|*id*|True|[numeric](/types/numeric)|ID сообщения.<br/>|
