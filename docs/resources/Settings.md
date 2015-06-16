
# Settings

## Описание ресурса
Settings

# Методы

## showFeatureStates

### Описание метода
Settings.showFeatureStates
Возвращает данные о доступности функциональных возможностей на аккаунте.
Параметры
Метод не имеет параметров.
Результат
Объект типа «FeatureStates».
Уровень доступа для ролей


### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|

### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner
## showCobrowseSettings

### Описание метода
Settings.showCobrowseSettings
Возвращает настройки функции «Виртуальный ассистент».
Параметры
Метод не имеет параметров.
Результат
Объект типа «CobrowseSettings».
Уровень доступа для ролей


### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|

### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner
## showFileTransferSettings

### Описание метода
Settings.showFileTransferSettings
Возвращает настройки функции «Передача файлов».
Параметры
Метод не имеет параметров.
Результат
Объект типа «FileTransferSettings».
Уровень доступа для ролей


### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|

### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner
## show

### Описание метода
Settings.show
Возвращает глобальные настройки.
Параметры
Метод не имеет параметров.
Результат
Объект типа «Settings».
Уровень доступа для ролей


### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|

### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner
## updateCobrowseSettings

### Описание метода
Settings.updateCobrowseSettings
Изменяет настройки функции "Виртуальный ассистент".
Параметры
Результат
Методов ничего не возвращает.
Уровень доступа для ролей


### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|is_active|False|boolean|Включение/выключение функции «Виртуальный ассистент».<br/>|

### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner
## updateAcceptanceByEmailSettings

### Описание метода
Settings.updateAcceptanceByEmailSettings
Изменяет настройки отправки актов по электронной почте.
Параметры
Результат
Методов ничего не возвращает.
Уровень доступа для ролей


### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|is_active|False|boolean|Включение/выключение отправки актов на электронную почту.<br/>|
|emails|False|string|Список через запятую адресов электронной почты.<br/><br/>|

### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner
## showAcceptanceByEmailSettings

### Описание метода
Settings.showAcceptanceByEmailSettings
Возвращает настройки отправки актов по электронной почте.
Параметры
Метод не имеет параметров.
Результат
Объект типа «AcceptanceByEmailSettings».
Уровень доступа для ролей


### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|

### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner
## updateEmployeeRemarkSettings

### Описание метода
Settings.updateEmployeeRemarkSettings
Изменяет настройки функции оценок сотрудника.
Параметры
Результат
Методов ничего не возвращает.
Уровень доступа для ролей


### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|is_active|False|boolean|Включение/выключение возможности оценки чатов сотрудниками.<br/>|

### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner
## updateFileTransferSettings

### Описание метода
Settings.updateFileTransferSettings
Изменяет настройки функции «Передача файлов».
Параметры
Результат
Методов ничего не возвращает.
Уровень доступа для ролей


### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|is_active|False|boolean|Включение/выключение функции «Передача файлов».<br/>|

### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner
## showCallSettings

### Описание метода
Settings.showCallSettings
Возвращает настройки звонковой функциональности.
Параметры
Метод не имеет параметров.
Результат
Объект типа «CallSettings».
Уровень доступа для ролей


### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|

### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner
## showTypingIndicatorSettings

### Описание метода
Settings.showTypingIndicatorSettings
Возвращает настройки функции «Подглядывания».
Параметры
Метод не имеет параметров.
Результат
Объект типа «TypingIndicatorSettings».
Уровень доступа для ролей


### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|

### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner
## showReportByEmailSettings

### Описание метода
Settings.showReportByEmailSettings
Возвращает настройки отправки отчетов по email.
Параметры
Метод не имеет параметров.
Результат
Объект типа «ReportByEmailSettings».
Уровень доступа для ролей


### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|

### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner
## updateTypingIndicatorSettings

### Описание метода
Settings.updateTypingIndicatorSettings
Изменяет настройки функции «Подглядывание».
Параметры
Результат
Методов ничего не возвращает.
Уровень доступа для ролей


### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|is_active|False|boolean|Включение/выключение функции «Подглядывание».<br/>|

### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner
## updateCallSettings

### Описание метода
Settings.updateCallSettings
Изменяет настройки звонковой функциональности.
Параметры
Результат
Методов ничего не возвращает.
Уровень доступа для ролей


### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|is_forward|False|boolean|Включение/выключение переадресации.<br/>|
|is_active|False|boolean|Включение/выключение функциональности звонков.<br/>|
|forward_sip_host|False|string|Имя хоста SIP.<br/>Обязательно при forward_type=SIP и is_forward=true.<br/>|
|forward_sip_login|False|string|Логин для подключения по SIP.<br/>Обязательно при forward_type=SIP и is_forward=true.<br/>|
|forward_sip_password|False|string|Пароль для подключения по SIP.<br/>Обязательно при forward_type=SIP и is_forward=true.<br/>|
|forward_type|False|string|Тип переадресации.<br/>Возможные значения:<br/>sip – переадресация на SIP,<br/>phone – переадресация на телефон.<br/>|

### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner
## updateReportByEmailSettings

### Описание метода
Settings.updateReportByEmailSettings
Изменяет настройки отправки отчетом по email.
Параметры
Результат
Методов ничего не возвращает.
Уровень доступа для ролей


### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|is_active|False|boolean|Включение/выключение отправки отчетов на email.<br/>|
|period|False|string|Периодичность.<br/>Возможные значения:<br/>daily – ежедневно;<br/>weekly – еженедельно;<br/>monthly – ежемесячно.<br/>|
|emails|False|string|Список через запятую адресов электронной почты, на которые следует отправлять отчеты.<br/>Если указана пустая строка, то отчеты отправляться не будут.<br/>|

### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner
## showEmployeeRemarkSettings

### Описание метода
Settings.showEmployeeRemarkSettings
Возвращает настройки оценок сотрудника.
Параметры
Метод не имеет параметров.
Результат
Объект типа «EmployeeRemarkSettings».
Уровень доступа для ролей


### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|

### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner