
## Payment

### Описание типа
Платеж.<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*comment*|True|[string](/docs/types/string.md)|Комментарий.<br/>|
|*created_at*|True|[datetime](/docs/types/datetime.md)|Дата создания.<br/>|
|*amount*|True|[numeric](/docs/types/numeric.md)|Сумма.<br/>|
|*invoice*|False|[Invoice](/docs/types/Invoice.md)|Внутренний ID инвойса, к которому относится платеж.<br/>|
|*payer*|True|[Payer](/docs/types/Payer.md)|Плательщик.<br/>|
