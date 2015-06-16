
## Conversation

### Описание типа
Обращение – совокупность диалогов разного типа в рамках одного сеанса консультации посетителя с сотрудниками сайта.<br/><br/>Контроллер: Conversations<br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*visitor_variables*|False|[Object](/docs/types/Object.md)|Объект с переменными посетителя на момент создания обращения.<br/>|
|*visitor*|True|[Visitor](/docs/types/Visitor.md)|Посетитель.<br/>|
|*page_count*|True|[numeric](/docs/types/numeric.md)|Количество страниц, просмотренных посетителем в ходе визита, перед тем, как он начал обращение.<br/>|
|*updated_at*|True|[datetime](/docs/types/datetime.md)|Дата последнего обновления.<br/>|
|*leads*|False|Array.<[Lead](/docs/types/Lead.md)>|Список лидов в хронологическом порядке.<br/>|
|*result*|True|[numeric](/docs/types/numeric.md)|Результат обращения.<br/>Возможные значения:<br/>failure – не успешное,<br/>success – успешное.<br/>|
|*duration*|True|[numeric](/docs/types/numeric.md)|Общая продолжительность обращения в секундах.<br/>|
|*prechat_fields*|False|[Object](/docs/types/Object.md)|Объект со значениями пречат-полей.<br/>В этом объекте содержаться настраиваемые в Личном кабинете пречат поля, а также видимые оператору и скрытые от него пречат-поля, устанавливаемые с помощью LiveTex Client API.<br/>|
|*visit_count*|True|[numeric](/docs/types/numeric.md)|Общее количество визитов посетителя на сайт, включая визит, в котором состоялось обращение.<br/>|
|*id*|True|[numeric](/docs/types/numeric.md)|ID обращения.<br/>|
|*search_engine*|False|[string](/docs/types/string.md)|Название поискового сервиса.<br/>Содержит значение, если посетитель начал обращение, перейдя на сайт из результатов поиска сервисов типа Yandex или Google.<br/>|
|*city*|False|[string](/docs/types/string.md)|Город, из которого посетитель инициировал обращение.<br/>Определяется механизмами геолокации LiveTex.<br/>|
|*lead_count*|True|[numeric](/docs/types/numeric.md)|Количество лидов.<br/>|
|*department*|False|[Department](/docs/types/Department.md)|Отдел, которому было адресовано обращение.<br/>|
|*ext_referer*|False|[string](/docs/types/string.md)|Адрес, с которого посетитель перешел на сайт. <br/>|
|*events*|False|Array.<[ConversationEvent](/docs/types/ConversationEvent.md)>|Список событий обращения в хронологическом порядке за все время обращения.<br/>|
|*call_count*|True|[numeric](/docs/types/numeric.md)|Количество звонков.<br/>|
|*chats*|False|Array.<[Chat](/docs/types/Chat.md)>|Список чатов обращения в хронологическом порядке.<br/>|
|*site*|True|[Site](/docs/types/Site.md)|Сайт, на котором инициировано обращение.<br/>|
|*message_count*|True|[numeric](/docs/types/numeric.md)|Общее количество текстовых сообщений чатов.<br/>|
|*complaints*|False|Array.<[Complaint](/docs/types/Complaint.md)>|Список жалоб в хронологическом порядке, оставленных посетителем в данном обращении.<br/>|
|*widget_id*|False|[string](/docs/types/string.md)|ID виджета или сценария вовлечения, с которого начался чат.<br/>Содержит соответствующий ID, за исключением следующих случаев:<br/>Если widget_type = 'invite', то содержит текст приглашения оператора.<br/>Если widget_type = 'api', то - пустая строка.<br/>|
|*widget_type*|False|[string](/docs/types/string.md)|Тип виджета, с которого началось обращение.<br/>Возможные значения:<br/>auto - автоприглашение;<br/>api - вызов метода API;<br/>invite - ручное приглашение оператора;<br/>label - ярлык чата;<br/>sound-label - ярлык звонка;<br/>button - кнопка чата;<br/>sound-button - звонковая кнопка.<br/>|
|*calls*|False|Array.<[Call](/docs/types/Call.md)>|Список звонков обращения в хронологическом порядке.<br/>|
|*int_referer*|False|[string](/docs/types/string.md)|Адрес страницы, на которой начался первый диалог обращения.<br/>|
|*country*|False|[string](/docs/types/string.md)|Страна, из которой посетитель инициировал обращение.<br/>Определяется механизмами геолокации LiveTex.<br/>|
|*employees*|False|Array.<[Employee](/docs/types/Employee.md)>|Список сотрудников, который приняли участие в обработке обращения в хронологическом порядке их участия.<br/>|
|*chat_count*|True|[numeric](/docs/types/numeric.md)|Количество чатов.<br/>|
|*search_query*|False|[string](/docs/types/string.md)|Строка поискового запроса.<br/>Содержит значение, если посетитель начал обращение, перейдя на сайт из результатов поиска сервисов типа Yandex или Google.<br/>|
|*entry_page*|False|[string](/docs/types/string.md)|Страница, с которой посетитель начал визит, в котором было создано обращение.<br/>|
|*created_at*|True|[datetime](/docs/types/datetime.md)|Дата создания.<br/>|
