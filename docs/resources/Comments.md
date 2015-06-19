
# Comments

## Описание ресурса

# Методы

## add

### Описание метода
Добавляет новый комментарий к обращению в поддержку.<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*text*|True|[string](/types/string)|Текст комментария.<br/>Максимум 2000 символов.<br/>|
|*ticket_id*|True|[numeric](/types/numeric)|ID обращения в поддержку.<br/>|

### Результат
[Comment](/types/Comment)
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
|*q*|False|[string](/types/string)|Критерий поиска.<br/>Доступные поля:<br/>ids – idlist, список ID тикетов;<br/>ticket_ids – idlist, список ID тикетов;<br/>employee_ids – idlist, список ID сотрудников.<br/>created_at.<br/>|
|*fields*|False|[string](/types/string)|Список через запятую возвращаемых полей.<br/>|
|*limit*|False|[numeric](/types/numeric)|По умолчанию – 50.<br/>|
|*sort*|False|[string](/types/string)|Сортировка результатов.<br/>Возможные значение:<br/>created_at:d – по умолчанию.<br/>|
|*offset*|False|[numeric](/types/numeric)|По умолчанию – 0.<br/>|

### Результат
Array.<[Comment](/types/Comment)>
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
|*fields*|False|[string](/types/string)|Список через запятую возвращаемых полей.<br/>|
|*id*|True|[numeric](/types/numeric)|ID комментария к обращению в поддержку.<br/>|

### Результат
[Comment](/types/Comment)
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|*admin*|full||
|*manager*|full||
|*chief*|full||
|*chief_partner*|full||
|*operator*|user|Комментарии своих тикетов.|
|*admin_partner*|full||
