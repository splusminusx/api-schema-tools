
## Ticket

### Описание типа
Ticket
Обращение в поддержку.
Таблица 84. Поля обращения в поддержку


### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|status|True|None|Статус тикета.<br/>Возможные значения:<br/>submitted – новый тикет;<br/>inprogress – в работе;<br/>w4lt – ожидает ответа технического специалиста LiveTex;<br/>w4e – ожидает ответа сотрудника;<br/>closed – закрыто.<br/>|
|text|True|None|Текст обращения в поддержку.<br/>Максимум 2000 символов.<br/>|
|created_at|True|None|Дата создания.<br/>|
|updated_at|True|None|Дата последнего обновления.<br/>|
|comments|False|Array.<[Comment](/docs/types/Comment.md)>|Массив комментариев в рамках данного тикета.<br/>|
|priority|True|None|Приоритет:<br/>Возможные значения:<br/>undefined - не определено;<br/>low – низкий;<br/>normal – обычный;<br/>high – высокий;<br/>critical – критичный.<br/>|
|employee|True|None|Сотрудник, инициировавший обращение.<br/>|
|type|True|None|Тип обращения.<br/>Возможные значения:<br/>undefined – не определено;<br/>incident – инцидент;<br/>request – запрос на обслуживание.<br/>|
|id|True|None|ID обращения в поддержку.<br/>|
|subject|False|None|Тема обращения в поддержку.<br/>|
