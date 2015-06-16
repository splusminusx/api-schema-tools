
## CartItem

### Описание типа
CartItem
Позиция корзины.
Таблица 18. Поля позиции корзины

Контроллер: CartItems.

### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|created_at|True|[datetime](/docs/types/datetime.md)|Дата создания.<br/>|
|quantity|True|[numeric](/docs/types/numeric.md)|Количество ресурсов (например, операторов).<br/>|
|amount|True|[numeric](/docs/types/numeric.md)|Стоимость.<br/>|
|offering|True|[Offering](/docs/types/Offering.md)|Предложение.<br/>|
|id|True|[numeric](/docs/types/numeric.md)|ID позиции.<br/>|
