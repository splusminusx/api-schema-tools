
## HoldRule

### Описание типа
Сценарий удержания.<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*title*|True|[string](/docs/types/string.md)|Название сценария удержания.<br/>|
|*created_at*|True|[datetime](/docs/types/datetime.md)|Дата и время создания.<br/>|
|*updated_at*|True|[datetime](/docs/types/datetime.md)|Дата и время последнего обновления.<br/>|
|*site*|False|Array.<[Site](/docs/types/Site.md)>|Массив сайтов, на которых включен сценарий удержания.<br/>|
|*transfer_after*|False|[numeric](/docs/types/numeric.md)|Интервал в секундах после последнего сообщения, по истечение которого выполнить перенаправление на другого оператора, если указано is_transfer.<br/>Должен быть от 5 до 3600 секунд.<br/>Обязательно, если is_transfer = true.<br/>Принимается во внимание, только если hold_messages содержит хотя бы один элемент.<br/>|
|*is_transfer*|True|[boolean](/docs/types/boolean.md)|Признак перенаправления на другого оператора после последнего сообщения.<br/>Принимается во внимание, только если hold_messages содержит хотя бы один элемент.<br/>|
|*hold_messages*|True|Array.<[HoldMessage](/docs/types/HoldMessage.md)>|Массив удерживающих сообщений.<br/>От 1 до 3 элементов. <br/>|
|*id*|True|[numeric](/docs/types/numeric.md)|ID сценария удержания.<br/>|
