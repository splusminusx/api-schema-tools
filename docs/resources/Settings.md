
# Settings

## Описание ресурса
Settings<br/>
# Методы

## showFeatureStates

### Описание метода
Settings.showFeatureStates<br/>Возвращает данные о доступности функциональных возможностей на аккаунте.<br/>Параметры<br/>Метод не имеет параметров.<br/>Результат<br/>Объект типа «FeatureStates».<br/>Уровень доступа для ролей<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|

### Резудьтат
[FeatureStates](/docs/types/FeatureStates.md)
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner
## showCobrowseSettings

### Описание метода
Settings.showCobrowseSettings<br/>Возвращает настройки функции «Виртуальный ассистент».<br/>Параметры<br/>Метод не имеет параметров.<br/>Результат<br/>Объект типа «CobrowseSettings».<br/>Уровень доступа для ролей<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|

### Резудьтат
[CobrowseSettings](/docs/types/CobrowseSettings.md)
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner
## showFileTransferSettings

### Описание метода
Settings.showFileTransferSettings<br/>Возвращает настройки функции «Передача файлов».<br/>Параметры<br/>Метод не имеет параметров.<br/>Результат<br/>Объект типа «FileTransferSettings».<br/>Уровень доступа для ролей<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|

### Резудьтат
[FileTransferSettings](/docs/types/FileTransferSettings.md)
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner
## show

### Описание метода
Settings.show<br/>Возвращает глобальные настройки.<br/>Параметры<br/>Метод не имеет параметров.<br/>Результат<br/>Объект типа «Settings».<br/>Уровень доступа для ролей<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|

### Резудьтат
[Settings](/docs/types/Settings.md)
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner
## updateCobrowseSettings

### Описание метода
Settings.updateCobrowseSettings<br/>Изменяет настройки функции "Виртуальный ассистент".<br/>Параметры<br/>Результат<br/>Методов ничего не возвращает.<br/>Уровень доступа для ролей<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|is_active|False|[boolean](/docs/types/boolean.md)|Включение/выключение функции «Виртуальный ассистент».<br/>|

### Резудьтат
None
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner
## updateAcceptanceByEmailSettings

### Описание метода
Settings.updateAcceptanceByEmailSettings<br/>Изменяет настройки отправки актов по электронной почте.<br/>Параметры<br/>Результат<br/>Методов ничего не возвращает.<br/>Уровень доступа для ролей<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|is_active|False|[boolean](/docs/types/boolean.md)|Включение/выключение отправки актов на электронную почту.<br/>|
|emails|False|[string](/docs/types/string.md)|Список через запятую адресов электронной почты.<br/><br/>|

### Резудьтат
None
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner
## showAcceptanceByEmailSettings

### Описание метода
Settings.showAcceptanceByEmailSettings<br/>Возвращает настройки отправки актов по электронной почте.<br/>Параметры<br/>Метод не имеет параметров.<br/>Результат<br/>Объект типа «AcceptanceByEmailSettings».<br/>Уровень доступа для ролей<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|

### Резудьтат
[AcceptanceByEmailSettings](/docs/types/AcceptanceByEmailSettings.md)
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner
## updateEmployeeRemarkSettings

### Описание метода
Settings.updateEmployeeRemarkSettings<br/>Изменяет настройки функции оценок сотрудника.<br/>Параметры<br/>Результат<br/>Методов ничего не возвращает.<br/>Уровень доступа для ролей<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|is_active|False|[boolean](/docs/types/boolean.md)|Включение/выключение возможности оценки чатов сотрудниками.<br/>|

### Резудьтат
None
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner
## updateFileTransferSettings

### Описание метода
Settings.updateFileTransferSettings<br/>Изменяет настройки функции «Передача файлов».<br/>Параметры<br/>Результат<br/>Методов ничего не возвращает.<br/>Уровень доступа для ролей<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|is_active|False|[boolean](/docs/types/boolean.md)|Включение/выключение функции «Передача файлов».<br/>|

### Резудьтат
None
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner
## showCallSettings

