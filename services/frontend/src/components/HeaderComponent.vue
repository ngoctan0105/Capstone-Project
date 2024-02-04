<template>
    <div class="header">
      <img src="../assets/logo.png" alt="logo">
      <p>Plantex</p>
    </div>
</template>

<script>
export default {
  name: "HeaderComponent",
};
</script>

<style>

.header {
  height: 80px;
  display: flex;
  float: left;
  position: absolute;
  left: 50px;
  top: 20px;
  font-family: 'Simonetta';
  font-size: 48px;  
  font-weight: bold;
}

.header img {
  width: 48px;
  height: 48px;
  margin-top: 8px;
  margin-right: 10px;
}


</style>
