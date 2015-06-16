
# Сhats

## Описание ресурса

# Методы

## setContactInfoExist

### Описание метода
Chats.setContactInfoExist<br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*id*|True|[numeric](/docs/types/numeric.md)|ID чата.<br/>|
|*contact_info*|True|[Object](/docs/types/Object.md)|Объект с информацией о найденных контактных данных.<br/>Может содержать ключи:<br/>emails – массив найденных адресов электронной почты.<br/>phones – массив найденных номеров телефонов.<br/>Должен содержать хотя бы один из этих ключей с непустым массивом.<br/>|

### Результат
None
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|user|Только для чатов, в которых сотрудник является участником.|
|manager|user|Только для чатов, в которых сотрудник является участником.|
|chief|user|Только для чатов, в которых сотрудник является участником.|
|chief_partner|user|Только для чатов, в которых сотрудник является участником.|
|operator|user|Только для чатов, в которых сотрудник является участником.|
|admin_partner|user|Только для чатов, в которых сотрудник является участником.|

## list

### Описание метода
Сhats.list<br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*q*|False|[string](/docs/types/string.md)|Критерий поиска.<br/>Доступные поля:<br/>ids – idlist, список ID чатов;<br/>site_ids – idlist, список ID сайтов;<br/>department_ids – idlist, список ID отделов;<br/>employee_ids – idlist, список ID сотрудников;<br/>conversation_ids – idlist, список ID обращений;<br/>visitor_ids – idlist, список ID посетителей;<br/>message_text – string, подстрока в тексте сообщения;<br/>result;<br/>message_count;<br/>queue_time;<br/>first_answer_time;<br/>duration;<br/>is_complaint – boolean, наличие жалобы в обращении, которому принадлежит чат;<br/>employee_remark_ids – idlist, список оценок операторов, поставленных обращению, которому принадлежит чат;<br/>rem_long_answer;<br/>rem_transfer;<br/>rem_empty;<br/>rem_auto;<br/>rem_lost_in_queue;<br/>visitor_vote – enum, оценка посетителя;<br/>is_managed;<br/>created_at.<br/>|
|*fields*|False|[string](/docs/types/string.md)|Список через запятую возвращаемых полей.<br/>|
|*limit*|False|[numeric](/docs/types/numeric.md)|По умолчанию – 50.<br/>|
|*sort*|False|[string](/docs/types/string.md)|Сортировка результатов.<br/>Возможные значения:<br/>created_at:a;<br/>updated_at:a;<br/>duration:a;<br/>result:a.<br/>|
|*offset*|False|[numeric](/docs/types/numeric.md)|По умолчанию – 0.<br/>|

### Результат
Array.<[Chat](/docs/types/Chat.md)>
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|full||
|manager|managed|Все чаты, но без messages и events.|
|chief|managed|Все чаты, но без messages и events.|
|chief_partner|managed|Все чаты, но без messages и events.|
|operator|managed|Все чаты, но без messages и events.|
|admin_partner|full||

## show

### Описание метода
Chats.show<br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*fields*|False|[string](/docs/types/string.md)|Список через запятую возвращаемых полей.<br/>|
|*id*|True|[numeric](/docs/types/numeric.md)|ID чата.<br/>|

### Результат
[Chat](/docs/types/Chat.md)
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|full||
|manager|managed|Все чаты, но без messages и events.|
|chief|managed|Все чаты, но без messages и events.|
|chief_partner|managed|Все чаты, но без messages и events.|
|operator|managed|Все чаты, но без messages и events.|
|admin_partner|full||
