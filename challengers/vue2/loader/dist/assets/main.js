(function (ctx) {
  const {App} = ctx.components;
  ctx.app = new Vue({
    el: '#app',
    render: (h) => h(App)
  })
})(window)

