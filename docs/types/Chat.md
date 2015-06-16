
## Chat

### Описание типа
Chat<br/>Чат – текстовый диалог между конкретным сотрудником и посетителем.<br/>Таблица 19. Поля чата<br/><br/>Контроллер: Сhats.<br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*visitor_variables*|False|[Object](/docs/types/Object.md)|Объект с переменными посетителя на момент создания чата.<br/>|
|*rem_transfer*|True|[boolean](/docs/types/boolean.md)|Признак "Ручной перевод".<br/>|
|*first_message*|True|[Message](/docs/types/Message.md)|Первое сообщение.<br/>|
|*is_contact_info_exist*|True|[boolean](/docs/types/boolean.md)|Признак присутствия контактной информации в сообщениях чата.<br/>|
|*visitor*|True|[Visitor](/docs/types/Visitor.md)|Посетитель.<br/>|
|*rem_lost_in_queue*|True|[boolean](/docs/types/boolean.md)|Признак "Потерянный в очереди".<br/>|
|*updated_at*|True|[datetime](/docs/types/datetime.md)|Дата последнего обновления.<br/>|
|*result*|True|[string](/docs/types/string.md)|Итог.<br/>Возможные значения:<br/>missed – пропущенный,<br/>completed – состоявшийся.<br/>transfer_manual – передан вручную<br/>ransfer_auto – передан автоматически<br/>|
|*duration*|True|[numeric](/docs/types/numeric.md)|Длительность чата в секундах, включая answer_time и queue_time.<br/>|
|*answer_time_avg*|True|[numeric](/docs/types/numeric.md)|Среднее время в секундах ответа оператора на вопросы посетителя в чате.<br/>|
|*id*|True|[numeric](/docs/types/numeric.md)|ID диалога.<br/>|
|*is_closed*|True|[boolean](/docs/types/boolean.md)|Признак завершённого чата.<br/>Устанавливается, когда оператор удалил посетителя из панели активных чатов в ПО "Пульт оператора".<br/>|
|*prechats_chat*|False|Array.<[Object](/docs/types/Object.md)>|Пречат поля, видимые в Пульте оператора.<br/>Эти поля могут быть настроены в Личном кабинете. В этом случае их значение указывает посетитель при старте чата.<br/>Кроме того, пречат поля могут быть программно определены в параметрах chatAttributes методов Client API: .<br/>Значение поля – массив объектов, каждый из которых имеет 2 ключа: name и value, содержащие соответственно имя и значение пречат поля.<br/>|
|*rem_long_answer*|True|[boolean](/docs/types/boolean.md)|Признак "Долгий ответ".<br/>|
|*visitor_vote*|True|[string](/docs/types/string.md)|Оценка посетителя.<br/>Возможные значения:<br/>positive – положительная оценка,<br/>negative – отрицательная оценка,<br/>undefined – посетитель не поставил оценку.<br/>ВНИМАНИЕ!<br/>Посетитель может поставит только одну оценку в обращении. И, вне зависимости от того, во время какого чата она установлена, ее получит хронологически первый чат в обращении. Все остальные чаты будут без оценки.<br/>|
|*department*|False|[Department](/docs/types/Department.md)|Отдел, в контексте которого инициировано обращение.<br/>|
|*queue_time*|True|[numeric](/docs/types/numeric.md)|Время в секундах, проведенное посетителем в очереди.<br/>|
|*first_answer_time*|True|[numeric](/docs/types/numeric.md)|Время в секундах, через которое оператор ответил на первое сообщение посетителя.<br/>|
|*events*|True|Array.<[ConversationEvents](/docs/types/ConversationEvents.md)>|Список событий обращения в хронологическом порядке за время чата.<br/>|
|*prechats_hidden*|False|Array.<[Object](/docs/types/Object.md)>|Скрытые пречат поля. В Пульте оператора они не отображаются.<br/>Пречат поля этого типа могут быть программно определены в параметрах hiddenAttributes методов Client API: .<br/>Значение поля – массив объектов, каждый из которых имеет 2 ключа: name и value, содержащие соответственно имя и значение пречат поля.<br/>|
|*employee_remark*|False|[EmployeeRemark](/docs/types/EmployeeRemark.md)|Оценка сотрудника.<br/>|
|*site*|True|[Site](/docs/types/Site.md)|Сайт.<br/>|
|*message_count*|True|[numeric](/docs/types/numeric.md)|Количество сообщений.<br/>|
|*employee*|True|[Employee](/docs/types/Employee.md)|Сотрудник.<br/>|
|*rem_empty*|True|[boolean](/docs/types/boolean.md)|Признак "Отсеянный".<br/>|
|*rem_auto*|True|[boolean](/docs/types/boolean.md)|Признак "Автоматический перевод". <br/>|
|*created_at*|True|[datetime](/docs/types/datetime.md)|Дата создания.<br/>|
|*messages*|True|Array.<[Message](/docs/types/Message.md)>|Список сообщений в хронологическом порядке.<br/>|
|*conversation*|True|[Conversation](/docs/types/Conversation.md)|Обращение, в рамках которого инициирован чат.<br/>|
|*is_managed*|True|[boolean](/docs/types/boolean.md)|True, если чат входит в число своих чатов сотрудника, вызывающего метод.<br/>Это признак доступен только для чтения.<br/>|
|*callback_url*|False|[string](/docs/types/string.md)|Значение настройки Callback URL на момент начала чата.<br/>|
