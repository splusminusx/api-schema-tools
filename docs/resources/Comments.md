
# Comments

## Описание ресурса

# Методы

## add

### Описание метода
Добавляет новый комментарий к обращению в поддержку.<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*text*|True|[string](/docs/types/string.md)|Текст комментария.<br/>Максимум 2000 символов.<br/>|
|*ticket_id*|True|[numeric](/docs/types/numeric.md)|ID обращения в поддержку.<br/>|

### Результат
[Comment](/docs/types/Comment.md)
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|*admin*|full||
|*manager*|full||
|*chief*|full||
|*chief_partner*|full||
|*operator*|user|Добавление комментариев к своим тикетам.|
|*admin_partner*|full||

## list

### Описание метода
Возвращает список комментариев к обращению в поддержку.<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*q*|False|[string](/docs/types/string.md)|Критерий поиска.<br/>Доступные поля:<br/>ids – idlist, список ID тикетов;<br/>ticket_ids – idlist, список ID тикетов;<br/>employee_ids – idlist, список ID сотрудников.<br/>created_at.<br/>|
|*fields*|False|[string](/docs/types/string.md)|Список через запятую возвращаемых полей.<br/>|
|*limit*|False|[numeric](/docs/types/numeric.md)|По умолчанию – 50.<br/>|
|*sort*|False|[string](/docs/types/string.md)|Сортировка результатов.<br/>Возможные значение:<br/>created_at:d – по умолчанию.<br/>|
|*offset*|False|[numeric](/docs/types/numeric.md)|По умолчанию – 0.<br/>|

### Результат
Array.<[Comment](/docs/types/Comment.md)>
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|*admin*|full||
|*manager*|full||
|*chief*|full||
|*chief_partner*|full||
|*operator*|user|Комментарии своих тикетов.|
|*admin_partner*|full||

## show

### Описание метода
Возвращает данные указанного обращения в поддержку.<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*fields*|False|[string](/docs/types/string.md)|Список через запятую возвращаемых полей.<br/>|
|*id*|True|[numeric](/docs/types/numeric.md)|ID комментария к обращению в поддержку.<br/>|

### Результат
[Comment](/docs/types/Comment.md)
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|*admin*|full||
|*manager*|full||
|*chief*|full||
|*chief_partner*|full||
|*operator*|user|Комментарии своих тикетов.|
|*admin_partner*|full||
