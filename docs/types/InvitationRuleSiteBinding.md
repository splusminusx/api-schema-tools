
## InvitationRuleSiteBinding

### Описание типа
InvitationRuleSiteBinding<br/>Связь сценария вовлечения и сайта.<br/>Таблица 48. Поля связи сценария вовлечения и сайта.<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*invitation_rule*|True|[InvitationRule](/docs/types/InvitationRule.md)|Сценарий вовлечения.<br/>|
|*created_at*|False|[datetime](/docs/types/datetime.md)|Дата создания.<br/>|
|*site*|True|[Site](/docs/types/Site.md)|Сайт.<br/>|
|*updated_at*|False|[datetime](/docs/types/datetime.md)|Дата последнего изменения.<br/>|
|*department*|False|[Department](/docs/types/Department.md)|Отдел, на который будет адресовано приглашение.<br/>|
|*employee*|False|[Employee](/docs/types/Employee.md)|Сотрудник, на которого будет назначен чат или лид.<br/>|
|*id*|True|[numeric](/docs/types/numeric.md)|ID связи.<br/>|
