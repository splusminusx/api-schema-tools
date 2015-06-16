
# Carts

## Описание ресурса

# Методы

## addToPeriod

### Описание метода
Создает новую корзину в указанном периоде.<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*activation_type*|False|[string](/docs/types/string.md)|Тип активации.<br/>Возможные значения:<br/>now – активация сразу после покупки (по умолчанию);<br/>after_current – активация после завершения текущего периода;<br/>after_payment – активация после оплаты.<br/>|
|*period_id*|True|[numeric](/docs/types/numeric.md)|ID периода.<br/>|

### Результат
[Cart](/docs/types/Cart.md)
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
Возвращает данные указанной корзины.<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*fields*|False|[string](/docs/types/string.md)|Список через запятую возвращаемых полей.<br/>|
|*id*|True|[numeric](/docs/types/numeric.md)|ID корзины.<br/>|

### Результат
[Cart](/docs/types/Cart.md)
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|*admin*|full||
|*manager*|none||
|*chief*|full||
|*chief_partner*|none||
|*operator*|none||
|*admin_partner*|none||

## list

### Описание метода
Возвращает список корзин.<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*q*|False|[string](/docs/types/string.md)|Критерий поиска.<br/>Доступные поля:<br/>ids – idlist, список ID корзин.<br/>|
|*fields*|False|[string](/docs/types/string.md)|Список через запятую возвращаемых полей.<br/>|
|*limit*|False|[numeric](/docs/types/numeric.md)|По умолчанию – 50.<br/>|
|*sort*|False|[string](/docs/types/string.md)|Сортировка результатов.<br/>Возможные значения:<br/>created_at:d – по умолчанию.<br/>|
|*offset*|False|[numeric](/docs/types/numeric.md)|По умолчанию – 0.<br/>|

### Результат
Array.<[Cart](/docs/types/Cart.md)>
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|*admin*|full||
|*manager*|none||
|*chief*|full||
|*chief_partner*|none||
|*operator*|none||
|*admin_partner*|none||

## update

### Описание метода
Изменяет указанную корзину.<br/><br/><br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*activation_type*|False|[string](/docs/types/string.md)|Тип активации.<br/>Возможные значения:<br/>now – активация сразу после покупки;<br/>after_current – активация после завершения текущего периода;<br/>after_payment – активация после оплаты.<br/>|
|*id*|True|[numeric](/docs/types/numeric.md)|ID корзины.<br/>|

### Результат
None
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|*admin*|full||
|*manager*|none||
|*chief*|full||
|*chief_partner*|none||
|*operator*|none||
|*admin_partner*|none||

## add

### Описание метода
Создает новую корзину.<br/><br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*activation_type*|False|[string](/docs/types/string.md)|Тип активации.<br/>Возможные значения:<br/>now – активация сразу после покупки (по умолчанию);<br/>after_current – активация после завершения текущего периода;<br/>after_payment – активация после оплаты.<br/>|
|*is_current_period*|False|[boolean](/docs/types/boolean.md)|Признак текущего периода.<br/>Если true (по умолчанию), то корзина создается для текущего периода. <br/>Если false, то будет создан новый период.<br/>|

### Результат
[Cart](/docs/types/Cart.md)
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|*admin*|full||
|*manager*|none||
|*chief*|full||
|*chief_partner*|none||
|*operator*|none||
|*admin_partner*|none||

## commit

### Описание метода
Операция покупки позиций указанной корзины.<br/>Метод создает заказ, выставляет счет на оплату на активного плательщика и удаляет корзину. <br/> Параметры<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*id*|True|[numeric](/docs/types/numeric.md)|ID корзины.<br/>|
|*payer_id*|False|[numeric](/docs/types/numeric.md)|ID плательщика.<br/>Если не указано, то счет будет выписан на активного плательщика.<br/>|

### Результат
[Order](/docs/types/Order.md)
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|*admin*|full||
|*manager*|none||
|*chief*|full||
|*chief_partner*|none||
|*operator*|none||
|*admin_partner*|none||

## delete

### Описание метода
Удаляет указанную корзину.<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*id*|True|[numeric](/docs/types/numeric.md)|ID корзины.<br/>|

### Результат
None
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|*admin*|full||
|*manager*|none||
|*chief*|full||
|*chief_partner*|none||
|*operator*|none||
|*admin_partner*|none||
