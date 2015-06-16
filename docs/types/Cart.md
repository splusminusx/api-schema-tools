
## Cart

### Описание типа
Cart
Корзина.
Таблица 17. Поля корзины

Контроллер: Carts

### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|activation_type|True|string|Тип активации.<br/>Возможные значения:	<br/>now – активация сразу после покупки;<br/>after_current – активация после завершения текущего периода;<br/>after_payment – активация после оплаты.<br/>|
|created_at|True|datetime|Дата создания.<br/>|
|period|True|Period|Период.<br/>|
|cart_items|True|Array.<[CartItems](/docs/types/CartItems.md)>|Позиции корзины.<br/>|
|updated_at|True|datetime|Дата обновления.<br/>|
|id|True|numeric|ID корзины.<br/>|
