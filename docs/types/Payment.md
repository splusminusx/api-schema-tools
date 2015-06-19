
## Payment

### Описание типа
Платеж.<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*comment*|True|[string](/types/string)|Комментарий.<br/>|
|*created_at*|True|[datetime](/types/datetime)|Дата создания.<br/>|
|*amount*|True|[numeric](/types/numeric)|Сумма.<br/>|
|*invoice*|False|[Invoice](/types/Invoice)|Внутренний ID инвойса, к которому относится платеж.<br/>|
|*payer*|True|[Payer](/types/Payer)|Плательщик.<br/>|
