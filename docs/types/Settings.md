
## Settings

### Описание типа
Settings<br/>Глобальные настройки.<br/>Таблица 78. Поля глобальных настроек<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*lang*|True|None|Язык пользовательского интерфейса Личного кабинета.<br/>|
|*is_console_connected*|False|[boolean](/docs/types/boolean.md)|Признак подключения оператора.<br/>Устанавливается в true при первом успешном входе оператора через Пульт.<br/>Доступен только для чтения.<br/>|
|*file_transfer_settings*|False|[FileTransferSettings](/docs/types/FileTransferSettings.md)|Настройки функции передачи файлов.<br/>|
|*typing_indicator_settings*|True|[TypingIndicatorSettings](/docs/types/TypingIndicatorSettings.md)|Настройки функции «Подглядывание».<br/>|
|*feature_states*|True|[FeatureStates](/docs/types/FeatureStates.md)|Данные о доступности функциональных возможностей на аккаунте.<br/>|
|*time_zone*|True|None|Временная зона Личного кабинета.<br/>|
|*updated_at*|True|[datetime](/docs/types/datetime.md)|Дата последнего обновления.<br/>|
|*cobrowse_settings*|True|[CobrowseSettings](/docs/types/CobrowseSettings.md)|Настройки функции «Виртуальный ассистент».<br/>|
|*employee_remark_settings*|True|[EmployeeRemarkSettings](/docs/types/EmployeeRemarkSettings.md)|Настройки оценок сотрудников.<br/>|
|*country*|True|[country](/docs/types/country.md)|Двухбуквенный код страны по стандарту ISO 3166-1 alpha-2.<br/><br/>|
|*report_by_email_settings*|True|[ReportByEmailSettings](/docs/types/ReportByEmailSettings.md)|Настройки отправки отчетов на email.<br/>|
|*call_settings*|True|[CallSettings](/docs/types/CallSettings.md)|Настройки звонковой функциональности.<br/>|
|*acceptance_by_email_settings*|True|[AcceptanceByEmailSettings](/docs/types/AcceptanceByEmailSettings.md)|Настройки отправки актов на электронную почту.<br/>|
