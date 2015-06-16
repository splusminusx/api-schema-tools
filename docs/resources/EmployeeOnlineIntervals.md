
# EmployeeOnlineIntervals

## Описание ресурса

# Методы

## listBySite

### Описание метода
EmployeeOnlineIntervals.listBySite<br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*q*|False|[string](/docs/types/string.md)|Критерий поиска.<br/>Доступные поля:<br/>site_ids – idlist, список ID сайтов.<br/>department_ids – idlist, список ID отделов.<br/>employee_ids – idlist, список ID сотрудников.<br/>date – date, период, за который запрашивается статистика.<br/>Максимум - 30 дней. По умолчанию устанавливается период равный предыдущим суткам.<br/>time – time, период времени в течение суток, принимаемый во внимание при поиске сотрудников в состоянии «В сети». Возможные значения от 00:00:00 до 23:59:59.<br/>|
|*fields*|False|[string](/docs/types/string.md)|Список возвращаемых полей через запятую.<br/>По умолчанию возвращаются стандартные поля сайта, а также:<br/>online_time;<br/>intervals.<br/>|
|*limit*|False|[numeric](/docs/types/numeric.md)|По умолчанию – 5.<br/>|
|*sort*|False|[string](/docs/types/string.md)|Сортировка результатов.<br/>Возможные значения:<br/>url:a – по умолчанию.<br/>|
|*offset*|False|[numeric](/docs/types/numeric.md)|По умолчанию – 0.<br/>|

### Результат
Array.<[Site](/docs/types/Site.md)>
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|full||
|manager|managed|Данные только для своих сайтов.|
|chief|managed|Данные только для своих сайтов.|
|chief_partner|managed|Данные только для своих сайтов.|
|operator|user||
|admin_partner|full||

## listByEmployee

### Описание метода
EmployeeOnlineIntervals.listByEmployee<br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*q*|False|[string](/docs/types/string.md)|Критерий поиска.<br/>Доступные поля:<br/>site_ids – idlist, список ID сайтов.<br/>department_ids – idlist, список ID отделов.<br/>employee_ids – idlist, список ID сотрудников.<br/>date – date, период, за который запрашивается статистика.<br/>Максимум - 30 дней. По умолчанию устанавливается период равный предыдущим суткам.<br/>time – time, период времени в течение суток, принимаемый во внимание при поиске сотрудников в состоянии «В сети». Возможные значения от 00:00:00 до 23:59:59.<br/>|
|*fields*|False|[string](/docs/types/string.md)|Список возвращаемых полей через запятую.<br/>По умолчанию возвращаются стандартные поля сайта, а также:<br/>online_time;<br/>intervals.<br/>|
|*limit*|False|[numeric](/docs/types/numeric.md)|По умолчанию – 5.<br/>|
|*sort*|False|[string](/docs/types/string.md)|Сортировка результатов.<br/>Возможные значения:<br/>last_name:a – по умолчанию;<br/>first_name:a.<br/>|
|*offset*|False|[numeric](/docs/types/numeric.md)|По умолчанию – 0.<br/>|

### Результат
Array.<[Employee](/docs/types/Employee.md)>
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|full||
|manager|managed|Данные только для своих сотрудников.|
|chief|managed|Данные только для своих сотрудников.|
|chief_partner|managed|Данные только для своих сотрудников.|
|operator|user||
|admin_partner|full||

## listByDepartment

### Описание метода
EmployeeOnlineIntervals.listByDepartment<br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*q*|False|[string](/docs/types/string.md)|Критерий поиска.<br/>Доступные поля:<br/>site_ids – idlist, список ID сайтов.<br/>department_ids – idlist, список ID отделов.<br/>employee_ids – idlist, список ID сотрудников.<br/>date – date, период, за который запрашивается статистика.<br/>Максимум - 30 дней. По умолчанию устанавливается период равный предыдущим суткам.<br/>time – time, период времени в течение суток, принимаемый во внимание при поиске сотрудников в состоянии "В сети". Возможные значения от 00:00:00 до 23:59:59.<br/>|
|*fields*|False|[string](/docs/types/string.md)|Список возвращаемых полей через запятую.<br/>По умолчанию возвращаются стандартные поля сайта, а также:<br/>online_time;<br/>intervals.<br/>|
|*limit*|False|[numeric](/docs/types/numeric.md)|По умолчанию – 5.<br/>|
|*sort*|False|[string](/docs/types/string.md)|Сортировка результатов.<br/>Возможные значения:<br/>title:a – по умолчанию.<br/>|
|*offset*|False|[numeric](/docs/types/numeric.md)|По умолчанию – 0.<br/>|

### Результат
Array.<[Department](/docs/types/Department.md)>
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|full||
|manager|managed|Данные только для своих отделов.|
|chief|managed|Данные только для своих отделов.|
|chief_partner|managed|Данные только для своих отделов.|
|operator|user||
|admin_partner|full||
