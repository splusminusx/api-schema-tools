
## Ticket

### Описание типа
Ticket<br/>Обращение в поддержку.<br/>Таблица 84. Поля обращения в поддержку<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|status|True|[string](/docs/types/string.md)|Статус тикета.<br/>Возможные значения:<br/>submitted – новый тикет;<br/>inprogress – в работе;<br/>w4lt – ожидает ответа технического специалиста LiveTex;<br/>w4e – ожидает ответа сотрудника;<br/>closed – закрыто.<br/>|
|text|True|[string](/docs/types/string.md)|Текст обращения в поддержку.<br/>Максимум 2000 символов.<br/>|
|created_at|True|[datetime](/docs/types/datetime.md)|Дата создания.<br/>|
|updated_at|True|[datetime](/docs/types/datetime.md)|Дата последнего обновления.<br/>|
|comments|False|Array.<[Comment](/docs/types/Comment.md)>|Массив комментариев в рамках данного тикета.<br/>|
|priority|True|[string](/docs/types/string.md)|Приоритет:<br/>Возможные значения:<br/>undefined - не определено;<br/>low – низкий;<br/>normal – обычный;<br/>high – высокий;<br/>critical – критичный.<br/>|
|employee|True|[Employee](/docs/types/Employee.md)|Сотрудник, инициировавший обращение.<br/>|
|type|True|[string](/docs/types/string.md)|Тип обращения.<br/>Возможные значения:<br/>undefined – не определено;<br/>incident – инцидент;<br/>request – запрос на обслуживание.<br/>|
|id|True|[numeric](/docs/types/numeric.md)|ID обращения в поддержку.<br/>|
|subject|False|[string](/docs/types/string.md)|Тема обращения в поддержку.<br/>|
