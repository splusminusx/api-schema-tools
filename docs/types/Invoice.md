
## Invoice

### Описание типа
Счет.<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*comment*|False|[string](/types/string)|Текст счета (перечисление всех заказанных услуг).<br/>|
|*payer*|True|[Payer](/types/Payer)|Плательщик.<br/>|
|*is_paid*|True|[boolean](/types/boolean)|Признак оплаченности счета.<br/>|
|*updated_at*|False|[datetime](/types/datetime)|Дата изменения.<br/>|
|*number*|True|[string](/types/string)|Номер счета.<br/>|
|*amount*|True|[numeric](/types/numeric)|Общая сумма счета.<br/>|
|*paid_at*|True|[datetime](/types/datetime)|Дата оплаты.<br/>|
|*file*|True|[file](/types/file)|Файл инвойса в формате PDF.<br/>|
|*id*|True|[numeric](/types/numeric)|Внутренний ID счета.<br/>|
|*order*|True|[Order](/types/Order)|Заказ.<br/>|
|*created_at*|False|[datetime](/types/datetime)|Дата создания.<br/>|
