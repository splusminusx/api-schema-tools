
# Products

## Описание ресурса
Products

# Методы

## list

### Описание метода
Products.list
Возвращает список продуктов клиента, в том числе и ранее подключенных, если они есть в базе.
Параметры
Результат
Массив объектов типа «Product».
Уровень доступа для ролей


### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|q|False|[string](/docs/types/string.md)|Критерий поиска.<br/>Доступные поля:<br/>ids – idlist, список ID продуктов;<br/>product_state – enum, статус продукта.<br/>|
|fields|False|[string](/docs/types/string.md)|Список через запятую возвращаемых полей.<br/>|
|limit|False|[numeric](/docs/types/numeric.md)|По умолчанию – 50.<br/>|
|sort|False|[string](/docs/types/string.md)|Сортировка результатов.<br/>Возможные значения:<br/>created_at:d – по умолчанию.<br/>|
|offset|False|[numeric](/docs/types/numeric.md)|По умолчанию – 0.<br/>|

### Резудьтат
Array.<[Product](/docs/types/Product.md)>
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner
## show

### Описание метода
Products.show
Возвращает данные указанного продукта клиента.
Параметры
Результат
Объект типа «Product».
Уровень доступа для ролей


### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|fields|False|[string](/docs/types/string.md)|Список через запятую возвращаемых полей.<br/>|
|id|True|[numeric](/docs/types/numeric.md)|ID продукта.<br/>|

### Резудьтат
[Product](/docs/types/Product.md)
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner