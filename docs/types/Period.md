## Period
### Описание типа
Period
Период.
Таблица 62. Поля периода

Контроллер: Periods.
### Поля
| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|vat_invoices|False|Array.<VATInvoice>|Массив счетов-фактур.<br/>|
|carts|False|Array.<Cart>|Массив корзин.<br/>|
|created_at|True|datetime|Дата создания.<br/>|
|is_autorenewal|True|boolean|Признак автоматического продления.<br/>|
|updated_at|True|datetime|Дата последнего обновления.<br/>|
|id|True|numeric|ID периода.<br/>|
|invoices|False|Array.<Invoice>|Массив счетов.<br/>|
|products|True|Array.<Product>|Массив продуктов.<br/>|
|period_state|True|string|Статус периода.<br/>Возможные значения:<br/>expired – прошедший;<br/>active – активный;<br/>next – будущий.<br/>|
|acceptances|False|Array.<Acceptance>|Массив актов.<br/>|
|orders|False|Array.<Order>|Массив заказов.<br/>|
