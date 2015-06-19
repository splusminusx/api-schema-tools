
## Lead

### Описание типа
Лид.<br/><br/>Контроллер: Leads.<br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*text*|True|[string](/types/string)|Текст сообщения.<br/>Максимум - 2000 символов.<br/>|
|*page_count*|False|[numeric](/types/numeric)|Количество страниц, просмотренных посетителем в ходе визита, перед тем, как он отправил лид.<br/>|
|*updated_at*|True|[datetime](/types/datetime)|Дата последнего обновления.<br/>|
|*completed_at*|False|[datetime](/types/datetime)|Дата пометки «обработано».<br/>|
|*answer_text*|False|[string](/types/string)|Текст ответа сотрудника.<br/>Максимум - 2000 символов.<br/>|
|*result*|True|[string](/types/string)|Статус обработки лида.<br/>Возможные значения:<br/>missed – еще не обработанный;<br/>completed – обработан.<br/>|
|*duration*|False|[numeric](/types/numeric)|Время в секундах, прошедшее с момента отправки сообщения посетителем и пометкой обработано (result = completed).<br/>|
|*visit_count*|False|[numeric](/types/numeric)|Общее количество визитов посетителя на сайт, включая визит, в котором был отправлен лид.<br/>|
|*id*|True|[numeric](/types/numeric)|ID лида.<br/>|
|*search_engine*|False|[string](/types/string)|Название поискового сервиса.<br/>Содержит значение, если посетитель открыл форму офлайн сообщения, перейдя на сайт из результатов поиска сервисов типа Yandex или Google.<br/>|
|*city*|False|[string](/types/string)|Город, из которого посетитель инициировал обращение.<br/>Определяется механизмами геолокации LiveTex.<br/>|
|*created_by*|False|[Employee](/types/Employee)|Сотрудник, создавший лид.<br/>null, если лид создан посетителем.<br/>|
|*department*|False|[Department](/types/Department)|Отдел, в который отправлен лид.<br/>|
|*ext_referer*|False|[string](/types/string)|Адрес, с которого посетитель перешел на сайт. <br/>|
|*email*|False|[string](/types/string)|Адрес электронной почты.<br/>Одно из полей email или phone должно быть указано.<br/>|
|*site*|False|[Site](/types/Site)|Сайт, на котором отправлен лид.<br/>|
|*phone*|False|[string](/types/string)|Номер телефона.<br/>Одно из полей email или phone должно быть указано.<br/>|
|*completed_by*|False|[Employee](/types/Employee)|Сотрудник, который поставил отметку «обработано».<br/>|
|*name*|True|[string](/types/string)|Имя посетителя.<br/>|
|*int_referer*|False|[string](/types/string)|Адрес страницы, на которой инициирована форма офлайн-сообщения.<br/>|
|*search_query*|False|[string](/types/string)|Строка поискового запроса.<br/>Содержит значение, если посетитель открыл форму офлайн сообщения, перейдя на сайт из результатов поиска сервисов типа Yandex или Google.<br/>|
|*is_locked*|False|[boolean](/types/boolean)|Признак блокировки лида.<br/>|
|*type*|True|[string](/types/string)|Тип лида.<br/>Возможные значения:<br/>form – обычный лид, созданный посетителем через форму лида;<br/>callback – лид, созданный посетителем по кнопке «Перезвоните мне» или через X-widget;<br/>chat – лид, созданный сотрудником из чата.<br/>|
|*created_at*|True|[datetime](/types/datetime)|Дата создания.<br/>|
|*locked_by*|False|[Employee](/types/Employee)|Сотрудник, заблокировавший лид.<br/>|
|*conversation*|False|[Conversation](/types/Conversation)|Обращение, в рамках которого отправлен лид.<br/>Обращение и лид имеют некоторое количество одноименных атрибутов (country, city, ext_referer и т.д.), которые идентичны по смыслу, но фиксируются в разные моменты времени и, как следствие могут иметь разные значения.<br/>|
|*assigned_to*|False|[Employee](/types/Employee)|Сотрудник, за которым закреплен лид. Как правило этот сотрудник является создателем лида.<br/>|
|*is_managed*|True|[boolean](/types/boolean)|True, если лид входит в число своих лидов сотрудника, вызывающего метод.<br/>Это признак доступен только для чтения.<br/>|
|*country*|False|[string](/types/string)|Страна, из которой посетитель инициировал обращение.<br/>Определяется механизмами геолокации LiveTex.<br/>|
|*entry_page*|False|[string](/types/string)|Страница, с которой посетитель начал визит, в котором был отправлен лид.<br/>|
