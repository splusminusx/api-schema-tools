
# Locations

## Описание ресурса
Locations<br/>
# Методы

## list

### Описание метода
Locations.list<br/>Возвращает список географических расположений.<br/>Параметры<br/>Результат<br/>Массив объектов типа «Location».<br/>Уровень доступа для ролей<br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|q|False|[string](/docs/types/string.md)|Критерий поиска.<br/>Доступные поля:<br/>title – string, поиск по текстам полей title в соответствующих стране, региону и городу.<br/>|
|fields|False|[string](/docs/types/string.md)|Список через запятую возвращаемых полей.<br/>|
|limit|False|[numeric](/docs/types/numeric.md)|По умолчанию – 50.<br/>|
|sort|False|[string](/docs/types/string.md)|Сортировка результатов.<br/>Возможные значения:<br/>title:a – по умолчанию. Записи сортируются по названию страны, затем по названию региона затем по названию города.<br/>|
|offset|False|[numeric](/docs/types/numeric.md)|По умолчанию – 0.<br/>|

### Резудьтат
Array.<[Location](/docs/types/Location.md)>
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner