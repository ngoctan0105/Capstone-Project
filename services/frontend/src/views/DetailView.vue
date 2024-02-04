<template>

    <div class="detailPageBody">
      <button @click="closeDetail" class="backBtn">Trở về</button>
      <div class="imageContainerDetail">

        <div class="imageBackground">
        <img v-if="height > width" :src="plantDiseaseObj['Ảnh']" ref="image" @load="getImageSize" class="verticalImage">
        <img v-else-if="height < width" :src="plantDiseaseObj['Ảnh']" ref="image" @load="getImageSize" class="horizontalImage">
        <img v-else :src="plantDiseaseObj['Ảnh']" ref="image" @load="getImageSize" class="squareImage">

      </div>        
      </div>
      <div class="textContainerDetail">

        <div class="textContainerBodyDetail">
          <PredictionComponent :plantDiseaseObj="plantDisease" 
        
        v-if="plantDiseaseObj['Độ tin cậy'] >= 0.95"
          />
          <div v-else class="undefined">
            <p>Không thể xác định được loại cây và tình trạng của cây.<br>Vui lòng chọn ảnh khác!</p>
            <img src="../assets/undefined.gif" >
            </div>

        </div>
      </div>
    </div>
</template>

<script>
import HeaderComponent from "@/components/HeaderComponent.vue";
import PredictionComponent from "@/components/PredictionComponent.vue";
import axios from "axios";
const sound = require('../assets/button-click.mp3');

export default {
  name: "DetailView",
  components: {
    HeaderComponent,
    PredictionComponent,
  },

  data() {
    return {
      previewImage: null,
      plantDisease: null,
      height: '',
      width: ''
    };
  },
  props: {
    plantDiseaseObj: Object
  },
  mounted() {
    console.log("this.plantDiseaseObj: ", this.plantDiseaseObj);
    this.showResult();
  },

  methods: {
    getImageSize() {
                    const img = new Image();
                    console.log('this.$refs.image.src: ', this.$refs.image.src);
                    img.src = this.$refs.image.src;
                    img.onload = () => {
                        this.width = img.width;
                        this.height = img.height;
                        console.log('size: ', this.width + ' ' + this.height);
                    };
                    
                },    
    async showResult() {
      console.log("this.plantDiseaseObj['Class']", this.plantDiseaseObj["Class"]);
      try {
            const plantDisease = await axios.get(
              "http://localhost:8000/plant_disease/" +
                this.plantDiseaseObj["Class"]
            );

            console.log("plantDisease: ", plantDisease);
            this.plantDisease = plantDisease.data;
            console.log('this.plantDisease: ', this.plantDisease);
          } catch (error) {
            console.error(error);
          }
    },
    closeDetail() {
      let audio = new Audio(sound);
audio.play();
      this.$emit("showDetail", false);
    }
  }

};
</script>

<style>
.detailPageBody {
  display: inline-flex;
  position: absolute;
  top: 80px;
  left: 40px;
}

.imageBackground {
  width: 410px;
  height: 410px;
  display: flex;
  margin: 30px auto 30px auto;
  background-size: cover;
  background-position: center center;
  border-radius: 25px;  
  background-color: black;
}

.squareImage {
  width: 100%;
  height: 100%;
  border-radius: 25px;  

}

.verticalImage {
  height: 100%;
  margin-left: auto;
  margin-right: auto; 
}

.horizontalImage {
  width: 100%;
  align-self: center;
  justify-self: center;
}

.imageContainerDetail {
  height: 470px;
  width: 460px;
  background-color: #f9f7e5;
  border-radius: 25px;
  align-self: center;
  margin-right: 70px;
  align-self: flex-end;
}

.textContainerDetail {
  height: 640px;
  width: 760px;
  background-color: #d5e6d8;
  border-radius: 25px;
  align-self: flex-end;
  display: flex;
  place-items: center;
}

.textContainerBodyDetail {

  background-color: white;
  border-radius: 25px;
  height: 600px;
  width: 720px;
  padding: 30px;
  margin-left: auto;
  margin-right: auto;
}

.backBtn {
position: absolute;
top: 70px;
left: 130px;
display: block;

  background-color: #39483e;
  height: 50px;
  width: 200px;
  border-radius: 50px;
  color: white;
  font-family: 'AR One Sans';
  font-size: 24px;
}

.backBtn:hover {
  background-color: black;
}
</style>
