# 🧪 QA Automation Engineer Learning

Учебный проект по автоматизации тестирования веб-приложений и REST API.

Проект создан в процессе изучения и практики **QA Automation** и содержит UI- и API-автотесты на Python с использованием **Playwright, Pytest, Allure, Requests и Pydantic**.

В качестве тестового стенда для UI и API используется [DemoQA](https://demoqa.com/).

---

## 📌 О проекте

Основная цель проекта — практическое изучение подходов к автоматизации тестирования:

* UI Automation;
* API Testing;
* Page Object Model;
* собственные UI-компоненты;
* Pytest fixtures;
* Allure Report;
* валидация API-ответов с помощью Pydantic;
* работа с авторизацией;
* работа с формами и элементами веб-интерфейса;
* CRUD-сценарии через API.

Проект находится в процессе развития и постепенно расширяется по мере изучения новых инструментов и подходов автоматизации тестирования.

---

## 🛠 Tech Stack

### Programming Language

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge\&logo=python\&logoColor=white)

### UI Automation

![Playwright](https://img.shields.io/badge/Playwright-1.40.0-2EAD33?style=for-the-badge\&logo=playwright\&logoColor=white)

### Test Framework

![Pytest](https://img.shields.io/badge/Pytest-7.4.3-0A9EDC?style=for-the-badge\&logo=pytest\&logoColor=white)

### API Testing

![Requests](https://img.shields.io/badge/Requests-2.32.3-202020?style=for-the-badge\&logo=python\&logoColor=white)

### Data Validation

![Pydantic](https://img.shields.io/badge/Pydantic-2.8.2-E92063?style=for-the-badge\&logo=pydantic\&logoColor=white)

### Test Reports

![Allure](https://img.shields.io/badge/Allure-2.13.5-FF6A00?style=for-the-badge)

---

# 🧩 Project Features

## 🌐 UI Automation

UI-тесты реализованы с использованием **Playwright** и **Pytest**.

На текущий момент автоматизированы следующие сценарии:

| Раздел            | Проверяемый функционал        |
| ----------------- | ----------------------------- |
| Buttons           | Работа с кнопками             |
| Checkbox          | Выбор checkbox                |
| Date Picker       | Выбор даты                    |
| Login             | Авторизация                   |
| Modal Dialogs     | Работа с модальными окнами    |
| Practice Form     | Заполнение формы              |
| Radio Button      | Работа с radio button         |
| Select Menu       | Работа с выпадающими списками |
| TextBox           | Заполнение текстовых полей    |
| Upload / Download | Загрузка и скачивание файлов  |

---

## 🔌 API Testing

API-тесты построены на основе библиотеки **Requests**.

Реализованы сценарии для API DemoQA:

* авторизация пользователя;
* генерация токена;
* создание пользователя;
* получение пользователя;
* удаление пользователя;
* проверка состояния пользователя до и после удаления.

Пример API workflow:

```text
Create User
     │
     ▼
Generate Token
     │
     ▼
Authorize
     │
     ▼
Get User
     │
     ▼
Delete User
     │
     ▼
Get User
     │
     ▼
Validate Response
```

---

# 🏗 Architecture

В проекте используется разделение тестовой логики и взаимодействия с интерфейсом.

Основные уровни:

```text
┌──────────────────────────────┐
│            Tests             │
│      UI / API Test Cases     │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│          Page Layer          │
│       Page Object Model      │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│       Page Components        │
│    Button / Input / etc.     │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│          Playwright          │
└──────────────────────────────┘
```

API-направление:

```text
┌──────────────────────────────┐
│          API Tests           │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│        API Methods           │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│          Requests            │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│     Pydantic Validation      │
└──────────────────────────────┘
```

---

# 📁 Project Structure

```text
QA-Automation-Engineer-Learning/
│
├── base/
│   │
│   ├── models_api_pydantic/
│   │   └── auth/
│   │       ├── model_auth_v1.py
│   │       ├── model_delete_v1_user.py
│   │       ├── model_get_user.py
│   │       ├── model_post_v1_token_generate.py
│   │       └── model_post_v1_user.py
│   │
│   ├── page_factory/
│   │   ├── button.py
│   │   ├── component.py
│   │   └── input.py
│   │
│   ├── pages/
│   │   │
│   │   ├── api_pages/
│   │   │   └── authorized/
│   │   │       ├── auth_base.py
│   │   │       └── methods_v1_authorized.py
│   │   │
│   │   ├── authorization/
│   │   │   └── authorization_method.py
│   │   │
│   │   ├── buttons/
│   │   ├── checkbox/
│   │   ├── date_picker/
│   │   ├── login/
│   │   ├── modal_dialogs/
│   │   ├── practice_form/
│   │   ├── radiobutton/
│   │   ├── select_menu/
│   │   ├── textbox/
│   │   └── upload_and_download/
│   │
│   └── base.py
│
├── src/
│   ├── config/
│   │   ├── expectations.py
│   │   ├── playwright.py
│   │   └── url.py
│   │
│   └── image/
│
├── tests/
│   ├── test_api/
│   │   └── test_v1_demoqa.py
│   │
│   └── test_ui/
│       ├── test_buttons.py
│       ├── test_checkbox.py
│       ├── test_date_picker.py
│       ├── test_login.py
│       ├── test_modal_dialogs.py
│       ├── test_practice_form.py
│       ├── test_radiobutton.py
│       ├── test_select_menu.py
│       ├── test_textbox.py
│       └── test_upload_and_download.py
│
├── conftest.py
├── pytest.ini
├── requirements.txt
├── settings.py
└── README.md
```

---

# 🧱 Page Factory

Для работы с элементами интерфейса реализован собственный слой компонентов.

Основные компоненты:

```text
Component
   │
   ├── Button
   │
   └── Input
```

Это позволяет инкапсулировать часто используемые операции с элементами интерфейса.

Например, для кнопок доступны операции:

```python
button.click()
button.double_click()
button.right_click()
button.hover()
```

а также проверки состояния элемента.

Для текстовых полей используется компонент `Input`.

---

# 🧪 Pytest Fixtures

Для создания объектов страниц используются Pytest fixtures.

Основная fixture:

```python
@pytest.fixture()
def page() -> Page:
    ...
```

На её основе создаются Page Object:

```python
@pytest.fixture(scope='function')
def practice_form(page: Page) -> PracticeFormPage:
    return PracticeFormPage(page)
```

Аналогичный подход используется для остальных страниц проекта.

Это позволяет тестам получать готовый Page Object через dependency injection Pytest:

```python
def test_practice_form(
    page: Page,
    practice_form: PracticeFormPage
):
    ...
```

---

# 🌐 Browser Configuration

Настройки Playwright находятся в:

```text
src/config/playwright.py
```

Поддерживаются следующие параметры:

* browser;
* headless mode;
* slow motion;
* viewport size;
* environment.

Значения могут задаваться через переменные окружения.

Например:

```bash
BROWSER=firefox
HEADLESS=true
SLOW_MO=100
```

По умолчанию используется:

```text
Browser: Chrome
Headless: False
Viewport: 1920x1080
Slow motion: 50 ms
Locale: en-US
```

---

# 📊 Allure Report

Для формирования результатов тестирования используется **Allure**.

В тестах применяются:

```python
@allure.epic()
@allure.feature()
@allure.title()
```

а также Allure steps и attachments.

Например:

```python
@allure.epic("API")
@allure.title("Создание пользователя v1")
def test_create_v1_user():
    ...
```

Результаты сохраняются в:

```text
allure-results/
```

---

# ▶️ Installation

## 1. Clone repository

```bash
git clone https://github.com/EvgenyGord/QA-Automation-Engineer-Learning.git
```

Перейдите в директорию проекта:

```bash
cd QA-Automation-Engineer-Learning
```

---

## 2. Create virtual environment

### Windows

```bash
python -m venv .venv
```

Активация:

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Install Playwright browsers

После установки зависимостей необходимо установить браузеры Playwright:

```bash
playwright install
```

---

# ▶️ Running Tests

Запуск всех тестов:

```bash
pytest
```

Запуск только UI-тестов:

```bash
pytest tests/test_ui
```

Запуск API-тестов:

```bash
pytest tests/test_api
```

Запуск отдельного теста:

```bash
pytest tests/test_ui/test_login.py
```

---

# 🖥 Running Playwright in Headless Mode

По умолчанию проект запускает браузер с:

```text
HEADLESS=False
```

Для headless-запуска:

### Windows CMD

```cmd
set HEADLESS=true
pytest
```

### PowerShell

```powershell
$env:HEADLESS="true"
pytest
```

### Linux / macOS

```bash
HEADLESS=true pytest
```

---

# 🌍 Browser Selection

Для запуска в Firefox:

```bash
BROWSER=firefox pytest
```

Для Chrome:

```bash
BROWSER=chrome pytest
```

---

# 🐢 Slow Motion

Для визуального наблюдения за действиями Playwright можно увеличить задержку:

```bash
SLOW_MO=500 pytest
```

Например:

```text
SLOW_MO=500
```

добавляет задержку 500 мс между действиями Playwright.

---

# 📈 Test Reporting

После запуска тестов результаты Allure находятся в:

```text
allure-results/
```

Для генерации HTML-отчёта:

```bash
allure generate allure-results -o allure-report --clean
```

Для открытия отчёта:

```bash
allure open allure-report
```

---

# 🔍 Test Coverage

## UI

На текущем этапе автоматизированы:

* Buttons;
* Checkbox;
* Date Picker;
* Login;
* Modal Dialogs;
* Practice Form;
* Radio Button;
* Select Menu;
* TextBox;
* Upload / Download.

## API

Автоматизированы сценарии:

* Authorization;
* Token generation;
* User creation;
* User retrieval;
* User deletion;
* Проверка пользователя до и после удаления.

---

# 🧬 API Response Models

Для проверки структуры API-ответов используются **Pydantic models**.

Пример:

```python
class GenerateTokenResponse(BaseModel):
    token: StrictStr
    expires: StrictStr
    status: StrictStr
    result: StrictStr
```

Таким образом, API-ответ может дополнительно проверяться на соответствие ожидаемой структуре и типам данных.

---

# 🔐 Authentication

В проекте реализованы сценарии работы с API authentication:

```text
Authorization
      │
      ├── Generate Token
      │
      └── Authorized Requests
```

Также присутствуют UI-сценарии для страницы Login.

---

# 🧪 Testing Approach

В проекте используются следующие подходы:

### Page Object Model

Локаторы и взаимодействие со страницей вынесены в Page Object.

### Component Abstraction

Повторно используемые элементы представлены отдельными компонентами:

```text
Button
Input
Component
```

### Pytest Fixtures

Объекты страниц и Playwright `Page` предоставляются через fixtures.

### API Response Validation

API-ответы проверяются с использованием Pydantic-моделей.

### Allure

Тестовые сценарии размечены для формирования структурированного отчёта.

---

# 📚 Learning Goals

Проект развивается как практическая площадка для изучения:

* Python;
* Pytest;
* Playwright;
* UI Automation;
* API Testing;
* REST API;
* Page Object Model;
* Fixtures;
* Allure;
* Pydantic;
* автоматизации тестовых сценариев;
* организации automation framework.

---

# 🚧 Roadmap

Проект находится в разработке.

Планируемые направления развития:

* [ ] Рефакторинг Page Object;
* [ ] Улучшение архитектуры API-клиента;
* [ ] Расширение API-тестов;
* [ ] Parametrized tests;
* [ ] Генерация тестовых данных;
* [ ] Улучшение обработки ошибок;
* [ ] Расширение Allure reporting;
* [ ] Логирование;
* [ ] Code formatting / linting;
* [ ] CI/CD;
* [ ] Docker;
* [ ] Расширение покрытия UI;
* [ ] Улучшение конфигурации окружений.

---

# 📌 Test Environment

UI и API-тесты в текущей версии проекта ориентированы на:

**DemoQA**

```text
https://demoqa.com/
```

Проект использует публичное учебное приложение для демонстрации различных сценариев автоматизированного тестирования.

---

# 👨‍💻 Author

**Evgeny Gordenko**

QA Automation Engineer — Learning & Practice

GitHub:
https://github.com/EvgenyGord

GitLab:
https://gitlab.com/evgenygord-group

Telegram: @evgeny_gord

---

## 📖 Project Status

> 🚧 Educational / Learning Project
> The framework is continuously evolving as new QA Automation practices and tools are studied and implemented.

---

⭐ Если проект оказался полезным — буду рад звезде репозитория.
