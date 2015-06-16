
# IgnoreListItems

## Описание ресурса

# Методы

## list

### Описание метода
Возвращает список записей игнор-листа.<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*q*|False|[string](/docs/types/string.md)|Критерий поиска.<br/>Доступные поля:<br/>site_ids – idlist, список ID сайтов;<br/>employee_ids – idlist, список ID сотрудников.<br/>created_at.<br/>|
|*fields*|False|[string](/docs/types/string.md)|Список через запятую возвращаемых полей.<br/>|
|*limit*|False|[numeric](/docs/types/numeric.md)|По умолчанию – 50.<br/>|
|*sort*|False|[string](/docs/types/string.md)|Сортировка результатов.<br/>Возможные значение:<br/>created_at:a – по умолчанию.<br/>|
|*offset*|False|[numeric](/docs/types/numeric.md)|По умолчанию – 0.<br/>|

### Результат
Array.<[IgnoreListItem](/docs/types/IgnoreListItem.md)>
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|*admin*|full||
|*manager*|managed|Только записи на своих сайтах.|
|*chief*|managed|Только записи на своих сайтах.|
|*chief_partner*|managed|Только записи на своих сайтах.|
|*operator*|none||
|*admin_partner*|full||

## delete

### Описание метода
Удаляет запись в игнор-листе.<br/><br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*site_id*|True|[numeric](/docs/types/numeric.md)|ID сайта.<br/>|
|*visitor_id*|True|[string](/docs/types/string.md)|ID посетителя.<br/>|

### Результат
None
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|*admin*|full||
|*manager*|managed|Только записи на своих сайтах.|
|*chief*|managed|Только записи на своих сайтах.|
|*chief_partner*|managed|Только записи на своих сайтах.|
|*operator*|none||
|*admin_partner*|full||