### Описание метода
Settings.showCallSettings<br/>Возвращает настройки звонковой функциональности.<br/>Параметры<br/>Метод не имеет параметров.<br/>Результат<br/>Объект типа «CallSettings».<br/>Уровень доступа для ролей<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|

### Резудьтат
[CallSettings](/docs/types/CallSettings.md)
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner
## showTypingIndicatorSettings

### Описание метода
Settings.showTypingIndicatorSettings<br/>Возвращает настройки функции «Подглядывания».<br/>Параметры<br/>Метод не имеет параметров.<br/>Результат<br/>Объект типа «TypingIndicatorSettings».<br/>Уровень доступа для ролей<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|

### Резудьтат
[TypingIndicatorSettings](/docs/types/TypingIndicatorSettings.md)
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner
## showReportByEmailSettings

### Описание метода
Settings.showReportByEmailSettings<br/>Возвращает настройки отправки отчетов по email.<br/>Параметры<br/>Метод не имеет параметров.<br/>Результат<br/>Объект типа «ReportByEmailSettings».<br/>Уровень доступа для ролей<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|

### Резудьтат
[ReportByEmailSettings](/docs/types/ReportByEmailSettings.md)
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner
## updateTypingIndicatorSettings

### Описание метода
Settings.updateTypingIndicatorSettings<br/>Изменяет настройки функции «Подглядывание».<br/>Параметры<br/>Результат<br/>Методов ничего не возвращает.<br/>Уровень доступа для ролей<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|is_active|False|[boolean](/docs/types/boolean.md)|Включение/выключение функции «Подглядывание».<br/>|

### Резудьтат
None
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner
## updateCallSettings

### Описание метода
Settings.updateCallSettings<br/>Изменяет настройки звонковой функциональности.<br/>Параметры<br/>Результат<br/>Методов ничего не возвращает.<br/>Уровень доступа для ролей<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|is_forward|False|[boolean](/docs/types/boolean.md)|Включение/выключение переадресации.<br/>|
|is_active|False|[boolean](/docs/types/boolean.md)|Включение/выключение функциональности звонков.<br/>|
|forward_sip_host|False|[string](/docs/types/string.md)|Имя хоста SIP.<br/>Обязательно при forward_type=SIP и is_forward=true.<br/>|
|forward_sip_login|False|[string](/docs/types/string.md)|Логин для подключения по SIP.<br/>Обязательно при forward_type=SIP и is_forward=true.<br/>|
|forward_sip_password|False|[string](/docs/types/string.md)|Пароль для подключения по SIP.<br/>Обязательно при forward_type=SIP и is_forward=true.<br/>|
|forward_type|False|[string](/docs/types/string.md)|Тип переадресации.<br/>Возможные значения:<br/>sip – переадресация на SIP,<br/>phone – переадресация на телефон.<br/>|

### Резудьтат
None
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner
## updateReportByEmailSettings

### Описание метода
Settings.updateReportByEmailSettings<br/>Изменяет настройки отправки отчетом по email.<br/>Параметры<br/>Результат<br/>Методов ничего не возвращает.<br/>Уровень доступа для ролей<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|is_active|False|[boolean](/docs/types/boolean.md)|Включение/выключение отправки отчетов на email.<br/>|
|period|False|[string](/docs/types/string.md)|Периодичность.<br/>Возможные значения:<br/>daily – ежедневно;<br/>weekly – еженедельно;<br/>monthly – ежемесячно.<br/>|
|emails|False|[string](/docs/types/string.md)|Список через запятую адресов электронной почты, на которые следует отправлять отчеты.<br/>Если указана пустая строка, то отчеты отправляться не будут.<br/>|

### Резудьтат
None
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner
## showEmployeeRemarkSettings

### Описание метода
Settings.showEmployeeRemarkSettings<br/>Возвращает настройки оценок сотрудника.<br/>Параметры<br/>Метод не имеет параметров.<br/>Результат<br/>Объект типа «EmployeeRemarkSettings».<br/>Уровень доступа для ролей<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|

### Резудьтат
[EmployeeRemarkSettings](/docs/types/EmployeeRemarkSettings.md)
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner