
## ConversationEvent

### Описание типа
ConversationEvent
Событие, произошедшее в течение обращения посетителя.
Таблица 31. Поля события обращения


### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|event_text|True|[string](/docs/types/string.md)|Описание события. Например:<br/>"Иван Петрович начал переписку с оператором Егор Климов"<br/>|
|employee|False|[Employee](/docs/types/Employee.md)|Оператор.<br/>Присутствует для тех типов событий, для которых это имеет смысл.<br/>|
|created_at|True|[datetime](/docs/types/datetime.md)|Дата и время события.<br/>|
|event_type|True|[string](/docs/types/string.md)|Тип события.<br/>Возможные значения:<br/>cobrowse-activation-refuse – посетитель отказался от использования функции "Виртуальный ассистент";<br/>cobrowse-activation-request – оператор послал запрос на активацию функции "Виртуальный ассистент";<br/>cobrowse-activation-timeout - превышен лимит ожидания ответа на активацию модуля "Виртуальный ассистент";<br/>cobrowse-member-close – оператор завершил использование функции "Виртуальный ассистент";<br/>cobrowse-member-refuse – оператор завершил использование функции "Виртуальный ассистент" до того, как посетитель ответил на запрос;<br/>cobrowse-redirect – оператор перенаправил посетителя на другую страницу;<br/>cobrowse-select – оператор выделил области на странице;<br/>cobrowse-start – посетитель принял запрос на использование функции "Виртуальный ассистент";<br/>cobrowse-visitor-close – посетитель закрыл активную вкладку или вышел из чата;<br/>file-upload-to-storage-start – начата загрузка файла в хранилище;<br/>file-get-upload-url – отправитель инициировал процедуру отправки файла;<br/>file-download-from-storage-start – начато скачивание файла из хранилища;<br/>file-download-from-storage-complete – завершено скачивание файла из хранилища;<br/>file-ready-to-download – файл загружен в хранилище и готов к скачиванию;<br/>visitor-call-end – посетитель завершил звонок;<br/>visitor-call-start – посетитель инициировал звонок;<br/>visitor-chat-close – посетитель закрыл чат;<br/>visitor-chat-move – выполнена передача чата;<br/>visitor-chat-open – посетитель начал переписку с оператором;<br/>visitor-chat-reopen – посетитель переоткрыл чат;<br/>vistor-navigate – посетитель перешел на другую страницу.<br/>|
|page|False|[string](/docs/types/string.md)|Адрес страницы.<br/>Присутствует для тех типов событий, для которых это имеет смысл.<br/>|
