# Vue comparison

Сравниваем vue со сборкой и без. Чтобы на замеры происходили
в равных условиях будем использовать простой веб-сервер на `aiohttp`,
который раздает `index.html` и немного ассетов.

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

## Кандидаты на сравнения

## Vue 2

1. vue2 без сборки с inline компонентами [dist](challengers/vue2/inline/dist)
1. vue2 без сборки с загрузчиком компонент [dist](challengers/vue2/loader/dist)
1. vue2 собран vite [dist](challengers/vue2/vite/dist)
1. vue2 собран webpack [dist](challengers/vue2/webpack/dist)

### Vue 3

1. vue3 собран vite [dist](challengers/vue3/vite/dist)
1. vue3 без сборки с shim загрузчиком модулей [dist](challengers/vue3/shim/dist)
