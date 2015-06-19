
# Documents

## Описание ресурса

# Методы

## list

### Описание метода
Возвращает список документов.<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*q*|False|[string](/types/string)|Критерий поиска.<br/>Доступные поля:<br/>doc_type – enum, документа.<br/>is_bound – boolean, признак связанности документа с каким-либо периодом.<br/>|
|*fields*|False|[string](/types/string)|Список через запятую возвращаемых полей.<br/>|
|*limit*|False|[numeric](/types/numeric)|По умолчанию – 50.<br/>|
|*sort*|False|[string](/types/string)|Сортировка результатов.<br/>Возможные значения:<br/>created_at:d – по умолчанию, created_at:a;<br/>|
|*offset*|False|[numeric](/types/numeric)|По умолчанию – 0.<br/>|

### Результат
Array.<[Document](/types/Document)>
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|*admin*|full||
|*manager*|none||
|*chief*|full||
|*chief_partner*|none||
|*operator*|none||
|*admin_partner*|none||
