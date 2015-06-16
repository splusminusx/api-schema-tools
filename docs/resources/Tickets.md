# Tickets
## Описание ресурса
Tickets
# Методы
## add
### Описание метода
Tickets.add
Добавляет новый тикет.
Параметры
Результат
Объект типа «Ticket».

Уровень доступа для ролей

### Поля
| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|text|True|string|Текст обращения в техническую поддержку.<br/>Максимум 2000 символов.<br/>|
|subject|False|string|Тема обращения в техническую поддержку.<br/>|
### Доступы к методу
| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner## list
### Описание метода
Tickets.list
Возвращает список тикетов.
Параметры
Результат
Массив объектов типа «Ticket».
Уровень доступа для ролей

### Поля
| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|q|False|string|Критерий поиска.<br/>Доступные поля:<br/>ids – idlist, список ID тикетов;<br/>employee_ids – idlist, список ID сотрудников;<br/>type;<br/>priority;<br/>status;<br/>created_at.<br/>|
|fields|False|string|Список через запятую возвращаемых полей.<br/>|
|limit|False|numeric|По умолчанию – 50.<br/>|
|sort|False|string|Сортировка результатов.<br/>Возможные значение:<br/>created_at:d – по умолчанию;<br/>type:a, type:d;<br/>priority:a, priority:d;<br/>status:a, status:d.<br/>|
|offset|False|numeric|По умолчанию – 0.<br/>|
### Доступы к методу
| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner## show
### Описание метода
Tickets.show
Возвращает данные указанного обращения в техническую поддержку.
Параметры
Результат
Объект типа «Ticket».
Уровень доступа для ролей

### Поля
| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|fields|False|string|Список через запятую возвращаемых полей.<br/>|
|id|True|numeric|ID обращения в техническую поддержку.<br/>|
### Доступы к методу
| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner