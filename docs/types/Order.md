
## Order

### Описание типа
Заказ.<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*activation_type*|True|[string](/types/string)|Тип активации.<br/>Возможные значения:	<br/>now – активация сразу после покупки;<br/>after_current – активация после завершения текущего периода;<br/>after_payment – активация после оплаты.<br/>|
|*created_at*|True|[datetime](/types/datetime)|Дата создания.<br/>|
|*period*|True|[Period](/types/Period)|Период.<br/>|
|*updated_at*|True|[datetime](/types/datetime)|Дата обновления.<br/>|
|*invoices*|False|Array.<[Invoice](/types/Invoice)>|Массив счетов.<br/>|
|*products*|True|Array.<[Product](/types/Product)>|Продукты заказа.<br/>|
|*id*|True|[numeric](/types/numeric)|ID заказа.<br/>|
