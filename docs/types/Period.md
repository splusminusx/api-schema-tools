
## Period

### Описание типа
Period
Период.
Таблица 62. Поля периода

Контроллер: Periods.

### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|vat_invoices|False|Array.<[VATInvoice](/docs/types/VATInvoice.md)>|Массив счетов-фактур.<br/>|
|carts|False|Array.<[Cart](/docs/types/Cart.md)>|Массив корзин.<br/>|
|created_at|True|None|Дата создания.<br/>|
|is_autorenewal|True|None|Признак автоматического продления.<br/>|
|updated_at|True|None|Дата последнего обновления.<br/>|
|id|True|None|ID периода.<br/>|
|invoices|False|Array.<[Invoice](/docs/types/Invoice.md)>|Массив счетов.<br/>|
|products|True|Array.<[Product](/docs/types/Product.md)>|Массив продуктов.<br/>|
|period_state|True|None|Статус периода.<br/>Возможные значения:<br/>expired – прошедший;<br/>active – активный;<br/>next – будущий.<br/>|
|acceptances|False|Array.<[Acceptance](/docs/types/Acceptance.md)>|Массив актов.<br/>|
|orders|False|Array.<[Order](/docs/types/Order.md)>|Массив заказов.<br/>|
