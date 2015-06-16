
# EmployeeChatMessages

## Описание ресурса

# Методы

## list

### Описание метода
EmployeeChatMessages.list<br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*q*|False|[string](/docs/types/string.md)|Критерий поиска.<br/>Доступные поля:<br/>employee_ids – idlist, список ID сотрудников – участников переписки.<br/>Если указан только один ID, то в результатах поиска будут сообщения, в которых сотрудник был получателем или отправителем.<br/>Если указано два ID, то в результатах поиска будут только сообщения, переданные между указанными сотрудниками.<br/>Если указано более двух ID, то в результатах поиска будут сообщения, переданные между любыми двумя сотрудниками из числа перечисленных.<br/>created_at – datetime, максимальный период выборки – 30 дней.<br/>|
|*fields*|False|[string](/docs/types/string.md)|Список через запятую возвращаемых полей.<br/>|
|*limit*|False|[numeric](/docs/types/numeric.md)|По умолчанию – 50.<br/>|
|*sort*|False|[string](/docs/types/string.md)|Сортировка результатов.<br/>Возможные значения:<br/>created_at:a – по умолчанию.<br/>|
|*offset*|False|[numeric](/docs/types/numeric.md)|По умолчанию – 0.<br/>|

### Результат
Array.<[EmployeeChatMessage](/docs/types/EmployeeChatMessage.md)>
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner