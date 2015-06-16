
## Product

### Описание типа
Продукт клиента – это приобретенный продукт (тариф, опция).<br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*begin_at*|False|[datetime](/docs/types/datetime.md)|Дата подключения.<br/>|
|*offering*|True|[Offering](/docs/types/Offering.md)|Предложение, на котором базируется этот продукт клиента.<br/>|
|*frozen_at*|False|[datetime](/docs/types/datetime.md)|Дата последней заморозки.<br/>Присутствует только для product_state = frozen.<br/>|
|*created_at*|True|[datetime](/docs/types/datetime.md)|Дата создания.<br/>|
|*id*|True|[numeric](/docs/types/numeric.md)|ID продукта клиента.<br/>|
|*amount*|True|[numeric](/docs/types/numeric.md)|Стоимость покупки в валюте плательщика.<br/>|
|*frozen_till*|False|[datetime](/docs/types/datetime.md)|Дата, до которой заморожен продукт (после этого произойдет блокировка). Присутствует только для product_state = frozen.<br/>|
|*product_state*|True|[string](/docs/types/string.md)|Статус основного продукта в периоде.<br/>Возможные значения:<br/>expired – завершен,<br/>frozen – заморожен,<br/>active – активен,<br/>waiting – ждет.<br/>|
|*expire_at*|False|[datetime](/docs/types/datetime.md)|Дата отключения.<br/>|
|*quantity*|True|[numeric](/docs/types/numeric.md)|Количество ресурсов (например, операторов).<br/>|
