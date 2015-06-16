
## Cart

### Описание типа
Cart<br/>Корзина.<br/>Таблица 17. Поля корзины<br/><br/>Контроллер: Carts<br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|activation_type|True|[string](/docs/types/string.md)|Тип активации.<br/>Возможные значения:	<br/>now – активация сразу после покупки;<br/>after_current – активация после завершения текущего периода;<br/>after_payment – активация после оплаты.<br/>|
|created_at|True|[datetime](/docs/types/datetime.md)|Дата создания.<br/>|
|period|True|[Period](/docs/types/Period.md)|Период.<br/>|
|cart_items|True|Array.<[CartItems](/docs/types/CartItems.md)>|Позиции корзины.<br/>|
|updated_at|True|[datetime](/docs/types/datetime.md)|Дата обновления.<br/>|
|id|True|[numeric](/docs/types/numeric.md)|ID корзины.<br/>|
