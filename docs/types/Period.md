
## Period

### Описание типа
Period<br/>Период.<br/>Таблица 62. Поля периода<br/><br/>Контроллер: Periods.<br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*vat_invoices*|False|Array.<[VATInvoice](/docs/types/VATInvoice.md)>|Массив счетов-фактур.<br/>|
|*carts*|False|Array.<[Cart](/docs/types/Cart.md)>|Массив корзин.<br/>|
|*created_at*|True|[datetime](/docs/types/datetime.md)|Дата создания.<br/>|
|*is_autorenewal*|True|[boolean](/docs/types/boolean.md)|Признак автоматического продления.<br/>|
|*updated_at*|True|[datetime](/docs/types/datetime.md)|Дата последнего обновления.<br/>|
|*id*|True|[numeric](/docs/types/numeric.md)|ID периода.<br/>|
|*invoices*|False|Array.<[Invoice](/docs/types/Invoice.md)>|Массив счетов.<br/>|
|*products*|True|Array.<[Product](/docs/types/Product.md)>|Массив продуктов.<br/>|
|*period_state*|True|[string](/docs/types/string.md)|Статус периода.<br/>Возможные значения:<br/>expired – прошедший;<br/>active – активный;<br/>next – будущий.<br/>|
|*acceptances*|False|Array.<[Acceptance](/docs/types/Acceptance.md)>|Массив актов.<br/>|
|*orders*|False|Array.<[Order](/docs/types/Order.md)>|Массив заказов.<br/>|
