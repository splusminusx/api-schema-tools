
## QuickMessageCategory

### Описание типа
Категория быстрых сообщений.<br/><br/>Контроллер: QuickMessageCategories.<br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*is_global*|True|[boolean](/types/boolean)|Признак глобальности категории.<br/>Если true, то категория видна всем сотрудникам. В противном случае - только сотруднику, создавшему категорию.<br/>|
|*title*|True|[string](/types/string)|Название категории.<br/>|
|*color*|True|[string](/types/string)|Цвет.<br/>Возможные значения:<br/>green – зеленый;<br/>orange – оранжевый;<br/>blue – синий;<br/>red – красный;<br/>purple – фиолетовый;<br/>gray – серый;<br/>rose – розовый;<br/>black – черный;<br/>yellow – желтый;<br/>white – белый.<br/>|
|*created_at*|True|[datetime](/types/datetime)|Дата создания.<br/>|
|*site*|False|[Site](/types/Site)|Сайт.<br/>Не указывается для персональных категорий, созданных сотрудниками (is_global = false). Такие категории не могут быть специфичными для сайтов.<br/>|
|*updated_at*|True|[datetime](/types/datetime)|Дата последнего обновления.<br/>|
|*id*|True|[numeric](/types/numeric)|ID категории быстрых сообщений.<br/>|
