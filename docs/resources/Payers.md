
# Payers

## Описание ресурса

# Методы

## list

### Описание метода
Payers.list<br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*q*|False|[string](/docs/types/string.md)|Критерий поиска.<br/>Доступные поля:<br/>ids – idlist, список ID плательщиков;<br/>is_active – boolean, если указано, то возвращаются записи с указанным значением.<br/>|
|*fields*|False|[string](/docs/types/string.md)|Список через запятую возвращаемых полей.<br/>|
|*limit*|False|[numeric](/docs/types/numeric.md)|По умолчанию – 50.<br/>|
|*sort*|False|[string](/docs/types/string.md)|Сортировка результатов.<br/>Возможные значения:<br/>created_at:d – по умолчанию.<br/>|
|*offset*|False|[numeric](/docs/types/numeric.md)|По умолчанию – 0.<br/>|

### Результат
Array.<[Payer](/docs/types/Payer.md)>
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|full||
|manager|none||
|chief|full||
|chief_partner|none||
|operator|none||
|admin_partner|none||

## add

### Описание метода
Payers.add<br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*requisites*|True|[Requisites](/docs/types/Requisites.md)|Реквизиты плательщика.<br/>|
|*currency*|False|[currency](/docs/types/currency.md)|Валюта плательщика.<br/>|
|*payer_type*|True|[string](/docs/types/string.md)|Тип плательщика.<br/>Возможные значения:<br/>ru_person – физическое лицо РФ;<br/>ru_legal – юридическое лицо РФ;<br/>ua_person – физическое лицо Украины;<br/>ua_legal – юридическое лицо Украины;<br/>ua_sp – ФОП Украины.<br/>|

### Результат
[Payer](/docs/types/Payer.md)
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|full||
|manager|none||
|chief|full||
|chief_partner|none||
|operator|none||
|admin_partner|none||

## transferBalance

### Описание метода
Payers.transferBalance<br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*id*|True|[numeric](/docs/types/numeric.md)|ID плательщика, остатки со счета которого требуется перенести на активного плательщика.<br/>|

### Результат
None
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|full||
|manager|none||
|chief|full||
|chief_partner|none||
|operator|none||
|admin_partner|none||

## update

### Описание метода
Payers.update<br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*is_recurring*|False|[boolean](/docs/types/boolean.md)|Включение/выключение рекуррентных платежей.<br/>|
|*id*|True|[numeric](/docs/types/numeric.md)|ID плательщика.<br/>|

### Результат
None
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|full||
|manager|none||
|chief|full||
|chief_partner|none||
|operator|none||
|admin_partner|none||

## show

### Описание метода
Payers.show<br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*fields*|False|[string](/docs/types/string.md)|Список через запятую возвращаемых полей.<br/>|
|*id*|True|[numeric](/docs/types/numeric.md)|ID плательщика.<br/>|

### Результат
[Payer](/docs/types/Payer.md)
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|full||
|manager|none||
|chief|full||
|chief_partner|none||
|operator|none||
|admin_partner|none||
