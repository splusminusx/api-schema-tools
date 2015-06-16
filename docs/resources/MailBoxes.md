
# MailBoxes

## Описание ресурса
MailBoxes<br/>
# Методы

## add

### Описание метода
MailBoxes.add<br/>Добавляет новый почтовый ящик.<br/>Параметры<br/>Результат<br/>Объект типа «MailBox».<br/>Уровень доступа для ролей<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|username|False|[string](/docs/types/string.md)|Логин для подключения к почтовому серверу.<br/>|
|is_ssl|False|[boolean](/docs/types/boolean.md)|Признак использования защищенного соединения.<br/>По умолчанию - false.<br/>|
|smtp_port|False|[numeric](/docs/types/numeric.md)|Порт для подключения к почтовому серверу.<br/>По умолчанию - 25.<br/>Целое число в диапазоне от 1 до 65535.<br/>|
|smtp_server|True|[string](/docs/types/string.md)|Адрес почтового сервера.<br/>|
|password|False|[string](/docs/types/string.md)|Пароль для подключения к почтовому серверу.<br/>|
|email|True|[email](/docs/types/email.md)|Адрес электронной почты.<br/>|

### Резудьтат
[MailBox](/docs/types/MailBox.md)
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner
## show

### Описание метода
MailBoxes.show<br/>Возвращает данные указанного почтового ящика.<br/>Параметры<br/>Результат<br/>Объект типа «MailBox».<br/>Уровень доступа для ролей<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|fields|False|[string](/docs/types/string.md)|Список через запятую возвращаемых полей.<br/>|
|id|True|[numeric](/docs/types/numeric.md)|ID почтового ящика.<br/>|

### Резудьтат
[MailBox](/docs/types/MailBox.md)
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner
## list

### Описание метода
MailBoxes.list<br/>Возвращает список почтовых ящиков.<br/>Параметры<br/>Результат<br/>Массив объектов типа «MailBox».<br/>Уровень доступа для ролей<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|q|False|[string](/docs/types/string.md)|Критерий поиска.<br/>Доступные поля:<br/>ids – idlist, список ID почтовых ящиков.<br/>|
|fields|False|[string](/docs/types/string.md)|Список через запятую возвращаемых полей.<br/>|
|limit|False|[numeric](/docs/types/numeric.md)|По умолчанию – 50.<br/>|
|sort|False|[string](/docs/types/string.md)|Сортировка результатов.<br/>Возможные значение:<br/>created_at:d – по умолчанию.<br/>|
|offset|False|[numeric](/docs/types/numeric.md)|По умолчанию – 0.<br/>|

### Резудьтат
Array.<[MailBox](/docs/types/MailBox.md)>
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner
## update

### Описание метода
MailBoxes.update<br/>Обновляет данные указанного почтового ящика.<br/>Параметры<br/>Результат<br/>Метод ничего не возвращает.<br/>Уровень доступа для ролей<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|username|False|[string](/docs/types/string.md)|Логин для подключения к почтовому серверу.<br/>|
|is_ssl|False|[boolean](/docs/types/boolean.md)|Признак использования защищенного соединения.<br/>|
|smtp_port|False|[numeric](/docs/types/numeric.md)|Порт для подключения к почтовому серверу.<br/>Целое число в диапазоне от 1 до 65535.<br/>|
|smtp_server|False|[string](/docs/types/string.md)|Адрес почтового сервера.<br/>|
|id|True|[numeric](/docs/types/numeric.md)|ID почтового ящика.<br/>|
|password|False|[string](/docs/types/string.md)|Пароль для подключения к почтовому серверу.<br/>|
|email|False|[email](/docs/types/email.md)|Адрес электронной почты.<br/>|

### Резудьтат
None
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner
## delete

### Описание метода
MailBoxes.delete<br/>Удаляет указанный почтовый ящик.<br/>Параметры<br/>Результат<br/>Метод ничего не возвращает.<br/>Уровень доступа для ролей<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|id|True|[numeric](/docs/types/numeric.md)|ID почтового ящика.<br/>|

### Резудьтат
None
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner