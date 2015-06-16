
# ConsoleNews

## Описание ресурса

# Методы

## markRead

### Описание метода
ConsoleNews.markRead<br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*id*|True|[numeric](/docs/types/numeric.md)|ID новости.<br/>|

### Результат
None
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|full||
|manager|full||
|chief|full||
|chief_partner|full||
|operator|full||
|admin_partner|full||

## listLatest

### Описание метода
ConsoleNews.listLatest<br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*fields*|False|[string](/docs/types/string.md)|Список через запятую возвращаемых полей.<br/>|
|*limit*|False|[numeric](/docs/types/numeric.md)|По умолчанию – 50.<br/>|
|*offset*|False|[numeric](/docs/types/numeric.md)|По умолчанию – 0.<br/>|

### Результат
Array.<[ConsoleNews](/docs/types/ConsoleNews.md)>
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
