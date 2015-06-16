
# Settings

## Описание ресурса

# Методы

## showFeatureStates

### Описание метода
Возвращает данные о доступности функциональных возможностей на аккаунте.<br/>Метод не имеет параметров.<br/>Объект типа «FeatureStates».<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|

### Результат
[FeatureStates](/docs/types/FeatureStates.md)
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|*admin*|full||
|*manager*|full||
|*chief*|full||
|*chief_partner*|full||
|*operator*|full||
|*admin_partner*|full||

## showCobrowseSettings

### Описание метода
Возвращает настройки функции «Виртуальный ассистент».<br/>Метод не имеет параметров.<br/>Объект типа «CobrowseSettings».<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|

### Результат
[CobrowseSettings](/docs/types/CobrowseSettings.md)
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|*admin*|full||
|*manager*|none||
|*chief*|full||
|*chief_partner*|full||
|*operator*|none||
|*admin_partner*|full||

## showFileTransferSettings

### Описание метода
Возвращает настройки функции «Передача файлов».<br/>Метод не имеет параметров.<br/>Объект типа «FileTransferSettings».<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|

### Результат
[FileTransferSettings](/docs/types/FileTransferSettings.md)
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|*admin*|full||
|*manager*|none||
|*chief*|full||
|*chief_partner*|full||
|*operator*|none||
|*admin_partner*|full||

## show

### Описание метода
Возвращает глобальные настройки.<br/>Метод не имеет параметров.<br/>Объект типа «Settings».<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|

### Результат
[Settings](/docs/types/Settings.md)
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|*admin*|full||
|*manager*|none||
|*chief*|full||
|*chief_partner*|full||
|*operator*|none||
|*admin_partner*|full||

## updateCobrowseSettings

### Описание метода
Изменяет настройки функции "Виртуальный ассистент".<br/>Методов ничего не возвращает.<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*is_active*|False|[boolean](/docs/types/boolean.md)|Включение/выключение функции «Виртуальный ассистент».<br/>|

### Результат
None
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|*admin*|full||
|*manager*|none||
|*chief*|full||
|*chief_partner*|full||
|*operator*|none||
|*admin_partner*|full||

## updateAcceptanceByEmailSettings

### Описание метода
Изменяет настройки отправки актов по электронной почте.<br/>Методов ничего не возвращает.<br/><br/>
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
|*admin*|full||
|*manager*|none||
|*chief*|full||
|*chief_partner*|none||
|*operator*|none||
|*admin_partner*|none||

## showAcceptanceByEmailSettings

### Описание метода
Возвращает настройки отправки актов по электронной почте.<br/>Метод не имеет параметров.<br/>Объект типа «AcceptanceByEmailSettings».<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|

### Результат
[AcceptanceByEmailSettings](/docs/types/AcceptanceByEmailSettings.md)
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|*admin*|full||
|*manager*|none||
|*chief*|full||
|*chief_partner*|none||
|*operator*|none||
|*admin_partner*|none||

## updateEmployeeRemarkSettings

### Описание метода
Изменяет настройки функции оценок сотрудника.<br/>Методов ничего не возвращает.<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*is_active*|False|[boolean](/docs/types/boolean.md)|Включение/выключение возможности оценки чатов сотрудниками.<br/>|

### Результат
None
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|*admin*|full||
|*manager*|none||
|*chief*|full||
|*chief_partner*|full||
|*operator*|none||
|*admin_partner*|full||

## updateFileTransferSettings

### Описание метода
Изменяет настройки функции «Передача файлов».<br/>Методов ничего не возвращает.<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*is_active*|False|[boolean](/docs/types/boolean.md)|Включение/выключение функции «Передача файлов».<br/>|

### Результат
None
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|*admin*|full||
|*manager*|none||
|*chief*|full||
|*chief_partner*|full||
|*operator*|none||
|*admin_partner*|full||

## showCallSettings

### Описание метода
Возвращает настройки звонковой функциональности.<br/>Метод не имеет параметров.<br/>Объект типа «CallSettings».<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|

### Результат
[CallSettings](/docs/types/CallSettings.md)
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|*admin*|full||
|*manager*|none||
|*chief*|full||
|*chief_partner*|full||
|*operator*|none||
|*admin_partner*|full||

## showTypingIndicatorSettings

### Описание метода
Возвращает настройки функции «Подглядывания».<br/>Метод не имеет параметров.<br/>Объект типа «TypingIndicatorSettings».<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|

### Результат
[TypingIndicatorSettings](/docs/types/TypingIndicatorSettings.md)
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|*admin*|full||
|*manager*|none||
|*chief*|full||
|*chief_partner*|full||
|*operator*|none||
|*admin_partner*|full||

## showReportByEmailSettings

### Описание метода
Возвращает настройки отправки отчетов по email.<br/>Метод не имеет параметров.<br/>Объект типа «ReportByEmailSettings».<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|

### Результат
[ReportByEmailSettings](/docs/types/ReportByEmailSettings.md)
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|*admin*|full||
|*manager*|full||
|*chief*|full||
|*chief_partner*|full||
|*operator*|none||
|*admin_partner*|full||

## updateTypingIndicatorSettings

### Описание метода
Изменяет настройки функции «Подглядывание».<br/>Методов ничего не возвращает.<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*is_active*|False|[boolean](/docs/types/boolean.md)|Включение/выключение функции «Подглядывание».<br/>|

### Результат
None
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|*admin*|full||
|*manager*|none||
|*chief*|full||
|*chief_partner*|full||
|*operator*|none||
|*admin_partner*|full||

## updateCallSettings

### Описание метода
Изменяет настройки звонковой функциональности.<br/>Методов ничего не возвращает.<br/><br/>
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
|*admin*|full||
|*manager*|none||
|*chief*|full||
|*chief_partner*|full||
|*operator*|none||
|*admin_partner*|full||

## updateReportByEmailSettings

### Описание метода
Изменяет настройки отправки отчетом по email.<br/>Методов ничего не возвращает.<br/><br/>
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
|*admin*|full||
|*manager*|full||
|*chief*|full||
|*chief_partner*|full||
|*operator*|none||
|*admin_partner*|full||

## showEmployeeRemarkSettings

### Описание метода
Возвращает настройки оценок сотрудника.<br/>Метод не имеет параметров.<br/>Объект типа «EmployeeRemarkSettings».<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|

### Результат
[EmployeeRemarkSettings](/docs/types/EmployeeRemarkSettings.md)
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|*admin*|full||
|*manager*|none||
|*chief*|full||
|*chief_partner*|full||
|*operator*|none||
|*admin_partner*|full||
