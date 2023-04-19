<script>
import HelloWorld from './components/HelloWorld.vue'

export default {
  components: { HelloWorld },
}
</script>

<template>
  <div class="app">
    <div>
      <a href="https://vitejs.dev" target="_blank">
        <img src="./assets/vite.svg" class="logo" alt="Vite logo" />
      </a>
      <a href="https://v2.vuejs.org" target="_blank">
        <img src="./assets/vue.svg" class="logo vue" alt="Vue logo" />
      </a>
    </div>
    <HelloWorld msg="Vite + Vue" />
  </div>
</template>
