
## Ticket

### Описание типа
Обращение в поддержку.<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*status*|True|[string](/types/string)|Статус тикета.<br/>Возможные значения:<br/>submitted – новый тикет;<br/>inprogress – в работе;<br/>w4lt – ожидает ответа технического специалиста LiveTex;<br/>w4e – ожидает ответа сотрудника;<br/>closed – закрыто.<br/>|
|*text*|True|[string](/types/string)|Текст обращения в поддержку.<br/>Максимум 2000 символов.<br/>|
|*created_at*|True|[datetime](/types/datetime)|Дата создания.<br/>|
|*updated_at*|True|[datetime](/types/datetime)|Дата последнего обновления.<br/>|
|*comments*|False|Array.<[Comment](/types/Comment)>|Массив комментариев в рамках данного тикета.<br/>|
|*priority*|True|[string](/types/string)|Приоритет:<br/>Возможные значения:<br/>undefined - не определено;<br/>low – низкий;<br/>normal – обычный;<br/>high – высокий;<br/>critical – критичный.<br/>|
|*employee*|True|[Employee](/types/Employee)|Сотрудник, инициировавший обращение.<br/>|
|*type*|True|[string](/types/string)|Тип обращения.<br/>Возможные значения:<br/>undefined – не определено;<br/>incident – инцидент;<br/>request – запрос на обслуживание.<br/>|
|*id*|True|[numeric](/types/numeric)|ID обращения в поддержку.<br/>|
|*subject*|False|[string](/types/string)|Тема обращения в поддержку.<br/>|
