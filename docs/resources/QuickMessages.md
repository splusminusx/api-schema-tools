
# QuickMessages

## Описание ресурса

# Методы

## add

### Описание метода
Добавляет новое быстрое сообщение.<br/>Объект типа «QuickMessage».<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*text*|True|[string](/docs/types/string.md)|Текст сообщения.<br/>Максимум 2000 символов.<br/>|
|*is_global*|True|[boolean](/docs/types/boolean.md)|Признак глобальности быстрого сообщения.<br/>Если true, то сообщение видно всем сотрудникам. В противном случае - только сотруднику, создавшему сообщение.<br/>ВНИМАНИЕ! В категории с is_global = false нельзя создать сообщение с is_global = true.<br/>|
|*category_id*|True|[numeric](/docs/types/numeric.md)|ID категории быстрых сообщений.<br/>|

### Результат
[QuickMessage](/docs/types/QuickMessage.md)
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|*admin*|full||
|*manager*|managed|Быстрые сообщения с is_global = true разрешается создавать только на своих сайтах.|
|*chief*|managed|Быстрые сообщения с is_global = true разрешается создавать только на своих сайтах.|
|*chief_partner*|managed|Быстрые сообщения с is_global = true разрешается создавать только на своих сайтах.|
|*operator*|user|На любых сайтах можно создавать только сообщения с is_global = false.|
|*admin_partner*|full||

## show

### Описание метода
Возвращает данные указанного быстрого сообщения.<br/>Объект типа «QuickMessage».<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*fields*|False|[string](/docs/types/string.md)|Список через запятую возвращаемых полей.<br/>|
|*id*|True|[numeric](/docs/types/numeric.md)|ID быстрого сообщения.<br/>|

### Результат
[QuickMessage](/docs/types/QuickMessage.md)
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|*admin*|full|За исключением чужих быстрых сообщений с is_global = false.|
|*manager*|full|За исключением чужих быстрых сообщений с is_global = false.|
|*chief*|full|За исключением чужих быстрых сообщений с is_global = false.|
|*chief_partner*|full|За исключением чужих быстрых сообщений с is_global = false.|
|*operator*|full|За исключением чужих быстрых сообщений с is_global = false.|
|*admin_partner*|full|За исключением чужих быстрых сообщений с is_global = false.|

## list

### Описание метода
Возвращает список быстрых сообщений.<br/>Массив объектов типа «QuickMessage».<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*q*|False|[string](/docs/types/string.md)|Критерий поиска.<br/>Доступные поля:<br/>ids – idlist, список ID сообщений;<br/>category_ids – idlist, список ID категорий;<br/>site_ids – idlist, список ID сайтов.<br/>|
|*fields*|False|[string](/docs/types/string.md)|Список через запятую возвращаемых полей.<br/>|
|*limit*|False|[numeric](/docs/types/numeric.md)|По умолчанию – 50.<br/>|
|*sort*|False|[string](/docs/types/string.md)|Сортировка результатов.<br/>Возможные значение:<br/>text:a – по умолчанию.<br/>|
|*offset*|False|[numeric](/docs/types/numeric.md)|По умолчанию – 0.<br/>|

### Результат
Array.<[QuickMessage](/docs/types/QuickMessage.md)>
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|*admin*|full|За исключением чужих быстрых сообщений с is_global = false.|
|*manager*|full|За исключением чужих быстрых сообщений с is_global = false.|
|*chief*|full|За исключением чужих быстрых сообщений с is_global = false.|
|*chief_partner*|full|За исключением чужих быстрых сообщений с is_global = false.|
|*operator*|full|За исключением чужих быстрых сообщений с is_global = false.|
|*admin_partner*|full|За исключением чужих быстрых сообщений с is_global = false.|

## update

### Описание метода
Обновляет быстрое сообщение.<br/>Метод ничего не возвращает.<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*text*|False|[string](/docs/types/string.md)|Текст сообщения.<br/>Максимум 2000 символов.<br/>|
|*category_id*|False|[numeric](/docs/types/numeric.md)|ID категории быстрых сообщений.<br/>ВНИМАНИЕ! В категории с is_global = false нельзя создать сообщение с is_global = true. <br/>|
|*id*|True|[numeric](/docs/types/numeric.md)|ID быстрого сообщения.<br/>|

### Результат
None
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|*admin*|full|Только быстрые сообщения с is_global = true, а также свои быстрые сообщения с is_global = false.|
|*manager*|managed|Быстрые сообщения с is_global = true разрешается обновлять только на своих сайтах.|
|*chief*|managed|Быстрые сообщения с is_global = true разрешается обновлять только на своих сайтах.|
|*chief_partner*|managed|Быстрые сообщения с is_global = true разрешается обновлять только на своих сайтах.|
|*operator*|user|На любых сайтах можно обновлять только сообщения с is_global = false.|
|*admin_partner*|full|Только быстрые сообщения с is_global = true, а также свои быстрые сообщения с is_global = false.|

## delete

### Описание метода
Удаляет указанное быстрое сообщение.<br/>Метод ничего не возвращает.<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*id*|True|[numeric](/docs/types/numeric.md)|ID быстрого сообщения.<br/>|

### Результат
None
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|*admin*|full|Только быстрые сообщения с is_global = true, а также свои быстрые сообщения с is_global = false.|
|*manager*|managed|Быстрые сообщения с is_global = true разрешается удалять только на своих сайтах.|
|*chief*|managed|Быстрые сообщения с is_global = true разрешается удалять только на своих сайтах.|
|*chief_partner*|managed|Быстрые сообщения с is_global = true разрешается удалять только на своих сайтах.|
|*operator*|user|На любых сайтах можно удалять только сообщения с is_global = false.|
|*admin_partner*|full|Только быстрые сообщения с is_global = true, а также свои быстрые сообщения с is_global = false.|
