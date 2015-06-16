
# HoldRules

## Описание ресурса
HoldRules

# Методы

## add

### Описание метода
HoldRules.add
Создает новый сценарий удержания.
Параметры
Результат
Объект типа «HoldRule».
Пример вызова
curl "https://api.livetex.ru/v2/holdrules" \
-H "Authorization: Bearer ACCESS_TOKEN" \
	-d "title=Одно сообщение и перевод" \
	-d "hold_messages[0][text]=Оператор скоро вам ответит" \
	-d "hold_messages[0][send_after]=15" \
	-d "is_transfer=true" \
	-d "transfer_after=15"

Уровень доступа для ролей


### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|is_transfer|True|[boolean](/docs/types/boolean.md)|Признак перенаправления на другого оператора после последнего сообщения.<br/>Принимается во внимание, только если hold_messages содержит хотя бы один элемент.<br/>|
|site_ids|False|[idlist](/docs/types/idlist.md)|Список ID сайтов, к которым следует подключить сценарий удержания.<br/>Если на указанном сайте уже используется какой-нибудь сценарий удержания, то он будет заменен на создаваемый.<br/>|
|hold_messages|True|Array.<[HoldMessage](/docs/types/HoldMessage.md)>|Массив удерживающих сообщений.<br/>От 1 до 3 элементов.<br/>|
|transfer_after|False|[numeric](/docs/types/numeric.md)|Интервал в секундах после последнего сообщения, по истечение которого выполнить перенаправление на другого оператора, если указано is_transfer.<br/>Должен быть от 5 до 3600 секунд.<br/>Обязательно, если is_transfer = true.<br/>Принимается во внимание, только если hold_messages содержит хотя бы один элемент.<br/>|
|title|True|[string](/docs/types/string.md)|Название сценария удержания.<br/>|

### Резудьтат
[HoldRule](/docs/types/HoldRule.md)
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner
## show

### Описание метода
HoldRules.show
Возвращает данные указанного сценария удержания.
Параметры
Результат
Объект типа «HoldRule».
Уровень доступа для ролей


### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|fields|False|[string](/docs/types/string.md)|Список через запятую возвращаемых полей.<br/>|
|id|True|[numeric](/docs/types/numeric.md)|ID сценария удержания.<br/>|

### Резудьтат
[HoldRule](/docs/types/HoldRule.md)
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner
## list

### Описание метода
HoldRules.list
Возвращает список сценариев удержания.
Параметры
Результат
Массив объектов типа «HoldRule».
Уровень доступа для ролей


### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|q|False|[string](/docs/types/string.md)|Критерий поиска.<br/>Доступные поля:<br/>ids – idlist, список ID сценариев удержания;<br/>site_ids – idlist, список ID сайтов, на которых используется сценарий;<br/>title.<br/>|
|fields|False|[string](/docs/types/string.md)|Список через запятую возвращаемых полей.<br/>|
|limit|False|[numeric](/docs/types/numeric.md)|По умолчанию – 50.<br/>|
|sort|False|[string](/docs/types/string.md)|Сортировка результатов.<br/>Возможные значения:<br/>title:a – по умолчанию, title:d.<br/>|
|offset|False|[numeric](/docs/types/numeric.md)|По умолчанию – 0.<br/>|

### Резудьтат
Array.<[HoldRule](/docs/types/HoldRule.md)>
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner
## update

### Описание метода
HoldRules.update
Изменяет указанный сценарий удержания.
Параметры
Результат
Метод ничего не возвращает.
Уровень доступа для ролей


### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|title|False|[string](/docs/types/string.md)|Название сценария удержания.<br/>|
|transfer_after|False|[numeric](/docs/types/numeric.md)|Интервал в секундах после последнего сообщения, по истечение которого выполнить перенаправление на другого оператора, если указано is_transfer.<br/>Должен быть от 5 до 3600 секунд.<br/>Обязательно, если is_transfer = true.<br/>Принимается во внимание, только если hold_messages содержит хотя бы один элемент.<br/>|
|is_transfer|False|[boolean](/docs/types/boolean.md)|Признак перенаправления на другого оператора после последнего сообщения.<br/>Принимается во внимание, только если hold_messages содержит хотя бы один элемент.<br/>|
|site_ids|False|[idlist](/docs/types/idlist.md)|Список через запятую ID сайтов, на которых должен работать обновляемые сценарий удержания.<br/>Если на указанном сайте уже используется какой-нибудь сценарий удержания, то он будет заменен на обновляемый сценарий.<br/>Если обновляемый сценарий удержания используется на сайтах, не указанных в списке, то значение поля hold_rule этих сайтов устанавливается в null.<br/>Если в качестве значение указана пустая строка, то сценарий удержания будет отвязан от всех сайтов.<br/>|
|hold_messages|False|Array.<[HoldMessage](/docs/types/HoldMessage.md)>|Массив удерживающих сообщений.<br/>От 1 до 3 элементов.<br/>|
|id|True|[numeric](/docs/types/numeric.md)|ID сценария удержания.<br/>|

### Резудьтат
None
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner
## delete

### Описание метода
HoldRules.delete
Удаляет указанный сценария удержания.
Параметры
Результат
Метод ничего не возвращает.
Уровень доступа для ролей


### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|id|True|[numeric](/docs/types/numeric.md)|ID сценария удержания.<br/>|

### Резудьтат
None
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner