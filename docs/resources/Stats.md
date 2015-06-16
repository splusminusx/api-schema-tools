
# Stats

## Описание ресурса
Stats<br/>Статистические данные различного типа.<br/>
# Методы

## employees

### Описание метода
Stats.employees<br/>Возвращает статистику по сотрудникам.<br/>Параметры<br/><br/>Особенности работы метода<br/>Критерии фильтрации определяют подмножество диалогов (чатов, звонков, лидов). На это подмножество накладываются права доступа текущего пользователя - выделяются свои диалоги (см. раздел «1.2.10. Ролевая модель») - получается целевое множество диалогов.<br/>Если не указан критерий employee_ids, то выборка будет содержать сотрудников (в том числе удаленных), участвовавших в целевом множестве диалогов, а также сотрудников (исключая удаленных), связанных с сайтами и отделами, к которым есть доступ у текущего пользователя вне зависимости от того, какие сайты и отделы указаны в критериях site_ids, department_ids.<br/>Если критерий employee_ids указан, от выборка будет содержать только указанных сотрудников. <br/>Статистические данные рассчитываются для каждого сотрудника в выборке по целевому множеству диалогов.<br/>Результат<br/>Массив объектов типа «Employee» с добавлением статистических данных.<br/>Перечень доступных статистических данных<br/><br/>Пример без поля "by_date"<br/>curl https://api.livetex.ru/v2/stats/employees \<br/>-H "Authorization: Bearer ACCESS_TOKEN"<br/><br/>{<br/>    "total": 2,<br/>    "results": [<br/>        {<br/>            "id": 1234567,<br/>            "first_name": "Денис",<br/>            "last_name": "Колесников",<br/>            "online_time_avg": 14680,<br/>            "chats_total": 12,<br/>            "calls_total": 2,<br/>            "leads_total": 0<br/>        },<br/>        {<br/>            "id": 1234595,<br/>            "first_name": "Ирина",<br/>            "last_name": "Попова",<br/>            "online_time_avg": 21654,<br/>            "chats_total": 15,<br/>            "calls_total": 4,<br/>            "leads_total": 0<br/>        }<br/>    ]<br/>}<br/>Пример c полем "by_date"<br/>curl "https://api.livetex.ru/v2/stats/employees?fields=id,first_name,last_name,chats_total,by_date" \<br/>-H "Authorization: Bearer ACCESS_TOKEN"<br/><br/>{<br/>    "total": 2,<br/>    "results": [<br/>        {<br/>            "id": 1234567,<br/>            "first_name": "Денис",<br/>            "last_name": "Колесников",<br/>            "chats_total": 12,<br/>            "by_date":[<br/>                {<br/>                    "date": "2013-10-15",<br/>                    "chats_total": 7<br/>                },<br/>                {<br/>                    "date": "2013-10-16",<br/>                    "chats_total": 5<br/>                }<br/>            ]<br/>        },<br/>        {<br/>            "id": 1234595,<br/>            "first_name": "Ирина",<br/>            "last_name": "Попова",<br/>            "chats_total": 15,<br/>            "by_date":[<br/>                {<br/>                    "date": "2013-10-15",<br/>                    "chats_total": 8<br/>                },<br/>                {<br/>                    "date": "2013-10-16",<br/>                    "chats_total": 7<br/>                }<br/>            ]<br/>        }<br/>    ]<br/>}<br/><br/>Уровень доступа для ролей<br/><br/>
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
Stats.contacts<br/>Возвращает статистику по контактным данным.<br/>Параметры<br/>Метод не имеет параметров.<br/>Результат<br/>Объект с полями, описанными в нижеследующей таблице.<br/>Перечень доступных статистических данных<br/>Уровень доступа для ролей<br/><br/>
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
Stats.sites<br/>Возвращает статистику по сайтам.<br/>Параметры<br/><br/>Особенности работы метода<br/>Критерии фильтрации определяют подмножество диалогов (чатов, звонков, лидов). На это подмножество накладываются права доступа текущего пользователя - выделяются свои диалоги (см. раздел «1.2.10. Ролевая модель») - получается целевое множество диалогов.<br/>Если не указан критерий site_ids, то выборка будет содержать сайты (в том числе удаленные), в которые были адресованы диалоги из целевого множества, а также сайты (исключая удаленные), доступные текущему пользователю.<br/>Если критерий site_ids указан, от выборка будет содержать только указанные сайты. <br/>Статистические данные рассчитываются для каждого сайта в выборке по целевому множеству диалогов.<br/>Результат<br/>Массив объектов типа «Site», с добавлением статистических данных.<br/>Перечень доступных статистических данных<br/><br/>Пример <br/>curl https://api.livetex.ru/v2/stats/sites \<br/>-H "Authorization: Bearer ACCESS_TOKEN"<br/><br/>{<br/>    "results": [<br/>        {<br/>            "id": 1234567,<br/>            "url": "first.mysyte.ru",<br/>            "online_time_avg": 21654,<br/>            "chats_total": 12,<br/>            "calls_total": 2,<br/>            "leads_total": 0<br/>        },<br/>        {<br/>            "id": 1234568,<br/>            "url": "second.mysyte.ru",<br/>            "online_time_avg": 14680,<br/>            "chats_total": 15,<br/>            "calls_total": 4,<br/>            "leads_total": 0<br/>        }<br/>    ]<br/>}<br/>Пример c полем "by_date"<br/>curl "https://api.livetex.ru/v2/stats/sites?fields=id,url,chats_total,by_date" \<br/>-H "Authorization: Bearer ACCESS_TOKEN"<br/><br/>{<br/>    "total": 2,<br/>    "results": [<br/>        {<br/>            "id": 1234567,<br/>            "url": "first.mysyte.ru",<br/>            "chats_total": 12,<br/>            "by_date":[<br/>                {<br/>                    "date": "2013-10-15",<br/>                    "chats_total": 7<br/>                },<br/>                {<br/>                    "date": "2013-10-16",<br/>                    "chats_total": 5<br/>                }<br/>            ]<br/>        },<br/>        {<br/>            "id": 1234568,<br/>            "url": "second.mysyte.ru",<br/>            "chats_total": 15,<br/>            "by_date":[<br/>                {<br/>                    "date": "2013-10-15",<br/>                    "chats_total": 8<br/>                },<br/>                {<br/>                    "date": "2013-10-16",<br/>                    "chats_total": 7<br/>                }<br/>            ]<br/>        }<br/>    ]<br/>}<br/><br/>Пример c полем by_department<br/>curl "https://api.livetex.ru/v2/stats/sites?fields=id,url,chats_total,by_department" \<br/>-H "Authorization: Bearer ACCESS_TOKEN"<br/><br/>{<br/>    "total": 2,<br/>    "results": [<br/>        {<br/>            "id": 1234567,<br/>            "url": "first.mysyte.ru",<br/>            "chats_total": 12,<br/>            "by_department": [<br/>                {<br/>                    "id": "123456",<br/>                    "title": "Отдел доставки",<br/>                    "chats_total": 7<br/>                },<br/>                {<br/>                    "id": "123457",<br/>                    "title": "Отдел продаж",<br/>                    "chats_total": 5<br/>                }<br/>            ]<br/>        },<br/>        {<br/>            "id": 1234568,<br/>            "url": "second.mysyte.ru",<br/>            "chats_total": 15,<br/>            "by_department": [<br/>                {<br/>                    "id": "123456",<br/>                    "title": "Отдел доставки",<br/>                    "chats_total": 8<br/>                },<br/>                {<br/>                    "id": "123457",<br/>                    "title": "Отдел продаж ",<br/>                    "chats_total": 7<br/>                }<br/>            ]<br/>        }<br/>    ]<br/>}<br/><br/>Пример c полем by_employee<br/>curl "https://api.livetex.ru/v2/stats/sites?fields=id,url,chats_total,by_employee" \<br/>-H "Authorization: Bearer ACCESS_TOKEN"<br/><br/>{<br/>    "total": 2,<br/>    "results": [<br/>        {<br/>            "id": 1234567,<br/>            "url": "first.mysyte.ru",<br/>            "chats_total": 12,<br/>            "by_employee": [<br/>                {<br/>                    "id": "123456",<br/>                    "first_name": "Иван",<br/>                    "last_name": "Давыдов",<br/>                    "chats_total": 7<br/>                },<br/>                {<br/>                    "id": "123457",<br/>                    "first_name": "Елена",<br/>                    "last_name": "Изосимова",<br/>                    "chats_total": 5<br/>                }<br/>            ]<br/>        },<br/>        {<br/>            "id": 1234568,<br/>            "url": "second.mysyte.ru",<br/>            "chats_total": 15,<br/>            "by_employee": [<br/>                {<br/>                    "id": "123456",<br/>                    "first_name": "Иван",<br/>                    "last_name": "Давыдов",<br/>                    "chats_total": 8<br/>                },<br/>                {<br/>                    "id": "123457",<br/>                    "first_name": "Елена",<br/>                    "last_name": "Изосимова",<br/>                    "chats_total": 7<br/>                }<br/>            ]<br/>        }<br/>    ]<br/>}<br/><br/>Уровень доступа для ролей<br/><br/>
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
Stats.departments<br/>Возвращает статистику по отделам.<br/>Параметры<br/><br/>Особенности работы метода<br/>Критерии фильтрации определяют подмножество диалогов (чатов, звонков, лидов). На это подмножество накладываются права доступа текущего пользователя - выделяются свои диалоги (см. раздел «1.2.10. Ролевая модель») - получается целевое множество диалогов.<br/>Если не указан критерий department_ids, то выборка будет содержать отделы (в том числе удаленные), в которые были адресованы диалоги из целевого множества, а также отделы (исключая удаленные), доступные текущему пользователю. Если в целевом множестве есть диалоги без указания отдела, то в выборке будет присутствовать фиктивный отдел, со статистическими данными по таким диалогам.<br/>Если критерий department_ids указан, от выборка будет содержать только указанные отделы. <br/>Статистические данные рассчитываются для каждого отдела в выборке по целевому множеству диалогов.<br/>Результат<br/>Массив объектов типа «Department» с добавлением статистических данных.<br/>Перечень доступных статистических данных<br/><br/>Пример без поля by_date<br/>curl https://api.livetex.ru/v2/stats/departments \<br/>-H "Authorization: Bearer ACCESS_TOKEN"<br/><br/>{<br/>    "total": 2,<br/>    "results": [<br/>        {<br/>            "id": 1234567,<br/>            "title": "Отдел продаж",<br/>            "online_time_avg": 21654,<br/>            "chats_total": 12,<br/>            "calls_total": 2,<br/>            "leads_total": 0<br/>        },<br/>        {<br/>            "id": 1234595,<br/>            "title": "Отдел доставки",<br/>            "online_time_avg": 14680,<br/>            "chats_total": 15,<br/>            "calls_total": 4,<br/>            "leads_total": 0<br/>        }<br/>    ]<br/>}<br/>Пример c полем by_date<br/>curl "https://api.livetex.ru/v2/stats/departments?fields=department,chats_total,by_date" \<br/>-H "Authorization: Bearer ACCESS_TOKEN"<br/><br/>{<br/>    "total": 2,<br/>    "results": [<br/>        {<br/>            "id": 1234567,<br/>            "title": "Отдел продаж",<br/>            "chats_total": 12,<br/>            "by_date":[<br/>                {<br/>                    "date": "2013-10-15",<br/>                    "chats_total": 7<br/>                },<br/>                {<br/>                    "date": "2013-10-16",<br/>                    "chats_total": 5<br/>                }<br/>            ]<br/>        },<br/>        {<br/>            "id": 1234595,<br/>            "title": "Отдел доставки",<br/>            "chats_total": 15,<br/>            "by_date":[<br/>                {<br/>                    "date": "2013-10-15",<br/>                    "chats_total": 8<br/>                },<br/>                {<br/>                    "date": "2013-10-16",<br/>                    "chats_total": 7<br/>                }<br/>            ]<br/>        }<br/>    ]<br/>}<br/><br/>Уровень доступа для ролей<br/><br/>
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
Stats.summary<br/>Возвращает общую статистику.<br/>Параметры<br/>Перечень доступных статистических данных<br/>Особенность работы метода<br/>Критерии фильтрации определяют подмножество диалогов (чатов, звонков, лидов). На это подмножество накладываются права доступа текущего пользователя (только свои диалоги). Соответствующие статистические показатели подсчитываются для результирующего набора диалогов.<br/>Пример без поля by_date<br/>curl https://api.livetex.ru/v2/stats/summary \<br/>-H "Authorization: Bearer ACCESS_TOKEN"<br/><br/>{<br/>    "results": {<br/>        "online_time_avg": 14680,<br/>        "chats_total": 28,<br/>        "calls_total": 7,<br/>        "leads_total": 7<br/>    }<br/>}<br/>Пример c полем by_date<br/>curl https://api.livetex.ru/v2/stats/summary?fields=chats_total,calls_total,by_date \<br/>-H "Authorization: Bearer ACCESS_TOKEN"<br/><br/>{<br/>    "results": {<br/>        "chats_total": 28,<br/>        "calls_total": 7,<br/>        "by_date":[<br/>            {<br/>                "date": "2013-10-15",<br/>                "chats_total": 12,<br/>                "calls_total": 2<br/>            },<br/>            {<br/>                "date": "2013-10-16",<br/>                "chats_total": 16,<br/>                "calls_total": 5<br/>            }<br/>        ]<br/>    }<br/>}<br/><br/>Пример c полем employee_remarks_by_remark<br/>curl https://api.livetex.ru/v2/stats/summary -G \<br/>-H "Authorization: Bearer ACCESS_TOKEN" \<br/>-d "fields=employee_remarks,employee_remarks_by_remark(id,title)"<br/><br/>{<br/>    "results": {<br/>        "employee_remarks": 28,<br/>        "employee_remarks_by_remark":[<br/>            {<br/>                "id": 123456,<br/>                "title": "Консультация была эффективной",<br/>                "employee_remarks": 22<br/>            },<br/>            {<br/>                "id": 123457,<br/>                "title": "Консультация была неэффективной",<br/>                "employee_remarks": 6<br/>            }<br/>        ]<br/>    }<br/>}<br/><br/>Уровень доступа для ролей<br/><br/>
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