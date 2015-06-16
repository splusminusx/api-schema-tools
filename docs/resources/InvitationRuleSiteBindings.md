
# InvitationRuleSiteBindings

## Описание ресурса
InvitationRuleSiteBindings

# Методы

## add

### Описание метода
InvitationRuleSiteBindings.add
Добавляет новую связь сценария вовлечения и сайта.
Возможно существование только одной связи конкретного сайта и конкретного сценария вовлечения.
Параметры
Результат
Объект типа «InvitationRuleSiteBinding».
Уровень доступа для ролей


### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|invitation_rule_id|True|None|Сценарий вовлечения.<br/>|
|employee_id|False|None|ID сотрудника, на которого будет назначен чат или лид.<br/>|
|site_id|True|None|Сайт.<br/>|
|department_id|False|None|ID отдела, на который будет адресовано приглашение.<br/>|

### Резудьтат
None
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner
## show

### Описание метода
InvitationRuleSiteBindings.show
Возвращает данные указанной связи сценария вовлечения и сайта.
Параметры
Результат
Объект типа «InvitationRuleSiteBinding».
Уровень доступа для ролей


### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|fields|False|None|Список через запятую возвращаемых полей.<br/>|
|id|True|None|ID связи сценария вовлечения и сайта.<br/>|

### Резудьтат
None
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner
## list

### Описание метода
InvitationRuleSiteBindings.list
Возвращает список связей сценариев вовлечения и сайтов.
Параметры
Результат
Массив объектов типа «InvitationRuleSiteBinding».
Уровень доступа для ролей


### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|q|False|None|Критерий поиска.<br/>Доступные поля:<br/>ids – idlist, список ID сценариев вовлечения;<br/>site_ids – idlist, список ID сайтов.<br/>|
|fields|False|None|Список через запятую возвращаемых полей.<br/>|
|limit|False|None|По умолчанию – 50.<br/>|
|sort|False|None|Сортировка результатов.<br/>Возможные значение:<br/>created_at:a – по умолчанию.<br/>|
|offset|False|None|По умолчанию – 0.<br/>|

### Резудьтат
Array.<[InvitationRuleSiteBinding](/docs/types/InvitationRuleSiteBinding.md)>
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner
## update

### Описание метода
InvitationRuleSiteBindings.update
Изменяет указанную связь сценария вовлечения и сайта.
Возможно существование только одной связи конкретного сайта и конкретного сценария вовлечения.
Параметры
Результат
Метод ничего не возвращает.
Уровень доступа для ролей


### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|invitation_rule_id|False|None|Сценарий вовлечения.<br/>|
|employee_id|False|None|ID сотрудника, на которого будет назначен чат или лид.<br/>|
|site_id|False|None|Сайт.<br/>|
|id|True|None|ID связи.<br/>|
|department_id|False|None|ID отдела, на который будет адресовано приглашение.<br/>|

### Резудьтат
None
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner
## delete

### Описание метода
InvitationRuleSiteBindings.delete
Удаляет указанную связь сценария вовлечения и сайта.
Параметры
Результат
Метод ничего не возвращает.
Уровень доступа для ролей


### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|id|True|None|ID связи.<br/>|

### Резудьтат
None
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner