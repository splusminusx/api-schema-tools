
# Locations

## Описание ресурса

# Методы

## list

### Описание метода
Возвращает список географических расположений.<br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*q*|False|[string](/types/string)|Критерий поиска.<br/>Доступные поля:<br/>title – string, поиск по текстам полей title в соответствующих стране, региону и городу.<br/>|
|*fields*|False|[string](/types/string)|Список через запятую возвращаемых полей.<br/>|
|*limit*|False|[numeric](/types/numeric)|По умолчанию – 50.<br/>|
|*sort*|False|[string](/types/string)|Сортировка результатов.<br/>Возможные значения:<br/>title:a – по умолчанию. Записи сортируются по названию страны, затем по названию региона затем по названию города.<br/>|
|*offset*|False|[numeric](/types/numeric)|По умолчанию – 0.<br/>|

### Результат
Array.<[Location](/types/Location)>
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|*admin*|full||
|*manager*|full||
|*chief*|full||
|*chief_partner*|full||
|*operator*|none||
|*admin_partner*|full||
