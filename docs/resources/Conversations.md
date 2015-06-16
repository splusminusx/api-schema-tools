
# Conversations

## Описание ресурса
Conversations<br/>
# Методы

## show

### Описание метода
Conversations.show<br/>Возвращает данные указанного обращения.<br/>Параметры<br/>Результат<br/>Объект типа «Conversation».<br/>Уровень доступа для ролей<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|**fields**|False|[string](/docs/types/string.md)|Список через запятую возвращаемых полей.<br/>|
|**id**|True|[numeric](/docs/types/numeric.md)|ID обращения.<br/>|

### Резудьтат
[Conversation](/docs/types/Conversation.md)
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|None|admin_partner