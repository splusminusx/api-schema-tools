
# Documents

## Описание ресурса
Documents

# Методы

## list

### Описание метода
Documents.list
Возвращает список документов.
Параметры
Результат
Массив объектов типа «Document».
Уровень доступа для ролей


### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|q|False|string|Критерий поиска.<br/>Доступные поля:<br/>doc_type – enum, документа.<br/>is_bound – boolean, признак связанности документа с каким-либо периодом.<br/>|
|fields|False|string|Список через запятую возвращаемых полей.<br/>|
|limit|False|numeric|По умолчанию – 50.<br/>|
|sort|False|string|Сортировка результатов.<br/>Возможные значения:<br/>created_at:d – по умолчанию, created_at:a;<br/>|
|offset|False|numeric|По умолчанию – 0.<br/>|

### Резудьтат
Array.<[Document](/docs/types/Document.md)>
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner