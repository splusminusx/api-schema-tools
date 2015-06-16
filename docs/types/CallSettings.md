
## CallSettings

### Описание типа
CallSettings
Настройки функциональности звонков.
Таблица 16. Поля настроек функциональности звонков.


### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|is_forward|True|None|Включение/выключение переадресации.<br/>|
|is_active|True|None|Включение/выключение функциональности звонков.<br/>|
|forward_sip_host|False|None|Имя хоста SIP.<br/>Обязательно при forward_type=SIP и is_forward=true.<br/>|
|forward_sip_login|False|None|Логин для подключения по SIP.<br/>Обязательно при forward_type=SIP и is_forward=true.<br/>|
|forward_sip_password|False|None|Пароль для подключения по SIP.<br/>Обязательно при forward_type=SIP и is_forward=true.<br/>|
|forward_type|True|None|Тип переадресации.<br/>Возможные значения:<br/>sip – переадресация на SIP;<br/>phone – переадресация на телефон.<br/>|
