
# Contacts

## Описание ресурса

# Методы

## list

### Описание метода
Contacts.list<br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*q*|False|[string](/docs/types/string.md)|Критерий поиска.<br/>Доступные поля:<br/>site_ids – idlist, список ID сайтов;<br/>source_type – enum, тип источника контактных данных;<br/>creator_type – enum, тип создателя контактных данных;<br/>is_auto;<br/>created_at.<br/>|
|*fields*|False|[string](/docs/types/string.md)|Список через запятую возвращаемых полей.<br/>|
|*limit*|False|[numeric](/docs/types/numeric.md)|По умолчанию – 50.<br/>|
|*sort*|False|[string](/docs/types/string.md)|Сортировка результатов.<br/>Возможные значение:<br/>created_at:d – по умолчанию.<br/>|
|*offset*|False|[numeric](/docs/types/numeric.md)|По умолчанию – 0.<br/>|

### Результат
Array.<[Contact](/docs/types/Contact.md)>
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|full||
|manager|managed|Только на своих сайтах.|
|chief|managed|Только на своих сайтах.|
|chief_partner|managed|Только на своих сайтах.|
|operator|none||
|admin_partner|full||

## show

### Описание метода
Contacts.show<br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*fields*|False|[string](/docs/types/string.md)|Список через запятую возвращаемых полей.<br/>|
|*id*|True|[numeric](/docs/types/numeric.md)|ID элемента контактных данных.<br/>|

### Результат
[Contact](/docs/types/Contact.md)
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|full||
|manager|managed|Только на своих сайтах.|
|chief|managed|Только на своих сайтах.|
|chief_partner|managed|Только на своих сайтах.|
|operator|none||
|admin_partner|full||
