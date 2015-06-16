
# Conversations

## Описание ресурса

# Методы

## show

### Описание метода
Conversations.show<br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*fields*|False|[string](/docs/types/string.md)|Список через запятую возвращаемых полей.<br/>|
|*id*|True|[numeric](/docs/types/numeric.md)|ID обращения.<br/>|

### Результат
[Conversation](/docs/types/Conversation.md)
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|full||
|manager|None|Обращения, в которых есть свои диалоги (чаты, звонки, лиды).|
|chief|managed|Обращения, в которых есть свои диалоги (чаты, звонки, лиды).|
|chief_partner|managed|Обращения, в которых есть свои диалоги (чаты, звонки, лиды).|
|operator|managed|Обращения, в которых есть свои диалоги (чаты, звонки, лиды).|
|None|None||
|admin_partner|full||
