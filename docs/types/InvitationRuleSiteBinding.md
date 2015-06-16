## InvitationRuleSiteBinding
### Описание типа
InvitationRuleSiteBinding
Связь сценария вовлечения и сайта.
Таблица 48. Поля связи сценария вовлечения и сайта.

### Поля
| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|invitation_rule|True|InvitationRule|Сценарий вовлечения.<br/>|
|created_at|False|datetime|Дата создания.<br/>|
|site|True|Site|Сайт.<br/>|
|updated_at|False|datetime|Дата последнего изменения.<br/>|
|department|False|Department|Отдел, на который будет адресовано приглашение.<br/>|
|employee|False|Employee|Сотрудник, на которого будет назначен чат или лид.<br/>|
|id|True|numeric|ID связи.<br/>|
