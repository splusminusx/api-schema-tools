
# VATInvoices

## Описание ресурса
VATInvoices

# Методы

## list

### Описание метода
VATInvoices.list
Возвращает список счетов-фактур.
Параметры
Результат
Массив объектов типа «VATInvoice».
Уровень доступа для ролей


### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|q|False|string|Критерий поиска.<br/>Доступные поля:<br/>ids – idlist, список ID счетов-фактур;<br/>is_bound – boolean, признак связанности счета-фактуры с каким-либо периодом;<br/>payer_ids – idlist, список ID плательщиков. <br/>|
|fields|False|string|Список через запятую возвращаемых полей.<br/>|
|limit|False|numeric|По умолчанию – 50.<br/>|
|sort|False|string|Сортировка результатов.<br/>Возможные значение:<br/>created_at:d – по умолчанию.<br/>|
|offset|False|numeric|По умолчанию – 0.<br/>|

### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner