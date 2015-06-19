
# Complaints

## Описание ресурса

# Методы

## list

### Описание метода
Возвращает список жалоб посетителей.<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*q*|False|[string](/types/string)|Критерий поиска.<br/>Доступные поля:<br/>ids – idlist, список ID жалоб;<br/>employee_ids – idlist, список ID сотрудников;<br/>site_ids – idlist, список ID сайтов;<br/>department_ids – idlist, список ID отделов;<br/>created_at.<br/>|
|*fields*|False|[string](/types/string)|Список через запятую возвращаемых полей.<br/>|
|*limit*|False|[numeric](/types/numeric)|По умолчанию – 50.<br/>|
|*sort*|False|[string](/types/string)|Сортировка результатов.<br/>Возможные значения:<br/>created_at:d – по умолчанию.<br/>|
|*offset*|False|[numeric](/types/numeric)|По умолчанию – 0.<br/>|

### Результат
Array.<[Complaint](/types/Complaint)>
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|*admin*|full||
|*manager*|managed|Жалобы в обращениях, в которых есть свои диалоги.|
|*chief*|managed|Жалобы в обращениях, в которых есть свои диалоги.|
|*chief_partner*|managed|Жалобы в обращениях, в которых есть свои диалоги.|
|*operator*|managed|Жалобы в обращениях, в которых есть свои диалоги.|
|*admin_partner*|full||

## show

### Описание метода
Возвращает данные указанной жалобы.<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*fields*|False|[string](/types/string)|Список через запятую возвращаемых полей.<br/>|
|*id*|True|[numeric](/types/numeric)|ID жалобы.<br/>|

### Результат
[Complaint](/types/Complaint)
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|*admin*|full||
|*manager*|managed|Жалобы в обращениях, в которых есть свои диалоги.|
|*chief*|managed|Жалобы в обращениях, в которых есть свои диалоги.|
|*chief_partner*|managed|Жалобы в обращениях, в которых есть свои диалоги.|
|*operator*|none|Жалобы в обращениях, в которых есть свои диалоги.|
|*admin_partner*|full||
