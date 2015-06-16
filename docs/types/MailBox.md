
## MailBox

### Описание типа
MailBox<br/>Почтовый ящик.<br/>Почтовые ящики используются для нотификации сотрудников о поступлении нового лида и отправки ответа сотрудника посетителю.<br/>Таблица 53. Поля почтового ящика<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*username*|False|[string](/docs/types/string.md)|Логин для подключения к почтовому серверу.<br/>|
|*is_ssl*|True|[boolean](/docs/types/boolean.md)|Признак использования защищенного соединения.<br/>|
|*smtp_port*|True|[numeric](/docs/types/numeric.md)|Порт для подключения к почтовому серверу.<br/>По умолчанию - 25.<br/>Целое число в диапазоне от 1 до 65535.<br/>|
|*smtp_server*|True|[string](/docs/types/string.md)|Адрес почтового сервера.<br/>|
|*id*|True|[numeric](/docs/types/numeric.md)|ID почтового ящика.<br/>|
|*password*|False|[string](/docs/types/string.md)|Пароль для подключения к почтовому серверу.<br/>|
|*email*|True|[email](/docs/types/email.md)|Адрес электронной почты.<br/>|
