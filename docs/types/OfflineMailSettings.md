
## OfflineMailSettings

### Описание типа
OfflineMailSettings<br/>Настройки механизмов отправки нотификаций о приходе новых лидов и отправки ответов посетителям.<br/>Таблица 57. Настройки офлайн переписки<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|subject|True|[string](/docs/types/string.md)|Тема письма.<br/>Максимум 60 символов.<br/>|
|from_name|False|[string](/docs/types/string.md)|Отправитель.<br/>Максимум 60 символов.<br/>|
|is_active|True|[boolean](/docs/types/boolean.md)|Включение/выключение использования внешних почтовых ящиков.<br/>Если функция выключена, то письма будут отправляться через сервера LiveTex c системными значениями отправителя, темы и подписи.<br/>|
|mailbox|True|[MailBox](/docs/types/MailBox.md)|Почтовый ящик.<br/>|
|signature|False|[string](/docs/types/string.md)|Подпись.<br/>Максимум 60 символов.<br/>|
