
## Call

### Описание типа
Звонок.<br/><br/>Контроллер: Сalls.<br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*employee_vote*|False|[EmployeeVote](/types/EmployeeVote)|Оценка сотрудника.<br/>|
|*visitor*|True|[Visitor](/types/Visitor)|Посетитель.<br/>|
|*page_count*|False|[numeric](/types/numeric)|Количество страниц, просмотренных посетителем в ходе визита, перед тем, как он совершил звонок.<br/>|
|*rem_lost_in_queue*|True|[boolean](/types/boolean)|Признак "Потерянный в очереди".<br/>В данный момент всегда false.<br/>|
|*rem_transfer*|True|[boolean](/types/boolean)|Признак "Ручной перевод".<br/>|
|*result*|True|[string](/types/string)|Итог звонка.<br/>Возможные значения:<br/>missed – пропущенный;<br/>completed – состоявшийся.<br/>|
|*duration*|True|[numeric](/types/numeric)|Продолжительность звонка в секундах, включая answer_time.<br/>|
|*visit_count*|False|[numeric](/types/numeric)|Общее количество визитов посетителя на сайт, включая визит, в котором был совершен звонок.<br/>|
|*id*|True|[numeric](/types/numeric)|ID звонка.<br/>|
|*prechats_chat*|False|Array.<[Object](/types/Object)>|Пречат поля, видимые в Пульте оператора.<br/>Эти поля могут быть настроены в Личном кабинете. В этом случае их значение указывает посетитель при старте чата.<br/>Кроме того, пречат поля могут быть программно определены в параметрах chatAttributes методов Client API: .<br/>Значение поля – массив объектов, каждый из которых имеет 2 ключа: name и value, содержащие соответственно имя и значение пречат поля.<br/>|
|*answer_time*|True|[numeric](/types/numeric)|Время в секундах, через которое оператор ответил на ответил на звонок.<br/>|
|*lead*|False|[Lead](/types/Lead)|Лид, из которого был сделан звонок.<br/>Имеет смысл только для исходящих звонков.<br/>|
|*rem_long_answer*|True|[boolean](/types/boolean)|Признак "Долгий ответ".<br/>В данный момент всегда false.<br/>|
|*visitor_vote*|False|[string](/types/string)|Оценка посетителя.<br/>Возможные значения:<br/>positive – положительная оценка;<br/>negative – отрицательная оценка;<br/>undefined – посетитель не поставил оценку.<br/>|
|*employee*|True|[Employee](/types/Employee)|Сотрудник.<br/>|
|*ext_referer*|False|[string](/types/string)|Адрес, с которого посетитель перешел на сайт. <br/>|
|*prechats_hidden*|False|Array.<[Object](/types/Object)>|Скрытые пречат поля. В Пульте оператора они не отображаются.<br/>Пречат поля этого типа могут быть программно определены в параметрах hiddenAttributes методов Client API: .<br/>Значение поля – массив объектов, каждый из которых имеет 2 ключа: name и value, содержащие соответственно имя и значение пречат поля.<br/>|
|*search_engine*|False|[string](/types/string)|Название поискового сервиса.<br/>Содержит значение, если посетитель начал звонок, перейдя на сайт из результатов поиска сервисов типа Yandex или Google.<br/>|
|*is_managed*|True|[boolean](/types/boolean)|True, если звонок входит в число своих звонков сотрудника, вызывающего метод.<br/>Это признак доступен только для чтения.<br/>|
|*updated_at*|True|[datetime](/types/datetime)|Дата последнего обновления.<br/>|
|*department*|False|[Department](/types/Department)|Отдел.<br/>|
|*rem_empty*|True|[boolean](/types/boolean)|Признак "Отсеянный".<br/>|
|*rem_auto*|True|[boolean](/types/boolean)|Признак "Автоматический перевод". <br/>|
|*int_referer*|False|[string](/types/string)|Адрес страницы, на которой начался диалог.<br/>|
|*is_incoming*|True|[boolean](/types/boolean)|Признак входящего звонка.<br/>|
|*search_query*|False|[string](/types/string)|Строка поискового запроса.<br/>Содержит значение, если посетитель начал звонок, перейдя на сайт из результатов поиска сервисов типа Yandex или Google.<br/>|
|*created_at*|True|[datetime](/types/datetime)|Дата создания.<br/>|
|*recording*|False|[string](/types/string)|URL записи разговора.<br/>|
|*conversation*|False|[Conversation](/types/Conversation)|Обращение, в рамках которого состоялся звонок.<br/>|
|*site*|True|[Site](/types/Site)|Сайт.<br/>|
|*callback_url*|False|[string](/types/string)|Значение настройки Callback URL на момент начала чата.<br/>|
|*entry_page*|False|[string](/types/string)|Страница, с которой посетитель начал визит, в котором было отправлен лид.<br/>|
