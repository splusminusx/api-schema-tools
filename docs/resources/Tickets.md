
# Tickets

## Описание ресурса

# Методы

## add

### Описание метода
Добавляет новый тикет.<br/><br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*text*|True|[string](/types/string)|Текст обращения в техническую поддержку.<br/>Максимум 2000 символов.<br/>|
|*subject*|False|[string](/types/string)|Тема обращения в техническую поддержку.<br/>|

### Результат
[Ticket](/types/Ticket)
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|*admin*|full||
|*manager*|full||
|*chief*|full||
|*chief_partner*|full||
|*operator*|full||
|*admin_partner*|full||

## list

### Описание метода
Возвращает список тикетов.<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*q*|False|[string](/types/string)|Критерий поиска.<br/>Доступные поля:<br/>ids – idlist, список ID тикетов;<br/>employee_ids – idlist, список ID сотрудников;<br/>type;<br/>priority;<br/>status;<br/>created_at.<br/>|
|*fields*|False|[string](/types/string)|Список через запятую возвращаемых полей.<br/>|
|*limit*|False|[numeric](/types/numeric)|По умолчанию – 50.<br/>|
|*sort*|False|[string](/types/string)|Сортировка результатов.<br/>Возможные значение:<br/>created_at:d – по умолчанию;<br/>type:a, type:d;<br/>priority:a, priority:d;<br/>status:a, status:d.<br/>|
|*offset*|False|[numeric](/types/numeric)|По умолчанию – 0.<br/>|

### Результат
Array.<[Ticket](/types/Ticket)>
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|*admin*|full||
|*manager*|full||
|*chief*|full||
|*chief_partner*|full||
|*operator*|user|Только свои тикеты|
|*admin_partner*|full||

## show

### Описание метода
Возвращает данные указанного обращения в техническую поддержку.<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*fields*|False|[string](/types/string)|Список через запятую возвращаемых полей.<br/>|
|*id*|True|[numeric](/types/numeric)|ID обращения в техническую поддержку.<br/>|

### Результат
[Ticket](/types/Ticket)
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|*admin*|full||
|*manager*|full||
|*chief*|full||
|*chief_partner*|full||
|*operator*|user|Только свои тикеты.|
|*admin_partner*|full||
