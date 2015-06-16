# IgnoreListItems
## Описание ресурса
IgnoreListItems
# Методы
## list
### Описание метода
IgnoreListItems.list
Возвращает список записей игнор-листа.
Параметры
Результат
Массив объектов типа «IgnoreListItem».
Уровень доступа для ролей

### Поля
| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|q|False|string|Критерий поиска.<br/>Доступные поля:<br/>site_ids – idlist, список ID сайтов;<br/>employee_ids – idlist, список ID сотрудников.<br/>created_at.<br/>|
|fields|False|string|Список через запятую возвращаемых полей.<br/>|
|limit|False|numeric|По умолчанию – 50.<br/>|
|sort|False|string|Сортировка результатов.<br/>Возможные значение:<br/>created_at:a – по умолчанию.<br/>|
|offset|False|numeric|По умолчанию – 0.<br/>|
### Доступы к методу
| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner## delete
### Описание метода
IgnoreListItems.delete
Удаляет запись в игнор-листе.
Параметры
Результат
Метод ничего не возвращает.
Уровень доступа для ролей


### Поля
| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|site_id|True|numeric|ID сайта.<br/>|
|visitor_id|True|string|ID посетителя.<br/>|
### Доступы к методу
| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner