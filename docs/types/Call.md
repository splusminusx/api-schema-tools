
## Call

### Описание типа
Call<br/>Звонок.<br/>Таблица 13. Поля звонка<br/><br/>Контроллер: Сalls.<br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*employee_vote*|False|[EmployeeVote](/docs/types/EmployeeVote.md)|Оценка сотрудника.<br/>|
|*visitor*|True|[Visitor](/docs/types/Visitor.md)|Посетитель.<br/>|
|*page_count*|False|[numeric](/docs/types/numeric.md)|Количество страниц, просмотренных посетителем в ходе визита, перед тем, как он совершил звонок.<br/>|
|*rem_lost_in_queue*|True|[boolean](/docs/types/boolean.md)|Признак "Потерянный в очереди".<br/>В данный момент всегда false.<br/>|
|*rem_transfer*|True|[boolean](/docs/types/boolean.md)|Признак "Ручной перевод".<br/>|
|*result*|True|[string](/docs/types/string.md)|Итог звонка.<br/>Возможные значения:<br/>missed – пропущенный;<br/>completed – состоявшийся.<br/>|
|*duration*|True|[numeric](/docs/types/numeric.md)|Продолжительность звонка в секундах, включая answer_time.<br/>|
|*visit_count*|False|[numeric](/docs/types/numeric.md)|Общее количество визитов посетителя на сайт, включая визит, в котором был совершен звонок.<br/>|
|*id*|True|[numeric](/docs/types/numeric.md)|ID звонка.<br/>|
|*prechats_chat*|False|Array.<[Object](/docs/types/Object.md)>|Пречат поля, видимые в Пульте оператора.<br/>Эти поля могут быть настроены в Личном кабинете. В этом случае их значение указывает посетитель при старте чата.<br/>Кроме того, пречат поля могут быть программно определены в параметрах chatAttributes методов Client API: .<br/>Значение поля – массив объектов, каждый из которых имеет 2 ключа: name и value, содержащие соответственно имя и значение пречат поля.<br/>|
|*answer_time*|True|[numeric](/docs/types/numeric.md)|Время в секундах, через которое оператор ответил на ответил на звонок.<br/>|
|*lead*|False|[Lead](/docs/types/Lead.md)|Лид, из которого был сделан звонок.<br/>Имеет смысл только для исходящих звонков.<br/>|
|*rem_long_answer*|True|[boolean](/docs/types/boolean.md)|Признак "Долгий ответ".<br/>В данный момент всегда false.<br/>|
|*visitor_vote*|False|[string](/docs/types/string.md)|Оценка посетителя.<br/>Возможные значения:<br/>positive – положительная оценка;<br/>negative – отрицательная оценка;<br/>undefined – посетитель не поставил оценку.<br/>|
|*employee*|True|[Employee](/docs/types/Employee.md)|Сотрудник.<br/>|
|*ext_referer*|False|[string](/docs/types/string.md)|Адрес, с которого посетитель перешел на сайт. <br/>|
|*prechats_hidden*|False|Array.<[Object](/docs/types/Object.md)>|Скрытые пречат поля. В Пульте оператора они не отображаются.<br/>Пречат поля этого типа могут быть программно определены в параметрах hiddenAttributes методов Client API: .<br/>Значение поля – массив объектов, каждый из которых имеет 2 ключа: name и value, содержащие соответственно имя и значение пречат поля.<br/>|
|*search_engine*|False|[string](/docs/types/string.md)|Название поискового сервиса.<br/>Содержит значение, если посетитель начал звонок, перейдя на сайт из результатов поиска сервисов типа Yandex или Google.<br/>|
|*is_managed*|True|[boolean](/docs/types/boolean.md)|True, если звонок входит в число своих звонков сотрудника, вызывающего метод.<br/>Это признак доступен только для чтения.<br/>|
|*updated_at*|True|[datetime](/docs/types/datetime.md)|Дата последнего обновления.<br/>|
|*department*|False|[Department](/docs/types/Department.md)|Отдел.<br/>|
|*rem_empty*|True|[boolean](/docs/types/boolean.md)|Признак "Отсеянный".<br/>|
|*rem_auto*|True|[boolean](/docs/types/boolean.md)|Признак "Автоматический перевод". <br/>|
|*int_referer*|False|[string](/docs/types/string.md)|Адрес страницы, на которой начался диалог.<br/>|
|*is_incoming*|True|[boolean](/docs/types/boolean.md)|Признак входящего звонка.<br/>|
|*search_query*|False|[string](/docs/types/string.md)|Строка поискового запроса.<br/>Содержит значение, если посетитель начал звонок, перейдя на сайт из результатов поиска сервисов типа Yandex или Google.<br/>|
|*created_at*|True|[datetime](/docs/types/datetime.md)|Дата создания.<br/>|
|*recording*|False|[string](/docs/types/string.md)|URL записи разговора.<br/>|
|*conversation*|False|[Conversation](/docs/types/Conversation.md)|Обращение, в рамках которого состоялся звонок.<br/>|
|*site*|True|[Site](/docs/types/Site.md)|Сайт.<br/>|
|*callback_url*|False|[string](/docs/types/string.md)|Значение настройки Callback URL на момент начала чата.<br/>|
|*entry_page*|False|[string](/docs/types/string.md)|Страница, с которой посетитель начал визит, в котором было отправлен лид.<br/>|
