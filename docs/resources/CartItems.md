
# CartItems

## Описание ресурса
CartItems<br/>
# Методы

## add

### Описание метода
CartItems.add<br/>Добавляет позицию в указанную корзину.<br/>Параметры<br/>Результат<br/>Объект типа «CartItem».<br/>Уровень доступа для ролей<br/><br/>
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
CartItems.update<br/>Обновляет указанную позицию корзины.<br/>Параметры<br/>Результат<br/>Метод ничего не возвращает.<br/>Уровень доступа для ролей<br/><br/><br/>
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
CartItems.delete<br/>Удаляет указанную позицию корзины.<br/>Параметры<br/>Результат<br/>Метод ничего не возвращает.<br/>Уровень доступа для ролей<br/><br/>
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