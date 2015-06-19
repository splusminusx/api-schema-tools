
## VATInvoice

### Описание типа
Счет-фактура.<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*comment*|False|[string](/types/string)|Текст счета (перечисление всех заказанных услуг).<br/>|
|*invoice*|True|[Invoice](/types/Invoice)|Счет. <br/>|
|*payer*|True|[Payer](/types/Payer)|Плательщик.<br/>|
|*created_at*|False|[datetime](/types/datetime)|Дата создания.<br/>|
|*number*|True|[string](/types/string)|Номер счета-фактуры.<br/>|
|*amount*|True|[numeric](/types/numeric)|Общая сумма.<br/>|
|*file*|True|[file](/types/file)|Файл счета-фактуры в формате PDF.<br/>|
|*id*|True|[numeric](/types/numeric)|Внутренний ID счета.<br/>|
