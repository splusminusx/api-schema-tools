
## DepartmentSiteBinding

### Описание типа
DepartmentSiteBinding
Связь отдела и сайта.
Таблица 34. Поля связи отдела и сайта


### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|prechats_chat|False|Array.<[Prechat](/docs/types/Prechat.md)>|Массив пречат-полей.<br/>Максимум 2 элемента.<br/>|
|is_visible|True|None|Признак видимости отдела в сайте.<br/>|
|created_at|True|None|Дата создания.<br/>|
|site|True|None|Сайт.<br/>|
|updated_at|True|None|Дата последнего обновления.<br/>|
|alias|True|None|Имя, под которым отдел будет виден на сайте.<br/>|
|department|True|None|Отдел.<br/>|
|position|True|None|Порядковый номер отдела на данном сайте.<br/>|
|callback_url|False|None|Настройка Callback URL.<br/>|
|id|True|None|ID связи.<br/>|
