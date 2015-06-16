
## ReportByEmailSettings

### Описание типа
ReportByEmailSettings
Настройки отправки отчетов на email.
Таблица 76. Настройки отправки отчетов на e-mail


### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|is_active|True|[boolean](/docs/types/boolean.md)|Включение/выключение отправки отчетов на email.<br/>|
|period|True|[string](/docs/types/string.md)|Периодичность.<br/>Возможные значения:<br/>daily – ежедневно;<br/>weekly – еженедельно;<br/>monthly – ежемесячно.<br/>|
|emails|False|[string](/docs/types/string.md)|Список через запятую адресов электронной почты, на которые следует отправлять отчеты.<br/>Если ни одного адреса не указано, то отчеты отправляться не будут.<br/>|
