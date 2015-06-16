
## Invoice

### Описание типа
Invoice
Счет.
Таблица 49. Поля счета


### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|comment|False|None|Текст счета (перечисление всех заказанных услуг).<br/>|
|payer|True|None|Плательщик.<br/>|
|is_paid|True|None|Признак оплаченности счета.<br/>|
|updated_at|False|None|Дата изменения.<br/>|
|number|True|None|Номер счета.<br/>|
|amount|True|None|Общая сумма счета.<br/>|
|paid_at|True|None|Дата оплаты.<br/>|
|file|True|None|Файл инвойса в формате PDF.<br/>|
|id|True|None|Внутренний ID счета.<br/>|
|order|True|None|Заказ.<br/>|
|created_at|False|None|Дата создания.<br/>|
