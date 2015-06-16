
# Payments

## Описание ресурса
- Payments<br/>
# Методы

## list

### Описание метода
- Payments.list<br/>Возвращает список платежей.<br/>Параметры<br/>Результат<br/>Массив объектов типа «- Payment».<br/>Уровень доступа для ролей<br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|**q**|False|[string](/docs/types/string.md)|Критерий поиска.<br/>Доступные поля:<br/>payer_ids – idlist, список ID плательщиков.<br/>|
|**fields**|False|[string](/docs/types/string.md)|Список через запятую возвращаемых полей.<br/>|
|**limit**|False|[numeric](/docs/types/numeric.md)|По умолчанию – 50.<br/>|
|**sort**|False|[string](/docs/types/string.md)|Сортировка результатов.<br/>Возможные значения:<br/>created_at:d – по умолчанию.<br/>|
|**offset**|False|[numeric](/docs/types/numeric.md)|По умолчанию – 0.<br/>|

### Резудьтат
Array.<[Payment](/docs/types/Payment.md)>
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner