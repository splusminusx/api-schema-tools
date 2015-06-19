
## Document

### Описание типа
Документ. Документом является акт, счет и счет-фактура. <br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*comment*|False|[string](/types/string)|Описание документа<br/>|
|*doc_type*|True|[string](/types/string)|Тип документа.<br/>Возможные значения:<br/>acceptance – акт;<br/>invoice – счет;<br/>vatinvoice – счет-фактура.<br/>|
|*is_paid*|True|[boolean](/types/boolean)|Признак оплаченности счета.<br/>Актуален только для документов с doc_type = invoice. Для других типов документов всегда false.<br/>|
|*number*|True|[string](/types/string)|Номер документа. Уникален в пределах типа документа (doc_type).<br/>|
|*amount*|True|[numeric](/types/numeric)|Сумма, связанная с документом.<br/>|
|*file*|True|[file](/types/file)|Файл документа в формате PDF.<br/>|
|*doc_id*|True|[numeric](/types/numeric)|ID объекта, соответствующего типу документа (doc_type). <br/>Например, для doc_type = acceptance в этом поле будет ID объекта сущности Acceptance.<br/>|
|*created_at*|True|[datetime](/types/datetime)|Дата создания.<br/>|
