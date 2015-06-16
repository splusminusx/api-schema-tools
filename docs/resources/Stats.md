
# Stats

## Описание ресурса
Stats
Статистические данные различного типа.

# Методы

## employees

### Описание метода
Stats.employees
Возвращает статистику по сотрудникам.
Параметры

Особенности работы метода
Критерии фильтрации определяют подмножество диалогов (чатов, звонков, лидов). На это подмножество накладываются права доступа текущего пользователя - выделяются свои диалоги (см. раздел «1.2.10. Ролевая модель») - получается целевое множество диалогов.
Если не указан критерий employee_ids, то выборка будет содержать сотрудников (в том числе удаленных), участвовавших в целевом множестве диалогов, а также сотрудников (исключая удаленных), связанных с сайтами и отделами, к которым есть доступ у текущего пользователя вне зависимости от того, какие сайты и отделы указаны в критериях site_ids, department_ids.
Если критерий employee_ids указан, от выборка будет содержать только указанных сотрудников. 
Статистические данные рассчитываются для каждого сотрудника в выборке по целевому множеству диалогов.
Результат
Массив объектов типа «Employee» с добавлением статистических данных.
Перечень доступных статистических данных

Пример без поля "by_date"
curl https://api.livetex.ru/v2/stats/employees \
-H "Authorization: Bearer ACCESS_TOKEN"

{
    "total": 2,
    "results": [
        {
            "id": 1234567,
            "first_name": "Денис",
            "last_name": "Колесников",
            "online_time_avg": 14680,
            "chats_total": 12,
            "calls_total": 2,
            "leads_total": 0
        },
        {
            "id": 1234595,
            "first_name": "Ирина",
            "last_name": "Попова",
            "online_time_avg": 21654,
            "chats_total": 15,
            "calls_total": 4,
            "leads_total": 0
        }
    ]
}
Пример c полем "by_date"
curl "https://api.livetex.ru/v2/stats/employees?fields=id,first_name,last_name,chats_total,by_date" \
-H "Authorization: Bearer ACCESS_TOKEN"

{
    "total": 2,
    "results": [
        {
            "id": 1234567,
            "first_name": "Денис",
            "last_name": "Колесников",
            "chats_total": 12,
            "by_date":[
                {
                    "date": "2013-10-15",
                    "chats_total": 7
                },
                {
                    "date": "2013-10-16",
                    "chats_total": 5
                }
            ]
        },
        {
            "id": 1234595,
            "first_name": "Ирина",
            "last_name": "Попова",
            "chats_total": 15,
            "by_date":[
                {
                    "date": "2013-10-15",
                    "chats_total": 8
                },
                {
                    "date": "2013-10-16",
                    "chats_total": 7
                }
            ]
        }
    ]
}

Уровень доступа для ролей


### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|q|False|[string](/docs/types/string.md)|Критерий поиска.<br/>Доступные поля:<br/>site_ids – idlist, список ID сайтов.<br/>department_ids – idlist, список ID отделов.<br/>employee_ids – idlist, список ID сотрудников.<br/>date – date, период, за который запрашивается статистика.<br/>is_online – boolean, признак присутствия оператора в онлайн. Если указано, то метод вернет статистику по операторам с соответствующим текущим статусом.<br/>|
|fields|False|[string](/docs/types/string.md)|Список возвращаемых полей через запятую.<br/>Возможные значения приведены в нижеследующей таблице.<br/>По умолчанию возвращаются следующие поля:<br/>id;<br/>first_name;<br/>last_name;<br/>online_time_avg;<br/>chats_total;<br/>calls_total;<br/>leads_total.<br/>|
|sort|False|[string](/docs/types/string.md)|Сортировка результатов.<br/>Возможные значения:<br/>last_name:a – по умолчанию;<br/>first_name:a;<br/>online_time_avg:a, online_time_avg:d;<br/>chats_total:a, chats_total:d;<br/>calls_total:a, calls_total:d;<br/>leads_total:a, leads_total:d.<br/>|

### Резудьтат
Array.<[Employee](/docs/types/Employee.md)>
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner
## contacts

### Описание метода
Stats.contacts
Возвращает статистику по контактным данным.
Параметры
Метод не имеет параметров.
Результат
Объект с полями, описанными в нижеследующей таблице.
Перечень доступных статистических данных
Уровень доступа для ролей


### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|

### Резудьтат
None
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner
## sites

### Описание метода
Stats.sites
Возвращает статистику по сайтам.
Параметры

Особенности работы метода
Критерии фильтрации определяют подмножество диалогов (чатов, звонков, лидов). На это подмножество накладываются права доступа текущего пользователя - выделяются свои диалоги (см. раздел «1.2.10. Ролевая модель») - получается целевое множество диалогов.
Если не указан критерий site_ids, то выборка будет содержать сайты (в том числе удаленные), в которые были адресованы диалоги из целевого множества, а также сайты (исключая удаленные), доступные текущему пользователю.
Если критерий site_ids указан, от выборка будет содержать только указанные сайты. 
Статистические данные рассчитываются для каждого сайта в выборке по целевому множеству диалогов.
Результат
Массив объектов типа «Site», с добавлением статистических данных.
Перечень доступных статистических данных

Пример 
curl https://api.livetex.ru/v2/stats/sites \
-H "Authorization: Bearer ACCESS_TOKEN"

{
    "results": [
        {
            "id": 1234567,
            "url": "first.mysyte.ru",
            "online_time_avg": 21654,
            "chats_total": 12,
            "calls_total": 2,
            "leads_total": 0
        },
        {
            "id": 1234568,
            "url": "second.mysyte.ru",
            "online_time_avg": 14680,
            "chats_total": 15,
            "calls_total": 4,
            "leads_total": 0
        }
    ]
}
Пример c полем "by_date"
curl "https://api.livetex.ru/v2/stats/sites?fields=id,url,chats_total,by_date" \
-H "Authorization: Bearer ACCESS_TOKEN"

{
    "total": 2,
    "results": [
        {
            "id": 1234567,
            "url": "first.mysyte.ru",
            "chats_total": 12,
            "by_date":[
                {
                    "date": "2013-10-15",
                    "chats_total": 7
                },
                {
                    "date": "2013-10-16",
                    "chats_total": 5
                }
            ]
        },
        {
            "id": 1234568,
            "url": "second.mysyte.ru",
            "chats_total": 15,
            "by_date":[
                {
                    "date": "2013-10-15",
                    "chats_total": 8
                },
                {
                    "date": "2013-10-16",
                    "chats_total": 7
                }
            ]
        }
    ]
}

Пример c полем by_department
curl "https://api.livetex.ru/v2/stats/sites?fields=id,url,chats_total,by_department" \
-H "Authorization: Bearer ACCESS_TOKEN"

{
    "total": 2,
    "results": [
        {
            "id": 1234567,
            "url": "first.mysyte.ru",
            "chats_total": 12,
            "by_department": [
                {
                    "id": "123456",
                    "title": "Отдел доставки",
                    "chats_total": 7
                },
                {
                    "id": "123457",
                    "title": "Отдел продаж",
                    "chats_total": 5
                }
            ]
        },
        {
            "id": 1234568,
            "url": "second.mysyte.ru",
            "chats_total": 15,
            "by_department": [
                {
                    "id": "123456",
                    "title": "Отдел доставки",
                    "chats_total": 8
                },
                {
                    "id": "123457",
                    "title": "Отдел продаж ",
                    "chats_total": 7
                }
            ]
        }
    ]
}

Пример c полем by_employee
curl "https://api.livetex.ru/v2/stats/sites?fields=id,url,chats_total,by_employee" \
-H "Authorization: Bearer ACCESS_TOKEN"

{
    "total": 2,
    "results": [
        {
            "id": 1234567,
            "url": "first.mysyte.ru",
            "chats_total": 12,
            "by_employee": [
                {
                    "id": "123456",
                    "first_name": "Иван",
                    "last_name": "Давыдов",
                    "chats_total": 7
                },
                {
                    "id": "123457",
                    "first_name": "Елена",
                    "last_name": "Изосимова",
                    "chats_total": 5
                }
            ]
        },
        {
            "id": 1234568,
            "url": "second.mysyte.ru",
            "chats_total": 15,
            "by_employee": [
                {
                    "id": "123456",
                    "first_name": "Иван",
                    "last_name": "Давыдов",
                    "chats_total": 8
                },
                {
                    "id": "123457",
                    "first_name": "Елена",
                    "last_name": "Изосимова",
                    "chats_total": 7
                }
            ]
        }
    ]
}

Уровень доступа для ролей


### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|q|False|[string](/docs/types/string.md)|Критерий фильтрации.<br/>Доступные поля:<br/>site_ids – idlist, список ID сайтов.<br/>department_ids – idlist, список ID отделов.<br/>employee_ids – idlist, список ID сотрудников.<br/>date – date, период, за который запрашивается статистика.<br/>|
|fields|False|[string](/docs/types/string.md)|Список возвращаемых полей через запятую.<br/>Возможные значения приведены в нижеследующей таблице.<br/>По умолчанию возвращаются следующие поля:<br/>id;<br/>url;<br/>online_time_avg;<br/>chats_total;<br/>calls_total;<br/>leads_total.<br/>Если указано поле by_department, то принимаются во внимание также указания типа department(field_name), где field_name – имя поля отдела.<br/>|
|sort|False|[string](/docs/types/string.md)|Сортировка результатов.<br/>Возможные значения:<br/>url:a – по умолчанию;<br/>online_time_avg:a, online_time_avg:d;<br/>chats_total:a, chats_total:d;<br/>calls_total:a, calls_total:d;<br/>leads_total:a, leads_total:d.<br/>Указанная сортировка распространяется также на порядок данных в ключах "by_department" и "by_employee".<br/>Если указано "url:a", то для сортировки данных в ключе "by_department" можно указать одно из следующих возможных значений:<br/>department(title):a.<br/>А в ключе "by_employee":<br/>employee(last_name):a;<br/>employee(first_name):a.<br/>|

### Резудьтат
Array.<[Site](/docs/types/Site.md)>
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner
## departments

### Описание метода
Stats.departments
Возвращает статистику по отделам.
Параметры

Особенности работы метода
Критерии фильтрации определяют подмножество диалогов (чатов, звонков, лидов). На это подмножество накладываются права доступа текущего пользователя - выделяются свои диалоги (см. раздел «1.2.10. Ролевая модель») - получается целевое множество диалогов.
Если не указан критерий department_ids, то выборка будет содержать отделы (в том числе удаленные), в которые были адресованы диалоги из целевого множества, а также отделы (исключая удаленные), доступные текущему пользователю. Если в целевом множестве есть диалоги без указания отдела, то в выборке будет присутствовать фиктивный отдел, со статистическими данными по таким диалогам.
Если критерий department_ids указан, от выборка будет содержать только указанные отделы. 
Статистические данные рассчитываются для каждого отдела в выборке по целевому множеству диалогов.
Результат
Массив объектов типа «Department» с добавлением статистических данных.
Перечень доступных статистических данных

Пример без поля by_date
curl https://api.livetex.ru/v2/stats/departments \
-H "Authorization: Bearer ACCESS_TOKEN"

{
    "total": 2,
    "results": [
        {
            "id": 1234567,
            "title": "Отдел продаж",
            "online_time_avg": 21654,
            "chats_total": 12,
            "calls_total": 2,
            "leads_total": 0
        },
        {
            "id": 1234595,
            "title": "Отдел доставки",
            "online_time_avg": 14680,
            "chats_total": 15,
            "calls_total": 4,
            "leads_total": 0
        }
    ]
}
Пример c полем by_date
curl "https://api.livetex.ru/v2/stats/departments?fields=department,chats_total,by_date" \
-H "Authorization: Bearer ACCESS_TOKEN"

{
    "total": 2,
    "results": [
        {
            "id": 1234567,
            "title": "Отдел продаж",
            "chats_total": 12,
            "by_date":[
                {
                    "date": "2013-10-15",
                    "chats_total": 7
                },
                {
                    "date": "2013-10-16",
                    "chats_total": 5
                }
            ]
        },
        {
            "id": 1234595,
            "title": "Отдел доставки",
            "chats_total": 15,
            "by_date":[
                {
                    "date": "2013-10-15",
                    "chats_total": 8
                },
                {
                    "date": "2013-10-16",
                    "chats_total": 7
                }
            ]
        }
    ]
}

Уровень доступа для ролей


### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|q|False|[string](/docs/types/string.md)|Критерий фильтрации.<br/>Доступные поля:<br/>site_ids – idlist, список ID сайтов.<br/>department_ids – idlist, список ID отделов.<br/>employee_ids – idlist, список ID сотрудников.<br/>date – date, период, за который запрашивается статистика.<br/>|
|fields|False|[string](/docs/types/string.md)|Список возвращаемых полей через запятую.<br/>Возможные значения приведены в нижеследующей таблице.<br/>По умолчанию возвращаются следующие поля:<br/>online_time_avg;<br/>chats_total;<br/>calls_total;<br/>leads_total.<br/>|
|sort|False|[string](/docs/types/string.md)|Сортировка результатов.<br/>Возможные значения:<br/>title:a – по умолчанию;<br/>online_time_avg:a, online_time_avg:d;<br/>chats_total:a, chats_total:d;<br/>calls_total:a, calls_total:d;<br/>leads_total:a, leads_total:d.<br/>|

### Резудьтат
Array.<[Department](/docs/types/Department.md)>
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner
## summary

### Описание метода
Stats.summary
Возвращает общую статистику.
Параметры
Перечень доступных статистических данных
Особенность работы метода
Критерии фильтрации определяют подмножество диалогов (чатов, звонков, лидов). На это подмножество накладываются права доступа текущего пользователя (только свои диалоги). Соответствующие статистические показатели подсчитываются для результирующего набора диалогов.
Пример без поля by_date
curl https://api.livetex.ru/v2/stats/summary \
-H "Authorization: Bearer ACCESS_TOKEN"

{
    "results": {
        "online_time_avg": 14680,
        "chats_total": 28,
        "calls_total": 7,
        "leads_total": 7
    }
}
Пример c полем by_date
curl https://api.livetex.ru/v2/stats/summary?fields=chats_total,calls_total,by_date \
-H "Authorization: Bearer ACCESS_TOKEN"

{
    "results": {
        "chats_total": 28,
        "calls_total": 7,
        "by_date":[
            {
                "date": "2013-10-15",
                "chats_total": 12,
                "calls_total": 2
            },
            {
                "date": "2013-10-16",
                "chats_total": 16,
                "calls_total": 5
            }
        ]
    }
}

Пример c полем employee_remarks_by_remark
curl https://api.livetex.ru/v2/stats/summary -G \
-H "Authorization: Bearer ACCESS_TOKEN" \
-d "fields=employee_remarks,employee_remarks_by_remark(id,title)"

{
    "results": {
        "employee_remarks": 28,
        "employee_remarks_by_remark":[
            {
                "id": 123456,
                "title": "Консультация была эффективной",
                "employee_remarks": 22
            },
            {
                "id": 123457,
                "title": "Консультация была неэффективной",
                "employee_remarks": 6
            }
        ]
    }
}

Уровень доступа для ролей


### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|q|False|[string](/docs/types/string.md)|Критерий поиска.<br/>Доступные поля:<br/>site_ids – idlist, список ID сайтов.<br/>department_ids – idlist, список ID отделов.<br/>employee_ids – idlist, список ID сотрудников.<br/>date – date, период, за который запрашивается статистика.<br/>|
|fields|False|[string](/docs/types/string.md)|Список возвращаемых полей через запятую.<br/>Возможные значения приведены в нижеследующей таблице.<br/>По умолчанию возвращаются следующие поля:<br/>online_time_avg;<br/>chats_total;<br/>calls_total;<br/>leads_total;<br/>|

### Резудьтат
None
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner