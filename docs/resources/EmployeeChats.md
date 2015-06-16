
# EmployeeChats

## Описание ресурса

# Методы

## list

### Описание метода
EmployeeChats.list<br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*q*|False|[string](/docs/types/string.md)|Критерий поиска.<br/>Доступные поля:<br/>employee_ids – idlist, список ID сотрудников – участников чата. Чат удовлетворяет условию поиска, если хотя бы один его участник указан в этом списке.<br/>text – ключевое слово в тексте чата.<br/>created_at – datetime, максимум 30 дней.<br/>Если не указано, то фильтр устанавливается в значение, соответствующее последним 30 дням.<br/>|
|*fields*|False|[string](/docs/types/string.md)|Список через запятую возвращаемых полей сотрудников.<br/>Например: employee(first_name).<br/>|
|*limit*|False|[numeric](/docs/types/numeric.md)|По умолчанию – 50.<br/>|
|*offset*|False|[numeric](/docs/types/numeric.md)|По умолчанию – 0.<br/>|

### Результат
None
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner