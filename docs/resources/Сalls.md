
# Сalls

## Описание ресурса

# Методы

## list

### Описание метода
Сalls.list<br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*q*|False|[string](/docs/types/string.md)|Критерий поиска.<br/>Доступные поля:<br/>ids – idlist, список ID звонков;<br/>site_ids – idlist, список ID сайтов;<br/>department_ids – idlist, список ID отделов;<br/>employee_ids – idlist, список ID сотрудников;<br/>visitor_ids – idlist, список ID посетителей;<br/>conversation_ids – idlist, список ID обращений;<br/>is_incoming;<br/>result;<br/>answer_time;<br/>duration;<br/>rem_long_answer;<br/>rem_transfer;<br/>rem_empty;<br/>rem_auto;<br/>rem_lost_in_queue;<br/>visitor_vote;<br/>operator_vote_ids – idlist, список ID оценок сотрудника;<br/>search_engine;<br/>ext_referer;<br/>int_referer;<br/>is_managed;<br/>created_at.<br/>|
|*fields*|False|[string](/docs/types/string.md)|Список через запятую возвращаемых полей.<br/>|
|*limit*|False|[numeric](/docs/types/numeric.md)|По умолчанию – 50.<br/>|
|*sort*|False|[string](/docs/types/string.md)|Сортировка результатов.<br/>Возможные значения:<br/>created_at:d – по умолчанию;<br/>updated_at:d;<br/>duration:a, duration:d;<br/>answer_time:a, answer_time:d;<br/>result:a, result:d.<br/>|
|*offset*|False|[numeric](/docs/types/numeric.md)|По умолчанию – 0.<br/>|

### Результат
Array.<[Call](/docs/types/Call.md)>
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner
## show

### Описание метода
Сalls.show<br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*fields*|False|[string](/docs/types/string.md)|Список через запятую возвращаемых полей.<br/>|
|*id*|True|[numeric](/docs/types/numeric.md)|ID звонка.<br/>|

### Результат
[Call](/docs/types/Call.md)
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner