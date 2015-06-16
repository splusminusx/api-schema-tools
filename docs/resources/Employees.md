
# Employees

## Описание ресурса

# Методы

## me

### Описание метода
Employees.me<br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*fields*|False|[string](/docs/types/string.md)|Список через запятую возвращаемых полей.<br/>|

### Результат
[Employee](/docs/types/Employee.md)
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|full||
|manager|full||
|chief|full||
|chief_partner|full||
|operator|full||
|admin_partner|full||

## search

### Описание метода
Employees.search<br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*text*|True|[string](/docs/types/string.md)|Подстрока в имени или фамилии сотрудника.<br/>|

### Результат
Array.<[Employee](/docs/types/Employee.md)>
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|full||
|manager|full||
|chief|full||
|chief_partner|full||
|operator|full||
|admin_partner|full||

## show

### Описание метода
Employees.show<br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*fields*|False|[string](/docs/types/string.md)|Список через запятую возвращаемых полей.<br/>|
|*id*|True|[numeric](/docs/types/numeric.md)|ID сотрудника.<br/>|

### Результат
[Employee](/docs/types/Employee.md)
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|full||
|manager|full||
|chief|full||
|chief_partner|full||
|operator|full||
|admin_partner|full||

## register

### Описание метода
Employees.register<br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*first_name*|True|[string](/docs/types/string.md)|Полное имя.<br/>Значение будет записано в поле first_name соответствующей сотрудника.<br/>|
|*password*|True|[string](/docs/types/string.md)|Пароль.<br/>|
|*site_name*|True|[string](/docs/types/string.md)|Адрес сайта, на котором планируется использовать сервис LiveTex.<br/>|
|*phone*|False|[phone](/docs/types/phone.md)|Телефон.<br/>|
|*invite_id*|False|[numeric](/docs/types/numeric.md)|Идентификатор приглашения.<br/>|
|*partner_data*|False|[<RegistrationPartnerData>](/docs/types/<RegistrationPartnerData>.md)|Дополнительные поля, связанные с регистрацией, важные для партнерского отдела.<br/>|
|*referral*|False|[numeric](/docs/types/numeric.md)|Идентификатор аффилированного партнера.<br/>|
|*marketing_data*|False|[<RegistrationMarketingData >](/docs/types/<RegistrationMarketingData >.md)|Дополнительные поля, связанные с регистрацией, важные для отдела маркетинга.<br/>|
|*email*|True|[email](/docs/types/email.md)|Адрес электронной почты.<br/>|

### Результат
None
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|

## list

### Описание метода
Employees.list<br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*q*|False|[string](/docs/types/string.md)|Критерий поиска.<br/>Доступные поля:<br/>ids – idlist, список ID сотрудников;<br/>department_ids – idlist, список ID отделов;<br/>first_name;<br/>last_name;<br/>email;<br/>role;<br/>is_active;<br/>state – enum, состояние сотрудника;<br/>is_managed – boolean, признак своего сотрудника.<br/>|
|*fields*|False|[string](/docs/types/string.md)|Список через запятую возвращаемых полей.<br/>|
|*limit*|False|[numeric](/docs/types/numeric.md)|По умолчанию – 50.<br/>|
|*sort*|False|[string](/docs/types/string.md)|Сортировка результатов.<br/>Возможные значения:<br/>last_name:a – по умолчанию, last_name:d;<br/>first_name:a, first_name:d;<br/>is_active:a, is_active:d;<br/>created_at:a, created_at:d;<br/>updated_at:a, updated_at:d.<br/>|
|*offset*|False|[numeric](/docs/types/numeric.md)|По умолчанию – 0.<br/>|

### Результат
Array.<[Employee](/docs/types/Employee.md)>
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|full||
|manager|full||
|chief|full||
|chief_partner|full||
|operator|full||
|admin_partner|full||

## update

