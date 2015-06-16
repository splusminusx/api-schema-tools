
# Сhats

## Описание ресурса
Сhats<br/>
# Методы

## setContactInfoExist

### Описание метода
Chats.setContactInfoExist<br/>Устанавливает признак наличия контактной информации в чате.<br/>Повторный вызов этого метода для одного и того же чата приводит к пополнению массивов найденных контактных данных.<br/>Параметры<br/>Результат<br/>Метод ничего не возвращает.<br/>Уровень доступа для ролей<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|id|True|[numeric](/docs/types/numeric.md)|ID чата.<br/>|
|contact_info|True|[Object](/docs/types/Object.md)|Объект с информацией о найденных контактных данных.<br/>Может содержать ключи:<br/>emails – массив найденных адресов электронной почты.<br/>phones – массив найденных номеров телефонов.<br/>Должен содержать хотя бы один из этих ключей с непустым массивом.<br/>|

### Резудьтат
None
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner
## list

### Описание метода
Сhats.list<br/>Возвращает список чатов.<br/>Параметры<br/>Результат<br/>Массив объектов типа «Chat», а также, поле total_conversations.<br/>Перечень дополнительных полей<br/><br/>Уровень доступа для ролей<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|q|False|[string](/docs/types/string.md)|Критерий поиска.<br/>Доступные поля:<br/>ids – idlist, список ID чатов;<br/>site_ids – idlist, список ID сайтов;<br/>department_ids – idlist, список ID отделов;<br/>employee_ids – idlist, список ID сотрудников;<br/>conversation_ids – idlist, список ID обращений;<br/>visitor_ids – idlist, список ID посетителей;<br/>message_text – string, подстрока в тексте сообщения;<br/>result;<br/>message_count;<br/>queue_time;<br/>first_answer_time;<br/>duration;<br/>is_complaint – boolean, наличие жалобы в обращении, которому принадлежит чат;<br/>employee_remark_ids – idlist, список оценок операторов, поставленных обращению, которому принадлежит чат;<br/>rem_long_answer;<br/>rem_transfer;<br/>rem_empty;<br/>rem_auto;<br/>rem_lost_in_queue;<br/>visitor_vote – enum, оценка посетителя;<br/>is_managed;<br/>created_at.<br/>|
|fields|False|[string](/docs/types/string.md)|Список через запятую возвращаемых полей.<br/>|
|limit|False|[numeric](/docs/types/numeric.md)|По умолчанию – 50.<br/>|
|sort|False|[string](/docs/types/string.md)|Сортировка результатов.<br/>Возможные значения:<br/>created_at:a;<br/>updated_at:a;<br/>duration:a;<br/>result:a.<br/>|
|offset|False|[numeric](/docs/types/numeric.md)|По умолчанию – 0.<br/>|

### Резудьтат
Array.<[Chat](/docs/types/Chat.md)>
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner
## show

### Описание метода
Chats.show<br/>Возвращает данные указанного чата.<br/>Параметры<br/>Результат<br/>Объект типа «Chat».<br/>Уровень доступа для ролей<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|fields|False|[string](/docs/types/string.md)|Список через запятую возвращаемых полей.<br/>|
|id|True|[numeric](/docs/types/numeric.md)|ID чата.<br/>|

### Резудьтат
[Chat](/docs/types/Chat.md)
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner