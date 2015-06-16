
# EmployeeRemarks

## Описание ресурса
EmployeeRemarks<br/>
# Методы

## add

### Описание метода
EmployeeRemarks.add<br/>Создает новую запись в списке оценок сотрудника.<br/>Параметры<br/>Результат<br/>Объект типа «EmployeeRemark».<br/>Уровень доступа для ролей<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|text|True|[string](/docs/types/string.md)|Текст оценки.<br/>|
|position|False|[numeric](/docs/types/numeric.md)|Порядковый номер оценки.<br/>Если не указано, то оценка будет последней.<br/>|

### Резудьтат
[EmployeeRemark](/docs/types/EmployeeRemark.md)
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner
## show

### Описание метода
EmployeeRemarks.show<br/>Возвращает данные указанной оценки сотрудника.<br/>Параметры<br/>Результат<br/>Объект типа «EmployeeRemark».<br/>Уровень доступа для ролей<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|fields|False|[string](/docs/types/string.md)|Список через запятую возвращаемых полей.<br/>|
|id|True|[numeric](/docs/types/numeric.md)|ID оценки.<br/>|

### Резудьтат
[EmployeeRemark](/docs/types/EmployeeRemark.md)
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner
## list

### Описание метода
EmployeeRemarks.list<br/>Возвращает список оценок сотрудника.<br/>Параметры<br/>Результат<br/>Массив объектов типа «EmployeeRemark».<br/>Уровень доступа для ролей<br/><br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|q|False|[string](/docs/types/string.md)|Критерий поиска.<br/>Доступные поля:<br/>ids – idlist, список ID оценок.<br/>|
|fields|False|[string](/docs/types/string.md)|Список через запятую возвращаемых полей.<br/>|
|limit|False|[numeric](/docs/types/numeric.md)|По умолчанию – 50.<br/>|
|sort|False|[string](/docs/types/string.md)|Сортировка результатов.<br/>Возможные значения:<br/>position:a – по умолчанию,<br/>text:a, text:d,<br/>created_at:d,<br/>updated_at:d.<br/>|
|offset|False|[numeric](/docs/types/numeric.md)|По умолчанию – 0.<br/>|

### Резудьтат
Array.<[EmployeeRemark](/docs/types/EmployeeRemark.md)>
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner
## update

### Описание метода
EmployeeRemarks.update<br/>Изменяет данные оценки оператора.<br/>Параметры<br/>Результат<br/>Метод ничего не возвращает.<br/>Уровень доступа для ролей<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|text|False|[string](/docs/types/string.md)|Текст оценки.<br/>|
|id|True|[numeric](/docs/types/numeric.md)|ID оценки.<br/>|
|position|False|[numeric](/docs/types/numeric.md)|Порядковый номер оценки.<br/>|

### Резудьтат
None
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner
## delete

### Описание метода
EmployeeRemarks.delete<br/>Удаляет указанную оценку сотрудника.<br/>Параметры<br/>Результат<br/>Метод ничего не возвращает.<br/>Уровень доступа для ролей<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|id|True|[numeric](/docs/types/numeric.md)|ID оценки.<br/>|

### Резудьтат
None
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner