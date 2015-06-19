
# ChatButtons

## Описание ресурса

# Методы

## add

### Описание метода
Создает новую кнопку.<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*image_online*|False|[file](/types/file)|Картинка кнопки, когда есть доступные операторы.<br/>Принимается во внимание при design_type = custom.<br/>Изображение в формате JPEG, GIF или PNG с длинной стороной не более 500 пикселей.<br/>Максимальный размер файла – 2 MB.<br/>|
|*color*|True|[string](/types/string)|Цветовая схема.<br/>Возможные значения:<br/>green – зеленая;<br/>orange – оранжевая;<br/>blue – синяя;<br/>red – красная;<br/>purple – фиолетовая;<br/>gray – серая;<br/>rose – розовая;<br/>black – черная;<br/>yellow – желтая;<br/>white – белая.<br/>Принимается во внимание при design_type = predefined.<br/>|
|*design_type*|True|[string](/types/string)|Тип дизайна.<br/>Возможные значения:<br/>predefined – предустановленный;<br/>custom – свой дизайн.<br/>|
|*site_id*|True|[numeric](/types/numeric)|ID сайта.<br/>|
|*image_offline*|False|[file](/types/file)|Картинка кнопки, когда нет доступных операторов.<br/>Принимается во внимание при design_type = custom.<br/>Изображение в формате JPEG, GIF или PNG с длинной стороной не более 500 пикселей.<br/>Максимальный размер файла – 2 MB.<br/>|
|*employee_id*|False|[numeric](/types/numeric)|ID сотрудника.<br/>|
|*size*|True|[string](/types/string)|Размер кнопки.<br/>Возможные значения:<br/>small – маленький, 146x50 пикселей;<br/>middle – средний,  193x69 пикселей;<br/>large – большой, 223x100 пикселей.<br/>Принимается во внимание при design_type=predefined.<br/>|
|*department_id*|False|[numeric](/types/numeric)|ID отдел.<br/>|

### Результат
[ChatButton](/types/ChatButton)
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|*admin*|full||
|*manager*|managed|Создание кнопок на своих сайтах.|
|*chief*|managed|Создание кнопок на своих сайтах.|
|*chief_partner*|managed|Создание кнопок на своих сайтах.|
|*operator*|none||
|*admin_partner*|full||

## show

### Описание метода
Возвращает данные указанной кнопки.<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*fields*|False|[string](/types/string)|Список через запятую возвращаемых полей.<br/>|
|*id*|True|[numeric](/types/numeric)|ID кнопки.<br/>|

### Результат
[ChatButton](/types/ChatButton)
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|*admin*|full||
|*manager*|managed|Кнопки своих сайтов.|
|*chief*|managed|Кнопки своих сайтов.|
|*chief_partner*|managed|Кнопки своих сайтов.|
|*operator*|none||
|*admin_partner*|full||

## list

### Описание метода
Возвращает список кнопок.<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*q*|False|[string](/types/string)|Критерий поиска.<br/>Доступные поля:<br/>ids – idlist, список ID кнопок;<br/>site_ids – idlist, список ID сайтов.<br/>|
|*fields*|False|[string](/types/string)|Список через запятую возвращаемых полей.<br/>|
|*limit*|False|[numeric](/types/numeric)|По умолчанию – 50.<br/>|
|*sort*|False|[string](/types/string)|Сортировка результатов.<br/>Возможные значение:<br/>id:a – по умолчанию;<br/>updated_at:d.<br/>|
|*offset*|False|[numeric](/types/numeric)|По умолчанию – 0.<br/>|

### Результат
Array.<[ChatButton](/types/ChatButton)>
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|*admin*|full||
|*manager*|managed|Кнопки своих сайтов.|
|*chief*|managed|Кнопки своих сайтов.|
|*chief_partner*|managed|Кнопки своих сайтов.|
|*operator*|none||
|*admin_partner*|full||

## update

### Описание метода
Изменяет указанную кнопку.<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*image_online*|False|[file](/types/file)|Картинка кнопки, когда есть доступные операторы.<br/>Принимается во внимание при design_type = custom.<br/>Изображение в формате JPEG, GIF или PNG с длинной стороной не более 500 пикселей.<br/>Максимальный размер файла – 2 MB.<br/>|
|*color*|False|[string](/types/string)|Цветовая схема.<br/>Возможные значения:<br/>green – зеленая;<br/>orange – оранжевая;<br/>blue – синяя;<br/>red – красная;<br/>purple – фиолетовая;<br/>gray – серая;<br/>rose – розовая;<br/>black – черная;<br/>yellow – желтая;<br/>white – белая.<br/>Принимается во внимание при design_type = predefined.<br/>|
|*design_type*|False|[string](/types/string)|Тип дизайна.<br/>Возможные значения:<br/>predefined – предустановленный;<br/>custom – свой дизайн.<br/>|
|*site_id*|False|[numeric](/types/numeric)|ID сайта.<br/>|
|*image_offline*|False|[file](/types/file)|Картинка кнопки, когда нет доступных операторов.<br/>Принимается во внимание при design_type = custom.<br/>Изображение в формате JPEG, GIF или PNG с длинной стороной не более 500 пикселей.<br/>Максимальный размер файла – 2 MB.<br/>|
|*employee_id*|False|[numeric](/types/numeric)|ID сотрудника.<br/>|
|*size*|False|[string](/types/string)|Размер кнопки.<br/>Возможные значения:<br/>small – маленький, 146x50 пикселей;<br/>middle – средний,  193x69 пикселей;<br/>large – большой, 223x100 пикселей.<br/>|
|*id*|True|[numeric](/types/numeric)|ID кнопки.<br/>|
|*department_id*|False|[numeric](/types/numeric)|ID отдел.<br/>|

### Результат
None
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|*admin*|full||
|*manager*|managed|Обновление кнопок на своих сайтах.|
|*chief*|managed|Обновление кнопок на своих сайтах.|
|*chief_partner*|managed|Обновление кнопок на своих сайтах.|
|*operator*|none||
|*admin_partner*|full||

## delete

### Описание метода
Удаляет указанную кнопку.<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*id*|True|[numeric](/types/numeric)|ID кнопки.<br/>|

### Результат
None
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|*admin*|full||
|*manager*|managed|Кнопки своих сайтов.|
|*chief*|managed|Кнопки своих сайтов.|
|*chief_partner*|managed|Кнопки своих сайтов.|
|*operator*|none||
|*admin_partner*|full||
