
# Contacts

## Описание ресурса

# Методы

## list

### Описание метода
Возвращает список элементов контактных данных.<br/>ВНИМАНИЕ! Метод доступен только при наличии опции «Генератор лидов».<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*q*|False|[string](/types/string)|Критерий поиска.<br/>Доступные поля:<br/>site_ids – idlist, список ID сайтов;<br/>source_type – enum, тип источника контактных данных;<br/>creator_type – enum, тип создателя контактных данных;<br/>is_auto;<br/>created_at.<br/>|
|*fields*|False|[string](/types/string)|Список через запятую возвращаемых полей.<br/>|
|*limit*|False|[numeric](/types/numeric)|По умолчанию – 50.<br/>|
|*sort*|False|[string](/types/string)|Сортировка результатов.<br/>Возможные значение:<br/>created_at:d – по умолчанию.<br/>|
|*offset*|False|[numeric](/types/numeric)|По умолчанию – 0.<br/>|

### Результат
Array.<[Contact](/types/Contact)>
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|*admin*|full||
|*manager*|managed|Только на своих сайтах.|
|*chief*|managed|Только на своих сайтах.|
|*chief_partner*|managed|Только на своих сайтах.|
|*operator*|none||
|*admin_partner*|full||

## show

### Описание метода
Возвращает данные указанного элемента контактных данных.<br/>ВНИМАНИЕ! Метод доступен только при наличии опции «Генератор лидов».<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*fields*|False|[string](/types/string)|Список через запятую возвращаемых полей.<br/>|
|*id*|True|[numeric](/types/numeric)|ID элемента контактных данных.<br/>|

### Результат
[Contact](/types/Contact)
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|*admin*|full||
|*manager*|managed|Только на своих сайтах.|
|*chief*|managed|Только на своих сайтах.|
|*chief_partner*|managed|Только на своих сайтах.|
|*operator*|none||
|*admin_partner*|full||
