
# QuickMessages

## Описание ресурса
QuickMessages<br/>
# Методы

## add

### Описание метода
QuickMessages.add<br/>Добавляет новое быстрое сообщение.<br/>Параметры<br/>Результат<br/>Объект типа «QuickMessage».<br/>Уровень доступа для ролей<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|**text**|True|[string](/docs/types/string.md)|Текст сообщения.<br/>Максимум 2000 символов.<br/>|
|**is_global**|True|[boolean](/docs/types/boolean.md)|Признак глобальности быстрого сообщения.<br/>Если true, то сообщение видно всем сотрудникам. В противном случае - только сотруднику, создавшему сообщение.<br/>ВНИМАНИЕ! В категории с is_global = false нельзя создать сообщение с is_global = true.<br/>|
|**category_id**|True|[numeric](/docs/types/numeric.md)|ID категории быстрых сообщений.<br/>|

### Резудьтат
[QuickMessage](/docs/types/QuickMessage.md)
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner
## show

### Описание метода
QuickMessages.show<br/>Возвращает данные указанного быстрого сообщения.<br/>Параметры<br/>Результат<br/>Объект типа «QuickMessage».<br/>Уровень доступа для ролей<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|**fields**|False|[string](/docs/types/string.md)|Список через запятую возвращаемых полей.<br/>|
|**id**|True|[numeric](/docs/types/numeric.md)|ID быстрого сообщения.<br/>|

### Резудьтат
[QuickMessage](/docs/types/QuickMessage.md)
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner
## list

### Описание метода
QuickMessages.list<br/>Возвращает список быстрых сообщений.<br/>Параметры<br/>Результат<br/>Массив объектов типа «QuickMessage».<br/>Уровень доступа для ролей<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|**q**|False|[string](/docs/types/string.md)|Критерий поиска.<br/>Доступные поля:<br/>ids – idlist, список ID сообщений;<br/>category_ids – idlist, список ID категорий;<br/>site_ids – idlist, список ID сайтов.<br/>|
|**fields**|False|[string](/docs/types/string.md)|Список через запятую возвращаемых полей.<br/>|
|**limit**|False|[numeric](/docs/types/numeric.md)|По умолчанию – 50.<br/>|
|**sort**|False|[string](/docs/types/string.md)|Сортировка результатов.<br/>Возможные значение:<br/>text:a – по умолчанию.<br/>|
|**offset**|False|[numeric](/docs/types/numeric.md)|По умолчанию – 0.<br/>|

### Резудьтат
Array.<[QuickMessage](/docs/types/QuickMessage.md)>
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner
## update

### Описание метода
QuickMessages.update<br/>Обновляет быстрое сообщение.<br/>Параметры<br/>Результат<br/>Метод ничего не возвращает.<br/>Уровень доступа для ролей<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|**text**|False|[string](/docs/types/string.md)|Текст сообщения.<br/>Максимум 2000 символов.<br/>|
|**category_id**|False|[numeric](/docs/types/numeric.md)|ID категории быстрых сообщений.<br/>ВНИМАНИЕ! В категории с is_global = false нельзя создать сообщение с is_global = true. <br/>|
|**id**|True|[numeric](/docs/types/numeric.md)|ID быстрого сообщения.<br/>|

### Резудьтат
None
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner
## delete

### Описание метода
QuickMessages.delete<br/>Удаляет указанное быстрое сообщение.<br/>Параметры<br/>Результат<br/>Метод ничего не возвращает.<br/>Уровень доступа для ролей<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|**id**|True|[numeric](/docs/types/numeric.md)|ID быстрого сообщения.<br/>|

### Резудьтат
None
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner