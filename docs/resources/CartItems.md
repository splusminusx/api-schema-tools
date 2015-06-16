
# CartItems

## Описание ресурса

# Методы

## add

### Описание метода
CartItems.add<br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*product_addition*|False|[ProductAddition](/docs/types/ProductAddition.md)|Дополнение продукта.<br/>|
|*cart_id*|True|[numeric](/docs/types/numeric.md)|ID корзины.<br/>|

### Результат
[CartItem](/docs/types/CartItem.md)
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner
## update

### Описание метода
CartItems.update<br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*product_addition*|True|[ProductAddition](/docs/types/ProductAddition.md)|Дополнение продукта.<br/>|
|*id*|True|[numeric](/docs/types/numeric.md)|ID позиции корзины.<br/>|

### Результат
None
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner
## delete

### Описание метода
CartItems.delete<br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*id*|True|[numeric](/docs/types/numeric.md)|ID позиции корзины.<br/>|

### Результат
None
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner