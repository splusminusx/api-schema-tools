
# InvitationRuleSiteBindings

## Описание ресурса
InvitationRuleSiteBindings<br/>
# Методы

## add

### Описание метода
InvitationRuleSiteBindings.add<br/>Добавляет новую связь сценария вовлечения и сайта.<br/>Возможно существование только одной связи конкретного сайта и конкретного сценария вовлечения.<br/>Параметры<br/>Результат<br/>Объект типа «InvitationRuleSiteBinding».<br/>Уровень доступа для ролей<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|**invitation_rule_id**|True|[numeric](/docs/types/numeric.md)|Сценарий вовлечения.<br/>|
|**employee_id**|False|[numeric](/docs/types/numeric.md)|ID сотрудника, на которого будет назначен чат или лид.<br/>|
|**site_id**|True|[numeric](/docs/types/numeric.md)|Сайт.<br/>|
|**department_id**|False|[numeric](/docs/types/numeric.md)|ID отдела, на который будет адресовано приглашение.<br/>|

### Резудьтат
[InvitationRuleSiteBinding](/docs/types/InvitationRuleSiteBinding.md)
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner
## show

### Описание метода
InvitationRuleSiteBindings.show<br/>Возвращает данные указанной связи сценария вовлечения и сайта.<br/>Параметры<br/>Результат<br/>Объект типа «InvitationRuleSiteBinding».<br/>Уровень доступа для ролей<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|**fields**|False|[string](/docs/types/string.md)|Список через запятую возвращаемых полей.<br/>|
|**id**|True|[numeric](/docs/types/numeric.md)|ID связи сценария вовлечения и сайта.<br/>|

### Резудьтат
[InvitationRuleSiteBinding](/docs/types/InvitationRuleSiteBinding.md)
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner
## list

### Описание метода
InvitationRuleSiteBindings.list<br/>Возвращает список связей сценариев вовлечения и сайтов.<br/>Параметры<br/>Результат<br/>Массив объектов типа «InvitationRuleSiteBinding».<br/>Уровень доступа для ролей<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|**q**|False|[string](/docs/types/string.md)|Критерий поиска.<br/>Доступные поля:<br/>ids – idlist, список ID сценариев вовлечения;<br/>site_ids – idlist, список ID сайтов.<br/>|
|**fields**|False|[string](/docs/types/string.md)|Список через запятую возвращаемых полей.<br/>|
|**limit**|False|[numeric](/docs/types/numeric.md)|По умолчанию – 50.<br/>|
|**sort**|False|[string](/docs/types/string.md)|Сортировка результатов.<br/>Возможные значение:<br/>created_at:a – по умолчанию.<br/>|
|**offset**|False|[numeric](/docs/types/numeric.md)|По умолчанию – 0.<br/>|

### Резудьтат
Array.<[InvitationRuleSiteBinding](/docs/types/InvitationRuleSiteBinding.md)>
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner
## update

### Описание метода
InvitationRuleSiteBindings.update<br/>Изменяет указанную связь сценария вовлечения и сайта.<br/>Возможно существование только одной связи конкретного сайта и конкретного сценария вовлечения.<br/>Параметры<br/>Результат<br/>Метод ничего не возвращает.<br/>Уровень доступа для ролей<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|**invitation_rule_id**|False|[numeric](/docs/types/numeric.md)|Сценарий вовлечения.<br/>|
|**employee_id**|False|[numeric](/docs/types/numeric.md)|ID сотрудника, на которого будет назначен чат или лид.<br/>|
|**site_id**|False|[numeric](/docs/types/numeric.md)|Сайт.<br/>|
|**id**|True|[numeric](/docs/types/numeric.md)|ID связи.<br/>|
|**department_id**|False|[numeric](/docs/types/numeric.md)|ID отдела, на который будет адресовано приглашение.<br/>|

### Резудьтат
None
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner
## delete

### Описание метода
InvitationRuleSiteBindings.delete<br/>Удаляет указанную связь сценария вовлечения и сайта.<br/>Параметры<br/>Результат<br/>Метод ничего не возвращает.<br/>Уровень доступа для ролей<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|**id**|True|[numeric](/docs/types/numeric.md)|ID связи.<br/>|

### Резудьтат
None
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner