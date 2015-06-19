
# CartItems

## Описание ресурса

# Методы

## add

### Описание метода
Добавляет позицию в указанную корзину.<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*product_addition*|False|[ProductAddition](/types/ProductAddition)|Дополнение продукта.<br/>|
|*cart_id*|True|[numeric](/types/numeric)|ID корзины.<br/>|

### Результат
[CartItem](/types/CartItem)
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
Обновляет указанную позицию корзины.<br/><br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*product_addition*|True|[ProductAddition](/types/ProductAddition)|Дополнение продукта.<br/>|
|*id*|True|[numeric](/types/numeric)|ID позиции корзины.<br/>|

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

## delete

### Описание метода
Удаляет указанную позицию корзины.<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*id*|True|[numeric](/types/numeric)|ID позиции корзины.<br/>|

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
