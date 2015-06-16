
# Settings

## Описание ресурса

# Методы

## showFeatureStates

### Описание метода
Settings.showFeatureStates<br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|

### Результат
[FeatureStates](/docs/types/FeatureStates.md)
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner
## showCobrowseSettings

### Описание метода
Settings.showCobrowseSettings<br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|

### Результат
[CobrowseSettings](/docs/types/CobrowseSettings.md)
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner
## showFileTransferSettings

### Описание метода
Settings.showFileTransferSettings<br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|

### Результат
[FileTransferSettings](/docs/types/FileTransferSettings.md)
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner
## show

### Описание метода
Settings.show<br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|

### Результат
[Settings](/docs/types/Settings.md)
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner
## updateCobrowseSettings

### Описание метода
Settings.updateCobrowseSettings<br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*is_active*|False|[boolean](/docs/types/boolean.md)|Включение/выключение функции «Виртуальный ассистент».<br/>|

### Результат
None
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner
## updateAcceptanceByEmailSettings

### Описание метода
Settings.updateAcceptanceByEmailSettings<br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*is_active*|False|[boolean](/docs/types/boolean.md)|Включение/выключение отправки актов на электронную почту.<br/>|
|*emails*|False|[string](/docs/types/string.md)|Список через запятую адресов электронной почты.<br/><br/>|

### Результат
None
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner
## showAcceptanceByEmailSettings

### Описание метода
Settings.showAcceptanceByEmailSettings<br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|

### Результат
[AcceptanceByEmailSettings](/docs/types/AcceptanceByEmailSettings.md)
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner
## updateEmployeeRemarkSettings

### Описание метода
Settings.updateEmployeeRemarkSettings<br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*is_active*|False|[boolean](/docs/types/boolean.md)|Включение/выключение возможности оценки чатов сотрудниками.<br/>|

### Результат
None
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner
## updateFileTransferSettings

### Описание метода
Settings.updateFileTransferSettings<br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*is_active*|False|[boolean](/docs/types/boolean.md)|Включение/выключение функции «Передача файлов».<br/>|

### Результат
None
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner
## showCallSettings

### Описание метода
Settings.showCallSettings<br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|

### Результат
[CallSettings](/docs/types/CallSettings.md)
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner
## showTypingIndicatorSettings

### Описание метода
Settings.showTypingIndicatorSettings<br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|

### Результат
[TypingIndicatorSettings](/docs/types/TypingIndicatorSettings.md)
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner
## showReportByEmailSettings

### Описание метода
Settings.showReportByEmailSettings<br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|

### Результат
[ReportByEmailSettings](/docs/types/ReportByEmailSettings.md)
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner
## updateTypingIndicatorSettings

### Описание метода
Settings.updateTypingIndicatorSettings<br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*is_active*|False|[boolean](/docs/types/boolean.md)|Включение/выключение функции «Подглядывание».<br/>|

### Результат
None
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner
## updateCallSettings

### Описание метода
Settings.updateCallSettings<br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*is_forward*|False|[boolean](/docs/types/boolean.md)|Включение/выключение переадресации.<br/>|
|*is_active*|False|[boolean](/docs/types/boolean.md)|Включение/выключение функциональности звонков.<br/>|
|*forward_sip_host*|False|[string](/docs/types/string.md)|Имя хоста SIP.<br/>Обязательно при forward_type=SIP и is_forward=true.<br/>|
|*forward_sip_login*|False|[string](/docs/types/string.md)|Логин для подключения по SIP.<br/>Обязательно при forward_type=SIP и is_forward=true.<br/>|
|*forward_sip_password*|False|[string](/docs/types/string.md)|Пароль для подключения по SIP.<br/>Обязательно при forward_type=SIP и is_forward=true.<br/>|
|*forward_type*|False|[string](/docs/types/string.md)|Тип переадресации.<br/>Возможные значения:<br/>sip – переадресация на SIP,<br/>phone – переадресация на телефон.<br/>|

### Результат
None
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner
## updateReportByEmailSettings

### Описание метода
Settings.updateReportByEmailSettings<br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*is_active*|False|[boolean](/docs/types/boolean.md)|Включение/выключение отправки отчетов на email.<br/>|
|*period*|False|[string](/docs/types/string.md)|Периодичность.<br/>Возможные значения:<br/>daily – ежедневно;<br/>weekly – еженедельно;<br/>monthly – ежемесячно.<br/>|
|*emails*|False|[string](/docs/types/string.md)|Список через запятую адресов электронной почты, на которые следует отправлять отчеты.<br/>Если указана пустая строка, то отчеты отправляться не будут.<br/>|

### Результат
None
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner
## showEmployeeRemarkSettings

### Описание метода
Settings.showEmployeeRemarkSettings<br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|

### Результат
[EmployeeRemarkSettings](/docs/types/EmployeeRemarkSettings.md)
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner