
# ConsoleNews

## Описание ресурса
ConsoleNews

# Методы

## markRead

### Описание метода
ConsoleNews.markRead
Помечает новость как прочитанную.
Параметры
Результат
Метод ничего не возвращает.
Уровень доступа для ролей


### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|id|True|[numeric](/docs/types/numeric.md)|ID новости.<br/>|

### Резудьтат
None
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner
## listLatest

### Описание метода
ConsoleNews.listLatest
Возвращает список последних новостей для Пульта оператора в предопределенном порядке.
Параметры
Результат
Массив объектов типа «ConsoleNews».

### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|fields|False|[string](/docs/types/string.md)|Список через запятую возвращаемых полей.<br/>|
|limit|False|[numeric](/docs/types/numeric.md)|По умолчанию – 50.<br/>|
|offset|False|[numeric](/docs/types/numeric.md)|По умолчанию – 0.<br/>|

### Резудьтат
Array.<[ConsoleNews](/docs/types/ConsoleNews.md)>
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
