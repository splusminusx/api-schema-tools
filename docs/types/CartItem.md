
## CartItem

### Описание типа
CartItem<br/>Позиция корзины.<br/>Таблица 18. Поля позиции корзины<br/><br/>Контроллер: CartItems.<br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*created_at*|True|[datetime](/docs/types/datetime.md)|Дата создания.<br/>|
|*quantity*|True|[numeric](/docs/types/numeric.md)|Количество ресурсов (например, операторов).<br/>|
|*amount*|True|[numeric](/docs/types/numeric.md)|Стоимость.<br/>|
|*offering*|True|[Offering](/docs/types/Offering.md)|Предложение.<br/>|
|*id*|True|[numeric](/docs/types/numeric.md)|ID позиции.<br/>|
