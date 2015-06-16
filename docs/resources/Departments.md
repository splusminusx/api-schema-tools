
# Departments

## Описание ресурса

# Методы

## add

### Описание метода
Создает новый отдел.<br/>ВНИМАНИЕ!<br/>При создании отдела с привязкой к сайту, в котором еще нет отделов, все прямые связи такого сайта с сотрудниками удаляются.<br/>Новый отдел автоматически добавляется в поле managed_departments всем сотрудникам с ролью, имеющей is_full_by_default = true.<br/><br/>
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
|*admin*|full||
|*manager*|managed|В поле employee_ids принимаются во внимание только ID своих сотрудников.|
|*chief*|managed|В поле employee_ids принимаются во внимание только ID своих сотрудников.|
|*chief_partner*|managed|В поле employee_ids принимаются во внимание только ID своих сотрудников.|
|*operator*|none||
|*admin_partner*|full||

## show

### Описание метода
Возвращает данные указанного отдела.<br/><br/>
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
|*admin*|full||
|*manager*|full||
|*chief*|full||
|*chief_partner*|full||
|*operator*|full||
|*admin_partner*|full||

## list

### Описание метода
Возвращает список отделов.<br/><br/>
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
|*admin*|full||
|*manager*|full||
|*chief*|full||
|*chief_partner*|full||
|*operator*|full||
|*admin_partner*|full||

## update

### Описание метода
Изменяет данные указанного отдела.<br/>ВНИМАНИЕ!<br/>При опустошении списка сотрудников отдел автоматически удаляется.<br/><br/>
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
|*admin*|full||
|*manager*|managed|В поле employee_ids принимаются во внимание только ID своих сотрудников.|
|*chief*|managed|В поле employee_ids принимаются во внимание только ID своих сотрудников.|
|*chief_partner*|managed|В поле employee_ids принимаются во внимание только ID своих сотрудников.|
|*operator*|none||
|*admin_partner*|full||

## delete

### Описание метода
Удаляет указанный отдел.<br/>ВНИМАНИЕ!<br/>Если удаляемый отдел последний в каких-то сайтах, то сотрудники этого отдела напрямую привязываются к этим сайтам.<br/>При удалении отдела удаляются все его связи с объектами других сущностей, за исключением чатов, звонков и лидов и связей с сотрудниками в поле managed_departments.<br/><br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*id*|True|[numeric](/docs/types/numeric.md)|ID отдела.<br/>|

### Результат
None
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|*admin*|full||
|*manager*|managed|Только свои отделы.|
|*chief*|managed|Только свои отделы.|
|*chief_partner*|managed|Только свои отделы.|
|*operator*|none||
|*admin_partner*|full||
