
## HoldRule

### Описание типа
Сценарий удержания.<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*title*|True|[string](/types/string)|Название сценария удержания.<br/>|
|*created_at*|True|[datetime](/types/datetime)|Дата и время создания.<br/>|
|*updated_at*|True|[datetime](/types/datetime)|Дата и время последнего обновления.<br/>|
|*site*|False|Array.<[Site](/types/Site)>|Массив сайтов, на которых включен сценарий удержания.<br/>|
|*transfer_after*|False|[numeric](/types/numeric)|Интервал в секундах после последнего сообщения, по истечение которого выполнить перенаправление на другого оператора, если указано is_transfer.<br/>Должен быть от 5 до 3600 секунд.<br/>Обязательно, если is_transfer = true.<br/>Принимается во внимание, только если hold_messages содержит хотя бы один элемент.<br/>|
|*is_transfer*|True|[boolean](/types/boolean)|Признак перенаправления на другого оператора после последнего сообщения.<br/>Принимается во внимание, только если hold_messages содержит хотя бы один элемент.<br/>|
|*hold_messages*|True|Array.<[HoldMessage](/types/HoldMessage)>|Массив удерживающих сообщений.<br/>От 1 до 3 элементов. <br/>|
|*id*|True|[numeric](/types/numeric)|ID сценария удержания.<br/>|
