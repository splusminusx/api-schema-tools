
# Offerings

## Описание ресурса

# Методы

## list

### Описание метода
Возвращает список активных предложений, доступных текущему клиенту.<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*q*|False|[string](/types/string)|Критерий поиска.<br/>Доступные поля:<br/>ids – idlist, список ID предложений;<br/>cart_id – ID корзины, для которых нужно вернуть совместимые предложения;<br/>is_tariff;<br/>is_trial;<br/>resource_type;<br/>price;<br/>days.<br/>|
|*fields*|False|[string](/types/string)|Список через запятую возвращаемых полей.<br/>|
|*limit*|False|[numeric](/types/numeric)|По умолчанию – 50.<br/>|
|*sort*|False|[string](/types/string)|Сортировка результатов.<br/>Возможные значения:<br/>id:d - по умолчанию.<br/>|
|*offset*|False|[numeric](/types/numeric)|По умолчанию – 0.<br/>|

### Результат
Array.<[Offering](/types/Offering)>
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|*admin*|full||
|*manager*|none||
|*chief*|full||
|*chief_partner*|none||
|*operator*|none||
|*admin_partner*|none||

## show

### Описание метода
Возвращает данные указанного предложения.<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*fields*|False|[string](/types/string)|Список через запятую возвращаемых полей.<br/>|
|*id*|True|[numeric](/types/numeric)|ID предложения.<br/>|

### Результат
[Offering](/types/Offering)
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|*admin*|full||
|*manager*|none||
|*chief*|full||
|*chief_partner*|none||
|*operator*|none||
|*admin_partner*|none||
