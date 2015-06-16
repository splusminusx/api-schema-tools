
# Departments

## Описание ресурса

# Методы

## add

### Описание метода
Departments.add<br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*site_ids*|True|[idlist](/docs/types/idlist.md)|Список, через запятую, ID сайтов, с которыми требуется связать отдел. <br/>На основе этого поля автоматически создаются связи отдела с указанными сайтами (DepartmentSiteBinding). При этом в качестве псевдонима используется название отдела.<br/>|
|*title*|True|[string](/docs/types/string.md)|Название отдела.<br/>|
|*employee_ids*|True|[idlist](/docs/types/idlist.md)|Список, через запятую, ID сотрудников, входящих в отдел.<br/>|

### Результат
[Department](/docs/types/Department.md)
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner
## show

### Описание метода
Departments.show<br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*fields*|False|[string](/docs/types/string.md)|Список через запятую возвращаемых полей.<br/>|
|*id*|True|[numeric](/docs/types/numeric.md)|ID отдела.<br/>|

### Результат
[Department](/docs/types/Department.md)
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner
## list

### Описание метода
Departments.list<br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*q*|False|[string](/docs/types/string.md)|Критерий поиска.<br/>Доступные поля:<br/>ids – idlist, список ID отделов;<br/>employee_ids – idlist, список ID сотрудников;<br/>site_ids – idlist, список ID сайтов;<br/>title;<br/>is_managed – boolean, признак своего отдела.<br/>|
|*fields*|False|[string](/docs/types/string.md)|Список через запятую возвращаемых полей.<br/>|
|*limit*|False|[numeric](/docs/types/numeric.md)|По умолчанию – 50.<br/>|
|*sort*|False|[string](/docs/types/string.md)|Сортировка результатов.<br/>Возможные значения:<br/>title:a – по умолчанию;<br/>created_at:a;<br/>updated_at:a.<br/>|
|*offset*|False|[numeric](/docs/types/numeric.md)|По умолчанию – 0.<br/>|

### Результат
Array.<[Department](/docs/types/Department.md)>
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner
## update

### Описание метода
Departments.update<br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*title*|False|[string](/docs/types/string.md)|Название отдела.<br/>|
|*id*|True|[numeric](/docs/types/numeric.md)|ID отдела.<br/>|
|*employee_ids*|False|[idlist](/docs/types/idlist.md)|Список, через запятую, ID сотрудников, входящих в отдел.<br/>Если указать пустое значение, то все сотрудники будут отвязаны от отдела и отдел будет удален.<br/>|

### Результат
None
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner
## delete

### Описание метода
Departments.delete<br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*id*|True|[numeric](/docs/types/numeric.md)|ID отдела.<br/>|

### Результат
None
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner