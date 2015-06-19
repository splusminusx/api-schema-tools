
## Conversation

### Описание типа
Обращение – совокупность диалогов разного типа в рамках одного сеанса консультации посетителя с сотрудниками сайта.<br/><br/>Контроллер: Conversations<br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*visitor_variables*|False|[Object](/types/Object)|Объект с переменными посетителя на момент создания обращения.<br/>|
|*visitor*|True|[Visitor](/types/Visitor)|Посетитель.<br/>|
|*page_count*|True|[numeric](/types/numeric)|Количество страниц, просмотренных посетителем в ходе визита, перед тем, как он начал обращение.<br/>|
|*updated_at*|True|[datetime](/types/datetime)|Дата последнего обновления.<br/>|
|*leads*|False|Array.<[Lead](/types/Lead)>|Список лидов в хронологическом порядке.<br/>|
|*result*|True|[numeric](/types/numeric)|Результат обращения.<br/>Возможные значения:<br/>failure – не успешное,<br/>success – успешное.<br/>|
|*duration*|True|[numeric](/types/numeric)|Общая продолжительность обращения в секундах.<br/>|
|*prechat_fields*|False|[Object](/types/Object)|Объект со значениями пречат-полей.<br/>В этом объекте содержаться настраиваемые в Личном кабинете пречат поля, а также видимые оператору и скрытые от него пречат-поля, устанавливаемые с помощью LiveTex Client API.<br/>|
|*visit_count*|True|[numeric](/types/numeric)|Общее количество визитов посетителя на сайт, включая визит, в котором состоялось обращение.<br/>|
|*id*|True|[numeric](/types/numeric)|ID обращения.<br/>|
|*search_engine*|False|[string](/types/string)|Название поискового сервиса.<br/>Содержит значение, если посетитель начал обращение, перейдя на сайт из результатов поиска сервисов типа Yandex или Google.<br/>|
|*city*|False|[string](/types/string)|Город, из которого посетитель инициировал обращение.<br/>Определяется механизмами геолокации LiveTex.<br/>|
|*lead_count*|True|[numeric](/types/numeric)|Количество лидов.<br/>|
|*department*|False|[Department](/types/Department)|Отдел, которому было адресовано обращение.<br/>|
|*ext_referer*|False|[string](/types/string)|Адрес, с которого посетитель перешел на сайт. <br/>|
|*events*|False|Array.<[ConversationEvent](/types/ConversationEvent)>|Список событий обращения в хронологическом порядке за все время обращения.<br/>|
|*call_count*|True|[numeric](/types/numeric)|Количество звонков.<br/>|
|*chats*|False|Array.<[Chat](/types/Chat)>|Список чатов обращения в хронологическом порядке.<br/>|
|*site*|True|[Site](/types/Site)|Сайт, на котором инициировано обращение.<br/>|
|*message_count*|True|[numeric](/types/numeric)|Общее количество текстовых сообщений чатов.<br/>|
|*complaints*|False|Array.<[Complaint](/types/Complaint)>|Список жалоб в хронологическом порядке, оставленных посетителем в данном обращении.<br/>|
|*widget_id*|False|[string](/types/string)|ID виджета или сценария вовлечения, с которого начался чат.<br/>Содержит соответствующий ID, за исключением следующих случаев:<br/>Если widget_type = 'invite', то содержит текст приглашения оператора.<br/>Если widget_type = 'api', то - пустая строка.<br/>|
|*widget_type*|False|[string](/types/string)|Тип виджета, с которого началось обращение.<br/>Возможные значения:<br/>auto - автоприглашение;<br/>api - вызов метода API;<br/>invite - ручное приглашение оператора;<br/>label - ярлык чата;<br/>sound-label - ярлык звонка;<br/>button - кнопка чата;<br/>sound-button - звонковая кнопка.<br/>|
|*calls*|False|Array.<[Call](/types/Call)>|Список звонков обращения в хронологическом порядке.<br/>|
|*int_referer*|False|[string](/types/string)|Адрес страницы, на которой начался первый диалог обращения.<br/>|
|*country*|False|[string](/types/string)|Страна, из которой посетитель инициировал обращение.<br/>Определяется механизмами геолокации LiveTex.<br/>|
|*employees*|False|Array.<[Employee](/types/Employee)>|Список сотрудников, который приняли участие в обработке обращения в хронологическом порядке их участия.<br/>|
|*chat_count*|True|[numeric](/types/numeric)|Количество чатов.<br/>|
|*search_query*|False|[string](/types/string)|Строка поискового запроса.<br/>Содержит значение, если посетитель начал обращение, перейдя на сайт из результатов поиска сервисов типа Yandex или Google.<br/>|
|*entry_page*|False|[string](/types/string)|Страница, с которой посетитель начал визит, в котором было создано обращение.<br/>|
|*created_at*|True|[datetime](/types/datetime)|Дата создания.<br/>|
