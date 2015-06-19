
# InvitationRuleSiteBindings

## Описание ресурса

# Методы

## add

### Описание метода
Добавляет новую связь сценария вовлечения и сайта.<br/>Возможно существование только одной связи конкретного сайта и конкретного сценария вовлечения.<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*invitation_rule_id*|True|[numeric](/types/numeric)|Сценарий вовлечения.<br/>|
|*employee_id*|False|[numeric](/types/numeric)|ID сотрудника, на которого будет назначен чат или лид.<br/>|
|*site_id*|True|[numeric](/types/numeric)|Сайт.<br/>|
|*department_id*|False|[numeric](/types/numeric)|ID отдела, на который будет адресовано приглашение.<br/>|

### Результат
[InvitationRuleSiteBinding](/types/InvitationRuleSiteBinding)
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|*admin*|full||
|*manager*|managed|Только, если site_id указывает на свой сайт.|
|*chief*|managed|Только, если site_id указывает на свой сайт.|
|*chief_partner*|managed|Только, если site_id указывает на свой сайт.|
|*operator*|none||
|*admin_partner*|full||

## show

### Описание метода
Возвращает данные указанной связи сценария вовлечения и сайта.<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*fields*|False|[string](/types/string)|Список через запятую возвращаемых полей.<br/>|
|*id*|True|[numeric](/types/numeric)|ID связи сценария вовлечения и сайта.<br/>|

### Результат
[InvitationRuleSiteBinding](/types/InvitationRuleSiteBinding)
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|*admin*|full||
|*manager*|full||
|*chief*|full||
|*chief_partner*|full||
|*operator*|none||
|*admin_partner*|full||

## list

### Описание метода
Возвращает список связей сценариев вовлечения и сайтов.<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*q*|False|[string](/types/string)|Критерий поиска.<br/>Доступные поля:<br/>ids – idlist, список ID сценариев вовлечения;<br/>site_ids – idlist, список ID сайтов.<br/>|
|*fields*|False|[string](/types/string)|Список через запятую возвращаемых полей.<br/>|
|*limit*|False|[numeric](/types/numeric)|По умолчанию – 50.<br/>|
|*sort*|False|[string](/types/string)|Сортировка результатов.<br/>Возможные значение:<br/>created_at:a – по умолчанию.<br/>|
|*offset*|False|[numeric](/types/numeric)|По умолчанию – 0.<br/>|

### Результат
Array.<[InvitationRuleSiteBinding](/types/InvitationRuleSiteBinding)>
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|*admin*|full||
|*manager*|full||
|*chief*|full||
|*chief_partner*|full||
|*operator*|none||
|*admin_partner*|full||

## update

### Описание метода
Изменяет указанную связь сценария вовлечения и сайта.<br/>Возможно существование только одной связи конкретного сайта и конкретного сценария вовлечения.<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*invitation_rule_id*|False|[numeric](/types/numeric)|Сценарий вовлечения.<br/>|
|*employee_id*|False|[numeric](/types/numeric)|ID сотрудника, на которого будет назначен чат или лид.<br/>|
|*site_id*|False|[numeric](/types/numeric)|Сайт.<br/>|
|*id*|True|[numeric](/types/numeric)|ID связи.<br/>|
|*department_id*|False|[numeric](/types/numeric)|ID отдела, на который будет адресовано приглашение.<br/>|

### Результат
None
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|*admin*|full||
|*manager*|managed|Только, если предыдущее и новое значение site_id указывает на свой сайт.|
|*chief*|managed|Только, если предыдущее и новое значение site_id указывает на свой сайт.|
|*chief_partner*|managed|Только, если предыдущее и новое значение site_id указывает на свой сайт.|
|*operator*|none||
|*admin_partner*|full||

## delete

### Описание метода
Удаляет указанную связь сценария вовлечения и сайта.<br/><br/>
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
|*manager*|managed|Только, если site_id указывает на свой сайт.|
|*chief*|managed|Только, если site_id указывает на свой сайт.|
|*chief_partner*|managed|Только, если site_id указывает на свой сайт.|
|*operator*|none||
|*admin_partner*|full||
