
# Offerings

## Описание ресурса
Offerings<br/>
# Методы

## list

### Описание метода
Offerings.list<br/>Возвращает список активных предложений, доступных текущему клиенту.<br/>Параметры<br/>Результат<br/>Массив объектов типа «Offering».<br/>Уровень доступа для ролей<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|q|False|[string](/docs/types/string.md)|Критерий поиска.<br/>Доступные поля:<br/>ids – idlist, список ID предложений;<br/>cart_id – ID корзины, для которых нужно вернуть совместимые предложения;<br/>is_tariff;<br/>is_trial;<br/>resource_type;<br/>price;<br/>days.<br/>|
|fields|False|[string](/docs/types/string.md)|Список через запятую возвращаемых полей.<br/>|
|limit|False|[numeric](/docs/types/numeric.md)|По умолчанию – 50.<br/>|
|sort|False|[string](/docs/types/string.md)|Сортировка результатов.<br/>Возможные значения:<br/>id:d - по умолчанию.<br/>|
|offset|False|[numeric](/docs/types/numeric.md)|По умолчанию – 0.<br/>|

### Резудьтат
Array.<[Offering](/docs/types/Offering.md)>
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner
## show

### Описание метода
Offerings.show<br/>Возвращает данные указанного предложения.<br/>Параметры<br/>Результат<br/>Объект типа «Offering».<br/>Уровень доступа для ролей<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|fields|False|[string](/docs/types/string.md)|Список через запятую возвращаемых полей.<br/>|
|id|True|[numeric](/docs/types/numeric.md)|ID предложения.<br/>|

### Резудьтат
[Offering](/docs/types/Offering.md)
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner