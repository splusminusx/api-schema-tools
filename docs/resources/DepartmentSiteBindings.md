
# DepartmentSiteBindings

## Описание ресурса
DepartmentSiteBindings

# Методы

## add

### Описание метода
DepartmentSiteBindings.add
Создает новую связь отдела и сайта.
Возможно существование только одной связи конкретного отдела и конкретного сайта.
ВНИМАНИЕ!
При создании связи отдела с сайтом, в котором еще нет отделов, все прямые связи такого сайта с сотрудниками удаляются.
Параметры
Результат
Объект типа «DepartmentSiteBinding».
Уровень доступа для ролей



### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|prechats_chat|False|Array.<Prechat>|Массив пречат-полей.<br/>Максимум 2 элемента.<br/>|
|is_visible|False|boolean|Признак видимости отдела в сайте.<br/>По умолчанию – true.<br/>|
|site_id|True|numeric|ID сайта.<br/>|
|alias|True|string|Псевдоним отдела.<br/>|
|position|False|numeric|Порядковый номер отдела на данном сайте.<br/>Если не указано, то отдел будет последним по порядку в указанном сайте.<br/>|
|callback_url|False|string|Настройка Callback URL.<br/>|
|department_id|True|numeric|ID отдела.<br/>|

### Резудьтат
None
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner
## show

### Описание метода
DepartmentSiteBindings.show
Возвращает данные указанной связи отдела и сайта.
Параметры
Результат
Объект типа «DepartmentSiteBinding».
Уровень доступа для ролей


### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|fields|False|string|Список через запятую возвращаемых полей.<br/>|
|id|True|numeric|ID связи.<br/>|

### Резудьтат
None
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner
## list

### Описание метода
DepartmentSiteBindings.list
Возвращает список связей отделов и сайтов.
Параметры
Результат
Массив объектов типа «DepartmentSiteBinding».
Уровень доступа для ролей


### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|q|False|string|Критерий поиска.<br/>Доступные поля:<br/>ids – idlist, список ID связей.<br/>department_ids – idlist, список ID отделов.<br/>site_ids – idlist, список ID сайтов.<br/>|
|fields|False|string|Список через запятую возвращаемых полей.<br/>|
|limit|False|numeric|По умолчанию – 50.<br/>|
|sort|False|string|Сортировка результатов.<br/>Возможные значения:<br/>updated_at:d – по умолчанию.<br/>|
|offset|False|numeric|По умолчанию – 0.<br/>|

### Резудьтат
Array.<[DepartmentSiteBinding](/docs/types/DepartmentSiteBinding.md)>
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner
## update

### Описание метода
DepartmentSiteBindings.update
Обновляет свойства связи отдела и сайта.
Возможно существование только одной связи конкретного отдела и конкретного сайта.
ВНИМАНИЕ!
При создании связи отдела с сайтом, в котором еще нет отделов, все прямые связи такого сайта с сотрудниками удаляются. 
Параметры
Результат
Метод ничего не возвращает.
Уровень доступа для ролей


### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|prechats_chat|False|Array.<Prechat>|Массив пречат-полей.<br/>Максимум 2 элемента.<br/>|
|is_visible|False|boolean|Признак видимости отдела в сайте.<br/>|
|site_id|False|numeric|ID сайта.<br/>|
|alias|False|string|Псевдоним отдела.<br/>|
|position|False|numeric|Порядковый номер отдела на данном сайте.<br/>|
|callback_url|False|string|Настройка Callback URL.<br/>|
|id|True|numeric|ID связи.<br/>|
|department_id|False|numeric|ID отдела.<br/>|

### Резудьтат
None
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner
## delete

### Описание метода
DepartmentSiteBindings.delete
Удаляет указанную связь отдела и сайта.
ВНИМАНИЕ!
При удалении последней связи отдела с сайтами, отдел удаляется.
Если удаляется последняя связь сайта с отделами, сотрудники этого отдела напрямую связываются с сайтом.
Параметры
Результат
Метод ничего не возвращает.
Уровень доступа для ролей


### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|id|True|numeric|ID связи.<br/>|

### Резудьтат
None
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner