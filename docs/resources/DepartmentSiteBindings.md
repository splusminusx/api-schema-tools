
# DepartmentSiteBindings

## Описание ресурса

# Методы

## add

### Описание метода
DepartmentSiteBindings.add<br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*prechats_chat*|False|Array.<[Prechat](/docs/types/Prechat.md)>|Массив пречат-полей.<br/>Максимум 2 элемента.<br/>|
|*is_visible*|False|[boolean](/docs/types/boolean.md)|Признак видимости отдела в сайте.<br/>По умолчанию – true.<br/>|
|*site_id*|True|[numeric](/docs/types/numeric.md)|ID сайта.<br/>|
|*alias*|True|[string](/docs/types/string.md)|Псевдоним отдела.<br/>|
|*position*|False|[numeric](/docs/types/numeric.md)|Порядковый номер отдела на данном сайте.<br/>Если не указано, то отдел будет последним по порядку в указанном сайте.<br/>|
|*callback_url*|False|[string](/docs/types/string.md)|Настройка Callback URL.<br/>|
|*department_id*|True|[numeric](/docs/types/numeric.md)|ID отдела.<br/>|

### Результат
[DepartmentSiteBinding](/docs/types/DepartmentSiteBinding.md)
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner
## show

### Описание метода
DepartmentSiteBindings.show<br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*fields*|False|[string](/docs/types/string.md)|Список через запятую возвращаемых полей.<br/>|
|*id*|True|[numeric](/docs/types/numeric.md)|ID связи.<br/>|

### Результат
[DepartmentSiteBinding](/docs/types/DepartmentSiteBinding.md)
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner
## list

### Описание метода
DepartmentSiteBindings.list<br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*q*|False|[string](/docs/types/string.md)|Критерий поиска.<br/>Доступные поля:<br/>ids – idlist, список ID связей.<br/>department_ids – idlist, список ID отделов.<br/>site_ids – idlist, список ID сайтов.<br/>|
|*fields*|False|[string](/docs/types/string.md)|Список через запятую возвращаемых полей.<br/>|
|*limit*|False|[numeric](/docs/types/numeric.md)|По умолчанию – 50.<br/>|
|*sort*|False|[string](/docs/types/string.md)|Сортировка результатов.<br/>Возможные значения:<br/>updated_at:d – по умолчанию.<br/>|
|*offset*|False|[numeric](/docs/types/numeric.md)|По умолчанию – 0.<br/>|

### Результат
Array.<[DepartmentSiteBinding](/docs/types/DepartmentSiteBinding.md)>
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner
## update

### Описание метода
DepartmentSiteBindings.update<br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*prechats_chat*|False|Array.<[Prechat](/docs/types/Prechat.md)>|Массив пречат-полей.<br/>Максимум 2 элемента.<br/>|
|*is_visible*|False|[boolean](/docs/types/boolean.md)|Признак видимости отдела в сайте.<br/>|
|*site_id*|False|[numeric](/docs/types/numeric.md)|ID сайта.<br/>|
|*alias*|False|[string](/docs/types/string.md)|Псевдоним отдела.<br/>|
|*position*|False|[numeric](/docs/types/numeric.md)|Порядковый номер отдела на данном сайте.<br/>|
|*callback_url*|False|[string](/docs/types/string.md)|Настройка Callback URL.<br/>|
|*id*|True|[numeric](/docs/types/numeric.md)|ID связи.<br/>|
|*department_id*|False|[numeric](/docs/types/numeric.md)|ID отдела.<br/>|

### Результат
None
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner
## delete

### Описание метода
DepartmentSiteBindings.delete<br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*id*|True|[numeric](/docs/types/numeric.md)|ID связи.<br/>|

### Результат
None
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner