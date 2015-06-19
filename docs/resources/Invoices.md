
# Invoices

## Описание ресурса

# Методы

## list

### Описание метода
Возвращает список выставленных счетов.<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*q*|False|[string](/types/string)|Критерий поиска.<br/>Доступные поля:<br/>ids – idlist, список ID счетов;<br/>payer_ids – idlist, список ID плательщиков;<br/>is_bound – boolean, признак связанности счета с каким-либо периодом;<br/>is_paid – boolean, если указан, то возвращаются счета с соответствующим значением этого признака. <br/>|
|*fields*|False|[string](/types/string)|Список через запятую возвращаемых полей.<br/>|
|*limit*|False|[numeric](/types/numeric)|По умолчанию – 50.<br/>|
|*sort*|False|[string](/types/string)|Сортировка результатов.<br/>Возможные значение:<br/>created_at:d – по умолчанию; <br/>paid_at:d.<br/>|
|*offset*|False|[numeric](/types/numeric)|По умолчанию – 0.<br/>|

### Результат
Array.<[Invoice](/types/Invoice)>
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|*admin*|full||
|*manager*|full||
|*chief*|full||
|*chief_partner*|full||
|*operator*|none||
|*admin_partner*|full||

## show

### Описание метода
Возвращает данные указанного счета.<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*fields*|False|[string](/types/string)|Список через запятую возвращаемых полей.<br/>|
|*id*|True|[numeric](/types/numeric)|ID счета<br/>|

### Результат
[Invoice](/types/Invoice)
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|*admin*|full||
|*manager*|full||
|*chief*|full||
|*chief_partner*|full||
|*operator*|none||
|*admin_partner*|full||
