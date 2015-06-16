
## DepartmentSiteBinding

### Описание типа
DepartmentSiteBinding
Связь отдела и сайта.
Таблица 34. Поля связи отдела и сайта


### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|prechats_chat|False|Array.<Prechat>|Массив пречат-полей.<br/>Максимум 2 элемента.<br/>|
|is_visible|True|boolean|Признак видимости отдела в сайте.<br/>|
|created_at|True|datetime|Дата создания.<br/>|
|site|True|Site|Сайт.<br/>|
|updated_at|True|datetime|Дата последнего обновления.<br/>|
|alias|True|string|Имя, под которым отдел будет виден на сайте.<br/>|
|department|True|Department|Отдел.<br/>|
|position|True|numeric|Порядковый номер отдела на данном сайте.<br/>|
|callback_url|False|string|Настройка Callback URL.<br/>|
|id|True|numeric|ID связи.<br/>|
