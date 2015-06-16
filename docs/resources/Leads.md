# Leads
## Описание ресурса
Leads
# Методы
## showRouted
### Описание метода
Leads.showRouted
Возвращает данные указанного лида в контексте маршрутизации.
Метод работает точно также, как и метод Leads.show, но предоставляет доступ только к лидам, адресованным текущему сотруднику.
Параметры
Результат
Объект типа «Lead».
Уровень доступа для ролей

### Поля
| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|fields|False|string|Список через запятую возвращаемых полей.<br/>|
|id|True|numeric|ID лида.<br/>|
### Доступы к методу
| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner## show
### Описание метода
Leads.show
Возвращает данные указанного лида.
Параметры
Результат
Объект типа «Lead».
Уровень доступа для ролей

### Поля
| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|fields|False|string|Список через запятую возвращаемых полей.<br/>|
|id|True|numeric|ID лида.<br/>|
### Доступы к методу
| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner## lock
### Описание метода
Leads.lock
Блокирует указанный лид.
Блокировка устанавливается на ограниченный период времени – 30 минут. По прошествии этого времени блокировка автоматически снимается.
Нельзя заблокировать лид, уже заблокированный другим сотрудником. Повторный вызов метода для лида, заблокированного текущим сотрудником, выполняется успешно. При этом период блокировки пролонгируется еще на 30 минут. 
Параметры
Результат
Boolean. True – блокировка выполнена успешно. False – блокировка отклонена.
Пример ответа
{
    "results": true
}
Уровень доступа для ролей

### Поля
| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|id|True|numeric|ID лида.<br/>|
### Доступы к методу
| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner## listRouted
### Описание метода
Leads.listRouted
Возвращает список лидов в контексте маршрутизации.
Метод работает точно также, как и метод Leads.list, но предоставляет доступ только к лидам, адресованным текущему сотруднику.
Параметры
Результат
Массив объектов типа «Lead».
Уровень доступа для ролей

### Поля
| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|q|False|string|Критерий поиска.<br/>Доступные поля:<br/>ids – idlist, список ID лидов.<br/>site_ids – idlist, список ID сайтов.<br/>department_ids – idlist, список ID отделов.<br/>created_by_ids – idlist, список ID сотрудников. Поиск по полю created_by.<br/>assigned_to_ids – idlist, список ID сотрудников. Поиск по полю assigned_to.<br/>completed_by_ids – idlist, список ID сотрудников. Поиск по полю completed_by.<br/>visitor_ids – idlist, список ID посетителей;<br/>type;<br/>result;<br/>duration;<br/>email_exists – boolean, указан ли email;<br/>phone_exists – boolean, указан ли телефон;<br/>search_engine;<br/>ext_referer;<br/>enter_page;<br/>int_referer;<br/>created_at,<br/>text - string, подстрока в тексте лида.<br/>|
|fields|False|string|Список через запятую возвращаемых полей.<br/>|
|limit|False|numeric|По умолчанию – 50.<br/>|
|sort|False|string|Сортировка результатов.<br/>Возможные поля сортировки:<br/>created_at,<br/>updated_at,<br/>duration,<br/>result.<br/>|
|offset|False|numeric|По умолчанию – 0.<br/>|
### Доступы к методу
| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner## list
### Описание метода
Leads.list
Возвращает список лидов.
Параметры
Результат
Массив объектов типа «Lead».
Уровень доступа для ролей

### Поля
| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|q|False|string|Критерий поиска.<br/>Доступные поля:<br/>ids – idlist, список ID офлайн-сообщений.<br/>site_ids – idlist, список ID сайтов.<br/>department_ids – idlist, список ID отделов.<br/>created_by_ids – idlist, список ID сотрудников. Поиск по полю created_by.<br/>assigned_to_ids – idlist, список ID сотрудников. Поиск по полю assigned_to.<br/>completed_by_ids – idlist, список ID сотрудников. Поиск по полю completed_by.<br/>visitor_ids – idlist, список ID посетителей;<br/>type;<br/>result;<br/>duration;<br/>email_exists – boolean, указан ли email;<br/>phone_exists – boolean, указан ли телефон;<br/>is_managed;<br/>search_engine;<br/>ext_referer;<br/>enter_page;<br/>int_referer;<br/>created_at,<br/>text - string, подстрока в тексте лида.<br/>|
|fields|False|string|Список через запятую возвращаемых полей.<br/>|
|limit|False|numeric|По умолчанию – 50.<br/>|
|sort|False|string|Сортировка результатов.<br/>Возможные значения:<br/>created_at:a;<br/>updated_at:a;<br/>duration:a;<br/>result:a.<br/>|
|offset|False|numeric|По умолчанию – 0.<br/>|
### Доступы к методу
| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner## add
### Описание метода
Leads.add
Добавляет новый лид.
Лид, созданный с помощью этого получает type = chat.
Параметры
Результат
Объект типа «Lead».
Уровень доступа для ролей

### Поля
| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|name|True|string|Имя посетителя.<br/>|
|text|False|string|Текст сообщения.<br/>|
|site_id|True|numeric|ID сайта.<br/>|
|phone|False|phone|Номер телефона.<br/>Одно из полей email или phone должно быть указано.<br/>|
|result|False|string|Статус обработки лида.<br/>Возможные значения:<br/>missed – еще не обработанный;<br/>completed – обработан.<br/>|
|conversation_id|True|numeric|ID обращения.<br/>|
|email|False|email|Адрес электронной почты.<br/>Одно из полей email или phone должно быть указано.<br/>|
|department_id|False|numeric|ID отдела.<br/>|
### Доступы к методу
| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner## setCompleted
### Описание метода
Leads.setCompleted
Устанавливает признак обработанности (result = completed) указанного лида.
Если указанный лид уже обработан, то вызов метода НЕ приведет к изменению его свойств. При этом результат выполнения метода будет такой же, как если бы операция выполнилась успешно.
Параметры
Результат
Метод ничего не возвращает.
Уровень доступа для ролей

### Поля
| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|answer_text|False|string|Текст ответа сотрудника.<br/>|
|id|True|numeric|ID лида.<br/>|
### Доступы к методу
| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner## unlock
### Описание метода
Leads.unlock
Снимает блокировку с указанного лида.
Снять блокировку может только тот сотрудник, который ее поставил. Вызов метода для незаблокированного адресованного лида выполняется успешно.
Блокировки снимаются автоматически через 30 минут.
Параметры
Результат
Boolean. True – снятие блокировки выполнено успешно. False – операция отклонена.
Пример ответа
{
    "results": true
}
Уровень доступа для ролей

### Поля
| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|id|True|numeric|ID лида.<br/>|
### Доступы к методу
| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner