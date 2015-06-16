
# Acceptances

## Описание ресурса
Acceptances

# Методы

## list

### Описание метода
Acceptances.list
Возвращает список актов.
Параметры
Результат
Массив объектов типа «Acceptance».
Уровень доступа для ролей


### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|q|False|[string](/docs/types/string.md)|Критерий поиска.<br/>Доступные поля:<br/>ids – idlist, список ID актов;<br/>is_bound – boolean, признак связанности акта с каким-либо периодом;<br/>created_at.<br/>|
|fields|False|[string](/docs/types/string.md)|Список через запятую возвращаемых полей.<br/>|
|limit|False|[numeric](/docs/types/numeric.md)|По умолчанию – 50.<br/>|
|sort|False|[string](/docs/types/string.md)|Сортировка результатов.<br/>Возможные значение:<br/>created_at:d – по умолчанию, created_at:a.<br/>|
|offset|False|[numeric](/docs/types/numeric.md)|По умолчанию – 0.<br/>|

### Резудьтат
Array.<[Acceptance](/docs/types/Acceptance.md)>
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner
## update

### Описание метода
Acceptances.update
Изменяет указанный акт.
Параметры

Результат
Метод ничего не возвращает.
Уровень доступа для ролей


### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|id|True|[numeric](/docs/types/numeric.md)|ID акта.<br/>|
|file_signed|False|[file](/docs/types/file.md)|Файл акта, подписанного клиентом.<br/>Допустимые типы файлов: PDF, TIFF, JPEG, PNG, GIF.<br/>Максимальный размер файла – 10 MB.<br/>|

### Резудьтат
None
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner