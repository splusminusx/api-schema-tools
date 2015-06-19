
## Product

### Описание типа
Продукт клиента – это приобретенный продукт (тариф, опция).<br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*begin_at*|False|[datetime](/types/datetime)|Дата подключения.<br/>|
|*offering*|True|[Offering](/types/Offering)|Предложение, на котором базируется этот продукт клиента.<br/>|
|*frozen_at*|False|[datetime](/types/datetime)|Дата последней заморозки.<br/>Присутствует только для product_state = frozen.<br/>|
|*created_at*|True|[datetime](/types/datetime)|Дата создания.<br/>|
|*id*|True|[numeric](/types/numeric)|ID продукта клиента.<br/>|
|*amount*|True|[numeric](/types/numeric)|Стоимость покупки в валюте плательщика.<br/>|
|*frozen_till*|False|[datetime](/types/datetime)|Дата, до которой заморожен продукт (после этого произойдет блокировка). Присутствует только для product_state = frozen.<br/>|
|*product_state*|True|[string](/types/string)|Статус основного продукта в периоде.<br/>Возможные значения:<br/>expired – завершен,<br/>frozen – заморожен,<br/>active – активен,<br/>waiting – ждет.<br/>|
|*expire_at*|False|[datetime](/types/datetime)|Дата отключения.<br/>|
|*quantity*|True|[numeric](/types/numeric)|Количество ресурсов (например, операторов).<br/>|
