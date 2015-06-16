
## Document

### Описание типа
Document<br/>Документ. Документом является акт, счет и счет-фактура. <br/>Таблица 35. Поля документа<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|comment|False|[string](/docs/types/string.md)|Описание документа<br/>|
|doc_type|True|[string](/docs/types/string.md)|Тип документа.<br/>Возможные значения:<br/>acceptance – акт;<br/>invoice – счет;<br/>vatinvoice – счет-фактура.<br/>|
|is_paid|True|[boolean](/docs/types/boolean.md)|Признак оплаченности счета.<br/>Актуален только для документов с doc_type = invoice. Для других типов документов всегда false.<br/>|
|number|True|[string](/docs/types/string.md)|Номер документа. Уникален в пределах типа документа (doc_type).<br/>|
|amount|True|[numeric](/docs/types/numeric.md)|Сумма, связанная с документом.<br/>|
|file|True|[file](/docs/types/file.md)|Файл документа в формате PDF.<br/>|
|doc_id|True|[numeric](/docs/types/numeric.md)|ID объекта, соответствующего типу документа (doc_type). <br/>Например, для doc_type = acceptance в этом поле будет ID объекта сущности Acceptance.<br/>|
|created_at|True|[datetime](/docs/types/datetime.md)|Дата создания.<br/>|
