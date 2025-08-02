<script setup>
/* No logic needed here yet */
</script>

<template>
  <header class="topbar">
    <h1>Code Studio</h1>
  </header>

  <!-- Route views are injected here -->
  <router-view />
</template>

<style scoped lang="scss">
.topbar {
  padding: 0.75rem 1rem;
  background: #2c3e50;
  color: #fff;
  font-size: 1.2rem;

}
</style>
