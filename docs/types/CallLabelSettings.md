
## WARNING: Type is DEPRECATED

## CallLabelSettings

### Описание типа
CallLabelSettings - DEPRECATED
ВНИМАНИЕ! Сущность является устаревшей. Ярлыка звонков больше не будет.
Настройки ярлыка звонка.
Таблица 15. Поля настроек ярлыка звонка.


### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|is_visible|True|boolean|Показывать ярлык.<br/>|
|offset_value|True|numeric|Значение отступа.<br/>Целое число в диапазоне:<br/>от 0 до 100 для offset_type = percent;<br/>от 0 до 2000 для offset_type = pixel.<br/>|
|color|True|string|Цветовая схема.<br/>Возможные значения:<br/>green – зеленая;<br/>orange – оранжевая;<br/>blue – синяя;<br/>red – красная;<br/>purple – фиолетовая;<br/>gray – серая;<br/>rose – розовая;<br/>black – черная;<br/>yellow – желтая;<br/>white – белая.<br/>|
|updated_at|True|datetime|Дата последнего обновления.<br/>|
|offset_type|True|string|Тип отступа.<br/>Возможные значения:<br/>pixel – в пикселах;<br/>percent – в процентах.<br/>|
|is_custom|True|boolean|Признак заказного дизайна ярлыка звонка.<br/>Если true, то изменение некоторых настроек может не иметь должного результата, поскольку соответствующий аспект внешнего вида переопределяются заказным дизайном.<br/>Это признак доступен только для чтения.<br/>|
|department|False|Department|Отдел.<br/>|
|position|True|string|Положение ярлыка.<br/>Возможные значения:<br/>top – сверху;<br/>right – справа;<br/>bottom – снизу;<br/>left – слева.<br/>|
|size|True|string|Размер ярлыка.<br/>Возможные значения:<br/>small – маленький, 23x118 пикселей;<br/>large – большой, 38x174 пикселей.<br/>|
