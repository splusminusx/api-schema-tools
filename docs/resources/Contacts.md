
# Contacts

## Описание ресурса
Contacts<br/>
# Методы

## list

### Описание метода
Contacts.list<br/>Возвращает список элементов контактных данных.<br/>ВНИМАНИЕ! Метод доступен только при наличии опции «Генератор лидов».<br/>Параметры<br/>Результат<br/>Массив объектов типа «Contact».<br/>Уровень доступа для ролей<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|**q**|False|[string](/docs/types/string.md)|Критерий поиска.<br/>Доступные поля:<br/>site_ids – idlist, список ID сайтов;<br/>source_type – enum, тип источника контактных данных;<br/>creator_type – enum, тип создателя контактных данных;<br/>is_auto;<br/>created_at.<br/>|
|**fields**|False|[string](/docs/types/string.md)|Список через запятую возвращаемых полей.<br/>|
|**limit**|False|[numeric](/docs/types/numeric.md)|По умолчанию – 50.<br/>|
|**sort**|False|[string](/docs/types/string.md)|Сортировка результатов.<br/>Возможные значение:<br/>created_at:d – по умолчанию.<br/>|
|**offset**|False|[numeric](/docs/types/numeric.md)|По умолчанию – 0.<br/>|

### Резудьтат
Array.<[Contact](/docs/types/Contact.md)>
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner
## show

### Описание метода
Contacts.show<br/>Возвращает данные указанного элемента контактных данных.<br/>ВНИМАНИЕ! Метод доступен только при наличии опции «Генератор лидов».<br/>Параметры<br/>Результат<br/>Объект типа «Contact».<br/>Уровень доступа для ролей<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|**fields**|False|[string](/docs/types/string.md)|Список через запятую возвращаемых полей.<br/>|
|**id**|True|[numeric](/docs/types/numeric.md)|ID элемента контактных данных.<br/>|

### Резудьтат
[Contact](/docs/types/Contact.md)
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner