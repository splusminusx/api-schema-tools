## Document
### Описание типа
Document
Документ. Документом является акт, счет и счет-фактура. 
Таблица 35. Поля документа

### Поля
| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|comment|False|string|Описание документа<br/>|
|doc_type|True|string|Тип документа.<br/>Возможные значения:<br/>acceptance – акт;<br/>invoice – счет;<br/>vatinvoice – счет-фактура.<br/>|
|is_paid|True|boolean|Признак оплаченности счета.<br/>Актуален только для документов с doc_type = invoice. Для других типов документов всегда false.<br/>|
|number|True|string|Номер документа. Уникален в пределах типа документа (doc_type).<br/>|
|amount|True|numeric|Сумма, связанная с документом.<br/>|
|file|True|file|Файл документа в формате PDF.<br/>|
|doc_id|True|numeric|ID объекта, соответствующего типу документа (doc_type). <br/>Например, для doc_type = acceptance в этом поле будет ID объекта сущности Acceptance.<br/>|
|created_at|True|datetime|Дата создания.<br/>|
