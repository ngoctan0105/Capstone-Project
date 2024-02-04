<template>
    <div class="categories">
      <div class="categoryRow">
        <img src="../assets/coffee.jpg" class="categoryImg">
        <img src="../assets/corn.jpg" class="categoryImg">
        <img src="../assets/grape.jpg" class="categoryImg">
        <img src="../assets/jackfruit.jpg" class="categoryImg">
      </div>
      <div class="categoryRow">
        <img src="../assets/mango.jpg" class="categoryImg">
        <img src="../assets/rice.jpg" class="categoryImg">
        <img src="../assets/sugarcane.jpg" class="categoryImg">
        <img src="../assets/tea.jpg" class="categoryImg">
      </div>
    </div>
</template>

<script>
export default {
  name: "CategoriesComponent",
};
</script>

<style>

.categoryRow {
  display: flex;
}

.categoryImg {
  width: 80px;
  height: 80px;
  border-radius: 10px;
  margin: 5px;
}

</style>
