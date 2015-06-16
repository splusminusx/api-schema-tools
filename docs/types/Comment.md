
## Comment

### Описание типа
Комментарий к обращению в поддержку.<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*employee*|False|[Employee](/docs/types/Employee.md)|Сотрудник, пославший комментарий.<br/>Если null, то отправителем является сотрудник LiveTex.<br/>|
|*text*|True|[string](/docs/types/string.md)|Текст комментария.<br/>Максимум 2000 символов.<br/>|
|*ticket*|True|[Ticket](/docs/types/Ticket.md)|Обращение в поддержку.<br/>|
|*id*|True|[numeric](/docs/types/numeric.md)|ID комментария.<br/>|
|*created_at*|True|[datetime](/docs/types/datetime.md)|Дата создания.<br/>|
