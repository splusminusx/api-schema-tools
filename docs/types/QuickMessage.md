
## QuickMessage

### Описание типа
Быстрое сообщение.<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*category*|True|[QuickMessageCategory](/types/QuickMessageCategory)|Категория быстрых сообщений.<br/>|
|*is_global*|True|[boolean](/types/boolean)|Признак глобальности сообщения.<br/>Если true, то сообщение видно всем сотрудникам. В противном случае - только сотруднику, создавшему сообщение.<br/>|
|*is_common*|True|[boolean](/types/boolean)|Признак того, является ли быстрое сообщение общедоступным.<br/>|
|*text*|True|[string](/types/string)|Текст быстрого сообщения.<br/>Максимум 2000 символов.<br/>|
|*created_at*|True|[datetime](/types/datetime)|Дата создания.<br/>|
|*updated_at*|True|[datetime](/types/datetime)|Дата последнего обновления.<br/>|
|*creator_id*|True|[numeric](/types/numeric)|ID сотрудника создавшего быстрое сообщение.<br/>|
|*id*|True|[numeric](/types/numeric)|ID быстрого сообщения.<br/>|
