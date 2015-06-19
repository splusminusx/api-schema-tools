
# IgnoreListItems

## Описание ресурса

# Методы

## list

### Описание метода
Возвращает список записей игнор-листа.<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*q*|False|[string](/types/string)|Критерий поиска.<br/>Доступные поля:<br/>site_ids – idlist, список ID сайтов;<br/>employee_ids – idlist, список ID сотрудников.<br/>created_at.<br/>|
|*fields*|False|[string](/types/string)|Список через запятую возвращаемых полей.<br/>|
|*limit*|False|[numeric](/types/numeric)|По умолчанию – 50.<br/>|
|*sort*|False|[string](/types/string)|Сортировка результатов.<br/>Возможные значение:<br/>created_at:a – по умолчанию.<br/>|
|*offset*|False|[numeric](/types/numeric)|По умолчанию – 0.<br/>|

### Результат
Array.<[IgnoreListItem](/types/IgnoreListItem)>
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
|*site_id*|True|[numeric](/types/numeric)|ID сайта.<br/>|
|*visitor_id*|True|[string](/types/string)|ID посетителя.<br/>|

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
