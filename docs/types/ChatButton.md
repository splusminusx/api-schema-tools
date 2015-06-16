
## ChatButton

### Описание типа
ChatButton<br/>Кнопка чата.<br/> Таблица 20. Поля кнопки чата<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|image_online|False|[file](/docs/types/file.md)|Картинка кнопки, когда есть доступные операторы.<br/>Принимается во внимание при design_type = custom.<br/>Изображение в формате JPEG, GIF или PNG с длинной стороной не более 500 пикселей.<br/>Максимальный размер файла – 2 MB.<br/>|
|color|True|[string](/docs/types/string.md)|Цветовая схема.<br/>Возможные значения:<br/>green – зеленая;<br/>orange – оранжевая;<br/>blue – синяя;<br/>red – красная;<br/>purple – фиолетовая;<br/>gray – серая;<br/>rose – розовая;<br/>black – черная;<br/>yellow – желтая;<br/>white – белая.<br/>Принимается во внимание при design_type=predefined.<br/>|
|created_at|True|[datetime](/docs/types/datetime.md)|Дата создания.<br/>|
|site|True|[Site](/docs/types/Site.md)|Сайт, на котором размещается кнопка.<br/>|
|image_offline|False|[file](/docs/types/file.md)|Картинка кнопки, когда нет доступных операторов.<br/>Принимается во внимание при design_type = custom.<br/>Изображение в формате JPEG, GIF или PNG с длинной стороной не более 500 пикселей.<br/>Максимальный размер файла – 2 MB.<br/>|
|updated_at|True|[datetime](/docs/types/datetime.md)|Дата последнего обновления.<br/>|
|department|False|[Department](/docs/types/Department.md)|Отдел.<br/>|
|id|True|[numeric](/docs/types/numeric.md)|ID кнопки.<br/>|
|employee|False|[Employee](/docs/types/Employee.md)|Сотрудник.<br/>|
|design_type|True|[string](/docs/types/string.md)|Тип дизайна.<br/>Возможные значения:<br/>predefined – предустановленный;<br/>custom – свой дизайн.<br/>|
|size|True|[string](/docs/types/string.md)|Размер кнопки.<br/>Возможные значения:<br/>small – маленький, 146x50 пикселей;<br/>middle – средний,  193x69 пикселей;<br/>large – большой, 223x100 пикселей.<br/>Принимается во внимание при design_type=predefined.<br/>|
