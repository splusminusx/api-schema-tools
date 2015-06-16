## Product
### Описание типа
Product
Продукт клиента – это приобретенный продукт (тариф, опция).
Таблица 64. Поля продукта клиента
### Поля
| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|begin_at|False|datetime|Дата подключения.<br/>|
|offering|True|Offering|Предложение, на котором базируется этот продукт клиента.<br/>|
|frozen_at|False|datetime|Дата последней заморозки.<br/>Присутствует только для product_state = frozen.<br/>|
|created_at|True|datetime|Дата создания.<br/>|
|id|True|numeric|ID продукта клиента.<br/>|
|amount|True|numeric|Стоимость покупки в валюте плательщика.<br/>|
|frozen_till|False|datetime|Дата, до которой заморожен продукт (после этого произойдет блокировка). Присутствует только для product_state = frozen.<br/>|
|product_state|True|string|Статус основного продукта в периоде.<br/>Возможные значения:<br/>expired – завершен,<br/>frozen – заморожен,<br/>active – активен,<br/>waiting – ждет.<br/>|
|expire_at|False|datetime|Дата отключения.<br/>|
|quantity|True|numeric|Количество ресурсов (например, операторов).<br/>|
