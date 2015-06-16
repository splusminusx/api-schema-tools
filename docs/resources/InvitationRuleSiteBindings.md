
# InvitationRuleSiteBindings

## Описание ресурса

# Методы

## add

### Описание метода
Добавляет новую связь сценария вовлечения и сайта.<br/>Возможно существование только одной связи конкретного сайта и конкретного сценария вовлечения.<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*invitation_rule_id*|True|[numeric](/docs/types/numeric.md)|Сценарий вовлечения.<br/>|
|*employee_id*|False|[numeric](/docs/types/numeric.md)|ID сотрудника, на которого будет назначен чат или лид.<br/>|
|*site_id*|True|[numeric](/docs/types/numeric.md)|Сайт.<br/>|
|*department_id*|False|[numeric](/docs/types/numeric.md)|ID отдела, на который будет адресовано приглашение.<br/>|

### Результат
[InvitationRuleSiteBinding](/docs/types/InvitationRuleSiteBinding.md)
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
|*fields*|False|[string](/docs/types/string.md)|Список через запятую возвращаемых полей.<br/>|
|*id*|True|[numeric](/docs/types/numeric.md)|ID связи сценария вовлечения и сайта.<br/>|

### Результат
[InvitationRuleSiteBinding](/docs/types/InvitationRuleSiteBinding.md)
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
|*q*|False|[string](/docs/types/string.md)|Критерий поиска.<br/>Доступные поля:<br/>ids – idlist, список ID сценариев вовлечения;<br/>site_ids – idlist, список ID сайтов.<br/>|
|*fields*|False|[string](/docs/types/string.md)|Список через запятую возвращаемых полей.<br/>|
|*limit*|False|[numeric](/docs/types/numeric.md)|По умолчанию – 50.<br/>|
|*sort*|False|[string](/docs/types/string.md)|Сортировка результатов.<br/>Возможные значение:<br/>created_at:a – по умолчанию.<br/>|
|*offset*|False|[numeric](/docs/types/numeric.md)|По умолчанию – 0.<br/>|

### Результат
Array.<[InvitationRuleSiteBinding](/docs/types/InvitationRuleSiteBinding.md)>
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
|*invitation_rule_id*|False|[numeric](/docs/types/numeric.md)|Сценарий вовлечения.<br/>|
|*employee_id*|False|[numeric](/docs/types/numeric.md)|ID сотрудника, на которого будет назначен чат или лид.<br/>|
|*site_id*|False|[numeric](/docs/types/numeric.md)|Сайт.<br/>|
|*id*|True|[numeric](/docs/types/numeric.md)|ID связи.<br/>|
|*department_id*|False|[numeric](/docs/types/numeric.md)|ID отдела, на который будет адресовано приглашение.<br/>|

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
|*id*|True|[numeric](/docs/types/numeric.md)|ID связи.<br/>|

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
