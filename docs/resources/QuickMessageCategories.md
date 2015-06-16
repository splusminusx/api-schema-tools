
# QuickMessageCategories

## Описание ресурса

# Методы

## add

### Описание метода
QuickMessageCategories.add<br/>
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
|admin|manager|chief|chief_partner|operator|admin_partner
## show

### Описание метода
QuickMessageCategories.show<br/>
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
|admin|manager|chief|chief_partner|operator|admin_partner
## list

### Описание метода
QuickMessageCategories.list<br/>
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
|admin|manager|chief|chief_partner|operator|admin_partner
## update

### Описание метода
QuickMessageCategories.update<br/>
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
|admin|manager|chief|chief_partner|operator|admin_partner
## delete

### Описание метода
QuickMessageCategories.delete<br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*id*|True|[numeric](/docs/types/numeric.md)|ID категории быстрых сообщений.<br/>|

### Результат
None
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner