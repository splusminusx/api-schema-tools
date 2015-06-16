
## Settings

### Описание типа
Settings
Глобальные настройки.
Таблица 78. Поля глобальных настроек


### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|lang|True|None|Язык пользовательского интерфейса Личного кабинета.<br/>|
|is_console_connected|False|boolean|Признак подключения оператора.<br/>Устанавливается в true при первом успешном входе оператора через Пульт.<br/>Доступен только для чтения.<br/>|
|file_transfer_settings|False|FileTransferSettings|Настройки функции передачи файлов.<br/>|
|typing_indicator_settings|True|TypingIndicatorSettings|Настройки функции «Подглядывание».<br/>|
|feature_states|True|FeatureStates|Данные о доступности функциональных возможностей на аккаунте.<br/>|
|time_zone|True|None|Временная зона Личного кабинета.<br/>|
|updated_at|True|datetime|Дата последнего обновления.<br/>|
|cobrowse_settings|True|CobrowseSettings|Настройки функции «Виртуальный ассистент».<br/>|
|employee_remark_settings|True|EmployeeRemarkSettings|Настройки оценок сотрудников.<br/>|
|country|True|country|Двухбуквенный код страны по стандарту ISO 3166-1 alpha-2.<br/><br/>|
|report_by_email_settings|True|ReportByEmailSettings|Настройки отправки отчетов на email.<br/>|
|call_settings|True|CallSettings|Настройки звонковой функциональности.<br/>|
|acceptance_by_email_settings|True|AcceptanceByEmailSettings|Настройки отправки актов на электронную почту.<br/>|
