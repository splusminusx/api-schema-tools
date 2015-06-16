
# Complaints

## Описание ресурса
Complaints

# Методы

## list

### Описание метода
Complaints.list
Возвращает список жалоб посетителей.
Параметры
Результат
Массив объектов типа «Complaint».
Уровень доступа для ролей


### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|q|False|string|Критерий поиска.<br/>Доступные поля:<br/>ids – idlist, список ID жалоб;<br/>employee_ids – idlist, список ID сотрудников;<br/>site_ids – idlist, список ID сайтов;<br/>department_ids – idlist, список ID отделов;<br/>created_at.<br/>|
|fields|False|string|Список через запятую возвращаемых полей.<br/>|
|limit|False|numeric|По умолчанию – 50.<br/>|
|sort|False|string|Сортировка результатов.<br/>Возможные значения:<br/>created_at:d – по умолчанию.<br/>|
|offset|False|numeric|По умолчанию – 0.<br/>|

### Резудьтат
Array.<[Complaint](types/Complaint.md)>
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner
## show

### Описание метода
Complaints.show
Возвращает данные указанной жалобы.
Параметры
Результат
Объект типа «Complaint».
Уровень доступа для ролей


### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|fields|False|string|Список через запятую возвращаемых полей.<br/>|
|id|True|numeric|ID жалобы.<br/>|

### Резудьтат
None
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner