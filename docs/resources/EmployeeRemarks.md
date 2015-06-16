
# EmployeeRemarks

## Описание ресурса

# Методы

## add

### Описание метода
EmployeeRemarks.add<br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*text*|True|[string](/docs/types/string.md)|Текст оценки.<br/>|
|*position*|False|[numeric](/docs/types/numeric.md)|Порядковый номер оценки.<br/>Если не указано, то оценка будет последней.<br/>|

### Результат
[EmployeeRemark](/docs/types/EmployeeRemark.md)
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|full||
|manager|full||
|chief|full||
|chief_partner|full||
|operator|none||
|admin_partner|full||

## show

### Описание метода
EmployeeRemarks.show<br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*fields*|False|[string](/docs/types/string.md)|Список через запятую возвращаемых полей.<br/>|
|*id*|True|[numeric](/docs/types/numeric.md)|ID оценки.<br/>|

### Результат
[EmployeeRemark](/docs/types/EmployeeRemark.md)
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|full||
|manager|full||
|chief|full||
|chief_partner|full||
|operator|full||
|admin_partner|full||

## list

### Описание метода
EmployeeRemarks.list<br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*q*|False|[string](/docs/types/string.md)|Критерий поиска.<br/>Доступные поля:<br/>ids – idlist, список ID оценок.<br/>|
|*fields*|False|[string](/docs/types/string.md)|Список через запятую возвращаемых полей.<br/>|
|*limit*|False|[numeric](/docs/types/numeric.md)|По умолчанию – 50.<br/>|
|*sort*|False|[string](/docs/types/string.md)|Сортировка результатов.<br/>Возможные значения:<br/>position:a – по умолчанию,<br/>text:a, text:d,<br/>created_at:d,<br/>updated_at:d.<br/>|
|*offset*|False|[numeric](/docs/types/numeric.md)|По умолчанию – 0.<br/>|

### Результат
Array.<[EmployeeRemark](/docs/types/EmployeeRemark.md)>
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|full||
|manager|full||
|chief|full||
|chief_partner|full||
|operator|full||
|admin_partner|full||

## update

### Описание метода
EmployeeRemarks.update<br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*text*|False|[string](/docs/types/string.md)|Текст оценки.<br/>|
|*id*|True|[numeric](/docs/types/numeric.md)|ID оценки.<br/>|
|*position*|False|[numeric](/docs/types/numeric.md)|Порядковый номер оценки.<br/>|

### Результат
None
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|full||
|manager|full||
|chief|full||
|chief_partner|full||
|operator|none||
|admin_partner|full||

## delete

### Описание метода
EmployeeRemarks.delete<br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*id*|True|[numeric](/docs/types/numeric.md)|ID оценки.<br/>|

### Результат
None
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|full||
|manager|full||
|chief|full||
|chief_partner|full||
|operator|none||
|admin_partner|full||
