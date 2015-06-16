
## Contact

### Описание типа
Contact<br/>Контактные данные.<br/>Таблица 28. Поля элемента контактных данных<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|**name**|True|[string](/docs/types/string.md)|Имя, которое указал посетитель.<br/>|
|**visitor**|True|[Visitor](/docs/types/Visitor.md)|Посетитель, оставивший контактные данные.<br/>|
|**created_at**|True|[datetime](/docs/types/datetime.md)|Дата и время извлечения контактных данных.<br/>|
|**creator_type**|True|[string](/docs/types/string.md)|Тип создателя контактных данных.<br/>Возможные значения:<br/>employee – сотрудник,<br/>visitor – посетитель.<br/>|
|**site**|True|[Site](/docs/types/Site.md)|Сайт, на котором получены контактные данные.<br/>|
|**source_type**|True|[string](/docs/types/string.md)|Тип источника контактных данных.<br/>Возможные значения:<br/>chat – чат,<br/>lead – лид,<br/>complaint – жалоба.<br/>|
|**type**|True|[string](/docs/types/string.md)|Тип элемента контактных данных.<br/>Возможные значения:<br/>email – адрес электронной почты,<br/>phone – номер телефона.<br/>|
|**source_id**|True|[string](/docs/types/string.md)|ID объекта, из которого получены контактные данные.<br/>|
|**data**|True|[string](/docs/types/string.md)|Значение элемента контактных данных – конкретный адрес электронной почты или номер телефона.<br/>|
|**id**|True|[numeric](/docs/types/numeric.md)|ID элемента контактных данных.<br/>|
|**is_auto**|True|[boolean](/docs/types/boolean.md)|Признак автоматического извлечения контактных данных.<br/>true - данный извлечены из текста чата/лида/жалобы.<br/>false - данные введены пользователем в соответствующие поля формы.<br/>|
