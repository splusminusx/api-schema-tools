
## InvitationRuleSiteBinding

### Описание типа
Связь сценария вовлечения и сайта.<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*invitation_rule*|True|[InvitationRule](/types/InvitationRule)|Сценарий вовлечения.<br/>|
|*created_at*|False|[datetime](/types/datetime)|Дата создания.<br/>|
|*site*|True|[Site](/types/Site)|Сайт.<br/>|
|*updated_at*|False|[datetime](/types/datetime)|Дата последнего изменения.<br/>|
|*department*|False|[Department](/types/Department)|Отдел, на который будет адресовано приглашение.<br/>|
|*employee*|False|[Employee](/types/Employee)|Сотрудник, на которого будет назначен чат или лид.<br/>|
|*id*|True|[numeric](/types/numeric)|ID связи.<br/>|
