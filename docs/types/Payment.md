## Payment
### Описание типа
- Payment
Платеж.
Таблица 61. Поля платежа

### Поля
| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|comment|True|string|Комментарий.<br/>|
|created_at|True|datetime|Дата создания.<br/>|
|amount|True|numeric|Сумма.<br/>|
|invoice|False|Invoice|Внутренний ID инвойса, к которому относится платеж.<br/>|
|payer|True|Payer|Плательщик.<br/>|
