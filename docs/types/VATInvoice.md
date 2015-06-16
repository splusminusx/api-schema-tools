## VATInvoice
### Описание типа
VATInvoice
Счет-фактура.
Таблица 86. Поля счета

### Поля
| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|comment|False|string|Текст счета (перечисление всех заказанных услуг).<br/>|
|invoice|True|Invoice|Счет. <br/>|
|payer|True|Payer|Плательщик.<br/>|
|created_at|False|datetime|Дата создания.<br/>|
|number|True|string|Номер счета-фактуры.<br/>|
|amount|True|numeric|Общая сумма.<br/>|
|file|True|file|Файл счета-фактуры в формате PDF.<br/>|
|id|True|numeric|Внутренний ID счета.<br/>|
