
# Comments

## Описание ресурса
Comments<br/>
# Методы

## add

### Описание метода
Comments.add<br/>Добавляет новый комментарий к обращению в поддержку.<br/>Параметры<br/>Результат<br/>Объект типа «Comment».<br/>Уровень доступа для ролей<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|text|True|[string](/docs/types/string.md)|Текст комментария.<br/>Максимум 2000 символов.<br/>|
|ticket_id|True|[numeric](/docs/types/numeric.md)|ID обращения в поддержку.<br/>|

### Резудьтат
[Comment](/docs/types/Comment.md)
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner
## list

### Описание метода
Comments.list<br/>Возвращает список комментариев к обращению в поддержку.<br/>Параметры<br/>Результат<br/>Массив объектов типа «Comment».<br/>Уровень доступа для ролей<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|q|False|[string](/docs/types/string.md)|Критерий поиска.<br/>Доступные поля:<br/>ids – idlist, список ID тикетов;<br/>ticket_ids – idlist, список ID тикетов;<br/>employee_ids – idlist, список ID сотрудников.<br/>created_at.<br/>|
|fields|False|[string](/docs/types/string.md)|Список через запятую возвращаемых полей.<br/>|
|limit|False|[numeric](/docs/types/numeric.md)|По умолчанию – 50.<br/>|
|sort|False|[string](/docs/types/string.md)|Сортировка результатов.<br/>Возможные значение:<br/>created_at:d – по умолчанию.<br/>|
|offset|False|[numeric](/docs/types/numeric.md)|По умолчанию – 0.<br/>|

### Резудьтат
Array.<[Comment](/docs/types/Comment.md)>
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner
## show

### Описание метода
Comments.show<br/>Возвращает данные указанного обращения в поддержку.<br/>Параметры<br/>Результат<br/>Объект типа «Comment».<br/>Уровень доступа для ролей<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|fields|False|[string](/docs/types/string.md)|Список через запятую возвращаемых полей.<br/>|
|id|True|[numeric](/docs/types/numeric.md)|ID комментария к обращению в поддержку.<br/>|

### Резудьтат
[Comment](/docs/types/Comment.md)
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner