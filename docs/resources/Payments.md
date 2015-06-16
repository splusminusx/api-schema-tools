
# Payments

## Описание ресурса
- Payments

# Методы

## list

### Описание метода
- Payments.list
Возвращает список платежей.
Параметры
Результат
Массив объектов типа «- Payment».
Уровень доступа для ролей

### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|q|False|None|Критерий поиска.<br/>Доступные поля:<br/>payer_ids – idlist, список ID плательщиков.<br/>|
|fields|False|None|Список через запятую возвращаемых полей.<br/>|
|limit|False|None|По умолчанию – 50.<br/>|
|sort|False|None|Сортировка результатов.<br/>Возможные значения:<br/>created_at:d – по умолчанию.<br/>|
|offset|False|None|По умолчанию – 0.<br/>|

### Резудьтат
Array.<[Payment](/docs/types/Payment.md)>
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner