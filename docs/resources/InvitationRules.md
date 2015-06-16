
# InvitationRules

## Описание ресурса

# Методы

## add

### Описание метода
Добавляет новый сценарий вовлечения.<br/>Пример вызова<br/>curl "https://api.livetex.ru/v2/invitationrules" \<br/>-H "Authorization: Bearer ACCESS_TOKEN" \<br/>	-d "title=Первое посещение из России" \<br/>	-d "action=chat" \<br/>	-d "welcome=Могу ли я вам чем-то помочь?" \<br/>	-d "is_active=true" \<br/>	-d "is_new_visitor=true" \<br/>	-d "locations[0][country][id]=123" \<br/>	-d "locations[0][city][id]=3245" \<br/>	-d "site_bindings[0][site_id]=6789" \<br/>	-d "site_bindings[0][department_id]=65432"<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*site_bindings*|False|Array.<[InvitationRuleSiteBinding](/docs/types/InvitationRuleSiteBinding.md)>|Массив связей сценария вовлечения с сайтами.<br/>Состав полей объектов в массиве точно такой же, как и состав параметров метода  InvitationRuleSiteBinding.add, за исключением поля invitation_rule_id. В данном контексте оно игнорируется.<br/>|
|*page_title*|False|[string](/docs/types/string.md)|Показывать приглашение на странице с указанной подстрокой в названии (тег «title»).<br/>Если page_type=specified, то одно из двух полей page_url или page_title должно быть указано.<br/>|
|*is_new_visitor*|True|[boolean](/docs/types/boolean.md)|Показывать приглашение только новым посетителям.<br/>True – показывать только новым, false – показывать всем.<br/>|
|*site_time*|False|[numeric](/docs/types/numeric.md)|Время в секундах, проведенное на сайте посетителем, после которого ему необходимо показывать приглашение.<br/>|
|*title*|True|[string](/docs/types/string.md)|Название сценария.<br/>|
|*is_once_per_day*|False|[boolean](/docs/types/boolean.md)|Показывать приглашение только один раз в сутки.<br/>True – один раз, вне зависимости от значения max_count, false – в соответствии со значением max_count.<br/>|
|*welcome_chat*|False|[string](/docs/types/string.md)|Текст приглашения, если есть доступные операторы.<br/>Максимум 300 символов.<br/>Обязательно для action = chat или vary.<br/>|
|*confirmation_mobile*|False|[string](/docs/types/string.md)|Подтверждающее сообщение для мобильных устройств.<br/>Обязательно для action имеет значение vary или lead.<br/>ВНИМАНИЕ! В данный момент это поле не используется.<br/>|
|*page_count*|False|[numeric](/docs/types/numeric.md)|Количество просмотренных страниц посетителем, при котором ему необходимо показывать приглашение.<br/>|
|*is_active*|True|[boolean](/docs/types/boolean.md)|Признак активности сценария.<br/>|
|*welcome_lead*|False|[string](/docs/types/string.md)|Текст приглашения, если нет доступных операторов.<br/>Максимум 300 символов.<br/>Обязательно для action = lead или vary.<br/>|
|*locations*|False|Array.<[Location](/docs/types/Location.md)>|Массив географических расположений.<br/>|
|*page_type*|True|[string](/docs/types/string.md)|Тип страницы.<br/>Возможные значения:<br/>specified – показывать приглашение на странице, соответствующей критериям page_url и page_title.<br/>home – показывать приглашение на главной страницы;<br/>internal – показывать приглашение на внутренней странице;<br/>any – показывать приглашение на любой странице.<br/>|
|*page_time*|False|[numeric](/docs/types/numeric.md)|Время, проведенное на странице посетителем, после которого ему необходимо показывать приглашение.<br/>|
|*welcome_mobile*|True|[string](/docs/types/string.md)|Текст приглашения для мобильных устройств.<br/>Максимум 130 символов.<br/>ВНИМАНИЕ! В данный момент это поле не используется.<br/>|
|*action*|True|[string](/docs/types/string.md)|Действие, которое следует выполнить, если ситуация подпадает под настройки сценария.<br/>Возможные значения:<br/>vary – показать приглашение в чат, если есть доступные операторы или форму генератора лидов, если доступных операторов нет.<br/>chat – показать приглашение в чат, если есть активные операторы. В противном случае ничего не показывать;<br/>lead – показать форму генератора лида, если нет активных операторов. В противном случае ничего не показывать.<br/>|
|*confirmation_lead*|False|[string](/docs/types/string.md)|Подтверждающее сообщение, которое показывается посетителю после отправки формы лида.<br/>Максимум 180 символов.<br/>Обязательно для action = lead или vary.<br/>|
|*max_count*|False|[numeric](/docs/types/numeric.md)|Максимальное количество показов конкретному посетителю приглашений по данному сценарию в течение календарных суток.<br/>Счетчик показов обнуляется по истечению суток с момента последнего показа.<br/>Отсутствие значения или 0 – ограничения нет.<br/>|
|*page_url*|False|[string](/docs/types/string.md)|Показывать приглашение на странице с указанным адресом.<br/>Адрес указывается без приставки «http://» или «https://», например:<br/>www.mycompany.ru/about/contacts<br/>Если page_type=specified, то одно из двух полей page_url или page_title должно быть указано.<br/>|

### Результат
[InvitationRule](/docs/types/InvitationRule.md)
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|*admin*|full||
|*manager*|full|В параметре site_bindings принимаются во внимание только site_id своих сайтов. Все остальные игнорируются.|
|*chief*|full|В параметре site_bindings принимаются во внимание только site_id своих сайтов. Все остальные игнорируются.|
|*chief_partner*|full|В параметре site_bindings принимаются во внимание только site_id своих сайтов. Все остальные игнорируются.|
|*operator*|none||
|*admin_partner*|full||

## show

### Описание метода
Возвращает данные указанного сценария вовлечения.<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*fields*|False|[string](/docs/types/string.md)|Список через запятую возвращаемых полей.<br/>|
|*id*|True|[numeric](/docs/types/numeric.md)|ID сценария вовлечения.<br/>|

### Результат
[InvitationRule](/docs/types/InvitationRule.md)
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|*admin*|full||
|*manager*|full||
|*chief*|full||
|*chief_partner*|full||
|*operator*|none||
|*admin_partner*|full||

## list

### Описание метода
Возвращает список сценариев вовлечения.<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*q*|False|[string](/docs/types/string.md)|Критерий поиска.<br/>Доступные поля:<br/>ids – idlist, список ID сценариев вовлечения.<br/>site_ids – idlist, список ID сайтов.<br/>text – поиск по текстам полей welcome, welcome_mobile, confirmation, confirmation_mobile;<br/>action – enum, список возможных значение поля action;<br/>title;<br/>is_active.<br/>|
|*fields*|False|[string](/docs/types/string.md)|Список через запятую возвращаемых полей.<br/>|
|*limit*|False|[numeric](/docs/types/numeric.md)|По умолчанию – 50.<br/>|
|*sort*|False|[string](/docs/types/string.md)|Сортировка результатов.<br/>Возможные значение:<br/>title:a – по умолчанию;<br/>created_at:d.<br/>|
|*offset*|False|[numeric](/docs/types/numeric.md)|По умолчанию – 0.<br/>|

### Результат
Array.<[InvitationRule](/docs/types/InvitationRule.md)>
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|*admin*|full||
|*manager*|full||
|*chief*|full||
|*chief_partner*|full||
|*operator*|none||
|*admin_partner*|full||

## update

