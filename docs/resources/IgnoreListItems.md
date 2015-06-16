
# IgnoreListItems

## Описание ресурса
IgnoreListItems<br/>
# Методы

## list

### Описание метода
IgnoreListItems.list<br/>Возвращает список записей игнор-листа.<br/>Параметры<br/>Результат<br/>Массив объектов типа «IgnoreListItem».<br/>Уровень доступа для ролей<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|q|False|[string](/docs/types/string.md)|Критерий поиска.<br/>Доступные поля:<br/>site_ids – idlist, список ID сайтов;<br/>employee_ids – idlist, список ID сотрудников.<br/>created_at.<br/>|
|fields|False|[string](/docs/types/string.md)|Список через запятую возвращаемых полей.<br/>|
|limit|False|[numeric](/docs/types/numeric.md)|По умолчанию – 50.<br/>|
|sort|False|[string](/docs/types/string.md)|Сортировка результатов.<br/>Возможные значение:<br/>created_at:a – по умолчанию.<br/>|
|offset|False|[numeric](/docs/types/numeric.md)|По умолчанию – 0.<br/>|

### Резудьтат
Array.<[IgnoreListItem](/docs/types/IgnoreListItem.md)>
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner
## delete

### Описание метода
IgnoreListItems.delete<br/>Удаляет запись в игнор-листе.<br/>Параметры<br/>Результат<br/>Метод ничего не возвращает.<br/>Уровень доступа для ролей<br/><br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|site_id|True|[numeric](/docs/types/numeric.md)|ID сайта.<br/>|
|visitor_id|True|[string](/docs/types/string.md)|ID посетителя.<br/>|

### Резудьтат
None
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner