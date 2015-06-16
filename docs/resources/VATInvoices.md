
# VATInvoices

## Описание ресурса

# Методы

## list

### Описание метода
Возвращает список счетов-фактур.<br/>Массив объектов типа «VATInvoice».<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*q*|False|[string](/docs/types/string.md)|Критерий поиска.<br/>Доступные поля:<br/>ids – idlist, список ID счетов-фактур;<br/>is_bound – boolean, признак связанности счета-фактуры с каким-либо периодом;<br/>payer_ids – idlist, список ID плательщиков. <br/>|
|*fields*|False|[string](/docs/types/string.md)|Список через запятую возвращаемых полей.<br/>|
|*limit*|False|[numeric](/docs/types/numeric.md)|По умолчанию – 50.<br/>|
|*sort*|False|[string](/docs/types/string.md)|Сортировка результатов.<br/>Возможные значение:<br/>created_at:d – по умолчанию.<br/>|
|*offset*|False|[numeric](/docs/types/numeric.md)|По умолчанию – 0.<br/>|

### Результат
Array.<[VATInvoice](/docs/types/VATInvoice.md)>
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|full||
|manager|none||
|chief|full||
|chief_partner|none||
|operator|none||
|admin_partner|none||
