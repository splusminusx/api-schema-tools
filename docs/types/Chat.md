
## Chat

### Описание типа
Чат – текстовый диалог между конкретным сотрудником и посетителем.<br/><br/>Контроллер: Сhats.<br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*visitor_variables*|False|[Object](/types/Object)|Объект с переменными посетителя на момент создания чата.<br/>|
|*rem_transfer*|True|[boolean](/types/boolean)|Признак "Ручной перевод".<br/>|
|*first_message*|True|[Message](/types/Message)|Первое сообщение.<br/>|
|*is_contact_info_exist*|True|[boolean](/types/boolean)|Признак присутствия контактной информации в сообщениях чата.<br/>|
|*visitor*|True|[Visitor](/types/Visitor)|Посетитель.<br/>|
|*rem_lost_in_queue*|True|[boolean](/types/boolean)|Признак "Потерянный в очереди".<br/>|
|*updated_at*|True|[datetime](/types/datetime)|Дата последнего обновления.<br/>|
|*result*|True|[string](/types/string)|Итог.<br/>Возможные значения:<br/>missed – пропущенный,<br/>completed – состоявшийся.<br/>transfer_manual – передан вручную<br/>ransfer_auto – передан автоматически<br/>|
|*duration*|True|[numeric](/types/numeric)|Длительность чата в секундах, включая answer_time и queue_time.<br/>|
|*answer_time_avg*|True|[numeric](/types/numeric)|Среднее время в секундах ответа оператора на вопросы посетителя в чате.<br/>|
|*id*|True|[numeric](/types/numeric)|ID диалога.<br/>|
|*is_closed*|True|[boolean](/types/boolean)|Признак завершённого чата.<br/>Устанавливается, когда оператор удалил посетителя из панели активных чатов в ПО "Пульт оператора".<br/>|
|*prechats_chat*|False|Array.<[Object](/types/Object)>|Пречат поля, видимые в Пульте оператора.<br/>Эти поля могут быть настроены в Личном кабинете. В этом случае их значение указывает посетитель при старте чата.<br/>Кроме того, пречат поля могут быть программно определены в параметрах chatAttributes методов Client API: .<br/>Значение поля – массив объектов, каждый из которых имеет 2 ключа: name и value, содержащие соответственно имя и значение пречат поля.<br/>|
|*rem_long_answer*|True|[boolean](/types/boolean)|Признак "Долгий ответ".<br/>|
|*visitor_vote*|True|[string](/types/string)|Оценка посетителя.<br/>Возможные значения:<br/>positive – положительная оценка,<br/>negative – отрицательная оценка,<br/>undefined – посетитель не поставил оценку.<br/>ВНИМАНИЕ!<br/>Посетитель может поставит только одну оценку в обращении. И, вне зависимости от того, во время какого чата она установлена, ее получит хронологически первый чат в обращении. Все остальные чаты будут без оценки.<br/>|
|*department*|False|[Department](/types/Department)|Отдел, в контексте которого инициировано обращение.<br/>|
|*queue_time*|True|[numeric](/types/numeric)|Время в секундах, проведенное посетителем в очереди.<br/>|
|*first_answer_time*|True|[numeric](/types/numeric)|Время в секундах, через которое оператор ответил на первое сообщение посетителя.<br/>|
|*events*|True|Array.<[ConversationEvents](/types/ConversationEvents)>|Список событий обращения в хронологическом порядке за время чата.<br/>|
|*prechats_hidden*|False|Array.<[Object](/types/Object)>|Скрытые пречат поля. В Пульте оператора они не отображаются.<br/>Пречат поля этого типа могут быть программно определены в параметрах hiddenAttributes методов Client API: .<br/>Значение поля – массив объектов, каждый из которых имеет 2 ключа: name и value, содержащие соответственно имя и значение пречат поля.<br/>|
|*employee_remark*|False|[EmployeeRemark](/types/EmployeeRemark)|Оценка сотрудника.<br/>|
|*site*|True|[Site](/types/Site)|Сайт.<br/>|
|*message_count*|True|[numeric](/types/numeric)|Количество сообщений.<br/>|
|*employee*|True|[Employee](/types/Employee)|Сотрудник.<br/>|
|*rem_empty*|True|[boolean](/types/boolean)|Признак "Отсеянный".<br/>|
|*rem_auto*|True|[boolean](/types/boolean)|Признак "Автоматический перевод". <br/>|
|*created_at*|True|[datetime](/types/datetime)|Дата создания.<br/>|
|*messages*|True|Array.<[Message](/types/Message)>|Список сообщений в хронологическом порядке.<br/>|
|*conversation*|True|[Conversation](/types/Conversation)|Обращение, в рамках которого инициирован чат.<br/>|
|*is_managed*|True|[boolean](/types/boolean)|True, если чат входит в число своих чатов сотрудника, вызывающего метод.<br/>Это признак доступен только для чтения.<br/>|
|*callback_url*|False|[string](/types/string)|Значение настройки Callback URL на момент начала чата.<br/>|
