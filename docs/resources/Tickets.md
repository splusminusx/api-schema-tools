
# Tickets

## Описание ресурса
Tickets<br/>
# Методы

## add

### Описание метода
Tickets.add<br/>Добавляет новый тикет.<br/>Параметры<br/>Результат<br/>Объект типа «Ticket».<br/><br/>Уровень доступа для ролей<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|text|True|[string](/docs/types/string.md)|Текст обращения в техническую поддержку.<br/>Максимум 2000 символов.<br/>|
|subject|False|[string](/docs/types/string.md)|Тема обращения в техническую поддержку.<br/>|

### Резудьтат
[Ticket](/docs/types/Ticket.md)
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner
## list

### Описание метода
Tickets.list<br/>Возвращает список тикетов.<br/>Параметры<br/>Результат<br/>Массив объектов типа «Ticket».<br/>Уровень доступа для ролей<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|q|False|[string](/docs/types/string.md)|Критерий поиска.<br/>Доступные поля:<br/>ids – idlist, список ID тикетов;<br/>employee_ids – idlist, список ID сотрудников;<br/>type;<br/>priority;<br/>status;<br/>created_at.<br/>|
|fields|False|[string](/docs/types/string.md)|Список через запятую возвращаемых полей.<br/>|
|limit|False|[numeric](/docs/types/numeric.md)|По умолчанию – 50.<br/>|
|sort|False|[string](/docs/types/string.md)|Сортировка результатов.<br/>Возможные значение:<br/>created_at:d – по умолчанию;<br/>type:a, type:d;<br/>priority:a, priority:d;<br/>status:a, status:d.<br/>|
|offset|False|[numeric](/docs/types/numeric.md)|По умолчанию – 0.<br/>|

### Резудьтат
Array.<[Ticket](/docs/types/Ticket.md)>
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner
## show

### Описание метода
Tickets.show<br/>Возвращает данные указанного обращения в техническую поддержку.<br/>Параметры<br/>Результат<br/>Объект типа «Ticket».<br/>Уровень доступа для ролей<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|fields|False|[string](/docs/types/string.md)|Список через запятую возвращаемых полей.<br/>|
|id|True|[numeric](/docs/types/numeric.md)|ID обращения в техническую поддержку.<br/>|

### Резудьтат
[Ticket](/docs/types/Ticket.md)
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner