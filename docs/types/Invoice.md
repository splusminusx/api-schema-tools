## Invoice
### Описание типа
Invoice
Счет.
Таблица 49. Поля счета

### Поля
| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|comment|False|string|Текст счета (перечисление всех заказанных услуг).<br/>|
|payer|True|Payer|Плательщик.<br/>|
|is_paid|True|boolean|Признак оплаченности счета.<br/>|
|updated_at|False|datetime|Дата изменения.<br/>|
|number|True|string|Номер счета.<br/>|
|amount|True|numeric|Общая сумма счета.<br/>|
|paid_at|True|datetime|Дата оплаты.<br/>|
|file|True|file|Файл инвойса в формате PDF.<br/>|
|id|True|numeric|Внутренний ID счета.<br/>|
|order|True|Order|Заказ.<br/>|
|created_at|False|datetime|Дата создания.<br/>|
