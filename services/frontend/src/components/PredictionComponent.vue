<template>
  <div class="prediction" v-if="this.plantDiseaseObj">

    <div class="plant">
      <span class="title">🌿 Loại cây: </span>
      <span class="plantDetail">{{ this.plantDiseaseObj.plant }}</span>
    </div>

    <div class="disease">
      <span class="title">🔍 Tình trạng: </span>
      <span class="diseaseDetail">{{ this.plantDiseaseObj.disease }}</span>
    </div>

    <img src="../assets/healthy.gif" v-if="this.plantDiseaseObj.name.includes('Healthy')" class="healthy" >

    <div v-if="this.plantDiseaseObj.symptoms.length != 0" class="symptoms">
      <p class="title">🔬 Triệu chứng:</p>
      <ul v-for="(item, index) in plantDiseaseObj.symptoms" :key="index">
        <li style="margin-left: 20px;">🍃 {{ item }}</li>
      </ul>
    </div>

    <div v-if="this.plantDiseaseObj.causes.length != 0" class="causes">
      <p class="title">🦠 Nguyên nhân:</p>
      <ul v-for="(item, index) in plantDiseaseObj.causes" :key="index">
        <li style="margin-left: 20px;">🍃 {{ item }}</li>
      </ul>
    </div>

    <div v-if="this.plantDiseaseObj.measures.length != 0" class="measures">
      <p class="title">👨‍🌾 Phòng trừ:</p>
      <ul v-for="(item, index) in plantDiseaseObj.measures" :key="index">
        <li style="margin-left: 20px;">🍃 {{ item }}</li>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  name: "PredictionComponent",
  props: {
    plantDiseaseObj: Object,
  },
  mounted() {
    console.log("this.plantDiseaseObj: ", this.plantDiseaseObj);
  },
};
</script>

<style>
.prediction {
  font-family: "Alata";
  text-align: start;
  max-height: 550px;
  overflow-y: auto;
}

.title {
  font-weight: 600;
}

.healthy {
  margin: 80px auto 0  auto;
  height: 400px;
}
</style>
