## Order
### Описание типа
Order
Заказ.
Таблица 58. Поля заказа

### Поля
| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|activation_type|True|string|Тип активации.<br/>Возможные значения:	<br/>now – активация сразу после покупки;<br/>after_current – активация после завершения текущего периода;<br/>after_payment – активация после оплаты.<br/>|
|created_at|True|datetime|Дата создания.<br/>|
|period|True|Period|Период.<br/>|
|updated_at|True|datetime|Дата обновления.<br/>|
|invoices|False|Array.<Invoice>|Массив счетов.<br/>|
|products|True|Array.<Product>|Продукты заказа.<br/>|
|id|True|numeric|ID заказа.<br/>|
