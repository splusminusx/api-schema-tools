
# Documents

## Описание ресурса
Documents<br/>
# Методы

## list

### Описание метода
Documents.list<br/>Возвращает список документов.<br/>Параметры<br/>Результат<br/>Массив объектов типа «Document».<br/>Уровень доступа для ролей<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|**q**|False|[string](/docs/types/string.md)|Критерий поиска.<br/>Доступные поля:<br/>doc_type – enum, документа.<br/>is_bound – boolean, признак связанности документа с каким-либо периодом.<br/>|
|**fields**|False|[string](/docs/types/string.md)|Список через запятую возвращаемых полей.<br/>|
|**limit**|False|[numeric](/docs/types/numeric.md)|По умолчанию – 50.<br/>|
|**sort**|False|[string](/docs/types/string.md)|Сортировка результатов.<br/>Возможные значения:<br/>created_at:d – по умолчанию, created_at:a;<br/>|
|**offset**|False|[numeric](/docs/types/numeric.md)|По умолчанию – 0.<br/>|

### Резудьтат
Array.<[Document](/docs/types/Document.md)>
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner