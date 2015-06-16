
# EmployeeEvents

## Описание ресурса

# Методы

## list

### Описание метода
EmployeeEvents.list<br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*q*|False|[string](/docs/types/string.md)|Критерий поиска.<br/>Доступные поля:<br/>employee_ids – idlist, список ID сотрудников;<br/>event_type;<br/>created_at.<br/>|
|*fields*|False|[string](/docs/types/string.md)|Список через запятую возвращаемых полей.<br/>|
|*limit*|False|[numeric](/docs/types/numeric.md)|По умолчанию – 50.<br/>|
|*sort*|False|[string](/docs/types/string.md)|Сортировка результатов.<br/>Возможные значения:<br/>created_at:d – по умолчанию.<br/>|
|*offset*|False|[numeric](/docs/types/numeric.md)|По умолчанию – 0.<br/>|

### Результат
Array.<[EmployeeEvent](/docs/types/EmployeeEvent.md)>
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|full||
|manager|managed|События своих сотрудников.|
|chief|managed|События своих сотрудников.|
|chief_partner|managed|События своих сотрудников.|
|operator|user|Свои данные.|
|admin_partner|full||
