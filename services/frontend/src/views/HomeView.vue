<template>
  <div class="home">
    <HeaderComponent />
    <div class="homeBody">
      <div class="titleContainer">
        <p class="intro">Chăm sóc cây trồng <br> của bạn đúng cách</p>
        <p class="quote">Cùng trải nghiệm những tính năng thú vị về <br> những loại cây xung quanh chúng ta nhé!</p>
        <div class="decorComponent">
          <img src="../assets/decor.png" class="decorImg" />
        </div>
        <CategoriesComponent class="categoriesHome"/>
      </div>
      <div class="btnContainer">
        <img src="../assets/tree.png" class="treeImg" />
        <button class="singleFileBtn" @click="toSingleFilePage">Một ảnh</button>
        <div class="or">hoặc</div>
        <button class="multipleFilesBtn" @click="toMultipleFilesPage">
          Nhiều ảnh
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import router from "@/router";
import HeaderComponent from "@/components/HeaderComponent.vue";
import CategoriesComponent from '../components/CategoriesComponent.vue';
const sound = require('../assets/button-click.mp3');

export default {
  name: "HomeView",
  created(){
        document.title = "Plantex",
        document.im
    },
  components: {
    HeaderComponent,
    CategoriesComponent
  },
  methods: {
    toSingleFilePage() {


      let audio = new Audio(sound);
audio.play();
      router.push({ name: "SingleFileView" });
    },

    toMultipleFilesPage() {
      let audio = new Audio(sound);
audio.play();
      router.push({ name: "MultipleFilesView" });
    },
  },
};
</script>

<style>
.home {
  display: flex;
  background-repeat: no-repeat;
  background-size: 300px 300px;
}

.decorComponent {
  height: 300px;
  width: 400px;
  background-color: #f9f7e5;
  bottom: 0 !important;
  left: -80px !important;
  position: absolute;
  border-top-left-radius: 190px;
  border-top-right-radius: 190px;
  padding-top: 20px;
  overflow: hidden;
}

.decorImg {
  margin-left: auto;
  margin-right: auto;
  width: 342px;
  animation: spin 12s linear infinite;
}

@keyframes spin {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}


.intro {
  position: absolute;
  top: 130px;
  left: 100px;
  font-family: 'Bona Nova';
  font-size: 64px;
  color: black;
}

.quote {
  position: absolute;
  top: 340px;
  left: 160px;
  font-family:fantasy;
  font-weight: 500;
  font-size: 24px;
  color: black;
}

.btnContainer {
  padding-top: 30px;
  height: 720px;
  width: 500px;
  background-color: #d5e6d8;
  border-bottom-left-radius: 240px;
  border-bottom-right-radius: 240px;
  float: right !important;
  position: absolute;
  top: 0;
  right: 80px;
}

.treeImg {
  margin-left: auto;
  margin-right: auto;
  margin-bottom: 30px;
  height: 450px;
  width: 450px;
  animation: moveImage 4s infinite;
}

@keyframes moveImage {
  0% {
    transform: translateY(0);
  }
  50% {
    transform: translateY(-20px);
  }
  100% {
    transform: translateY(0);
  }
}

.singleFileBtn {
  display: block;
  margin-left: auto;
  margin-right: auto;
  background-color: #184226;
  height: 50px;
  width: 200px;
  border-radius: 50px;
  color: white;
  font-family: 'AR One Sans';
  font-size: 24px;
}

.singleFileBtn:hover {
  background-color: #0d2816;
}

.or {
  color: black;
  font-family: 'AR One Sans';
  font-size: 24px;
  margin-top: 10px;
  margin-bottom: 10px;
}

.multipleFilesBtn {
  display: block;
  margin-left: auto;
  margin-right: auto;
  background-color: #3a9e5b;
  height: 50px;
  width: 200px;
  border-radius: 50px;
  color: white;
  font-family: 'AR One Sans';
  font-size: 24px;
}

.multipleFilesBtn:hover {
  background-color: #286f40;
}

.categoriesHome {
  position: absolute;
  bottom: 75px;
  left: 27%;
}
</style>
