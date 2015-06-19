
# Leads

## Описание ресурса

# Методы

## showRouted

### Описание метода
Возвращает данные указанного лида в контексте маршрутизации.<br/>Метод работает точно также, как и метод Leads.show, но предоставляет доступ только к лидам, адресованным текущему сотруднику.<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*fields*|False|[string](/types/string)|Список через запятую возвращаемых полей.<br/>|
|*id*|True|[numeric](/types/numeric)|ID лида.<br/>|

### Результат
[Lead](/types/Lead)
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|*admin*|None|Все адресованные лиды.|
|*manager*|None|Все адресованные лиды.|
|*chief*|None|Все адресованные лиды.|
|*chief_partner*|None|Все адресованные лиды.|
|*operator*|None|Все адресованные лиды.|
|*admin_partner*|None|Все адресованные лиды.|

## show

### Описание метода
Возвращает данные указанного лида.<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*fields*|False|[string](/types/string)|Список через запятую возвращаемых полей.<br/>|
|*id*|True|[numeric](/types/numeric)|ID лида.<br/>|

### Результат
[Lead](/types/Lead)
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|*admin*|full||
|*manager*|managed|Все лиды, но без text и answer_text.|
|*chief*|managed|Все лиды, но без text и answer_text.|
|*chief_partner*|managed|Все лиды, но без text и answer_text.|
|*operator*|managed|Все лиды, но без text и answer_text.|
|*admin_partner*|full||

## lock

### Описание метода
Блокирует указанный лид.<br/>Блокировка устанавливается на ограниченный период времени – 30 минут. По прошествии этого времени блокировка автоматически снимается.<br/>Нельзя заблокировать лид, уже заблокированный другим сотрудником. Повторный вызов метода для лида, заблокированного текущим сотрудником, выполняется успешно. При этом период блокировки пролонгируется еще на 30 минут. <br/>Пример ответа<br/>{<br/>    "results": true<br/>}<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*id*|True|[numeric](/types/numeric)|ID лида.<br/>|

### Результат
[Boolean](/types/Boolean)
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|*admin*|None|Только для адресованных лидов.|
|*manager*|None|Только для адресованных лидов.|
|*chief*|None|Только для адресованных лидов.|
|*chief_partner*|None|Только для адресованных лидов.|
|*operator*|None|Только для адресованных лидов.|
|*admin_partner*|None|Только для адресованных лидов.|

## listRouted

### Описание метода
Возвращает список лидов в контексте маршрутизации.<br/>Метод работает точно также, как и метод Leads.list, но предоставляет доступ только к лидам, адресованным текущему сотруднику.<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*q*|False|[string](/types/string)|Критерий поиска.<br/>Доступные поля:<br/>ids – idlist, список ID лидов.<br/>site_ids – idlist, список ID сайтов.<br/>department_ids – idlist, список ID отделов.<br/>created_by_ids – idlist, список ID сотрудников. Поиск по полю created_by.<br/>assigned_to_ids – idlist, список ID сотрудников. Поиск по полю assigned_to.<br/>completed_by_ids – idlist, список ID сотрудников. Поиск по полю completed_by.<br/>visitor_ids – idlist, список ID посетителей;<br/>type;<br/>result;<br/>duration;<br/>email_exists – boolean, указан ли email;<br/>phone_exists – boolean, указан ли телефон;<br/>search_engine;<br/>ext_referer;<br/>enter_page;<br/>int_referer;<br/>created_at,<br/>text - string, подстрока в тексте лида.<br/>|
|*fields*|False|[string](/types/string)|Список через запятую возвращаемых полей.<br/>|
|*limit*|False|[numeric](/types/numeric)|По умолчанию – 50.<br/>|
|*sort*|False|[string](/types/string)|Сортировка результатов.<br/>Возможные поля сортировки:<br/>created_at,<br/>updated_at,<br/>duration,<br/>result.<br/>|
|*offset*|False|[numeric](/types/numeric)|По умолчанию – 0.<br/>|

### Результат
Array.<[Lead](/types/Lead)>
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|*admin*|None|Все адресованные лиды.|
|*manager*|None|Все адресованные лиды.|
|*chief*|None|Все адресованные лиды.|
|*chief_partner*|None|Все адресованные лиды.|
|*operator*|None|Все адресованные лиды.|
|*admin_partner*|None|Все адресованные лиды.|

## list

