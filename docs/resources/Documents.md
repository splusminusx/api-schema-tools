
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
|q|False|None|Критерий поиска.<br/>Доступные поля:<br/>doc_type – enum, документа.<br/>is_bound – boolean, признак связанности документа с каким-либо периодом.<br/>|
|fields|False|None|Список через запятую возвращаемых полей.<br/>|
|limit|False|None|По умолчанию – 50.<br/>|
|sort|False|None|Сортировка результатов.<br/>Возможные значения:<br/>created_at:d – по умолчанию, created_at:a;<br/>|
|offset|False|None|По умолчанию – 0.<br/>|

### Резудьтат
Array.<[Document](/docs/types/Document.md)>
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner