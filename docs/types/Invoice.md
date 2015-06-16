
## Invoice

### Описание типа
Invoice
Счет.
Таблица 49. Поля счета


### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|comment|False|[string](/docs/types/string.md)|Текст счета (перечисление всех заказанных услуг).<br/>|
|payer|True|[Payer](/docs/types/Payer.md)|Плательщик.<br/>|
|is_paid|True|[boolean](/docs/types/boolean.md)|Признак оплаченности счета.<br/>|
|updated_at|False|[datetime](/docs/types/datetime.md)|Дата изменения.<br/>|
|number|True|[string](/docs/types/string.md)|Номер счета.<br/>|
|amount|True|[numeric](/docs/types/numeric.md)|Общая сумма счета.<br/>|
|paid_at|True|[datetime](/docs/types/datetime.md)|Дата оплаты.<br/>|
|file|True|[file](/docs/types/file.md)|Файл инвойса в формате PDF.<br/>|
|id|True|[numeric](/docs/types/numeric.md)|Внутренний ID счета.<br/>|
|order|True|[Order](/docs/types/Order.md)|Заказ.<br/>|
|created_at|False|[datetime](/docs/types/datetime.md)|Дата создания.<br/>|