### Описание метода
Возвращает список лидов.<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*q*|False|[string](/types/string)|Критерий поиска.<br/>Доступные поля:<br/>ids – idlist, список ID офлайн-сообщений.<br/>site_ids – idlist, список ID сайтов.<br/>department_ids – idlist, список ID отделов.<br/>created_by_ids – idlist, список ID сотрудников. Поиск по полю created_by.<br/>assigned_to_ids – idlist, список ID сотрудников. Поиск по полю assigned_to.<br/>completed_by_ids – idlist, список ID сотрудников. Поиск по полю completed_by.<br/>visitor_ids – idlist, список ID посетителей;<br/>type;<br/>result;<br/>duration;<br/>email_exists – boolean, указан ли email;<br/>phone_exists – boolean, указан ли телефон;<br/>is_managed;<br/>search_engine;<br/>ext_referer;<br/>enter_page;<br/>int_referer;<br/>created_at,<br/>text - string, подстрока в тексте лида.<br/>|
|*fields*|False|[string](/types/string)|Список через запятую возвращаемых полей.<br/>|
|*limit*|False|[numeric](/types/numeric)|По умолчанию – 50.<br/>|
|*sort*|False|[string](/types/string)|Сортировка результатов.<br/>Возможные значения:<br/>created_at:a;<br/>updated_at:a;<br/>duration:a;<br/>result:a.<br/>|
|*offset*|False|[numeric](/types/numeric)|По умолчанию – 0.<br/>|

### Результат
Array.<[Lead](/types/Lead)>
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|*admin*|full||
|*manager*|managed|Все лиды, но без text и answer_text.|
|*chief*|managed|Все лиды, но без text и answer_text.|
|*chief_partner*|managed|Все лиды, но без text и answer_text.|
|*operator*|managed|Все лиды, но без text и answer_text.|
|*admin_partner*|full||

## add

### Описание метода
Добавляет новый лид.<br/>Лид, созданный с помощью этого получает type = chat.<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*name*|True|[string](/types/string)|Имя посетителя.<br/>|
|*text*|False|[string](/types/string)|Текст сообщения.<br/>|
|*site_id*|True|[numeric](/types/numeric)|ID сайта.<br/>|
|*phone*|False|[phone](/types/phone)|Номер телефона.<br/>Одно из полей email или phone должно быть указано.<br/>|
|*result*|False|[string](/types/string)|Статус обработки лида.<br/>Возможные значения:<br/>missed – еще не обработанный;<br/>completed – обработан.<br/>|
|*conversation_id*|True|[numeric](/types/numeric)|ID обращения.<br/>|
|*email*|False|[email](/types/email)|Адрес электронной почты.<br/>Одно из полей email или phone должно быть указано.<br/>|
|*department_id*|False|[numeric](/types/numeric)|ID отдела.<br/>|

### Результат
[Lead](/types/Lead)
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|*admin*|full||
|*manager*|full||
|*chief*|full||
|*chief_partner*|full||
|*operator*|full||
|*admin_partner*|full||

## setCompleted

### Описание метода
Устанавливает признак обработанности (result = completed) указанного лида.<br/>Если указанный лид уже обработан, то вызов метода НЕ приведет к изменению его свойств. При этом результат выполнения метода будет такой же, как если бы операция выполнилась успешно.<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*answer_text*|False|[string](/types/string)|Текст ответа сотрудника.<br/>|
|*id*|True|[numeric](/types/numeric)|ID лида.<br/>|

### Результат
None
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|*admin*|None|Только для адресованных лидов.|
|*manager*|None|Только для адресованных лидов.|
|*chief*|None|Только для адресованных лидов.|
|*chief_partner*|None|Только для адресованных лидов.|
|*operator*|None|Только для адресованных лидов.|
|*admin_partner*|None|Только для адресованных лидов.|

## unlock

### Описание метода
Снимает блокировку с указанного лида.<br/>Снять блокировку может только тот сотрудник, который ее поставил. Вызов метода для незаблокированного адресованного лида выполняется успешно.<br/>Блокировки снимаются автоматически через 30 минут.<br/>Пример ответа<br/>{<br/>    "results": true<br/>}<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*id*|True|[numeric](/types/numeric)|ID лида.<br/>|

### Результат
[Boolean](/types/Boolean)
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|*admin*|None|Только для адресованных лидов.|
|*manager*|None|Только для адресованных лидов.|
|*chief*|None|Только для адресованных лидов.|
|*chief_partner*|None|Только для адресованных лидов.|
|*operator*|None|Только для адресованных лидов.|
|*admin_partner*|None|Только для адресованных лидов.|