### Описание метода
Изменяет указанный сценарий вовлечения.<br/>Пример вызова<br/>curl "https://api.livetex.ru/v2/invitationrules/12345" \<br/>	-H "Authorization: Bearer ACCESS_TOKEN" \<br/>	–X PATCH \<br/>	-d "title=Первое посещение из России" \<br/>	-d "locations[0][country][id]=123" \<br/>	-d "locations[0][city][id]=3245" \<br/>	-d "site_bindings[0][site_id]=6789" \<br/>	-d "site_bindings[0][department_id]=65432"<br/>	-d "site_bindings[1][site_id]=6785"<br/><br/><br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*site_bindings*|False|Array.<[InvitationRuleSiteBinding](/docs/types/InvitationRuleSiteBinding.md)>|Массив связей сценария вовлечения с сайтами.<br/>Состав полей объектов в массиве точно такой же, как и состав параметров метода  InvitationRuleSiteBinding.add, за исключением поля invitation_rule_id. В данном контексте оно игнорируется.<br/>ВНИМАНИЕ!<br/>Значение этого параметра полностью замещает текущие связи сценария с сайтами, как если бы старые связи были удалены и созданы новые.<br/>Указание пустого массива приведет к удалению всех связей сценария с сайтами.<br/>|
|*page_title*|False|[string](/docs/types/string.md)|Показывать приглашение на странице с указанной подстрокой в названии (тег «title»).<br/>Если page_type=specified, то одно из двух полей page_url или page_title должно быть указано.<br/>|
|*is_new_visitor*|False|[boolean](/docs/types/boolean.md)|Показывать приглашение только новым посетителям.<br/>True – показывать только новым, false – показывать всем.<br/>|
|*site_time*|False|[numeric](/docs/types/numeric.md)|Время в секундах, проведенное на сайте посетителем, после которого ему необходимо показывать приглашение.<br/>|
|*title*|False|[string](/docs/types/string.md)|Название сценария.<br/>|
|*is_once_per_day*|False|[boolean](/docs/types/boolean.md)|Показывать приглашение только один раз в сутки.<br/>True – один раз, вне зависимости от значения max_count, false – в соответствии со значением max_count.<br/>|
|*welcome_chat*|False|[string](/docs/types/string.md)|Текст приглашения, если есть доступные операторы.<br/>Максимум 300 символов.<br/>Обязательно для action = chat или vary.<br/>|
|*confirmation_mobile*|False|[string](/docs/types/string.md)|Подтверждающее сообщение для мобильных устройств.<br/>ВНИМАНИЕ! В данный момент это поле не используется.<br/>|
|*page_count*|False|[numeric](/docs/types/numeric.md)|Количество просмотренных страниц посетителем, при котором ему необходимо показывать приглашение.<br/>|
|*is_active*|False|[boolean](/docs/types/boolean.md)|Признак активности сценария.<br/>|
|*welcome_lead*|False|[string](/docs/types/string.md)|Текст приглашения, если нет доступных операторов.<br/>Максимум 300 символов.<br/>Обязательно для action = lead или vary.<br/>|
|*locations*|False|Array.<[Location](/docs/types/Location.md)>|Массив географических расположений.<br/>|
|*page_type*|False|[string](/docs/types/string.md)|Тип страницы.<br/>Возможные значения:<br/>specified – показывать приглашение на странице, соответствующей критериям page_url и page_title.<br/>home – показывать приглашение на главной страницы;<br/>internal – показывать приглашение на внутренней странице;<br/>any – показывать приглашение на любой странице.<br/>|
|*page_time*|False|[numeric](/docs/types/numeric.md)|Время, проведенное на странице посетителем, после которого ему необходимо показывать приглашение.<br/>|
|*welcome_mobile*|False|[string](/docs/types/string.md)|Текст приглашения для мобильных устройств.<br/>Максимум 130 символов.<br/>ВНИМАНИЕ! В данный момент это поле не используется.<br/>|
|*action*|False|[string](/docs/types/string.md)|Действие, которое следует выполнить, если ситуация подпадает под настройки сценария.<br/>Возможные значения:<br/>vary – показать приглашение в чат, если есть доступные операторы или форму генератора лидов, если доступных операторов нет.<br/>chat – показать приглашение в чат, если есть активные операторы. В противном случае ничего не показывать;<br/>lead – показать форму генератора лида, если нет активных операторов. В противном случае ничего не показывать.<br/>|
|*confirmation_lead*|False|[string](/docs/types/string.md)|Подтверждающее сообщение, которое показывается посетителю после отправки формы лида.<br/>Максимум 180 символов.<br/>Обязательно для action = lead или vary.<br/>|
|*max_count*|False|[numeric](/docs/types/numeric.md)|Максимальное количество показов конкретному посетителю приглашений по данному сценарию в течение календарных суток.<br/>Счетчик показов обнуляется по истечению суток с момента последнего показа.<br/>Отсутствие значения или 0 – ограничения нет.<br/>|
|*id*|True|[numeric](/docs/types/numeric.md)|ID сценария вовлечения.<br/>|
|*page_url*|False|[string](/docs/types/string.md)|Показывать приглашение на странице с указанным адресом.<br/>Адрес указывается без приставки «http://» или «https://», например:<br/>www.mycompany.ru/about/contacts<br/>Если page_type=specified, то одно из двух полей page_url или page_title должно быть указано.<br/>|

### Результат
None
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|*admin*|full||
|*manager*|managed|Только свои сценарии.|
|*chief*|managed|Только свои сценарии.|
|*chief_partner*|managed|Только свои сценарии.|
|*operator*|none||
|*admin_partner*|full||

## delete

### Описание метода
Удаляет указанный сценария вовлечения.<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*id*|True|[numeric](/docs/types/numeric.md)|ID сценария вовлечения.<br/>|

### Результат
None
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|*admin*|full||
|*manager*|managed|Только свои сценарии.|
|*chief*|managed|Только свои сценарии.|
|*chief_partner*|managed|Только свои сценарии.|
|*operator*|none||
|*admin_partner*|full||
