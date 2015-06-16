
# Invoices

## Описание ресурса
Invoices<br/>
# Методы

## list

### Описание метода
Invoices.list<br/>Возвращает список выставленных счетов.<br/>Параметры<br/>Результат<br/>Массив объектов типа «Invoice».<br/>Уровень доступа для ролей<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*q*|False|[string](/docs/types/string.md)|Критерий поиска.<br/>Доступные поля:<br/>ids – idlist, список ID счетов;<br/>payer_ids – idlist, список ID плательщиков;<br/>is_bound – boolean, признак связанности счета с каким-либо периодом;<br/>is_paid – boolean, если указан, то возвращаются счета с соответствующим значением этого признака. <br/>|
|*fields*|False|[string](/docs/types/string.md)|Список через запятую возвращаемых полей.<br/>|
|*limit*|False|[numeric](/docs/types/numeric.md)|По умолчанию – 50.<br/>|
|*sort*|False|[string](/docs/types/string.md)|Сортировка результатов.<br/>Возможные значение:<br/>created_at:d – по умолчанию; <br/>paid_at:d.<br/>|
|*offset*|False|[numeric](/docs/types/numeric.md)|По умолчанию – 0.<br/>|

### Резудьтат
Array.<[Invoice](/docs/types/Invoice.md)>
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner
## show

### Описание метода
Invoices.show<br/>Возвращает данные указанного счета.<br/>Параметры<br/>Результат<br/>Объект типа «Invoice».<br/>Уровень доступа для ролей<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*fields*|False|[string](/docs/types/string.md)|Список через запятую возвращаемых полей.<br/>|
|*id*|True|[numeric](/docs/types/numeric.md)|ID счета<br/>|

### Резудьтат
[Invoice](/docs/types/Invoice.md)
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner