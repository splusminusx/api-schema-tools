
# EmployeeChats

## Описание ресурса
EmployeeChats<br/>
# Методы

## list

### Описание метода
EmployeeChats.list<br/>Возвращает список межоператорских чатов.<br/>Межоператорским чатом считается набор сообщений между двумя операторами в пределах указанного периода времени.<br/>Параметры<br/>Результат<br/>Массив объектов со следующими полями:<br/><br/>Пример<br/>curl https://api.livetex.ru/v2/employeechats \<br/>-H "Authorization: Bearer ACCESS_TOKEN"<br/><br/>{<br/>    "total": 1,<br/>    "results": [<br/>        {<br/>            "last_message_at": "2012-12-07T09:14:57+04:00",<br/>            "last_message_text": "Спасибо за консультацию. Пока!",<br/>            "employees":[<br/>                {<br/>                    "id": "123456",<br/>                    "first_name": "Иван",<br/>                    "last_name": "Давыдов"<br/>                },<br/>                {<br/>                    "id": "123457",<br/>                    "first_name": "Елена",<br/>                    "last_name": "Изосимова"<br/>                }<br/>            ],<br/>            message_count: 10<br/>        }<br/>    ]<br/>}<br/><br/>Уровень доступа для ролей<br/><br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|**q**|False|[string](/docs/types/string.md)|Критерий поиска.<br/>Доступные поля:<br/>employee_ids – idlist, список ID сотрудников – участников чата. Чат удовлетворяет условию поиска, если хотя бы один его участник указан в этом списке.<br/>text – ключевое слово в тексте чата.<br/>created_at – datetime, максимум 30 дней.<br/>Если не указано, то фильтр устанавливается в значение, соответствующее последним 30 дням.<br/>|
|**fields**|False|[string](/docs/types/string.md)|Список через запятую возвращаемых полей сотрудников.<br/>Например: employee(first_name).<br/>|
|**limit**|False|[numeric](/docs/types/numeric.md)|По умолчанию – 50.<br/>|
|**offset**|False|[numeric](/docs/types/numeric.md)|По умолчанию – 0.<br/>|

### Резудьтат
None
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner