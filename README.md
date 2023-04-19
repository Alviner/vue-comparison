# Vue comparison

Сравниваем vue со сборкой и без. Чтобы замеры происходили
в равных условиях будем использовать простой веб-сервер на `aiohttp`,
который раздает `index.html` и немного ассетов. Нас интересует насколько жизнеспособен vue без сборки на небольших проектах. Например, админки -- пара страниц с формой.

## Как использовать

Установите poetry `1.2.0` или выше. И следуйте инструкции ниже:

```(console)
poetry install
```

А запустить веб сервер можно командой:

```(console)
poetry run vue_admin --dist-path {DIST_PATH}
```

`{DIST_PATH}` это путь до папки `dist` соответственно нужноuj нам кандидата.

## Test Case

Тесты проводились на загрузке Vue приложения с hello-world компонентой.
Нас интересуют достаточно малые spa приложения, поэтому на текущий момент нам этого достаточно. Основным параметром будем считать время на чтение и выполнение js кода (scripting из раздела perfomance в консоле). Тесты запускались на Mac c чипом Apple M1 Pro.

## Кандидаты на сравнения

## Vue 2

1. собран webpack [dist](challengers/vue2/webpack/dist)
1. собран vite [dist](challengers/vue2/vite/dist)
1. без сборки с inline компонентами [dist](challengers/vue2/inline/dist). Используются iife модули с мапингом через идентификатор шаблона.
1. без сборки с загрузчиком компонент [dist](challengers/vue2/loader/dist). Аналогичен inline, но компоненты лежат в отдельных файлах, а перед инициализацией приложения загружаем все нужные компоненты последовательно.
### Vue 3

1. собран vite [dist](challengers/vue3/vite/dist)
1. без сборки с shim загрузчиком модулей [dist](challengers/vue3/shim/dist). Есть файл vendor, который единожды собирается esbuild, а компоненты приложения загружаются через [es-module-shims](https://github.com/guybedford/es-module-shims)

## Результаты

### Vue2

|               | Webpack | Vite | Inline | Loader |
|-----------|---------|------|--------|-------|
| safari | 18ms | 18ms | 23ms | 30ms|
| ya | 15ms | 9ms | 24ms | 31ms|
| chrome | 10ms | 7ms | 12ms | 22ms |

### Vue3
|               |  Vite | Shim Esm |
|-----------|------|----------|
| safari | 17ms | 44ms |
| ya | 7ms | 12ms |
| chrome | 7ms | 9ms  |

