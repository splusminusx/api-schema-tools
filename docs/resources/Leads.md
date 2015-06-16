
# Leads

## Описание ресурса
Leads<br/>
# Методы

## showRouted

### Описание метода
Leads.showRouted<br/>Возвращает данные указанного лида в контексте маршрутизации.<br/>Метод работает точно также, как и метод Leads.show, но предоставляет доступ только к лидам, адресованным текущему сотруднику.<br/>Параметры<br/>Результат<br/>Объект типа «Lead».<br/>Уровень доступа для ролей<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*fields*|False|[string](/docs/types/string.md)|Список через запятую возвращаемых полей.<br/>|
|*id*|True|[numeric](/docs/types/numeric.md)|ID лида.<br/>|

### Резудьтат
[Lead](/docs/types/Lead.md)
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner
## show

### Описание метода
Leads.show<br/>Возвращает данные указанного лида.<br/>Параметры<br/>Результат<br/>Объект типа «Lead».<br/>Уровень доступа для ролей<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*fields*|False|[string](/docs/types/string.md)|Список через запятую возвращаемых полей.<br/>|
|*id*|True|[numeric](/docs/types/numeric.md)|ID лида.<br/>|

### Резудьтат
[Lead](/docs/types/Lead.md)
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner
## lock

### Описание метода
Leads.lock<br/>Блокирует указанный лид.<br/>Блокировка устанавливается на ограниченный период времени – 30 минут. По прошествии этого времени блокировка автоматически снимается.<br/>Нельзя заблокировать лид, уже заблокированный другим сотрудником. Повторный вызов метода для лида, заблокированного текущим сотрудником, выполняется успешно. При этом период блокировки пролонгируется еще на 30 минут. <br/>Параметры<br/>Результат<br/>Boolean. True – блокировка выполнена успешно. False – блокировка отклонена.<br/>Пример ответа<br/>{<br/>    "results": true<br/>}<br/>Уровень доступа для ролей<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*id*|True|[numeric](/docs/types/numeric.md)|ID лида.<br/>|

### Резудьтат
[Boolean](/docs/types/Boolean.md)
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner
## listRouted

### Описание метода
Leads.listRouted<br/>Возвращает список лидов в контексте маршрутизации.<br/>Метод работает точно также, как и метод Leads.list, но предоставляет доступ только к лидам, адресованным текущему сотруднику.<br/>Параметры<br/>Результат<br/>Массив объектов типа «Lead».<br/>Уровень доступа для ролей<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*q*|False|[string](/docs/types/string.md)|Критерий поиска.<br/>Доступные поля:<br/>ids – idlist, список ID лидов.<br/>site_ids – idlist, список ID сайтов.<br/>department_ids – idlist, список ID отделов.<br/>created_by_ids – idlist, список ID сотрудников. Поиск по полю created_by.<br/>assigned_to_ids – idlist, список ID сотрудников. Поиск по полю assigned_to.<br/>completed_by_ids – idlist, список ID сотрудников. Поиск по полю completed_by.<br/>visitor_ids – idlist, список ID посетителей;<br/>type;<br/>result;<br/>duration;<br/>email_exists – boolean, указан ли email;<br/>phone_exists – boolean, указан ли телефон;<br/>search_engine;<br/>ext_referer;<br/>enter_page;<br/>int_referer;<br/>created_at,<br/>text - string, подстрока в тексте лида.<br/>|
|*fields*|False|[string](/docs/types/string.md)|Список через запятую возвращаемых полей.<br/>|
|*limit*|False|[numeric](/docs/types/numeric.md)|По умолчанию – 50.<br/>|
|*sort*|False|[string](/docs/types/string.md)|Сортировка результатов.<br/>Возможные поля сортировки:<br/>created_at,<br/>updated_at,<br/>duration,<br/>result.<br/>|
|*offset*|False|[numeric](/docs/types/numeric.md)|По умолчанию – 0.<br/>|

### Резудьтат
Array.<[Lead](/docs/types/Lead.md)>
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner
## list