### Описание метода
Employees.update<br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*last_name*|False|[string](/docs/types/string.md)|Фамилия сотрудника.<br/>|
|*chat_limit*|False|[numeric](/docs/types/numeric.md)|Количество одновременно обрабатываемых чатов.<br/>0 - отсутствие ограничения.<br/>|
|*photo*|False|[file](/docs/types/file.md)|Фотография сотрудника.<br/>Изображение в формате JPEG, GIF или PNG с размерами не менее 60x70px и не более 2560x2560px.<br/>Максимальный размер файла – 5 MB.<br/>|
|*is_sip_forward*|False|[boolean](/docs/types/boolean.md)|Включение/выключение переадресации на SIP.<br/>|
|*is_cobrowse*|False|[boolean](/docs/types/boolean.md)|Включение/выключение функции «Виртуальный ассистент».<br/>Принимается во внимание только, если эта функция включена на глобальном уровне. См. Settings.<br/>|
|*phone_forward_number*|False|[string](/docs/types/string.md)|Номер для переадресации на телефон.<br/>Обязательно при is_phone_forward=true.<br/>|
|*id*|True|[numeric](/docs/types/numeric.md)|ID сотрудника.<br/>|
|*first_name*|False|[string](/docs/types/string.md)|Имя сотрудника.<br/>|
|*password*|False|[string](/docs/types/string.md)|Новый пароль.<br/>Если не указано или пусто, то старый пароль не меняется.<br/>Минимальная длина – 6 символов.<br/>|
|*role_code*|False|[string](/docs/types/string.md)|Код роли.<br/>|
|*managed_department_ids*|False|[idlist](/docs/types/idlist.md)|Список, через запятую, ID отделов, входящих в область видимости сотрудника.<br/>Возможно указание удаленных отделов.<br/>|
|*is_lead_assigned*|False|[boolean](/docs/types/boolean.md)|Признак закрепления за оператором, созданных им лидов из чатов.<br/>|
|*email*|False|[email](/docs/types/email.md)|Адрес электронной почты.<br/>|
|*sip_forward_number*|False|[string](/docs/types/string.md)|Номер для переадресации на SIP.<br/>Обязательно при is_sip_forward=true.<br/>|
|*is_call*|False|[boolean](/docs/types/boolean.md)|Включение/выключение функциональности звонков.<br/>Принимается во внимание только, если эта функциональность включена на глобальном уровне. См. Settings.<br/>|
|*is_active*|False|[boolean](/docs/types/boolean.md)|Признак активности учетной записи сотрудника.<br/>|
|*phone*|False|[phone](/docs/types/phone.md)|Телефон сотрудника.<br/>|
|*managed_site_ids*|False|[idlist](/docs/types/idlist.md)|Список, через запятую, ID сайтов, входящих в область видимости сотрудника.<br/>Возможно указание удаленных сайтов.<br/>|
|*is_first_steps_passed*|False|[boolean](/docs/types/boolean.md)|Признак завершения первичного обучения.<br/>|
|*department_ids*|False|[idlist](/docs/types/idlist.md)|Список, через запятую, ID отделов, в которые входит сотрудник.<br/>|
|*is_lead_notify*|False|[boolean](/docs/types/boolean.md)|Включение/выключение нотификации на электронную почту о поступлении новых лидов.<br/>|
|*is_phone_forward*|False|[boolean](/docs/types/boolean.md)|Включение/выключение переадресации на телефон.<br/>|

### Результат
None
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|full|Для самого себя разрешено изменении всех полей, за исключением:|
|manager|managed|Для сотрудников с ролью «Оператор» разрешено изменении всех полей за исключением:|
|chief|managed|Только для своих сотрудников, за исключением сотрудника с ролью, имеющей признак is_admin = true.|
|chief_partner|managed|Только для своих сотрудников, за исключением сотрудника с ролью, имеющей признак is_admin = true.|
|operator|user|Разрешено изменение только самого себя и только следующих полей:|
|admin_partner|full|Для самого себя разрешено изменении всех полей, за исключением:|

## setNewPassword

### Описание метода
Employees.setNewPassword<br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*password*|True|[string](/docs/types/string.md)|Новый пароль.<br/>|
|*hash*|True|[string](/docs/types/string.md)|Одноразовый ключ, отправленный по email, указанному при вызове метода Employees.resetPassword.<br/>|

### Результат
None
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|

## registerAddPromo

### Описание метода
Employees.registerAddPromo<br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*id*|True|[numeric](/docs/types/numeric.md)|Идентификатор аккаунта LiveTex (LiveTex ID), который вернул метод Employees.register.<br/>|
|*promo_code*|True|[string](/docs/types/string.md)|Промо код.<br/>|

### Результат
None
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|

## add

