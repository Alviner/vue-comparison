<script>
(function (ctx) {
  const {HelloWorld} = ctx.components;

  ctx.components.App = {
    template: "#main-app",
    components: {HelloWorld},
  }

})(window)
</script>

<template id="main-app">
  <div class="app">
    <div>
      <a href="https://v2.vuejs.org" target="_blank">
        <img src="./assets/vue.svg" class="logo vue" alt="Vue logo" />
      </a>
    </div>
    <hello-world msg="Vue" />
  </div>
</template>
