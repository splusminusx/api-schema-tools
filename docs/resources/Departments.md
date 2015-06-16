# Departments
## Описание ресурса
Departments
# Методы
## add
### Описание метода
Departments.add
Создает новый отдел.
ВНИМАНИЕ!
При создании отдела с привязкой к сайту, в котором еще нет отделов, все прямые связи такого сайта с сотрудниками удаляются.
Новый отдел автоматически добавляется в поле managed_departments всем сотрудникам с ролью, имеющей is_full_by_default = true.
Параметры
Результат
Объект типа «Department».
Уровень доступа для ролей

### Поля
| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|site_ids|True|idlist|Список, через запятую, ID сайтов, с которыми требуется связать отдел. <br/>На основе этого поля автоматически создаются связи отдела с указанными сайтами (DepartmentSiteBinding). При этом в качестве псевдонима используется название отдела.<br/>|
|title|True|string|Название отдела.<br/>|
|employee_ids|True|idlist|Список, через запятую, ID сотрудников, входящих в отдел.<br/>|
### Доступы к методу
| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner## show
### Описание метода
Departments.show
Возвращает данные указанного отдела.
Параметры
Результат
Объект типа «Department».
Уровень доступа для ролей

### Поля
| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|fields|False|string|Список через запятую возвращаемых полей.<br/>|
|id|True|numeric|ID отдела.<br/>|
### Доступы к методу
| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner## list
### Описание метода
Departments.list
Возвращает список отделов.
Параметры
Результат
Массив объектов типа «Department».
Уровень доступа для ролей

### Поля
| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|q|False|string|Критерий поиска.<br/>Доступные поля:<br/>ids – idlist, список ID отделов;<br/>employee_ids – idlist, список ID сотрудников;<br/>site_ids – idlist, список ID сайтов;<br/>title;<br/>is_managed – boolean, признак своего отдела.<br/>|
|fields|False|string|Список через запятую возвращаемых полей.<br/>|
|limit|False|numeric|По умолчанию – 50.<br/>|
|sort|False|string|Сортировка результатов.<br/>Возможные значения:<br/>title:a – по умолчанию;<br/>created_at:a;<br/>updated_at:a.<br/>|
|offset|False|numeric|По умолчанию – 0.<br/>|
### Доступы к методу
| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner## update
### Описание метода
Departments.update
Изменяет данные указанного отдела.
ВНИМАНИЕ!
При опустошении списка сотрудников отдел автоматически удаляется.
Параметры
Результат
Метод ничего не возвращает.
Уровень доступа для ролей

### Поля
| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|title|False|string|Название отдела.<br/>|
|id|True|numeric|ID отдела.<br/>|
|employee_ids|False|idlist|Список, через запятую, ID сотрудников, входящих в отдел.<br/>Если указать пустое значение, то все сотрудники будут отвязаны от отдела и отдел будет удален.<br/>|
### Доступы к методу
| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner## delete
### Описание метода
Departments.delete
Удаляет указанный отдел.
ВНИМАНИЕ!
Если удаляемый отдел последний в каких-то сайтах, то сотрудники этого отдела напрямую привязываются к этим сайтам.
При удалении отдела удаляются все его связи с объектами других сущностей, за исключением чатов, звонков и лидов и связей с сотрудниками в поле managed_departments.

Параметры
Результат
Метод ничего не возвращает.
Уровень доступа для ролей

### Поля
| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|id|True|numeric|ID отдела.<br/>|
### Доступы к методу
| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner