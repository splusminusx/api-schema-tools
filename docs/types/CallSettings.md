
## CallSettings

### Описание типа
CallSettings
Настройки функциональности звонков.
Таблица 16. Поля настроек функциональности звонков.


### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|is_forward|True|boolean|Включение/выключение переадресации.<br/>|
|is_active|True|boolean|Включение/выключение функциональности звонков.<br/>|
|forward_sip_host|False|string|Имя хоста SIP.<br/>Обязательно при forward_type=SIP и is_forward=true.<br/>|
|forward_sip_login|False|string|Логин для подключения по SIP.<br/>Обязательно при forward_type=SIP и is_forward=true.<br/>|
|forward_sip_password|False|string|Пароль для подключения по SIP.<br/>Обязательно при forward_type=SIP и is_forward=true.<br/>|
|forward_type|True|string|Тип переадресации.<br/>Возможные значения:<br/>sip – переадресация на SIP;<br/>phone – переадресация на телефон.<br/>|
