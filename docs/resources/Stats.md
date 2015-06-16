
# Stats

## Описание ресурса
Статистические данные различного типа.<br/>
# Методы

## employees

### Описание метода
Stats.employees<br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*q*|False|[string](/docs/types/string.md)|Критерий поиска.<br/>Доступные поля:<br/>site_ids – idlist, список ID сайтов.<br/>department_ids – idlist, список ID отделов.<br/>employee_ids – idlist, список ID сотрудников.<br/>date – date, период, за который запрашивается статистика.<br/>is_online – boolean, признак присутствия оператора в онлайн. Если указано, то метод вернет статистику по операторам с соответствующим текущим статусом.<br/>|
|*fields*|False|[string](/docs/types/string.md)|Список возвращаемых полей через запятую.<br/>Возможные значения приведены в нижеследующей таблице.<br/>По умолчанию возвращаются следующие поля:<br/>id;<br/>first_name;<br/>last_name;<br/>online_time_avg;<br/>chats_total;<br/>calls_total;<br/>leads_total.<br/>|
|*sort*|False|[string](/docs/types/string.md)|Сортировка результатов.<br/>Возможные значения:<br/>last_name:a – по умолчанию;<br/>first_name:a;<br/>online_time_avg:a, online_time_avg:d;<br/>chats_total:a, chats_total:d;<br/>calls_total:a, calls_total:d;<br/>leads_total:a, leads_total:d.<br/>|

### Результат
Array.<[Employee](/docs/types/Employee.md)>
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner
## contacts

### Описание метода
Stats.contacts<br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|

### Результат
None
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner
## sites

### Описание метода
Stats.sites<br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*q*|False|[string](/docs/types/string.md)|Критерий фильтрации.<br/>Доступные поля:<br/>site_ids – idlist, список ID сайтов.<br/>department_ids – idlist, список ID отделов.<br/>employee_ids – idlist, список ID сотрудников.<br/>date – date, период, за который запрашивается статистика.<br/>|
|*fields*|False|[string](/docs/types/string.md)|Список возвращаемых полей через запятую.<br/>Возможные значения приведены в нижеследующей таблице.<br/>По умолчанию возвращаются следующие поля:<br/>id;<br/>url;<br/>online_time_avg;<br/>chats_total;<br/>calls_total;<br/>leads_total.<br/>Если указано поле by_department, то принимаются во внимание также указания типа department(field_name), где field_name – имя поля отдела.<br/>|
|*sort*|False|[string](/docs/types/string.md)|Сортировка результатов.<br/>Возможные значения:<br/>url:a – по умолчанию;<br/>online_time_avg:a, online_time_avg:d;<br/>chats_total:a, chats_total:d;<br/>calls_total:a, calls_total:d;<br/>leads_total:a, leads_total:d.<br/>Указанная сортировка распространяется также на порядок данных в ключах "by_department" и "by_employee".<br/>Если указано "url:a", то для сортировки данных в ключе "by_department" можно указать одно из следующих возможных значений:<br/>department(title):a.<br/>А в ключе "by_employee":<br/>employee(last_name):a;<br/>employee(first_name):a.<br/>|

### Результат
Array.<[Site](/docs/types/Site.md)>
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner
## departments

### Описание метода
Stats.departments<br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*q*|False|[string](/docs/types/string.md)|Критерий фильтрации.<br/>Доступные поля:<br/>site_ids – idlist, список ID сайтов.<br/>department_ids – idlist, список ID отделов.<br/>employee_ids – idlist, список ID сотрудников.<br/>date – date, период, за который запрашивается статистика.<br/>|
|*fields*|False|[string](/docs/types/string.md)|Список возвращаемых полей через запятую.<br/>Возможные значения приведены в нижеследующей таблице.<br/>По умолчанию возвращаются следующие поля:<br/>online_time_avg;<br/>chats_total;<br/>calls_total;<br/>leads_total.<br/>|
|*sort*|False|[string](/docs/types/string.md)|Сортировка результатов.<br/>Возможные значения:<br/>title:a – по умолчанию;<br/>online_time_avg:a, online_time_avg:d;<br/>chats_total:a, chats_total:d;<br/>calls_total:a, calls_total:d;<br/>leads_total:a, leads_total:d.<br/>|

### Результат
Array.<[Department](/docs/types/Department.md)>
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner
## summary

### Описание метода
Stats.summary<br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*q*|False|[string](/docs/types/string.md)|Критерий поиска.<br/>Доступные поля:<br/>site_ids – idlist, список ID сайтов.<br/>department_ids – idlist, список ID отделов.<br/>employee_ids – idlist, список ID сотрудников.<br/>date – date, период, за который запрашивается статистика.<br/>|
|*fields*|False|[string](/docs/types/string.md)|Список возвращаемых полей через запятую.<br/>Возможные значения приведены в нижеследующей таблице.<br/>По умолчанию возвращаются следующие поля:<br/>online_time_avg;<br/>chats_total;<br/>calls_total;<br/>leads_total;<br/>|

### Результат
None
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner