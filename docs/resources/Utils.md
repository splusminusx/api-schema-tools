
# Utils

## Описание ресурса

# Методы

## batch

### Описание метода
Осуществляет пакетное выполнение методов.<br/>Соответствует конкретному методу в пакете.<br/>ВНИМАНИЕ!<br/>Метод НЕ является транзакционным. Ошибка в каком-либо вызове НЕ приведет к отмене ранее выполненных изменений и НЕ остановит процесс исполнения оставшихся методов.<br/>Зависимость методов в пакете <br/>При указании параметров вызова метода можно ссылаться на результаты выполнения предыдущего метода с помощью инструкций JSONPath - . <br/>Метод, результаты которого требуется использовать, необходимо пометить с помощью поля id в BatchRequest. Это имя можно использовать в значениях параметров последующих методов с помощью конструкции вида:<br/>${REQUEST_ID:JSONPathExpression}<br/>Ссылаться можно только на результаты предыдущих методов, поскольку они выполняются строго в порядке их указания.<br/>Поле, на которое указывает JSONPathExpression, должно присутствовать в составе данных, возвращаемых методом (см. параметр fields). Если выражение JSONPathExpression некорректно или ссылается на несуществующее поле, то система вернет для данного вызова код 422 с ошибкой invalid для соответствующего параметра.<br/>Пример<br/>curl https://api.livetex.ru/v2/utils/batch \<br/>-H "Authorization: Bearer ACCESS_TOKEN" \<br/>-d "methods[0][method]=carts.commit" \<br/>-d "methods[0][parameters][id]=123456" \<br/>-d "methods[0][id]=invoice" \<br/>-d "methods[1][method]=products.list" \<br/>-d "methods[1][parameters][fields]=id,offering(id,title)" \<br/>--data-urlencoded 'methods[1][parameters][q]=ids=${invoice:$.order.products.*.id}'<br/><br/>{<br/>    "results": [<br/>        {<br/>            "id": "invoice",<br/>            "code": 200,<br/>            "message": "",<br/>            "results": {<br/>                "id": 987654,<br/>                "number": "987654",<br/>                "order": {<br/>                    "id":"45682",<br/>                    "products":[{"id": 1001}, {"id": 1002}],<br/>                    "activation_type": "now",<br/>                    "period":{<br/>                        ...<br/>                    },<br/>                    "created_at": "2014-09-24T15:24:45Z",<br/>                    "updated_at": "2014-09-24T15:24:45Z"<br/>                },<br/>                "payer": {<br/>                    ...<br/>                },<br/>                ...<br/>            }<br/>        },<br/>        {<br/>            "id": "",<br/>            "code": 200,<br/>            "message": "",<br/>            "total": 2,<br/>            "results": [<br/>                {<br/>                    "id": 1001,<br/>                    "offering": {<br/>                        "id": "2001",<br/>                        "title": "Генератор лидов"<br/>                    }<br/>                    <br/>                },<br/>                {<br/>                    "id": 1002,<br/>                    "offering": {<br/>                        "id": "2002",<br/>                        "title": "HTTPS"<br/>                    }<br/>                }<br/>            <br/>            ]<br/>        }<br/>    ]<br/>}<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*methods*|True|Array.<[BatchRequest](/types/BatchRequest)>|Массив методов и их параметров.<br/>Максимум 10 элементов. Одиннадцатый элемент и далее будут проигнорированы.<br/>|

### Результат
Array.<[BatchResponse](/types/BatchResponse)>
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
