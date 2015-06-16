
# QuickMessageCategories

## Описание ресурса

# Методы

## add

### Описание метода
Добавляет новую категорию быстрых сообщений.<br/>Объект типа «QuickMessageCategory».<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*color*|False|[string](/docs/types/string.md)|Цвет.<br/>Возможные значения:<br/>green – зеленый;<br/>orange – оранжевый;<br/>blue – синий;<br/>red – красный;<br/>purple – фиолетовый;<br/>gray – серый;<br/>rose – розовый;<br/>black – черный;<br/>yellow – желтый;<br/>white – белый.<br/>По умолчанию новой категории назначается следующий по порядку цвет относительно хронологически последней созданной категории в сайте.<br/>|
|*is_global*|True|[boolean](/docs/types/boolean.md)|Признак глобальности категории.<br/>Если false, то значение site_id игнорируется, поскольку персональные категории сотрудников не связаны с сайтами.<br/>|
|*site_id*|False|[numeric](/docs/types/numeric.md)|ID сайт.<br/>Должен быть указан, если is_global = true.<br/>|
|*title*|True|[string](/docs/types/string.md)|Название категории.<br/>|

### Результат
[QuickMessageCategory](/docs/types/QuickMessageCategory.md)
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|*admin*|full||
|*manager*|managed|Категории быстрые сообщения с is_global = true разрешается создавать только на своих сайтах.|
|*chief*|managed|Категории быстрые сообщения с is_global = true разрешается создавать только на своих сайтах.|
|*chief_partner*|managed|Категории быстрые сообщения с is_global = true разрешается создавать только на своих сайтах.|
|*operator*|user|Разрешается создавать категорий сообщений только с is_global = false.|
|*admin_partner*|full||

## show

### Описание метода
Возвращает данные указанной категории быстрых сообщений.<br/>Объект типа «QuickMessageCategory».<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*fields*|False|[string](/docs/types/string.md)|Список через запятую возвращаемых полей.<br/>|
|*id*|True|[numeric](/docs/types/numeric.md)|ID категории быстрых сообщений.<br/>|

### Результат
[QuickMessageCategory](/docs/types/QuickMessageCategory.md)
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|*admin*|full|За исключением чужих категорий быстрых сообщений с is_global = false.|
|*manager*|full|За исключением чужих категорий быстрых сообщений с is_global = false.|
|*chief*|full|За исключением чужих категорий быстрых сообщений с is_global = false.|
|*chief_partner*|full|За исключением чужих категорий быстрых сообщений с is_global = false.|
|*operator*|full|За исключением чужих категорий быстрых сообщений с is_global = false.|
|*admin_partner*|full|За исключением чужих категорий быстрых сообщений с is_global = false.|

## list

### Описание метода
Возвращает список глобальных категорий быстрых сообщений, а также персональных категорий, созданных текущим пользователем.<br/>Массив объектов типа «QuickMessageCategory».<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*q*|False|[string](/docs/types/string.md)|Критерий поиска.<br/>Доступные поля:<br/>ids – idlist, список ID категорий быстрых сообщений;<br/>site_ids – idlist, список ID сайтов.<br/>|
|*fields*|False|[string](/docs/types/string.md)|Список через запятую возвращаемых полей.<br/>|
|*limit*|False|[numeric](/docs/types/numeric.md)|По умолчанию – 50.<br/>|
|*sort*|False|[string](/docs/types/string.md)|Сортировка результатов.<br/>Возможные значение:<br/>title:a – по умолчанию.<br/>|
|*offset*|False|[numeric](/docs/types/numeric.md)|По умолчанию – 0.<br/>|

### Результат
Array.<[QuickMessageCategory](/docs/types/QuickMessageCategory.md)>
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|*admin*|full|За исключением чужих категорий быстрых сообщений с is_global = false.|
|*manager*|full|За исключением чужих категорий быстрых сообщений с is_global = false.|
|*chief*|full|За исключением чужих категорий быстрых сообщений с is_global = false.|
|*chief_partner*|full|За исключением чужих категорий быстрых сообщений с is_global = false.|
|*operator*|full|За исключением чужих категорий быстрых сообщений с is_global = false.|
|*admin_partner*|full|За исключением чужих категорий быстрых сообщений с is_global = false.|

## update

### Описание метода
Обновляет категорию быстрых сообщений.<br/>Метод ничего не возвращает.<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*color*|False|[string](/docs/types/string.md)|Цвет.<br/>Возможные значения:<br/>green – зеленый;<br/>orange – оранжевый;<br/>blue – синий;<br/>red – красный;<br/>purple – фиолетовый;<br/>gray – серый;<br/>rose – розовый;<br/>black – черный;<br/>yellow – желтый;<br/>white – белый.<br/>|
|*site_id*|False|[numeric](/docs/types/numeric.md)|ID сайта.<br/>Принимается во внимание только для глобальных категорий, поскольку персональные категории не связаны с сайтами.<br/>|
|*id*|True|[numeric](/docs/types/numeric.md)|ID категории быстрых сообщений.<br/>|
|*title*|False|[string](/docs/types/string.md)|Название категории.<br/>|

### Результат
None
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|*admin*|full|Только категории быстрые сообщения с is_global = true, а также свои категории с is_global = false.|
|*manager*|managed|Категории быстрые сообщения с is_global = true разрешается обновлять только на своих сайтах.|
|*chief*|managed|Категории быстрые сообщения с is_global = true разрешается обновлять только на своих сайтах.|
|*chief_partner*|managed|Категории быстрые сообщения с is_global = true разрешается обновлять только на своих сайтах.|
|*operator*|user|Разрешается обновлять только свои категории сообщений с is_global = false.|
|*admin_partner*|full|Только категории быстрые сообщения с is_global = true, а также свои категории с is_global = false.|

## delete

### Описание метода
Удаляет указанную категорию быстрых сообщений.<br/>Метод ничего не возвращает.<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*id*|True|[numeric](/docs/types/numeric.md)|ID категории быстрых сообщений.<br/>|

### Результат
None
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|*admin*|full|Только категории быстрые сообщения с is_global = true, а также свои категории с is_global = false.|
|*manager*|managed|Категории быстрые сообщения с is_global = true разрешается удалять только на своих сайтах.|
|*chief*|managed|Категории быстрые сообщения с is_global = true разрешается удалять только на своих сайтах.|
|*chief_partner*|managed|Категории быстрые сообщения с is_global = true разрешается удалять только на своих сайтах.|
|*operator*|user|Разрешается удалять только свои категории сообщений с is_global = false.|
|*admin_partner*|full|Только категории быстрые сообщения с is_global = true, а также свои категории с is_global = false.|
