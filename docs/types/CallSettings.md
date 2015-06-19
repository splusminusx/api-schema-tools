
## CallSettings

### Описание типа
Настройки функциональности звонков.<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*is_forward*|True|[boolean](/types/boolean)|Включение/выключение переадресации.<br/>|
|*is_active*|True|[boolean](/types/boolean)|Включение/выключение функциональности звонков.<br/>|
|*forward_sip_host*|False|[string](/types/string)|Имя хоста SIP.<br/>Обязательно при forward_type=SIP и is_forward=true.<br/>|
|*forward_sip_login*|False|[string](/types/string)|Логин для подключения по SIP.<br/>Обязательно при forward_type=SIP и is_forward=true.<br/>|
|*forward_sip_password*|False|[string](/types/string)|Пароль для подключения по SIP.<br/>Обязательно при forward_type=SIP и is_forward=true.<br/>|
|*forward_type*|True|[string](/types/string)|Тип переадресации.<br/>Возможные значения:<br/>sip – переадресация на SIP;<br/>phone – переадресация на телефон.<br/>|
