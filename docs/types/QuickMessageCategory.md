
## QuickMessageCategory

### Описание типа
QuickMessageCategory
Категория быстрых сообщений.
Таблица 67. Поля быстрого сообщения

Контроллер: QuickMessageCategories.

### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|is_global|True|[boolean](/docs/types/boolean.md)|Признак глобальности категории.<br/>Если true, то категория видна всем сотрудникам. В противном случае - только сотруднику, создавшему категорию.<br/>|
|title|True|[string](/docs/types/string.md)|Название категории.<br/>|
|color|True|[string](/docs/types/string.md)|Цвет.<br/>Возможные значения:<br/>green – зеленый;<br/>orange – оранжевый;<br/>blue – синий;<br/>red – красный;<br/>purple – фиолетовый;<br/>gray – серый;<br/>rose – розовый;<br/>black – черный;<br/>yellow – желтый;<br/>white – белый.<br/>|
|created_at|True|[datetime](/docs/types/datetime.md)|Дата создания.<br/>|
|site|False|[Site](/docs/types/Site.md)|Сайт.<br/>Не указывается для персональных категорий, созданных сотрудниками (is_global = false). Такие категории не могут быть специфичными для сайтов.<br/>|
|updated_at|True|[datetime](/docs/types/datetime.md)|Дата последнего обновления.<br/>|
|id|True|[numeric](/docs/types/numeric.md)|ID категории быстрых сообщений.<br/>|