### Описание метода
Leads.list<br/>Возвращает список лидов.<br/>Параметры<br/>Результат<br/>Массив объектов типа «Lead».<br/>Уровень доступа для ролей<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*q*|False|[string](/docs/types/string.md)|Критерий поиска.<br/>Доступные поля:<br/>ids – idlist, список ID офлайн-сообщений.<br/>site_ids – idlist, список ID сайтов.<br/>department_ids – idlist, список ID отделов.<br/>created_by_ids – idlist, список ID сотрудников. Поиск по полю created_by.<br/>assigned_to_ids – idlist, список ID сотрудников. Поиск по полю assigned_to.<br/>completed_by_ids – idlist, список ID сотрудников. Поиск по полю completed_by.<br/>visitor_ids – idlist, список ID посетителей;<br/>type;<br/>result;<br/>duration;<br/>email_exists – boolean, указан ли email;<br/>phone_exists – boolean, указан ли телефон;<br/>is_managed;<br/>search_engine;<br/>ext_referer;<br/>enter_page;<br/>int_referer;<br/>created_at,<br/>text - string, подстрока в тексте лида.<br/>|
|*fields*|False|[string](/docs/types/string.md)|Список через запятую возвращаемых полей.<br/>|
|*limit*|False|[numeric](/docs/types/numeric.md)|По умолчанию – 50.<br/>|
|*sort*|False|[string](/docs/types/string.md)|Сортировка результатов.<br/>Возможные значения:<br/>created_at:a;<br/>updated_at:a;<br/>duration:a;<br/>result:a.<br/>|
|*offset*|False|[numeric](/docs/types/numeric.md)|По умолчанию – 0.<br/>|

### Резудьтат
Array.<[Lead](/docs/types/Lead.md)>
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner
## add

### Описание метода
Leads.add<br/>Добавляет новый лид.<br/>Лид, созданный с помощью этого получает type = chat.<br/>Параметры<br/>Результат<br/>Объект типа «Lead».<br/>Уровень доступа для ролей<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*name*|True|[string](/docs/types/string.md)|Имя посетителя.<br/>|
|*text*|False|[string](/docs/types/string.md)|Текст сообщения.<br/>|
|*site_id*|True|[numeric](/docs/types/numeric.md)|ID сайта.<br/>|
|*phone*|False|[phone](/docs/types/phone.md)|Номер телефона.<br/>Одно из полей email или phone должно быть указано.<br/>|
|*result*|False|[string](/docs/types/string.md)|Статус обработки лида.<br/>Возможные значения:<br/>missed – еще не обработанный;<br/>completed – обработан.<br/>|
|*conversation_id*|True|[numeric](/docs/types/numeric.md)|ID обращения.<br/>|
|*email*|False|[email](/docs/types/email.md)|Адрес электронной почты.<br/>Одно из полей email или phone должно быть указано.<br/>|
|*department_id*|False|[numeric](/docs/types/numeric.md)|ID отдела.<br/>|

### Резудьтат
[Lead](/docs/types/Lead.md)
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner
## setCompleted

### Описание метода
Leads.setCompleted<br/>Устанавливает признак обработанности (result = completed) указанного лида.<br/>Если указанный лид уже обработан, то вызов метода НЕ приведет к изменению его свойств. При этом результат выполнения метода будет такой же, как если бы операция выполнилась успешно.<br/>Параметры<br/>Результат<br/>Метод ничего не возвращает.<br/>Уровень доступа для ролей<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*answer_text*|False|[string](/docs/types/string.md)|Текст ответа сотрудника.<br/>|
|*id*|True|[numeric](/docs/types/numeric.md)|ID лида.<br/>|

### Резудьтат
None
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner
## unlock

### Описание метода
Leads.unlock<br/>Снимает блокировку с указанного лида.<br/>Снять блокировку может только тот сотрудник, который ее поставил. Вызов метода для незаблокированного адресованного лида выполняется успешно.<br/>Блокировки снимаются автоматически через 30 минут.<br/>Параметры<br/>Результат<br/>Boolean. True – снятие блокировки выполнено успешно. False – операция отклонена.<br/>Пример ответа<br/>{<br/>    "results": true<br/>}<br/>Уровень доступа для ролей<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*id*|True|[numeric](/docs/types/numeric.md)|ID лида.<br/>|

### Резудьтат
[Boolean](/docs/types/Boolean.md)
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner