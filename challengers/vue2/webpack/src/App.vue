<script>
import HelloWorld from './components/HelloWorld.vue'

export default {
  components: {HelloWorld}
}
</script>

<template>
  <div>
    <div>
      <a href="https://webpack.js.org" target="_blank">
        <img src="./assets/webpack.svg" class="logo"  alt="Webpack logo" />
      </a>
      <a href="https://v2.vuejs.org" target="_blank">
        <img src="./assets/vue.svg" class="logo vue" alt="Vue logo" />
      </a>
    </div>
    <HelloWorld msg="Vite + Vue" />
  </div>
</template>
