
## Offering

### Описание типа
Offering
Доступные предложения - продукты (тарифы или опции), предлагаемые компанией LiveTex.
Таблица 55. Поля предложения


### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|quantity_min|False|numeric|Минимальное количество ресурсов.<br/>|
|is_tariff|False|boolean|Признак тарифа.<br/>Если false, то это опция.<br/>|
|description|False|string|Краткое описание предложения.<br/>|
|title|True|string|Название.<br/>|
|is_active|False|boolean|Признак активного предложения.<br/>Предполагается, что метод list возвращает только is_active = true, а вот метод show может вернуть данные и по тарифам, которые is_active = false. Тогда это поле даст понять, что тариф неактивен.<br/>|
|price|True|numeric|Цена.<br/>|
|quantity_max|False|numeric|Максимальное количество ресурсов.<br/>|
|days|False|numeric|Количество дней в продукте.<br/>|
|is_autorenewable|False|boolean|Признак, определяющий возможность автоматической пролонгации тарифа.<br/>|
|discount|False|numeric|Скидка в процентах.<br/>|
|is_trial|False|Boolean|Признак тестового тарифа/опции.<br/>Тестовые тарифы не могут быть подключены повторно.<br/>|
|next_offering|False|Offering|Для старых тарифов – тариф, на который автоматически произойдет переключение по завершении срока действия.<br/>|
|id|True|numeric|ID предложения.<br/>|
|resource_type|False|numeric|Тип предложения.<br/>Возможные значения:<br/>chat – чат;<br/>https – SSL;<br/>calls – переадресация;<br/>extend_license – расширение лицензии;<br/>lead – генератор лидов;<br/>cobrowse – кобрауз.<br/>|
