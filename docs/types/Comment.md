
## Comment

### Описание типа
Комментарий к обращению в поддержку.<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*employee*|False|[Employee](/types/Employee)|Сотрудник, пославший комментарий.<br/>Если null, то отправителем является сотрудник LiveTex.<br/>|
|*text*|True|[string](/types/string)|Текст комментария.<br/>Максимум 2000 символов.<br/>|
|*ticket*|True|[Ticket](/types/Ticket)|Обращение в поддержку.<br/>|
|*id*|True|[numeric](/types/numeric)|ID комментария.<br/>|
|*created_at*|True|[datetime](/types/datetime)|Дата создания.<br/>|
