
# CartItems

## Описание ресурса
CartItems

# Методы

## add

### Описание метода
CartItems.add
Добавляет позицию в указанную корзину.
Параметры
Результат
Объект типа «CartItem».
Уровень доступа для ролей


### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|product_addition|False|[ProductAddition](/docs/types/ProductAddition.md)|Дополнение продукта.<br/>|
|cart_id|True|[numeric](/docs/types/numeric.md)|ID корзины.<br/>|

### Резудьтат
[CartItem](/docs/types/CartItem.md)
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner
## update

### Описание метода
CartItems.update
Обновляет указанную позицию корзины.
Параметры
Результат
Метод ничего не возвращает.
Уровень доступа для ролей



### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|product_addition|True|[ProductAddition](/docs/types/ProductAddition.md)|Дополнение продукта.<br/>|
|id|True|[numeric](/docs/types/numeric.md)|ID позиции корзины.<br/>|

### Резудьтат
None
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner
## delete

### Описание метода
CartItems.delete
Удаляет указанную позицию корзины.
Параметры
Результат
Метод ничего не возвращает.
Уровень доступа для ролей


### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|id|True|[numeric](/docs/types/numeric.md)|ID позиции корзины.<br/>|

### Резудьтат
None
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner