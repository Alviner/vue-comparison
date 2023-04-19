<script>
(function (ctx) {
  ctx.components.HelloWorld = {
    template: '#hello-world',
    props: {
      msg: String,
    },
    data() {
      return {
        count: 0
      }
    }
  }
})(window)
</script>

<template id='hello-world'>
  <div>
    <h1>{{ msg }}</h1>

    <div class="card">
      <button type="button" @click="count++">count is {{ count }}</button>
    </div>

    <p class="read-the-docs">Click on the Vue logo to learn more</p>

  </div>
</template>
