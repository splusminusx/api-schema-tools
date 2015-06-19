
# MailBoxes

## Описание ресурса

# Методы

## add

### Описание метода
Добавляет новый почтовый ящик.<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*username*|False|[string](/types/string)|Логин для подключения к почтовому серверу.<br/>|
|*is_ssl*|False|[boolean](/types/boolean)|Признак использования защищенного соединения.<br/>По умолчанию - false.<br/>|
|*smtp_port*|False|[numeric](/types/numeric)|Порт для подключения к почтовому серверу.<br/>По умолчанию - 25.<br/>Целое число в диапазоне от 1 до 65535.<br/>|
|*smtp_server*|True|[string](/types/string)|Адрес почтового сервера.<br/>|
|*password*|False|[string](/types/string)|Пароль для подключения к почтовому серверу.<br/>|
|*email*|True|[email](/types/email)|Адрес электронной почты.<br/>|

### Результат
[MailBox](/types/MailBox)
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|*admin*|full||
|*manager*|full||
|*chief*|full||
|*chief_partner*|full||
|*operator*|none||
|*admin_partner*|full||

## show

### Описание метода
Возвращает данные указанного почтового ящика.<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*fields*|False|[string](/types/string)|Список через запятую возвращаемых полей.<br/>|
|*id*|True|[numeric](/types/numeric)|ID почтового ящика.<br/>|

### Результат
[MailBox](/types/MailBox)
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
Возвращает список почтовых ящиков.<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*q*|False|[string](/types/string)|Критерий поиска.<br/>Доступные поля:<br/>ids – idlist, список ID почтовых ящиков.<br/>|
|*fields*|False|[string](/types/string)|Список через запятую возвращаемых полей.<br/>|
|*limit*|False|[numeric](/types/numeric)|По умолчанию – 50.<br/>|
|*sort*|False|[string](/types/string)|Сортировка результатов.<br/>Возможные значение:<br/>created_at:d – по умолчанию.<br/>|
|*offset*|False|[numeric](/types/numeric)|По умолчанию – 0.<br/>|

### Результат
Array.<[MailBox](/types/MailBox)>
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|*admin*|full||
|*manager*|full||
|*chief*|full||
|*chief_partner*|full||
|*operator*|full||
|*admin_partner*|full||

## update

### Описание метода
Обновляет данные указанного почтового ящика.<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*username*|False|[string](/types/string)|Логин для подключения к почтовому серверу.<br/>|
|*is_ssl*|False|[boolean](/types/boolean)|Признак использования защищенного соединения.<br/>|
|*smtp_port*|False|[numeric](/types/numeric)|Порт для подключения к почтовому серверу.<br/>Целое число в диапазоне от 1 до 65535.<br/>|
|*smtp_server*|False|[string](/types/string)|Адрес почтового сервера.<br/>|
|*id*|True|[numeric](/types/numeric)|ID почтового ящика.<br/>|
|*password*|False|[string](/types/string)|Пароль для подключения к почтовому серверу.<br/>|
|*email*|False|[email](/types/email)|Адрес электронной почты.<br/>|

### Результат
None
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|*admin*|full||
|*manager*|full||
|*chief*|full||
|*chief_partner*|full||
|*operator*|none||
|*admin_partner*|full||

## delete

### Описание метода
Удаляет указанный почтовый ящик.<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*id*|True|[numeric](/types/numeric)|ID почтового ящика.<br/>|

### Результат
None
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|*admin*|full||
|*manager*|full||
|*chief*|full||
|*chief_partner*|full||
|*operator*|none||
|*admin_partner*|full||
