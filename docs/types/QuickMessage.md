
## QuickMessage

### Описание типа
Быстрое сообщение.<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*category*|True|[QuickMessageCategory](/docs/types/QuickMessageCategory.md)|Категория быстрых сообщений.<br/>|
|*is_global*|True|[boolean](/docs/types/boolean.md)|Признак глобальности сообщения.<br/>Если true, то сообщение видно всем сотрудникам. В противном случае - только сотруднику, создавшему сообщение.<br/>|
|*is_common*|True|[boolean](/docs/types/boolean.md)|Признак того, является ли быстрое сообщение общедоступным.<br/>|
|*text*|True|[string](/docs/types/string.md)|Текст быстрого сообщения.<br/>Максимум 2000 символов.<br/>|
|*created_at*|True|[datetime](/docs/types/datetime.md)|Дата создания.<br/>|
|*updated_at*|True|[datetime](/docs/types/datetime.md)|Дата последнего обновления.<br/>|
|*creator_id*|True|[numeric](/docs/types/numeric.md)|ID сотрудника создавшего быстрое сообщение.<br/>|
|*id*|True|[numeric](/docs/types/numeric.md)|ID быстрого сообщения.<br/>|
