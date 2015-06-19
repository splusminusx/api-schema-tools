
## DepartmentSiteBinding

### Описание типа
Связь отдела и сайта.<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*prechats_chat*|False|Array.<[Prechat](/types/Prechat)>|Массив пречат-полей.<br/>Максимум 2 элемента.<br/>|
|*is_visible*|True|[boolean](/types/boolean)|Признак видимости отдела в сайте.<br/>|
|*created_at*|True|[datetime](/types/datetime)|Дата создания.<br/>|
|*site*|True|[Site](/types/Site)|Сайт.<br/>|
|*updated_at*|True|[datetime](/types/datetime)|Дата последнего обновления.<br/>|
|*alias*|True|[string](/types/string)|Имя, под которым отдел будет виден на сайте.<br/>|
|*department*|True|[Department](/types/Department)|Отдел.<br/>|
|*position*|True|[numeric](/types/numeric)|Порядковый номер отдела на данном сайте.<br/>|
|*callback_url*|False|[string](/types/string)|Настройка Callback URL.<br/>|
|*id*|True|[numeric](/types/numeric)|ID связи.<br/>|
