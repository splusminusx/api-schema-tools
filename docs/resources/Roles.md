
# Roles

## Описание ресурса

# Методы

## list

### Описание метода
Возвращает список ролей.<br/>Массив объектов типа «Role».<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*q*|False|[string](/docs/types/string.md)|Критерий поиска.<br/>Доступные поля:<br/>code.<br/>|
|*fields*|False|[string](/docs/types/string.md)|Список через запятую возвращаемых полей.<br/>|
|*limit*|False|[numeric](/docs/types/numeric.md)|По умолчанию – 50.<br/>|
|*sort*|False|[string](/docs/types/string.md)|Сортировка результатов.<br/>Возможные значения:<br/>title:a, title:b.<br/>Если не указано, то записи сортируются в порядке убывания привилегий роли.<br/>|
|*offset*|False|[numeric](/docs/types/numeric.md)|По умолчанию – 0.<br/>|

### Результат
Array.<[Role](/docs/types/Role.md)>
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|*admin*|full||
|*manager*|full||
|*chief*|full||
|*chief_partner*|full||
|*operator*|full||
|*admin_partner*|full||
