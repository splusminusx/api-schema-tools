
## Complaint

### Описание типа
Complaint<br/>Жалоба посетителя.<br/>Таблица 26. Поля жалобы посетителя<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|**phone**|False|[string](/docs/types/string.md)|Номер телефона.<br/>Одно из полей email или phone должно быть указано.<br/>|
|**text**|True|[string](/docs/types/string.md)|Текст жалобы.<br/>|
|**created_at**|True|[datetime](/docs/types/datetime.md)|Дата создания.<br/>|
|**updated_at**|True|[datetime](/docs/types/datetime.md)|Дата последнего обновления.<br/>|
|**site**|True|[Site](/docs/types/Site.md)|Сайт.<br/>|
|**conversation**|True|[Conversation](/docs/types/Conversation.md)|Обращение, в ходе которого отправлена жалоба.<br/>|
|**department**|False|[Department](/docs/types/Department.md)|Отдел.<br/>|
|**id**|True|[string](/docs/types/string.md)|ID жалобы.<br/>|
|**visitor**|True|[Visitor](/docs/types/Visitor.md)|Посетитель.<br/>|
|**employee**|False|[Employee](/docs/types/Employee.md)|Сотрудник.<br/><br/>|
|**email**|False|[string](/docs/types/string.md)|Адрес электронной почты.<br/>Одно из полей email или phone должно быть указано.<br/>|
