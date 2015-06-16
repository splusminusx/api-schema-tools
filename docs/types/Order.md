
## Order

### Описание типа
Order<br/>Заказ.<br/>Таблица 58. Поля заказа<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*activation_type*|True|[string](/docs/types/string.md)|Тип активации.<br/>Возможные значения:	<br/>now – активация сразу после покупки;<br/>after_current – активация после завершения текущего периода;<br/>after_payment – активация после оплаты.<br/>|
|*created_at*|True|[datetime](/docs/types/datetime.md)|Дата создания.<br/>|
|*period*|True|[Period](/docs/types/Period.md)|Период.<br/>|
|*updated_at*|True|[datetime](/docs/types/datetime.md)|Дата обновления.<br/>|
|*invoices*|False|Array.<[Invoice](/docs/types/Invoice.md)>|Массив счетов.<br/>|
|*products*|True|Array.<[Product](/docs/types/Product.md)>|Продукты заказа.<br/>|
|*id*|True|[numeric](/docs/types/numeric.md)|ID заказа.<br/>|
