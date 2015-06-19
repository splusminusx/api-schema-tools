
## Period

### Описание типа
Период.<br/><br/>Контроллер: Periods.<br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*vat_invoices*|False|Array.<[VATInvoice](/types/VATInvoice)>|Массив счетов-фактур.<br/>|
|*carts*|False|Array.<[Cart](/types/Cart)>|Массив корзин.<br/>|
|*created_at*|True|[datetime](/types/datetime)|Дата создания.<br/>|
|*is_autorenewal*|True|[boolean](/types/boolean)|Признак автоматического продления.<br/>|
|*updated_at*|True|[datetime](/types/datetime)|Дата последнего обновления.<br/>|
|*id*|True|[numeric](/types/numeric)|ID периода.<br/>|
|*invoices*|False|Array.<[Invoice](/types/Invoice)>|Массив счетов.<br/>|
|*products*|True|Array.<[Product](/types/Product)>|Массив продуктов.<br/>|
|*period_state*|True|[string](/types/string)|Статус периода.<br/>Возможные значения:<br/>expired – прошедший;<br/>active – активный;<br/>next – будущий.<br/>|
|*acceptances*|False|Array.<[Acceptance](/types/Acceptance)>|Массив актов.<br/>|
|*orders*|False|Array.<[Order](/types/Order)>|Массив заказов.<br/>|
