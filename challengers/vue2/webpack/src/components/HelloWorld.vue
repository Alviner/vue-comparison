<script>

export default {
  props: {
    msg: String
  },
  data () {
    return {
      count: 0
    }
  }
}

</script>

<template>
  <div>
    <h1>{{ msg }}</h1>

    <div class="card">
      <button type="button" @click="count++">count is {{ count }}</button>
    </div>

    <p class="read-the-docs">Click on Webpack and Vue logos to learn more</p>

  </div>
</template>
