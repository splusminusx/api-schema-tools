
## VATInvoice

### Описание типа
Счет-фактура.<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*comment*|False|[string](/docs/types/string.md)|Текст счета (перечисление всех заказанных услуг).<br/>|
|*invoice*|True|[Invoice](/docs/types/Invoice.md)|Счет. <br/>|
|*payer*|True|[Payer](/docs/types/Payer.md)|Плательщик.<br/>|
|*created_at*|False|[datetime](/docs/types/datetime.md)|Дата создания.<br/>|
|*number*|True|[string](/docs/types/string.md)|Номер счета-фактуры.<br/>|
|*amount*|True|[numeric](/docs/types/numeric.md)|Общая сумма.<br/>|
|*file*|True|[file](/docs/types/file.md)|Файл счета-фактуры в формате PDF.<br/>|
|*id*|True|[numeric](/docs/types/numeric.md)|Внутренний ID счета.<br/>|
