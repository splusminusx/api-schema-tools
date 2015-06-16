
## DepartmentSiteBinding

### Описание типа
DepartmentSiteBinding<br/>Связь отдела и сайта.<br/>Таблица 34. Поля связи отдела и сайта<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|**prechats_chat**|False|Array.<[Prechat](/docs/types/Prechat.md)>|Массив пречат-полей.<br/>Максимум 2 элемента.<br/>|
|**is_visible**|True|[boolean](/docs/types/boolean.md)|Признак видимости отдела в сайте.<br/>|
|**created_at**|True|[datetime](/docs/types/datetime.md)|Дата создания.<br/>|
|**site**|True|[Site](/docs/types/Site.md)|Сайт.<br/>|
|**updated_at**|True|[datetime](/docs/types/datetime.md)|Дата последнего обновления.<br/>|
|**alias**|True|[string](/docs/types/string.md)|Имя, под которым отдел будет виден на сайте.<br/>|
|**department**|True|[Department](/docs/types/Department.md)|Отдел.<br/>|
|**position**|True|[numeric](/docs/types/numeric.md)|Порядковый номер отдела на данном сайте.<br/>|
|**callback_url**|False|[string](/docs/types/string.md)|Настройка Callback URL.<br/>|
|**id**|True|[numeric](/docs/types/numeric.md)|ID связи.<br/>|
