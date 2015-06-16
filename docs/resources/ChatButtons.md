
# ChatButtons

## Описание ресурса

# Методы

## add

### Описание метода
ChatButtons.add<br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*image_online*|False|[file](/docs/types/file.md)|Картинка кнопки, когда есть доступные операторы.<br/>Принимается во внимание при design_type = custom.<br/>Изображение в формате JPEG, GIF или PNG с длинной стороной не более 500 пикселей.<br/>Максимальный размер файла – 2 MB.<br/>|
|*color*|True|[string](/docs/types/string.md)|Цветовая схема.<br/>Возможные значения:<br/>green – зеленая;<br/>orange – оранжевая;<br/>blue – синяя;<br/>red – красная;<br/>purple – фиолетовая;<br/>gray – серая;<br/>rose – розовая;<br/>black – черная;<br/>yellow – желтая;<br/>white – белая.<br/>Принимается во внимание при design_type = predefined.<br/>|
|*design_type*|True|[string](/docs/types/string.md)|Тип дизайна.<br/>Возможные значения:<br/>predefined – предустановленный;<br/>custom – свой дизайн.<br/>|
|*site_id*|True|[numeric](/docs/types/numeric.md)|ID сайта.<br/>|
|*image_offline*|False|[file](/docs/types/file.md)|Картинка кнопки, когда нет доступных операторов.<br/>Принимается во внимание при design_type = custom.<br/>Изображение в формате JPEG, GIF или PNG с длинной стороной не более 500 пикселей.<br/>Максимальный размер файла – 2 MB.<br/>|
|*employee_id*|False|[numeric](/docs/types/numeric.md)|ID сотрудника.<br/>|
|*size*|True|[string](/docs/types/string.md)|Размер кнопки.<br/>Возможные значения:<br/>small – маленький, 146x50 пикселей;<br/>middle – средний,  193x69 пикселей;<br/>large – большой, 223x100 пикселей.<br/>Принимается во внимание при design_type=predefined.<br/>|
|*department_id*|False|[numeric](/docs/types/numeric.md)|ID отдел.<br/>|

### Результат
[ChatButton](/docs/types/ChatButton.md)
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|full||
|manager|managed|Создание кнопок на своих сайтах.|
|chief|managed|Создание кнопок на своих сайтах.|
|chief_partner|managed|Создание кнопок на своих сайтах.|
|operator|none||
|admin_partner|full||

## show

### Описание метода
ChatButtons.show<br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*fields*|False|[string](/docs/types/string.md)|Список через запятую возвращаемых полей.<br/>|
|*id*|True|[numeric](/docs/types/numeric.md)|ID кнопки.<br/>|

### Результат
[ChatButton](/docs/types/ChatButton.md)
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|full||
|manager|managed|Кнопки своих сайтов.|
|chief|managed|Кнопки своих сайтов.|
|chief_partner|managed|Кнопки своих сайтов.|
|operator|none||
|admin_partner|full||

## list

### Описание метода
ChatButtons.list<br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*q*|False|[string](/docs/types/string.md)|Критерий поиска.<br/>Доступные поля:<br/>ids – idlist, список ID кнопок;<br/>site_ids – idlist, список ID сайтов.<br/>|
|*fields*|False|[string](/docs/types/string.md)|Список через запятую возвращаемых полей.<br/>|
|*limit*|False|[numeric](/docs/types/numeric.md)|По умолчанию – 50.<br/>|
|*sort*|False|[string](/docs/types/string.md)|Сортировка результатов.<br/>Возможные значение:<br/>id:a – по умолчанию;<br/>updated_at:d.<br/>|
|*offset*|False|[numeric](/docs/types/numeric.md)|По умолчанию – 0.<br/>|

### Результат
Array.<[ChatButton](/docs/types/ChatButton.md)>
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|full||
|manager|managed|Кнопки своих сайтов.|
|chief|managed|Кнопки своих сайтов.|
|chief_partner|managed|Кнопки своих сайтов.|
|operator|none||
|admin_partner|full||

## update

### Описание метода
ChatButtons.update<br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*image_online*|False|[file](/docs/types/file.md)|Картинка кнопки, когда есть доступные операторы.<br/>Принимается во внимание при design_type = custom.<br/>Изображение в формате JPEG, GIF или PNG с длинной стороной не более 500 пикселей.<br/>Максимальный размер файла – 2 MB.<br/>|
|*color*|False|[string](/docs/types/string.md)|Цветовая схема.<br/>Возможные значения:<br/>green – зеленая;<br/>orange – оранжевая;<br/>blue – синяя;<br/>red – красная;<br/>purple – фиолетовая;<br/>gray – серая;<br/>rose – розовая;<br/>black – черная;<br/>yellow – желтая;<br/>white – белая.<br/>Принимается во внимание при design_type = predefined.<br/>|
|*design_type*|False|[string](/docs/types/string.md)|Тип дизайна.<br/>Возможные значения:<br/>predefined – предустановленный;<br/>custom – свой дизайн.<br/>|
|*site_id*|False|[numeric](/docs/types/numeric.md)|ID сайта.<br/>|
|*image_offline*|False|[file](/docs/types/file.md)|Картинка кнопки, когда нет доступных операторов.<br/>Принимается во внимание при design_type = custom.<br/>Изображение в формате JPEG, GIF или PNG с длинной стороной не более 500 пикселей.<br/>Максимальный размер файла – 2 MB.<br/>|
|*employee_id*|False|[numeric](/docs/types/numeric.md)|ID сотрудника.<br/>|
|*size*|False|[string](/docs/types/string.md)|Размер кнопки.<br/>Возможные значения:<br/>small – маленький, 146x50 пикселей;<br/>middle – средний,  193x69 пикселей;<br/>large – большой, 223x100 пикселей.<br/>|
|*id*|True|[numeric](/docs/types/numeric.md)|ID кнопки.<br/>|
|*department_id*|False|[numeric](/docs/types/numeric.md)|ID отдел.<br/>|

### Результат
None
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|full||
|manager|managed|Обновление кнопок на своих сайтах.|
|chief|managed|Обновление кнопок на своих сайтах.|
|chief_partner|managed|Обновление кнопок на своих сайтах.|
|operator|none||
|admin_partner|full||

## delete

### Описание метода
ChatButtons.delete<br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*id*|True|[numeric](/docs/types/numeric.md)|ID кнопки.<br/>|

### Результат
None
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|full||
|manager|managed|Кнопки своих сайтов.|
|chief|managed|Кнопки своих сайтов.|
|chief_partner|managed|Кнопки своих сайтов.|
|operator|none||
|admin_partner|full||