### Описание метода
Employees.add<br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*sip_forward_number*|False|[string](/docs/types/string.md)|Номер для переадресации на SIP.<br/>Обязательно при is_sip_forward=true.<br/>|
|*first_name*|True|[string](/docs/types/string.md)|Имя сотрудника.<br/>|
|*last_name*|False|[string](/docs/types/string.md)|Фамилия сотрудника.<br/>|
|*is_cobrowse*|False|[boolean](/docs/types/boolean.md)|Включение/выключение функции «Виртуальный ассистент».<br/>Принимается во внимание только, если эта функция включена на глобальном уровне. См. Settings.<br/>По умолчанию – true.<br/>|
|*chat_limit*|False|[numeric](/docs/types/numeric.md)|Количество одновременно обрабатываемых чатов.<br/>По умолчанию – 0, что означает отсутствие ограничения.<br/>|
|*photo*|False|[file](/docs/types/file.md)|Фотография сотрудника.<br/>Изображение в формате JPEG, GIF или PNG с размерами не менее 60x70px и не более 2560x2560px.<br/>Максимальный размер файла – 5 MB.<br/>|
|*department_ids*|False|[idlist](/docs/types/idlist.md)|Список, через запятую, ID отделов, в которые входит сотрудник.<br/>|
|*is_active*|False|[boolean](/docs/types/boolean.md)|Признак активности учетной записи сотрудника.<br/>По умолчанию – true.<br/>|
|*is_sip_forward*|False|[boolean](/docs/types/boolean.md)|Включение/выключение переадресации на SIP.<br/>По умолчанию – false.<br/>|
|*is_lead_notify*|False|[boolean](/docs/types/boolean.md)|Включение/выключение нотификации на электронную почту о поступлении новых лидов.<br/>По умолчанию – false.<br/>|
|*phone*|False|[phone](/docs/types/phone.md)|Телефон сотрудника.<br/>|
|*managed_site_ids*|False|[idlist](/docs/types/idlist.md)|Список, через запятую, ID сайтов, входящих в область видимости сотрудника.<br/>Возможно указание удаленных сайтов.<br/>|
|*managed_department_ids*|False|[idlist](/docs/types/idlist.md)|Список, через запятую, ID отделов, входящих в область видимости сотрудника.<br/>Возможно указание удаленных отделов.<br/>|
|*is_lead_assigned*|False|[boolean](/docs/types/boolean.md)|Признак закрепления за оператором, созданных им лидов из чатов.<br/>По умолчанию – false.<br/>|
|*is_call*|False|[boolean](/docs/types/boolean.md)|Включение/выключение функциональности звонков.<br/>Принимается во внимание только, если эта функциональность включена на глобальном уровне. См. Settings.<br/>По умолчанию – false.<br/>|
|*phone_forward_number*|False|[string](/docs/types/string.md)|Номер для переадресации на телефон.<br/>Обязательно при is_phone_forward=true.<br/>|
|*password*|True|[string](/docs/types/string.md)|Пароль.<br/>Минимальная длина – 6 символов.<br/>|
|*role_code*|False|[string](/docs/types/string.md)|Код роли. По умолчанию назначается роль, имеющая признак is_default = true.<br/>|
|*email*|True|[email](/docs/types/email.md)|Адрес электронной почты.<br/>|
|*is_phone_forward*|False|[boolean](/docs/types/boolean.md)|Включение/выключение переадресации на телефон.<br/>По умолчанию – false.<br/>|

### Результат
[Employee](/docs/types/Employee.md)
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|full||
|manager|full|В значении поля department_ids принимаются во внимание только свои отделы.|
|chief|full|В значении поля department_ids принимаются во внимание только свои отделы.|
|chief_partner|full|В значении поля department_ids принимаются во внимание только свои отделы.|
|operator|none||
|admin_partner|full||

## registerConfirm

### Описание метода
Employees.registerConfirm<br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*hash*|True|[string](/docs/types/string.md)|Ключ активации, отправленный по email, указанному при вызове метода Employees.register.<br/>|
|*id*|True|[numeric](/docs/types/numeric.md)|Идентификатор аккаунта LiveTex (LiveTex ID), который вернул метод Employees.register.<br/>|

### Результат
None
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|

## batchUpdate

### Описание метода
Employees.batchUpdate<br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*sip_forward_number*|False|[string](/docs/types/string.md)|Номер для переадресации на SIP.<br/>Обязательно при is_sip_forward=true.<br/>|
|*is_lead_notify*|False|[boolean](/docs/types/boolean.md)|Включение/выключение нотификации на электронную почту о поступлении новых лидов.<br/>|
|*is_cobrowse*|False|[boolean](/docs/types/boolean.md)|Включение/выключение функции «Виртуальный ассистент».<br/>Принимается во внимание только, если эта функция включена на глобальном уровне. См. Settings.<br/>|
|*chat_limit*|False|[numeric](/docs/types/numeric.md)|Количество одновременно обрабатываемых чатов.<br/>0 - отсутствие ограничения.<br/>|
|*is_active*|False|[boolean](/docs/types/boolean.md)|Признак активности учетной записи сотрудника.<br/>|
|*ids*|True|[idlist](/docs/types/idlist.md)|Список, через запятую, ID сотрудников.<br/>|
|*is_sip_forward*|False|[boolean](/docs/types/boolean.md)|Включение/выключение переадресации на SIP.<br/>|
|*is_call*|False|[boolean](/docs/types/boolean.md)|Включение/выключение функциональности звонков.<br/>Принимается во внимание только, если эта функциональность включена на глобальном уровне. См. Settings.<br/>|
|*phone_forward_number*|False|[string](/docs/types/string.md)|Номер для переадресации на телефон.<br/>Обязательно при is_phone_forward=true.<br/>|
|*is_phone_forward*|False|[boolean](/docs/types/boolean.md)|Включение/выключение переадресации на телефон.<br/>|

### Результат
None
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|full||
|manager|managed||
|chief|managed||
|chief_partner|managed||
|operator|user||
|admin_partner|full||

## delete

### Описание метода
Employees.delete<br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*id*|True|[numeric](/docs/types/numeric.md)|ID сотрудника.<br/>|

### Результат
None
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|full|За исключением самого себя.|
|manager|none||
|chief|managed|За исключением самого себя.|
|chief_partner|managed|За исключением самого себя.|
|operator|none||
|admin_partner|full|За исключением самого себя.|

## resetPassword

### Описание метода
Employees.resetPassword<br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*email*|True|[string](/docs/types/string.md)|Адрес электронной почты сотрудника.<br/>|

### Результат
None
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
