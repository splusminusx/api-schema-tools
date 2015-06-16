
## InvitationRule

### Описание типа
InvitationRule
Сценарий вовлечения.
Таблица 47. Поля сценария вовлечения


### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|confirmation_mobile|False|[string](/docs/types/string.md)|Подтверждающее сообщение для мобильных устройств.<br/>Максимум 180 символов.<br/>Обязательно, если action имеет значение vary или lead.<br/>ВНИМАНИЕ! В данный момент это поле не используется.<br/>|
|page_title|False|[string](/docs/types/string.md)|Показывать приглашение на странице с указанной подстрокой в названии (тег «title»).<br/>Если page_type=specified, то одно из двух полей page_url или page_title должно быть указано.<br/>|
|is_new_visitor|True|[boolean](/docs/types/boolean.md)|Показывать приглашение только новым посетителям.<br/>True – показывать только новым, false – показывать всем.<br/>|
|site_time|False|[numeric](/docs/types/numeric.md)|Время в секундах, проведенное на сайте посетителем, после которого ему необходимо показывать приглашение.<br/>|
|title|True|[string](/docs/types/string.md)|Название сценария.<br/>Максимум 70 символов.<br/>|
|is_once_per_day|False|[boolean](/docs/types/boolean.md)|Показывать приглашение только один раз в сутки.<br/>True – один раз, вне зависимости от значения max_count, false – в соответствии со значением max_count.<br/>|
|welcome_chat|False|[string](/docs/types/string.md)|Текст приглашения, если есть доступные операторы.<br/>Максимум 300 символов.<br/>Обязательно для action = chat или vary.<br/>|
|created_at|True|[datetime](/docs/types/datetime.md)|Дата создания.<br/>|
|page_count|False|[numeric](/docs/types/numeric.md)|Количество просмотренных страниц посетителем, при котором ему необходимо показывать приглашение.<br/>|
|is_active|True|[boolean](/docs/types/boolean.md)|Признак активности сценария.<br/>|
|welcome_lead|False|[string](/docs/types/string.md)|Текст приглашения, если нет доступных операторов.<br/>Максимум 300 символов.<br/>Обязательно для action = lead или vary.<br/>|
|locations|False|Array.<[Location](/docs/types/Location.md)>|Массив географических расположений.<br/>|
|updated_at|True|[datetime](/docs/types/datetime.md)|Дата последнего обновления.<br/>|
|page_type|True|[string](/docs/types/string.md)|Тип страницы.<br/>Возможные значения:<br/>specified – показывать приглашение на странице, соответствующей критериям page_url и page_title.<br/>home – показывать приглашение на главной страницы;<br/>internal – показывать приглашение на внутренней странице;<br/>any – показывать приглашение на любой странице.<br/>|
|page_time|False|[numeric](/docs/types/numeric.md)|Время, проведенное на странице посетителем, после которого ему необходимо показывать приглашение.<br/>|
|welcome_mobile|True|[string](/docs/types/string.md)|Текст приглашения для мобильных устройств.<br/>Максимум 130 символов.<br/>ВНИМАНИЕ! В данный момент это поле не используется.<br/>|
|action|True|[string](/docs/types/string.md)|Действие, которое следует выполнить, если ситуация подпадает под настройки сценария.<br/>Возможные значения:<br/>vary – показать приглашение в чат, если есть доступные операторы или форму генератора лидов, если доступных операторов нет.<br/>chat – показать приглашение в чат, если есть активные операторы. В противном случае ничего не показывать;<br/>lead – показать форму генератора лида, если нет активных операторов. В противном случае ничего не показывать.<br/>|
|confirmation_lead|False|[string](/docs/types/string.md)|Подтверждающее сообщение, которое показывается посетителю после отправки формы лида.<br/>Максимум 180 символов.<br/>Обязательно для action = lead или vary.<br/>|
|max_count|False|[numeric](/docs/types/numeric.md)|Максимальное количество показов конкретному посетителю приглашений по данному сценарию в течение календарных суток.<br/>Счетчик показов обнуляется по истечению суток с момента последнего показа.<br/>Отсутствие значения или 0 – ограничения нет.<br/>|
|id|True|[numeric](/docs/types/numeric.md)|ID сценария.<br/>|
|page_url|False|[string](/docs/types/string.md)|Показывать приглашение на странице с указанным адресом.<br/>Адрес указывается без приставки «http://» или «https://», например:<br/>www.mycompany.ru/about/contacts<br/>Если page_type=specified, то одно из двух полей page_url или page_title должно быть указано.<br/>|
