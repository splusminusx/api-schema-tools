
# Settings

## Описание ресурса

# Методы

## showFeatureStates

### Описание метода
Возвращает данные о доступности функциональных возможностей на аккаунте.<br/>Метод не имеет параметров.<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|

### Результат
[FeatureStates](/types/FeatureStates)
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
Возвращает настройки функции «Виртуальный ассистент».<br/>Метод не имеет параметров.<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|

### Результат
[CobrowseSettings](/types/CobrowseSettings)
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
Возвращает настройки функции «Передача файлов».<br/>Метод не имеет параметров.<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|

### Результат
[FileTransferSettings](/types/FileTransferSettings)
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
Возвращает глобальные настройки.<br/>Метод не имеет параметров.<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|

### Результат
[Settings](/types/Settings)
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
Изменяет настройки функции "Виртуальный ассистент".<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*is_active*|False|[boolean](/types/boolean)|Включение/выключение функции «Виртуальный ассистент».<br/>|

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
Изменяет настройки отправки актов по электронной почте.<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*is_active*|False|[boolean](/types/boolean)|Включение/выключение отправки актов на электронную почту.<br/>|
|*emails*|False|[string](/types/string)|Список через запятую адресов электронной почты.<br/><br/>|

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
Возвращает настройки отправки актов по электронной почте.<br/>Метод не имеет параметров.<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|

### Результат
[AcceptanceByEmailSettings](/types/AcceptanceByEmailSettings)
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
Изменяет настройки функции оценок сотрудника.<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*is_active*|False|[boolean](/types/boolean)|Включение/выключение возможности оценки чатов сотрудниками.<br/>|

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
Изменяет настройки функции «Передача файлов».<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*is_active*|False|[boolean](/types/boolean)|Включение/выключение функции «Передача файлов».<br/>|

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
Возвращает настройки звонковой функциональности.<br/>Метод не имеет параметров.<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|

### Результат
[CallSettings](/types/CallSettings)
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
Возвращает настройки функции «Подглядывания».<br/>Метод не имеет параметров.<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|

### Результат
[TypingIndicatorSettings](/types/TypingIndicatorSettings)
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
Возвращает настройки отправки отчетов по email.<br/>Метод не имеет параметров.<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|

### Результат
[ReportByEmailSettings](/types/ReportByEmailSettings)
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
Изменяет настройки функции «Подглядывание».<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*is_active*|False|[boolean](/types/boolean)|Включение/выключение функции «Подглядывание».<br/>|

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
Изменяет настройки звонковой функциональности.<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*is_forward*|False|[boolean](/types/boolean)|Включение/выключение переадресации.<br/>|
|*is_active*|False|[boolean](/types/boolean)|Включение/выключение функциональности звонков.<br/>|
|*forward_sip_host*|False|[string](/types/string)|Имя хоста SIP.<br/>Обязательно при forward_type=SIP и is_forward=true.<br/>|
|*forward_sip_login*|False|[string](/types/string)|Логин для подключения по SIP.<br/>Обязательно при forward_type=SIP и is_forward=true.<br/>|
|*forward_sip_password*|False|[string](/types/string)|Пароль для подключения по SIP.<br/>Обязательно при forward_type=SIP и is_forward=true.<br/>|
|*forward_type*|False|[string](/types/string)|Тип переадресации.<br/>Возможные значения:<br/>sip – переадресация на SIP,<br/>phone – переадресация на телефон.<br/>|

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
Изменяет настройки отправки отчетом по email.<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*is_active*|False|[boolean](/types/boolean)|Включение/выключение отправки отчетов на email.<br/>|
|*period*|False|[string](/types/string)|Периодичность.<br/>Возможные значения:<br/>daily – ежедневно;<br/>weekly – еженедельно;<br/>monthly – ежемесячно.<br/>|
|*emails*|False|[string](/types/string)|Список через запятую адресов электронной почты, на которые следует отправлять отчеты.<br/>Если указана пустая строка, то отчеты отправляться не будут.<br/>|

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
Возвращает настройки оценок сотрудника.<br/>Метод не имеет параметров.<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|

### Результат
[EmployeeRemarkSettings](/types/EmployeeRemarkSettings)
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|*admin*|full||
|*manager*|none||
|*chief*|full||
|*chief_partner*|full||
|*operator*|none||
|*admin_partner*|full||
