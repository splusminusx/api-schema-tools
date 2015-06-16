
## ChatButton

### Описание типа
ChatButton
Кнопка чата.
 Таблица 20. Поля кнопки чата


### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|image_online|False|None|Картинка кнопки, когда есть доступные операторы.<br/>Принимается во внимание при design_type = custom.<br/>Изображение в формате JPEG, GIF или PNG с длинной стороной не более 500 пикселей.<br/>Максимальный размер файла – 2 MB.<br/>|
|color|True|None|Цветовая схема.<br/>Возможные значения:<br/>green – зеленая;<br/>orange – оранжевая;<br/>blue – синяя;<br/>red – красная;<br/>purple – фиолетовая;<br/>gray – серая;<br/>rose – розовая;<br/>black – черная;<br/>yellow – желтая;<br/>white – белая.<br/>Принимается во внимание при design_type=predefined.<br/>|
|created_at|True|None|Дата создания.<br/>|
|site|True|None|Сайт, на котором размещается кнопка.<br/>|
|image_offline|False|None|Картинка кнопки, когда нет доступных операторов.<br/>Принимается во внимание при design_type = custom.<br/>Изображение в формате JPEG, GIF или PNG с длинной стороной не более 500 пикселей.<br/>Максимальный размер файла – 2 MB.<br/>|
|updated_at|True|None|Дата последнего обновления.<br/>|
|department|False|None|Отдел.<br/>|
|id|True|None|ID кнопки.<br/>|
|employee|False|None|Сотрудник.<br/>|
|design_type|True|None|Тип дизайна.<br/>Возможные значения:<br/>predefined – предустановленный;<br/>custom – свой дизайн.<br/>|
|size|True|None|Размер кнопки.<br/>Возможные значения:<br/>small – маленький, 146x50 пикселей;<br/>middle – средний,  193x69 пикселей;<br/>large – большой, 223x100 пикселей.<br/>Принимается во внимание при design_type=predefined.<br/>|
