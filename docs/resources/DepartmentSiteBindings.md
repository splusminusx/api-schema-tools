
# DepartmentSiteBindings

## Описание ресурса

# Методы

## add

### Описание метода
Создает новую связь отдела и сайта.<br/>Возможно существование только одной связи конкретного отдела и конкретного сайта.<br/>ВНИМАНИЕ!<br/>При создании связи отдела с сайтом, в котором еще нет отделов, все прямые связи такого сайта с сотрудниками удаляются.<br/><br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*prechats_chat*|False|Array.<[Prechat](/types/Prechat)>|Массив пречат-полей.<br/>Максимум 2 элемента.<br/>|
|*is_visible*|False|[boolean](/types/boolean)|Признак видимости отдела в сайте.<br/>По умолчанию – true.<br/>|
|*site_id*|True|[numeric](/types/numeric)|ID сайта.<br/>|
|*alias*|True|[string](/types/string)|Псевдоним отдела.<br/>|
|*position*|False|[numeric](/types/numeric)|Порядковый номер отдела на данном сайте.<br/>Если не указано, то отдел будет последним по порядку в указанном сайте.<br/>|
|*callback_url*|False|[string](/types/string)|Настройка Callback URL.<br/>|
|*department_id*|True|[numeric](/types/numeric)|ID отдела.<br/>|

### Результат
[DepartmentSiteBinding](/types/DepartmentSiteBinding)
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|*admin*|full||
|*manager*|managed|Только связи своих отделов со своими сайтами.|
|*chief*|managed|Только связи своих отделов со своими сайтами.|
|*chief_partner*|managed|Только связи своих отделов со своими сайтами.|
|*operator*|none||
|*admin_partner*|full||

## show

### Описание метода
Возвращает данные указанной связи отдела и сайта.<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*fields*|False|[string](/types/string)|Список через запятую возвращаемых полей.<br/>|
|*id*|True|[numeric](/types/numeric)|ID связи.<br/>|

### Результат
[DepartmentSiteBinding](/types/DepartmentSiteBinding)
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
Возвращает список связей отделов и сайтов.<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*q*|False|[string](/types/string)|Критерий поиска.<br/>Доступные поля:<br/>ids – idlist, список ID связей.<br/>department_ids – idlist, список ID отделов.<br/>site_ids – idlist, список ID сайтов.<br/>|
|*fields*|False|[string](/types/string)|Список через запятую возвращаемых полей.<br/>|
|*limit*|False|[numeric](/types/numeric)|По умолчанию – 50.<br/>|
|*sort*|False|[string](/types/string)|Сортировка результатов.<br/>Возможные значения:<br/>updated_at:d – по умолчанию.<br/>|
|*offset*|False|[numeric](/types/numeric)|По умолчанию – 0.<br/>|

### Результат
Array.<[DepartmentSiteBinding](/types/DepartmentSiteBinding)>
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
Обновляет свойства связи отдела и сайта.<br/>Возможно существование только одной связи конкретного отдела и конкретного сайта.<br/>ВНИМАНИЕ!<br/>При создании связи отдела с сайтом, в котором еще нет отделов, все прямые связи такого сайта с сотрудниками удаляются. <br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*prechats_chat*|False|Array.<[Prechat](/types/Prechat)>|Массив пречат-полей.<br/>Максимум 2 элемента.<br/>|
|*is_visible*|False|[boolean](/types/boolean)|Признак видимости отдела в сайте.<br/>|
|*site_id*|False|[numeric](/types/numeric)|ID сайта.<br/>|
|*alias*|False|[string](/types/string)|Псевдоним отдела.<br/>|
|*position*|False|[numeric](/types/numeric)|Порядковый номер отдела на данном сайте.<br/>|
|*callback_url*|False|[string](/types/string)|Настройка Callback URL.<br/>|
|*id*|True|[numeric](/types/numeric)|ID связи.<br/>|
|*department_id*|False|[numeric](/types/numeric)|ID отдела.<br/>|

### Результат
None
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|*admin*|full||
|*manager*|managed|Только связи своих отделов со своими сайтами.|
|*chief*|managed|Только связи своих отделов со своими сайтами.|
|*chief_partner*|managed|Только связи своих отделов со своими сайтами.|
|*operator*|none||
|*admin_partner*|full||

## delete

### Описание метода
Удаляет указанную связь отдела и сайта.<br/>ВНИМАНИЕ!<br/>При удалении последней связи отдела с сайтами, отдел удаляется.<br/>Если удаляется последняя связь сайта с отделами, сотрудники этого отдела напрямую связываются с сайтом.<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*id*|True|[numeric](/types/numeric)|ID связи.<br/>|

### Результат
None
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|*admin*|full||
|*manager*|managed|Только связи своих отделов со своими сайтами.|
|*chief*|managed|Только связи своих отделов со своими сайтами.|
|*chief_partner*|managed|Только связи своих отделов со своими сайтами.|
|*operator*|none||
|*admin_partner*|full||
