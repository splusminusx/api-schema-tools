
## WARNING: Type is DEPRECATED

## CallLabelSettings

### Описание типа
CallLabelSettings - DEPRECATED<br/>ВНИМАНИЕ! Сущность является устаревшей. Ярлыка звонков больше не будет.<br/>Настройки ярлыка звонка.<br/>Таблица 15. Поля настроек ярлыка звонка.<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*is_visible*|True|[boolean](/docs/types/boolean.md)|Показывать ярлык.<br/>|
|*offset_value*|True|[numeric](/docs/types/numeric.md)|Значение отступа.<br/>Целое число в диапазоне:<br/>от 0 до 100 для offset_type = percent;<br/>от 0 до 2000 для offset_type = pixel.<br/>|
|*color*|True|[string](/docs/types/string.md)|Цветовая схема.<br/>Возможные значения:<br/>green – зеленая;<br/>orange – оранжевая;<br/>blue – синяя;<br/>red – красная;<br/>purple – фиолетовая;<br/>gray – серая;<br/>rose – розовая;<br/>black – черная;<br/>yellow – желтая;<br/>white – белая.<br/>|
|*updated_at*|True|[datetime](/docs/types/datetime.md)|Дата последнего обновления.<br/>|
|*offset_type*|True|[string](/docs/types/string.md)|Тип отступа.<br/>Возможные значения:<br/>pixel – в пикселах;<br/>percent – в процентах.<br/>|
|*is_custom*|True|[boolean](/docs/types/boolean.md)|Признак заказного дизайна ярлыка звонка.<br/>Если true, то изменение некоторых настроек может не иметь должного результата, поскольку соответствующий аспект внешнего вида переопределяются заказным дизайном.<br/>Это признак доступен только для чтения.<br/>|
|*department*|False|[Department](/docs/types/Department.md)|Отдел.<br/>|
|*position*|True|[string](/docs/types/string.md)|Положение ярлыка.<br/>Возможные значения:<br/>top – сверху;<br/>right – справа;<br/>bottom – снизу;<br/>left – слева.<br/>|
|*size*|True|[string](/docs/types/string.md)|Размер ярлыка.<br/>Возможные значения:<br/>small – маленький, 23x118 пикселей;<br/>large – большой, 38x174 пикселей.<br/>|
