
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
|invitation_rule_id|True|numeric|Сценарий вовлечения.<br/>|
|employee_id|False|numeric|ID сотрудника, на которого будет назначен чат или лид.<br/>|
|site_id|True|numeric|Сайт.<br/>|
|department_id|False|numeric|ID отдела, на который будет адресовано приглашение.<br/>|

### Резудьтат
InvitationRuleSiteBinding
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
|fields|False|string|Список через запятую возвращаемых полей.<br/>|
|id|True|numeric|ID связи сценария вовлечения и сайта.<br/>|

### Резудьтат
InvitationRuleSiteBinding
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
|q|False|string|Критерий поиска.<br/>Доступные поля:<br/>ids – idlist, список ID сценариев вовлечения;<br/>site_ids – idlist, список ID сайтов.<br/>|
|fields|False|string|Список через запятую возвращаемых полей.<br/>|
|limit|False|numeric|По умолчанию – 50.<br/>|
|sort|False|string|Сортировка результатов.<br/>Возможные значение:<br/>created_at:a – по умолчанию.<br/>|
|offset|False|numeric|По умолчанию – 0.<br/>|

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
|invitation_rule_id|False|numeric|Сценарий вовлечения.<br/>|
|employee_id|False|numeric|ID сотрудника, на которого будет назначен чат или лид.<br/>|
|site_id|False|numeric|Сайт.<br/>|
|id|True|numeric|ID связи.<br/>|
|department_id|False|numeric|ID отдела, на который будет адресовано приглашение.<br/>|

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
|id|True|numeric|ID связи.<br/>|

### Резудьтат
None
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner